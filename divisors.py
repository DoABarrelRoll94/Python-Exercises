# Exercise 4, asks user for a number and prints out the divisors of that number

import random
import os
import sys

dividend = int(input("Give me a number. "))         # ask user for number

possible_divisors = list(range(1, dividend +1))     # list of possible divisors from 1 to number given

divisor_list = []                                   # empty list where divisors will be placed

for elem in possible_divisors:
    
    if (dividend) % elem == 0:                      # if number is divisor, place append to divisor_list
        divisor_list.append(elem)
        
print(divisor_list)                                 # print list of divisors 







