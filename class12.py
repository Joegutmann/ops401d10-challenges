#!/bin/bash

# Script Name:                  Ops Challenge -  Network Security Tool with Scapy Part 2 of 3
# Author:                       Joe Gutmann
# Date of latest revision:      23JAN24
# Purpose:                      Ops Challenge 401: Class 12

# sudo before running. 
from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP, sr, conf
import ipaddress

# Function to test a specific port, user menu below
def test_port(ip, port):
    response = sr1(IP(dst=ip)/TCP(dport=port, flags='S'), timeout=1, verbose=0)
    if response is not None:
        if response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK flags - 
                # Send packet to close the connection
                sr1(IP(dst=ip)/TCP(dport=port, flags='R'), timeout=1, verbose=0)
                return f'Port {port} is open.'
            elif response[TCP].flags == 0x14:  # RST flags
                return f'Port {port} is closed.'
    else:
        # No response, port might be filtered.. or not
        return f'Port {port} is filtered and might be silently dropped.'

def tcp_port_range_scanner(host, start_port, end_port):
    print("TCP Port Range Scanner Mode Selected")
    for port in range(start_port, end_port + 1):
        status = test_port(host, port)
        print(status)

def icmp_ping_sweep(network):
    print("ICMP Ping Sweep Mode Selected")
    net = ipaddress.ip_network(network, strict=False)
    online_hosts = 0
    conf.verb = 0  # Disable verbose in Scapy or do a 1 to flip the switch

    for ip in net.hosts():
        packet = IP(dst=str(ip))/ICMP()
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            print(f"Host {ip} is down or unresponsive.")
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip} is responding.")
                online_hosts += 1
        else:
            print(f"Host {ip} is down or unresponsive.")

    print(f"Total online hosts: {online_hosts}")

def main():
    choice = input("Choose mode (1- TCP Port Range Scanner, 2- ICMP Ping Sweep): ")

    if choice == '1':
        host = input("Enter target IP address: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        tcp_port_range_scanner(host, start_port, end_port)
    elif choice == '2':
        network = input("Enter a network address with CIDR (e.g., 10.10.0.0/24): ")
        icmp_ping_sweep(network)

if __name__ == "__main__":
    main()

    ## https://github.com/Joegutmann/ops401d10-challenges/blob/main/class11.py / my class.11py / Chatgpt 