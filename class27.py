# Script Name:                  Ops Challenge -  Event Logging Tool Part 2 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      13FEB24
# Purpose:                      Ops Challenge 401: Class 27

import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Setup logging with rotating file handler
def setup_logging():
    log_file_path = 'example.log'
    logger = logging.getLogger('CustomLogger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file_path, maxBytes=10, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Initialize logger
logger = setup_logging()

# Global variable to store the encrypted message
encrypted_message_global = None

# Function to generate a key
def generate_key():
    key = Fernet.generate_key()
    logger.info("Encryption key generated.")
    return key

# Function to save the key to a file
def save_key(key, filename='encryption.key'):
    with open(filename, 'wb') as file:
        file.write(key)
    logger.info("Encryption key saved.")
    print("Encryption key has been saved.")

# Function to load the key from a file
def load_key(filename='encryption.key'):
    with open(filename, 'rb') as file:
        key = file.read()
    logger.info("Encryption key loaded.")
    return key

# File encryption and decryption functions
def encrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)
    logger.info(f"File encrypted: {filepath}")
    print(f"File {filepath} has been encrypted.")

def decrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)
    logger.info(f"File decrypted: {filepath}")
    print(f"File {filepath} has been decrypted.")

# Message encryption and decryption functions
def encrypt_message(message, key):
    global encrypted_message_global
    f = Fernet(key)
    encrypted_message_global = f.encrypt(message.encode())
    logger.info("Message encrypted.")
    print("Message has been encrypted.")

def decrypt_message(key):
    global encrypted_message_global
    if encrypted_message_global is None:
        logger.info("No encrypted message to decrypt.")
        print("No message available to decrypt.")
        return
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message_global).decode()
    logger.info("Message decrypted.")
    print("Message decrypted:", decrypted_message)
    return decrypted_message

# Main function with menu
def main():
    print("Select a mode:")
    print("1. Generate and save a new encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Encrypt a message")
    print("5. Decrypt a message")
    print("6. Exit")

    while True:
        mode = input("Enter mode (1-6): ")

        if mode == '1':
            key = generate_key()
            save_key(key)
            print("A new encryption key has been generated and saved.")

        elif mode == '2':
            key = load_key()
            filepath = input("Enter the filepath to encrypt: ")
            encrypt_file(filepath, key)

        elif mode == '3':
            key = load_key()
            filepath = input("Enter the filepath to decrypt: ")
            decrypt_file(filepath, key)

        elif mode == '4':
            key = load_key()
            message = input("Enter the message to encrypt: ")
            encrypt_message(message, key)

        elif mode == '5':
            key = load_key()
            decrypted_message = decrypt_message(key)
            if decrypted_message is None:
                print("Failed to decrypt message or no message available.")

        elif mode == '6':
            print("Exiting program.")
            break

        else:
            logger.warning("Invalid mode selected. Please enter a valid option.")
            print("Invalid mode selected. Please enter a valid option.")

if __name__ == "__main__":
    main()


# code from class 6 challenge. and the https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    # tutorial. It logs the actions taken during the script and properly encrypts and decrypts
    # files. 