#!/bin/bash

# Script Name:                 Class 18
# Author:                       Joe Gutmann
# Date of latest revision:      31JAN24
# Purpose:                      Ops Challenge 401: Class 18

sudo apt-get install zip

#First, setup your target ZIP file.

#Create a .txt file containing a secret message.

file="secret.txt"
echo "this is the secret message." > "secret.txt"
echo "The not secret file has been created"

#Follow the guide, How to Protect Zip file with Password, to archive the .txt file with password protection.
#Next, add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.
#define file name

# file_name="secret.txt"
#define the name of the zip

#zip_file="secret.zip"

#prompt user for password
#read -s -p "Enter the password for the zip file: " zip_password
#echo

#create the zip and password protect it.
#echo "$zip_password" | zip -e -P - "$zip_file" "$file_name"

#echo "The File '$file_name' has been zipped and password protected in '$zip_file'."

#Use the zipfile library.
#Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.

# Challenges 16/17 integration with the above 2 comments and the zip code commented out above: I also removed the non english language options to simplify it as well as 
# taking out code that over complicated it, even more than it already is. This utilized chatgpt, demo in class, and prior challenges 16/17. 
import time
import paramiko
import zipfile
import nltk
from nltk.corpus import words

# Default file path for rockyou.txt
default_filepath = "/home/joe/Downloads/rockyou.txt"

# Download and setup NLTK words for English
nltk.download('words')
english_words = set(words.words('en'))

def dictionary_iterator(filepath):
    with open(filepath, 'r', encoding='latin-1') as file:
        for word in file:
            word = word.strip()
            if word.lower() in english_words:
                print(word)
                time.sleep(1)  # Delay between words

def password_recognized(search_string, filepath):
    with open(filepath, 'r', encoding='latin-1') as file:
        content = file.read()
        print(f"The string '{search_string}' is {'in' if search_string in content else 'not in'} the word list.")

def unleash_attack(ip, username, filepath):
    # [Existing SSH brute force function code]

def create_protected_zip(file_to_zip, zip_filename, password):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.setpassword(password.encode())
        zipf.write(file_to_zip)

def crack_zip(zip_filename, password_list_file):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        with open(password_list_file, 'r', encoding='latin-1') as file:
            for password in file:
                try:
                    zipf.extractall(pwd=password.strip().encode())
                    print(f"Success! The password is: '{password}'")
                    return
                except RuntimeError:
                    pass
    print("No valid password found in the file.")

def main():
    modes = {
        '1': ("Offensive; Dictionary Iterator", lambda: dictionary_iterator(default_filepath)),
        '2': ("Defensive; Password Recognized", lambda: password_recognized(input("Enter the string to search for: "), default_filepath)),
        '3': ("SSH Brute Force Attack", lambda: unleash_attack(input("Enter target IP address: "), input("Enter username: "), default_filepath)),
        '4': ("Create and Crack Zip File", lambda: (create_protected_zip(input("Enter the name of the file to zip: "), input("Enter the name of the zip file to create: "), input("Enter the password for the zip file: ")), crack_zip(input("Enter the name of the zip file to crack: "), default_filepath)))
    }

    print("Select mode:")
    for key, (desc, _) in modes.items():
        print(f"{key}. {desc}")

    choice = input("Enter your choice: ")
    if choice in modes:
        modes[choice][1]()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
