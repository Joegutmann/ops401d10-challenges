#!/bin/bash

# Script Name:                  Ops Challenge -  Network Security Tool with Scapy Part 1 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      22JAN24
# Purpose:                      Ops Challenge 401: Class 11

from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

#  host IP and port range
host = 'xx192.168.1.1xx'  # target IP
start_port = 20       # Start port range
end_port = 25         # Ending port range

# Function to test a specific port
def test_port(ip, port):
    response = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)
    if response is not None:
        if response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK flags
                # Send RST packet to close the connection
                sr1(IP(dst=ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
                return f'Port {port} is open.'
            elif response[TCP].flags == 0x14:  # RST flags
                return f'Port {port} is closed.'
    else:
        # No response, port might be filtered.. or not
        return f'Port {port} is filtered and might be silently dropped.'

# Scan the ports in the range
for port in range(start_port, end_port + 1):
    status = test_port(host, port)
    print(status)

# Example ARP request. can be commented out
request = ARP()
print(request.show())

# Sniffing packets can be commented out
packets = sniff(count=10)
for packet in packets:
    print(packet.show())

    # this should satisfy the requirements of the assignment, but I am not completely satisfied with it. Leveraged https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/demo.py
    # and chatgpt