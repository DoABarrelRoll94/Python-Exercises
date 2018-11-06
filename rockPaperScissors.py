# exercise 8, create a 2-player Rock-Paper-Scissors game

import random
import os
import sys

while True:
    
    print("Let's play Rock-Paper-Scissors!")

    player1 = input("Player 1, what's your name? ")
    player2 = input("Player 2, what's your name? ")

    p1_choice = input("%s, what is your choice? Rock, Paper, or Scissors? " % player1)
    p2_choice = input("%s, what is your choice? Rock, Paper, or Scissors? " % player2)
            
    def compare(p1, p2, name1, name2):
    
        if p1 == p2:
            choice = input("It's a tie! Would you like to play again?(y/n) ")
            if choice == 'y':
                decision()
            else:
                exit()
            
        elif p1 == 'Rock' or p1 == 'rock':
            if p2 == 'Scissors' or p2 == 'scissors':
                return("%s wins!" % name1)
            else:
                return("%s wins!" % name2)
            
        elif p1 == 'Paper' or p1 == 'paper':
            if p2 == 'Rock' or p2 == 'rock':
                return("%s wins!" % name1)
            else:
                return("%s wins!" % name2)
            
        elif p1 == 'Scissors' or p1 == 'scissors':
            if p2 == 'Paper' or p2 == 'paper':
                return("%s wins!" % name1)
            else:
                return("%s wins!" % name2)
            
        else:
            print("Check your fucking spelling. Try again.")
            decision()
            
    print(compare(p1_choice, p2_choice, player1, player2))

    restart = input("Would you like to play again?(y/n) ")
    if restart == 'n':
        break