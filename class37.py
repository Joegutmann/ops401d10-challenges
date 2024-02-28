# Script Name:                  Ops Challenge -  Cookie Capture Capades
# Author:                       Joe Gutmann
# Date of latest revision:      27FEB24
# Purpose:                      Ops Challenge 401: Class 37

#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
                                .'   `-.____.'-.
                              .'  `-._______.-'    # Stretch Goal Hands
        ''')             

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
response_with_cookie = requests.get(targetsite, cookies=cookie)
# - Generate a .html file to capture the contents of the HTTP response
filename = 'response.html'
with open(filename, 'w') as file:
    file.write(response_with_cookie.text)
# - Open it with Firefox
webbrowser.open_new_tab(filename)
# Stretch Goal
# - Give Cookie Monster hands

## leveraged https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-37/challenges/DEMO.md
