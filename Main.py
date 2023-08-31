import os
import random as rand
import time
from pprint import pformat, pprint

from Custom_functions import blank_list, clear, placed


#clear the screen to start the game
def clear():
    os.system("cls")
    os.system("clear")

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

clear() #clear the console to prepare to dislay the game

blank_list()

for i in range(20):
    while i>0:
        clear() #clear the console to display a new list
    number_gen = rand.randint(1,1000)
    print(f"\nHere's your number: {number_gen}")
    placement = int(input("Where would you like to put it? "))
    if placed[placement] != "":
        print("You Lost")
    placed[placement] = number_gen
    placed_fix = pformat(placed)
    chars_to_remove = ["{", "}", "'"]
    for char in chars_to_remove:
        placed_fix = placed_fix.replace(char, "")
    print(placed_fix)