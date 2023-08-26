import os
import random as rand
import time
from Custom_functions import roman_numeral

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

numbers_gened = []

for i in range(20):
    number_gen = rand.randint(1,1000)
    print(f"Here's your number: {number_gen}")
    numbers_gened.append(number_gen)
    placement = int(input("Where would you like to put it? "))
    roman_numeral(placement)
    print(f'''
1. {I}
2. {II}
3. {III}
4. {IV}
5. {V}
6. {VI}
7. {VII}
8. {VIII}
9. {VIIII}
10. {X}
11. {XI}
12. {XII}
13. {XIII}
14. {XIV}
15. {XV}
16. {XVI}
17. {XVII}
18. {XVIII}
19. {XVIIII}
20. {XX}
''')
