#create an editable dictionary such that the user can change its values
placed = {
  1: "",
  2: "",
  3: "",
  4: "",
  5: "",
  6: "",
  7: "",
  8: "",
  9: "",
  10: "",
  11: "",
  12: "",
  13: "",
  14: "",
  15: "",
  16: "",
  17: "",
  18: "",
  19: "",
  20: ""
}

#create a blank list 1-20
def blank_list() -> list:
  '''
  Creates a blank list by printing numbers 1-20 in the "#: " format.
  '''
  x = 1
  for i in range(20):
    print(f"{x}.")
    x+=1