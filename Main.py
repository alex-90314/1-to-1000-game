import os
import random as rand
import time
from pprint import pformat, pprint

from Custom_functions import blank_list, placed

#clear the screen to start the game
def clear() -> None:
    '''
    Runs a try/except logic gate to make sure that the terminal/console is clear.
    '''
    try:
        os.system("cls")
    except:
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

def fixed_output(placed:dict) -> None:
    '''
    Outputs the placed dictionary in a beautified format using the pformat from the pretty print library. 
    '''
    placed_fix = pformat(placed)
    chars_to_remove = ["{", "}", "'", ","]
    for char in chars_to_remove:
        placed_fix = placed_fix.replace(char, "")
    print(placed_fix)

for i in range(len(placed)):
    if i>0:
        clear() #clear the console to display the new list
        fixed_output(placed)
    number_gen = rand.randint(0,1000)
    print(f"\nHere's your number: {number_gen}")
    placement = int(input("Where would you like to put it? ")) #take the user's placement input
    if (placement<0 or placement>20): #give them a chance to try again
        print("Too low/high\ntry again!\n")
        print("\nPress Enter/Return to try again")
        next_game = input()
        os.system("python3 Main.py")
    elif (placed[placement] != ""): #only losing condition
        print("You Lost trying to overwrite an old number :(\ntry again!")
        print("\nPress Enter/Return to try again")
        next_game = input()
        os.system("python3 Main.py")

    placed[placement] = number_gen