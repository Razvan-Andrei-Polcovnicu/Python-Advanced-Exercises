import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import schedule
import time
import logging

# Configure logging to save email sending status and errors
logging.basicConfig(filename='email_log.txt', level=logging.INFO)

# SMTP server details and credentials
smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
smtp_port = 587  # Replace with your SMTP server port number
smtp_username = 'your_username'  # Replace with your SMTP server username
smtp_password = 'your_password'  # Replace with your SMTP server password

# List of recipients and their corresponding report file paths
recipients = [
    {'email': 'client1@example.com', 'report_file_path': 'report1.pdf'},
    {'email': 'client2@example.com', 'report_file_path': 'report2.pdf'},
    {'email': 'client3@example.com', 'report_file_path': 'report3.pdf'}
]

# Function to send daily report email to a recipient
def send_daily_report_email(recipient_email, report_file_path):
    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = 'Daily Report'

        body = 'Hello,\nPlease find the daily report attached.'
        msg.attach(MIMEText(body, 'plain'))

        # Attach the report file
        with open(report_file_path, 'rb') as report_file:
            attachment = MIMEApplication(report_file.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(report_file_path)}')
            msg.attach(attachment)

        # Send the email
        server.sendmail(smtp_username, recipient_email, msg.as_string())
        server.quit()

        logging.info(f'Successfully sent email to {recipient_email}')

    except Exception as e:
        # Log errors if email sending fails
        logging.error(f'Error sending email to {recipient_email}: {str(e)}')

# Schedule the email sending task for each recipient daily at 8:00 AM
for recipient in recipients:
    schedule.every().day.at('08:00').do(send_daily_report_email, recipient_email=recipient['email'], report_file_path=recipient['report_file_path'])

# Continuously check the schedule and run pending tasks
while True:
    schedule.run_pending()
    time.sleep(1)
