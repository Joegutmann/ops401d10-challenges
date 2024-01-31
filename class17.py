#!/bin/bash

# Script Name:                 Class 17
# Author:                       Joe Gutmann
# Date of latest revision:      30JAN24
# Purpose:                      Ops Challenge 401: Class 17

#In Python, create a script that prompts the user to select one of the following modes:

#Mode 1: Offensive; Dictionary Iterator

#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.
#Mode 2: Defensive; Password Recognized#

#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.

#Add to your Python brute force tool the capability to:

#Authenticate to an SSH server by its IP address.
#Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.


import time
import paramiko
import nltk
from nltk.corpus import words

# Default file path for rockyou.txt
default_filepath = "/home/joe/Downloads/rockyou.txt"

# Download and setup NLTK words for multiple languages
languages = ['en', 'es', 'de', 'fr', 'it']  # Add other language codes as needed
nltk.download('words')
word_lists = {lang: set(words.words(lang)) for lang in languages}

def is_word_in_any_language(word, word_lists):
    return any(word.lower() in word_lists[lang] for lang in word_lists)

def dictionary_iterator(filepath):
    try:
        with open(filepath, 'r', encoding='latin-1') as file:
            for word in file:
                word = word.strip()
                if is_word_in_any_language(word, word_lists):
                    print(word)
                    time.sleep(1)  # Delay between words
    except FileNotFoundError:
        print("The word list file was not found.")

def password_recognized(search_string, filepath):
    try:
        with open(filepath, 'r', encoding='latin-1') as file:
            if search_string in file.read():
                print(f"The string '{search_string}' is in the word list.")
            else:
                print(f"The string '{search_string}' is not in the word list.")
    except FileNotFoundError:
        print("The word list file was not found.")

def unleash_attack(ip, username, filepath):
    # [Existing SSH brute force function code]

def main():
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Brute Force Attack")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        filepath = input(f"Enter the full path to the word list file [{default_filepath}]: ") or default_filepath
        dictionary_iterator(filepath)
    elif choice == '2':
        search_string = input("Enter the string to search for: ")
        filepath = input(f"Enter the full path to the word list file [{default_filepath}]: ") or default_filepath
        password_recognized(search_string, filepath)
    elif choice == '3':
        default_ip = "192.168.1.100"
        default_username = "admin"
        filepath = default_filepath
        ip = input(f"Enter target IP address [{default_ip}]: ") or default_ip
        username = input(f"Enter username [{default_username}]: ") or default_username
        unleash_attack(ip, username, filepath)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

    ## Roger from class 16 in class lecture, chatgpt, and the work from class16.py .