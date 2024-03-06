#!/usr/bin/python3
#!/usr/bin/bash
# Script Name:                  Ops Challenge -  Lab: Attacking Juice Shop with Burp Suite

# Author:                       Joe Gutmann
# Date of latest revision:      05MAR24
# Purpose:                      Ops Challenge 401: Class 42

import nmap

scanner = nmap.PortScanner()

print("Simple Nmap Automation Tool")
ip_addr = input("Enter IP address to scan: ")
port_range = input("Enter port range to scan (e.g., 1-1024): ")

print("\nSelect scan type:")
print("1) SYN ACK Scan")
print("2) UDP Scan")
print("3) Comprehensive Scan")
scan_type = input("Your choice (1-3): ")

scan_options = {
    '1': ('-v -sS', 'tcp'),
    '2': ('-v -sU', 'udp'),
    '3': ('-v -sS -sU -A -T4', 'tcp')
}

if scan_type in scan_options:
    options, protocol = scan_options[scan_type]
    scanner.scan(ip_addr, port_range, options)
    print(f"Scan Report for {ip_addr}:")
    if scanner[ip_addr].state() == 'up':
        print(f"Host is up, scanned with {options}.")
        if protocol in scanner[ip_addr].all_protocols():
            print("Open Ports:", scanner[ip_addr][protocol].keys())
    else:
        print("Host seems down.")
else:
    print("Invalid scan type selected.")

# Utilized https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-42/challenges/DEMO.md // https://chat.openai.com/c/bd29a7ca-cd42-4f2e-96f7-9c88d4d475bc //
    # The googs.