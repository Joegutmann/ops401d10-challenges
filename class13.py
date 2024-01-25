#!/bin/bash

# Script Name:                  Ops Challenge -  Network Security Tool with Scapy Part 3 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      24JAN24
# Purpose:                      Ops Challenge 401: Class 13

# stil runs this with sudo and import scrapy if you need to. 

from scapy.all import IP, ICMP, TCP, sr1, conf
import ipaddress

# Function to test a specific port
def test_port(ip, port):
    response = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)
    if response is not None:
        if response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK flags
                # Send packet to close the connection
                sr1(IP(dst=ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
                return f'Port {port} is open.'
            elif response[TCP].flags == 0x14:  # RST flags
                return f'Port {port} is closed.'
    else:
        # No response, port might be filtered.. or not
        return f'Port {port} is filtered and might be silently dropped.'

# Function to perform port scanning
def port_scan(ip, start_port, end_port):
    print(f"Scanning ports on {ip} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        status = test_port(ip, port)
        print(status)

# Function to ping an IP address
def ping_host(ip):
    print(f"Pinging {ip}")
    conf.verb = 0  # Disable verbose in Scapy
    packet = IP(dst=str(ip))/ICMP()
    response = sr1(packet, timeout=1, verbose=0)
    return response is not None

def main():
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    if ping_host(target_ip):
        print(f"Host {target_ip} is responding to pings.")
        port_scan(target_ip, start_port, end_port)
    else:
        print(f"Host {target_ip} is not responding to pings.")

if __name__ == "__main__":
    main()

    ## / my class12.py and Chatgpt 