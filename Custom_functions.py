def roman_numeral(number:int) -> str: #convert numbers to roman numeral
  if number == 1:
    print("I")
  elif number == 2:
    print("II")
  elif number == 3:
    print("III")
  elif number == 4:
    print("IV")
  elif number == 5:
    print("V")
  elif number == 6:
    print("VI")
  elif number == 7:
    print("VII")
  elif number == 8:
    print("VIII")
  elif number == 9:
    print("IX")
  elif number == 10:
    print("X")
  else:
    print("Number must be between 1 and 20")
  
def blank_list(): #create a blank list 1-20
  x = 1
  for i in range(20):
    print(f"{x}.")
    x+=1