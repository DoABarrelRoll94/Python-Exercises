import random
import sys
import os

# 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]              # create a list "a", with numerical elements

new_list = []                                           # "new_list" will have list with number less than 5
for elem in a:
    if elem < 5:
        new_list.append(elem)
        
print(new_list)

# 2

print(list(filter(lambda x: x < 5, a)))                 # does same as "new_list" but in one line of code

# 3

x = int(input("Give me a number. "))

def list_less_than_input(x):                            # function that creates and returns a list containing numbers less than input
    new_list = []
    for elem in a:
        if elem < x:
            new_list.append(elem)
    return new_list
    
print(list_less_than_input(x))                          # print list with numbers less than given input


        
        

        
