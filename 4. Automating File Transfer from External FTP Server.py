# Import necessary libraries
from ftplib import FTP  # For FTP server interaction
import os  # For file and directory operations
import shutil  # For moving files
import schedule  # For scheduling tasks
import time  # For time-related operations
import logging  # For logging events and errors

# Configure logging settings
logging.basicConfig(filename='transfer.log', level=logging.INFO, format='%(asctime)s - %(message)s')


# Function to transfer files from external FTP server to internal network
def transfer_files():
    # FTP server credentials and directories
    ftp_server = 'external_ftp_server_address'
    username = 'username'
    password = 'password'
    ftp_directory = '/path/to/ftp/directory/'
    local_directory = 'local_directory_path'
    internal_network_directory = 'internal_network_directory_path'

    try:
        # Connect to the FTP server
        ftp = FTP(ftp_server)
        ftp.login(user=username, passwd=password)

        # Navigate to the specific directory on the FTP server
        ftp.cwd(ftp_directory)

        # List files in the FTP directory
        files = ftp.nlst()

        # Create local directory if it does not exist
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)

        # Download files from FTP server to local directory
        for file in files:
            local_file_path = os.path.join(local_directory, file)
            with open(local_file_path, 'wb') as local_file:
                ftp.retrbinary('RETR ' + file, local_file.write)

        # Move files from local directory to internal network directory
        for file in os.listdir(local_directory):
            local_file_path = os.path.join(local_directory, file)
            internal_network_file_path = os.path.join(internal_network_directory, file)
            shutil.move(local_file_path, internal_network_file_path)

        # Log successful file transfer
        logging.info('Files transferred successfully.')

    except Exception as e:
        # Log errors if any occur during the transfer process
        logging.error(f'Error occurred: {str(e)}')

    finally:
        # Close FTP connection
        ftp.quit()


# Schedule the file transfer to run daily at 2:00 AM
schedule.every().day.at('02:00').do(transfer_files)

# Continuous loop to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
