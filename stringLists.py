# exercise 6, ask user for a string and print whether string is palindrome or not

import os
import sys
import random

def reverse_string(s):              # function to reverse a string
    
    return s[::-1]
    
def is_palindrome(s):               # checks is string is a palindrome
    
    reverse = reverse_string(string)
    
    if s == reverse:
        return True
    else:
        return False
    
    
string = input("Give me a string.\n")

if is_palindrome(string):
    print("The string you gave is a palindrome.")
else:
    print("The string is not a palindrome.")






