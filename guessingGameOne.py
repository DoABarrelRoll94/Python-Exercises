# exercise 9, generate random number from 1-9, ask user to guess number, tell them whether they guessed too low, too high, or exactly

import random				# import random module
import os
import sys

# original, # extra 1, # extra 2

randNum = random.randint(1, 9)
count = 0
guess = 0

while guess != 'exit' or guess != randNum:                  # while loop will go if either are true
    
    guess = input("I'm guessing a number from 1 - 9. Guess which one. Type exit at any time to quit. ")
    
    if guess == 'exit':
        break
        
    count += 1
    
    guess = int(guess)
    
    if guess < randNum:
        print("Too low. Try again.")    
        
    elif guess > randNum:
        print("Too high. Try again.")
        
    else:
        print("Correct! It only took you %d tries!" % count)
    
        
    
    
    

    

    

    

    

