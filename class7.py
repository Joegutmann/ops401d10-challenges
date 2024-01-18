#!/bin/sh

import os
from cryptography.fernet import Fernet

# os.walk()
start_directory = "c:/Users/Joe/.vscode/ops401d10-challenges"

# for root, dirs, files in os.walk(start_directory):
#    for filename in files:
#        full_path = os.path.join(root, filename)
#        print(full_path)

# the above was utilized from https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/... ended up just folding it into the code with options 5/6 below.
        
# the filepath c:/Users/Joe/.vscode/ops401d10-challenges\experiment\fun.txt        

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Functions for file encryption and decryption.. good with new additions
def encrypt_file(filepath, key):
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key): # good with new additions
    f = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

def encrypt_folder_recur(folder_path, key): # encryp a folder and its insides
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            encrypt_file(full_path, key)

def decrypt_folder_recur(folder_path, key): # decryp a folder and its insides
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            decrypt_file(full_path, key)
# Functions for message encryption and decryption  // Don't need these anymore
# def encrypt_message(message, key):
#    f = Fernet(key)
#    return f.encrypt(message.encode())

#def decrypt_message(encrypted_message, key):
#    f = Fernet(key)
#    return f.decrypt(encrypted_message).decode()

# Main function
def main():
    key = generate_key()
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively encrypt a folder and its insides")
    print("6. Recursively decrypt a folder and its insides")

    mode = input("Enter mode (1-6): ")

    if mode == '1':
        filepath = input("Enter the filepath to encrypt: ")
        encrypt_file(filepath, key)
        print("File encrypted successfully.")

    elif mode == '2':
        filepath = input("Enter the filepath to decrypt: ")
        decrypt_file(filepath, key)
        print("File decrypted successfully.")

    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print(f"Encrypted message: {encrypted_message}")

    elif mode == '4':
        encrypted_message = input("Enter the encrypted message to decrypt: ")
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Decrypted message: {decrypted_message}")
    elif mode == '5':   
        folder_path = input("Enter the folder path to recursively encrypt: ")   
        encrypt_folder_recur(folder_path, key)
        print(f"5. Folder and its insides have been encrypted.")  
    elif mode == '6':   
        folder_path = input("Enter the folder path to recursively decrypt: ")   
        decrypt_folder_recur(folder_path, key)
        print(f"Folder and its insides have been decrypted")
    
    else:
        print("Invalid choice selected.")

if __name__ == "__main__":
    main()