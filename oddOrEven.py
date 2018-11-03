# Assignment #2

import random
import os
import sys

num = int(input("Give me a number bitch. "))

if(num % 4 == 0):
    print(num, "is a multiple of 4.")
elif(num % 2 == 0):
    print(num, "is even.")
else:
    print(num, "is odd.")
    
num, check = map(int, input("Give me two numbers. One number to check and one number to divide by. ").split())          # map function to get multiple input on 1 line

if(num % check == 0):
    print(str(num) + " divides evenly into " + str(check) + ".")
else:
    print(str(num) + " does not divide evenly into " + str(check) + ".")
    


