# Script Name:                  Ops Challenge -  Signature-Based Malware Detection 3 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      21FEB24
# Purpose:                      Ops Challenge 401: Class 33

import hashlib
import os
from datetime import datetime
import subprocess

def generate_md5_hash(file_path):
    """
    Generate MD5 hash for a file.
    
    Parameters:
        file_path (str): Path to the file for which the MD5 hash is generated.
        
    Returns:
        str: The MD5 hash of the file.
    """
    # Create a new md5 hash object
    hash_md5 = hashlib.md5()
    # Open the file in binary mode and read chunks to update the hash object
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    # Return the hexadecimal digest of the hash
    return hash_md5.hexdigest()

def query_virustotal(file_hash):
    """Query VirusTotal API for the given file hash."""
    # Assuming API_KEY_VIRUSTOTAL is set as an environment variable
    api_key = os.getenv('API_KEY_VIRUSTOTAL')
    if not api_key:
        print("API_KEY_VIRUSTOTAL environment variable not set. Please set it before proceeding.")
        return

    # Construct the command to call virustotal-search.py with the API key and file hash
    command = f"python virustotal-search.py -k {api_key} -m {file_hash}"
    try:
        # Execute the constructed command and capture its output
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error querying VirusTotal for hash {file_hash}: {e}")

def scan_directory(directory_path, include_virustotal=False):
    """
    Recursively scan each file in the directory and optionally query VirusTotal.
    
    Parameters:
        directory_path (str): The path of the directory to scan.
        include_virustotal (bool): Whether to query VirusTotal for each file's hash.
    """
    # Check for directory existence and validity
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Invalid directory: {directory_path}")
        return

    # Walk through the directory and process each file
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            try:
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Get the file size
                file_size = os.path.getsize(file_path)
                # Generate the MD5 hash for the file
                md5_hash = generate_md5_hash(file_path)
                # Get the current timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Print file details
                print(f"Timestamp: {timestamp}, File Name: {file}, File Size: {file_size} bytes, MD5 Hash: {md5_hash}, Path: {file_path}")
                # If enabled, query VirusTotal for the file's hash
                if include_virustotal:
                    query_virustotal(md5_hash)
            except Exception as e:
                print(f"Error processing file '{file}': {e}")

def main_menu():
    """
    Display the main menu and handle user input for the program's operations.
    """
    while True:
        # Display menu options
        print("\nMain Menu")
        print("1. Start directory scan")
        print("2. Start directory scan with VirusTotal check")
        print("3. Exit")
        # Get user choice
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            # Scan directory without VirusTotal check
            directory_path = input("Enter the directory path to scan: ").strip()
            scan_directory(directory_path)
        elif choice == '2':
            # Scan directory with VirusTotal check
            directory_path = input("Enter the directory path to scan with VirusTotal check: ").strip()
            scan_directory(directory_path, include_virustotal=True)
        elif choice == '3':
            # Exit the program
            print("Exiting program.")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()


# https://docs.python.org/3/library/hashlib.html // https://www.programiz.com/python-programming/examples/hash-file // chatgpt // demo videos were resources
# utilized to create this. //  as well as the class32 code.
