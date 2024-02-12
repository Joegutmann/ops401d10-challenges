#!/bin/bash

# Script Name:                  Ops Challenge -  Event Logging Tool Part 1 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      12FEB24
# Purpose:                      Ops Challenge 401: Class 26

import logging
import os
from cryptography.fernet import Fernet

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('and this, too')
#logging.error('And non-ASCII stuff, too, like 0resund and Malmo')



# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Functions for file encryption and decryption
def encrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

# Functions for message encryption and decryption
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()
# Save the key to a file
def save_key(key, filename='encryption.key'):
    with open(filename, 'wb') as file:
        file.write(key)

# Load the key from a file
def load_key(filename='encryption.key'):
    with open(filename, 'rb') as file:
        return file.read()

# Main function
def main():
    key = generate_key()
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    mode = input("Enter mode (1-4): ")

    if mode == '1':
        key = generate_key()
        save_key(key)
        filepath = input("Enter the filepath to encrypt: ")
        encrypt_file(filepath, key)
        print("File encrypted successfully.")
        logging.info(f"File encryption selected. Filepath: {filepath}")

    # For decryption, load the existing key
    elif mode == '2':
        key = load_key()
        filepath = input("Enter the filepath to decrypt: ")
        decrypt_file(filepath, key)
        print("File decrypted successfully.")
        logging.info(f"File decryption selected. Filepath: {filepath}")
    
    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print(f"Encrypted message: {encrypted_message}")
        logging.info("Message encryption selected.")

    elif mode == '4':
        encrypted_message = input("Enter the encrypted message to decrypt: ")
        try:
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
            logging.info("Message decryption selected.")
        except:
            print("Invalid encryption key or message.")
            logging.warning("Failed message decryption attempt.")
    else:
        print("Invalid mode selected.")
        logging.warning(f"Invalid mode selected: {mode}")
if __name__ == "__main__":
    main()

# code from class 6 challenge. and the https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    # tutorial. It logs the actions taken during the script and properly encrypts and decrypts
    # files. 