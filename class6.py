#!/bin/sh

# pip install cryptography
# pip3 install cryptography
# from cryptography.fernet import Fernet



# Prompt the user to select a mode. Encrypt a file (mode 1) / Decrypt a file (mode 2) / Encrypt a message (mode 3) / Decrypt a message (mode 4)

# def main_menu():
#    print("Menu: ")
#    print("1. Encrypt a file.")
#    print("2. Decrypt a file.")
#    print("3. Encrypt a message.")
#    print("4. Decrypt a message.")

#while True:
#    main_menu()
#    choice = input("Please choose 1,2,3 or 4: ")
# If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#if choice == '1':
#    file_path = input("Please enter a file path: ")
#    print(f"")
#elif == '2'
# If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

# Create 4 functions

# Encrypt the target file if in mode 1.
# Delete the existing target file and replace it entirely with the encrypted version.

# Decrypt the target file if in mode 2.
# Delete the encrypted target file and replace it entirely with the decrypted version.

# Encrypt the string if in mode 3.
# Print the ciphertext to the screen.

# Decrypt the string if in mode 4.
# Print the cleartext to the screen.


from cryptography.fernet import Fernet

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
        try:
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        except:
            print("Invalid encryption key or message.")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()

## Leveraged chatgpt for this, It took me waaaaaaaaaaaaay to long to realize my original code was not working because somehow I switched vs code locations
# and did not have the virtual environment venv set up on it. I still do not know why it moved me to a new terminal or anything, but atleast that portion
# is now working. I also got the 401d10 challenges folder reconnected to github and am able to push updates from vs code at this point.