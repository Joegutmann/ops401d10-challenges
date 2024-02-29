# Script Name:                  Ops Challenge -  Lab: Attacking Juice Shop with Burp Suite

# Author:                       Joe Gutmann
# Date of latest revision:      28FEB24
# Purpose:                      Ops Challenge 401: Class 38


#ensure to pip install wapiti3 before running

import subprocess

# The target URL you want to scan
target_url = 'http://example.com'

# Construct the Wapiti command
command = ['wapiti', '-u', target_url, '--scope', 'folder', '-m', 'xss', '--flush-session', '--no-colors']

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Decode the output from bytes to string
output = stdout.decode()

# Check the output for XSS vulnerability reports
if 'Cross Site Scripting' in output:
    print('XSS vulnerability detected.')
else:
    print('No XSS vulnerability detected in the output.')

# Optionally, you can save the output to a file for further analysis
with open('wapiti_output.txt', 'w') as file:
    file.write(output)
