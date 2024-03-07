#!/usr/bin/python3
#!/usr/bin/bash
# Script Name:                  Ops Challenge -  Lab: Attacking Juice Shop with Burp Suite

# Author:                       Joe Gutmann
# Date of latest revision:      05MAR24
# Purpose:                      Ops Challenge 401: Class 42

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5 # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter in the Host IP addy: ") # TODO: Collect a host IP from the user.
portno = int(input("Enter in the port number: ")) # TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0: # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port closed")
    else:
        print("Port open")

portScanner(port)

## Resources: https://docs.python.org/3/library/socket.html and chatgpt