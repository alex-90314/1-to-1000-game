roman_numeral = {
  1: "I",
  2: "II",
  3: "III",
  4: "IV",
  5: "V",
  6: "VI",
  7: "VII",
  8: "VIII",
  9: "VIII",
  10: "X",
  11: "XI",
  12: "XII",
  13: "XIII",
  14: "XIV",
  15: "XV",
  16: "XVI",
  17: "XVII",
  18: "XVIII",
  19: "XVIIII",
  20: "XX"
}
  
def blank_list(): #create a blank list 1-20
  x = 1
  for i in range(20):
    print(f"{x}.")
    x+=1