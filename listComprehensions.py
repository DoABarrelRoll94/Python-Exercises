# exercise 7, write one line of python that takes list and makes a new list that only has even elements

import os
import sys
import random

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([num for num in a if num % 2 == 0])           # prints list of just the even numbers in list 'a'