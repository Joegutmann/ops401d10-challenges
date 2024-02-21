# Script Name:                  Ops Challenge -  Signature-Based Malware Detection 2 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      20FEB24
# Purpose:                      Ops Challenge 401: Class 28

# importing the systems we need
import hashlib
import os
from datetime import datetime

# gen the hash, prompt for file path. It may be improved with a menu that provides multiple options for commonly used file paths with a prompt for
# a file name and an option to input your own.
def generate_md5_hash(file_path):
    """Generate MD5 hash for a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def scan_directory(directory_path):
    """Recursively scan each file in the directory and print details.""" # first time trying out a docstring
    # Checking if the directory exists
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist. Please enter a valid path.")
        return
    # Checking if the path is actually a directory
    elif not os.path.isdir(directory_path):
        print(f"'{directory_path}' is not a directory. Please enter a valid directory path.")
        return
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                md5_hash = generate_md5_hash(file_path)
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Print the variable to the screen along with a timestamp, file name, file size, and complete file path.
                print(f"Timestamp: {timestamp}, File Name: {file}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}, Path: {file_path}")
            except Exception as e:
                print(f"Error processing file '{file}': {e}")

def main_menu():  # I figure we will add another option so I'd get ahead of the menu creation.
    """Display the main menu and handle user input."""
    while True:
        print("\nMain Menu")
        print("1. Start directory scan")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            directory_path = input("Enter the directory path to scan: ").strip()
            if directory_path:
                scan_directory(directory_path)
            else:
                print("Input was empty. Please enter a valid directory path.")
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()

# https://docs.python.org/3/library/hashlib.html // https://www.programiz.com/python-programming/examples/hash-file // chatgpt // demo videos were resources
# utilized to create this.
