# Script Name:                  Ops Challenge -  Web Application Fingerprinting
# Author:                       Joe Gutmann
# Date of latest revision:      26FEB24
# Purpose:                      Ops Challenge 401: Class 36


# Import the subprocess module to execute system commands.
import subprocess

def banner_grabbing():
    # Prompt the user for a URL or IP address to target for banner grabbing.
    target = input("Enter the target URL or IP address: ")
    # Prompt the user for a specific port number to target.
    port = input("Enter the port number: ")
    
    # Using netcat for banner grabbing. The command structure is set to initiate a connection to the specified target and port.
    # The '-v' flag makes netcat operate in verbose mode, '-n' prevents DNS resolution, and the port is specified to focus the attempt.
    print("\n[+] Performing banner grabbing with netcat...")
    nc_command = f"nc -v -n {target} {port}"
    nc_result = subprocess.getoutput(nc_command)  # Execute the netcat command and capture its output.
    print(nc_result)  # Display the output from netcat, which includes any banners grabbed.
    
    # Using telnet for banner grabbing. This technique involves sending a simple input (echo '') to the telnet command targeting the same server and port.
    # The 'timeout' command ensures the operation doesn't hang indefinitely.
    print("\n[+] Performing banner grabbing with telnet...")
    telnet_command = f"echo '' | timeout 3 telnet {target} {port}"
    telnet_result = subprocess.getoutput(telnet_command)  # Execute the telnet command and capture its output.
    print(telnet_result)  # Display the output from telnet, which may include the service banner.
    
    # Using Nmap for a more comprehensive banner grabbing, scanning all well-known ports of the target.
    # The '-sV' flag tells Nmap to attempt service version detection.
    print("\n[+] Performing banner grab with Nmap...")
    nmap_command = f"nmap -sV --open -p- {target}"
    nmap_result = subprocess.getoutput(nmap_command)  # Execute the Nmap command and capture its output.
    print(nmap_result)  # Display the output from Nmap, including service versions and banners identified.

# Ensure that the banner_grabbing function is called when the script is directly executed.
if __name__ == "__main__":
    banner_grabbing()

# leverages https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/ and chatgpt