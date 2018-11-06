# exercise 10

import os 
import sys
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("a =", a)
print("b =", b)

new_list = [value for value in a and b if value in a and b]             # creates new list of values from a and b with no duplicates
print(new_list, "\n")

a = random.sample(range(100), 10)                                       # generates a random list of numbers from 0-99 with 10 elements 
b = random.sample(range(100), 13)

print("a =", a)
print("b =", b)

new_list = [value for value in a and b if value in a and b]
print(new_list)