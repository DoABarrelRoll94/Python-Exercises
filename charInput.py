# Assignment 1

import random 
import os
import sys
import datetime     # for current year

name = input("What is your name? ")
#print("Your name is", name, end="")         # end="" -> no new line
#sys.stdout.write(".\n")                     # sys.stdout.write to have period right after previous string(no whitespace)

age = int(input("What is your age? "))

now = datetime.datetime.now()               # current date
year_when_hundo = now.year - age + 100
message = ("The year will be " + str(year_when_hundo) + " when you are 100 years-old.")
print(message)

num = int(input("Enter another number. "))  # prints previous message x times depending on input given by user
print(message * num)
        
for x in range(num):                        # prints previous message x times (on separate lines) depending on input given by user
    print(message)
    

    





