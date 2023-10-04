# Python-Advanced-Exercises

1. Caesar Cipher Encryption and Decryption

This Python script implements the Caesar cipher algorithm, an ancient encryption technique used by Julius Caesar to secure his confidential messages. The cipher encrypts and decrypts text by shifting letters in the alphabet by a fixed key. This implementation allows users to choose between encryption and decryption modes, input their desired shift key, and enter the message they want to process.

Features:

Encryption: Shifts letters in the alphabet by the specified key to encrypt the message.
Decryption: Shifts letters in the opposite direction to decrypt an encrypted message back to its original form.
Input Validation: Ensures that only alphabetical characters are shifted, leaving special characters and numbers unchanged.
User-Friendly Interface: Guides users through the encryption or decryption process with clear prompts and instructions.
Usage:

Encryption: Protect sensitive information by encrypting messages before transmission.
Decryption: Decrypt received messages that were encrypted using the Caesar cipher.
How to Use:

Choose whether to encrypt or decrypt a message.
Enter the shift key (0 to 25) to determine the degree of encryption or decryption.
Input the message to be encrypted or decrypted.
Receive the processed message and share it securely!
Feel free to experiment with different shift keys and messages to explore the power of the Caesar cipher encryption.


2. Caesar Cipher Brute-Force Decryptor
   
This Python program allows users to decrypt messages encrypted using the Caesar cipher, even without knowing the encryption key. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Features:
Brute-Force Attack: The program performs a brute-force attack by trying all 26 possible shift positions, decrypts the message, and checks if the resulting words are valid English words.
English Word Validation: Utilizes the PyEnchant library to validate decrypted words, ensuring the accuracy of the decrypted message.
User Interaction: Provides a user-friendly interface where users can input the encrypted message and receive decrypted results for all possible shift positions.
How to Use:
Run the program and enter the encrypted message.
The program will perform a brute-force attack and display potential decrypted messages with valid English words.
Analyze the results to find the most meaningful decryption.
Feel free to use and modify this tool for your cryptographic analysis needs. Happy decrypting!


3. Automated Daily Email Reports Sender

This Python script automates the process of sending daily reports to clients via email. The program achieves this by following a systematic approach:

SMTP Server Connection: Utilizes the smtplib library to connect to the email server securely. SMTP server details such as address, port number, username, and password need to be configured.

Email Composition: Utilizes the email library to compose the email, including the recipient's email address, the subject, and the body of the email. The email body contains a polite message informing the recipient about the attached daily report.

Attachment Handling: Utilizes the os library to access the report files that need to be sent. The script attaches the appropriate report file to the email before sending.

Recipient List Iteration: Iterates through a list of recipients, each having a unique email address and a corresponding report file path. The script sends individual emails to each recipient with their respective report attachments.

Scheduling: Uses the schedule library to schedule the script to run daily at a specific time (8:00 AM). This ensures that the email reports are sent out automatically without manual intervention.

Logging: Implements logging functionality to keep track of the emails that have been sent and any errors that may occur during the email sending process. The log file, email_log.txt, captures the status of each email sent.

This versatile script can be adapted for various business contexts where automated daily email reports are required. Its modular design allows for easy customization, making it a valuable tool for businesses that prioritize efficient communication with clients.

4. Automating File Transfer from External FTP Server

Description:

In this exercise, you work for a company that receives daily data files from external partners. These files are crucial for the company's operations, but they first need to be transferred securely to the company's internal network for processing and analysis. Your task is to automate this file transfer process using Python.

Requirements:

FTP Server Interaction:

Use the ftplib library to establish a connection with the external FTP server.
List the files available in the specified directory on the FTP server.
Local Directory Management:

Use the os library to check if a local directory exists where the downloaded files will be stored.
Create the local directory if it does not exist.
File Transfer:

Iterate through the files on the FTP server using a loop.
Download each file from the FTP server and store it in the local directory.
Utilize the ftplib.retrbinary() method for file transfer.
Internal Network Transfer:

Use the shutil library to move the downloaded files from the local directory to the company's internal network directory.
Ensure that the files are seamlessly transferred without any corruption.
Scheduling:

Use the schedule library to schedule the script to run daily at a specific time (e.g., 2:00 AM).
Automate the file transfer process at the scheduled time without manual intervention.
Error Handling and Logging:

Implement error handling mechanisms to capture and log any errors that occur during the file transfer process.
Utilize the logging library to create a log file (transfer.log) to record successful file transfers and any encountered errors.
Constraints:

Ensure the script can handle different file types and sizes commonly found in the data files.
Use appropriate security measures, such as secure FTP (SFTP) or FTPS, to protect the file transfer process.
The script should be well-documented with clear comments explaining each step and the purpose of the code blocks.
Consider the possibility of network interruptions and implement robust error handling to resume the file transfer process seamlessly.
Expected Output:

Upon running the script, it should establish a connection with the external FTP server, download the daily data files, transfer them to the local directory, and then move them to the company's internal network directory. The script should run automatically at the scheduled time each day, ensuring the timely and secure transfer of essential data files.

Note: Before executing the script, ensure that the FTP server credentials, directory paths, and scheduling time are correctly configured in the script.
