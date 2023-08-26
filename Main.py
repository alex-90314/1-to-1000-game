import os
import random as rand
import time

from Custom_functions import roman_numeral, blank_list

#clear the console and show the instructions
os.system("cls")
print('''Welcome to the show.
The instructions are as follows:
The game has 20 slots which you will populate using numbers that are randomly generated and given to you from 1-1000.
If you get a number higher than the previous numbers and there are no slots for it to go into, you will lose :)
''')

time.sleep(1)
print ("Let's Go! (Press Enter to continue)")
next_game = input() #holds the player until they press enter so they have time to read the rules

#clear the screen to start the game
os.system("cls")
    
blank_list()

numbers_gened = []

for i in range(20):
    number_gen = rand.randint(1,1000)
    print(f"\nHere's your number: {number_gen}")
    numbers_gened.append(number_gen)
    placement = int(input("Where would you like to put it? "))
    roman_numeral(placement)