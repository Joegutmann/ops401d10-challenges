#!/bin/bash

# Script Name:                 Class 16
# Author:                       Joe Gutmann
# Date of latest revision:      29JAN24
# Purpose:                      Ops Challenge 401: Class 16

#In Python, create a script that prompts the user to select one of the following modes:

#Mode 1: Offensive; Dictionary Iterator

#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.
#Mode 2: Defensive; Password Recognized#

#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
# Print to the screen whether the string appeared in the word list.



import nltk
import ssl
from nltk.corpus import words

try: _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    return word_list 

def check_for_word():
    user_answer = input("Enter a word to verify its inclusion in the collection")
    if user_answer in words:
        print("It is here")
    else:
        print("The word is not in the collection")

# if __name__ == "__main__":
#    external_words() # or words = get_words()
#    print(external_words)
    check_for_word(externa)

    ## Roger from class 16 in class lecture, and a tiny bit of chatgpt.