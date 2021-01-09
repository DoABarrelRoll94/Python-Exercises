#exercise3

import random
import sys
import os

# 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]              # create a list "a", with numerical elements

new_list = []                                           # "new_list" will have list with number less than 5
for elem in a:
    if elem < 5:
        new_list.append(elem)

print("List A:", a)       
print("List of numbers in List A that are less than 5:", new_list)

# 2

print("Same function as line above, but coded in one line:", list(filter(lambda x: x < 5, a)))                 # does same as "new_list" but in one line of code

# 3

x = int(input("\nGive me a number. I will print out a list of numbers from List A that are less than what you give me.\n"))

def list_less_than_input(x):                            # function that creates and returns a list containing numbers less than input
    new_list = []
    for elem in a:
        if elem < x:
            new_list.append(elem)
    return new_list
    
print(list_less_than_input(x))                          # print list with numbers less than given input


        
        

        
