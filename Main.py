import os, time

#clear the console and show the instructions
os.system("cls")
print('''Welcome to the show.
The instructions are as follows:
The game has 20 slots which you will populate using numbers that are randomly generated and given to you from 1-1000.
If you get a number higher than the previous numbers and there are no slots for it to go into, you will lose :)
''')
time.sleep(1)
skip_start = input() #allows the player to skip the instructions
print ("Let's Go! (Press Enter to continue)")
next_game = input() #holds the player until they press enter so they have time to read the rules

#clear the screen to start the game
os.system("cls")
print("hi")