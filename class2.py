#!/bin/sh

import time
from pythonping import ping

targetip = input("Enter in an ip address you wish to ping: ") 

while True:
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S.%f')
    response = ping(targetip, count=1, timeout=2)

    if response.responses[0].success:
        status = "Network Active"
    else:
        status = "Network no go"   

    print(f"{timestamp} {status} to {targetip}")
    time.sleep(2)    

# I was having difficulties timestamp and needed refresher on some of the finicky details, so I leveraged chatgpt to assist and show several different ways
    # to execute.
