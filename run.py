import random

def swg(comp, mine):
  if (comp == mine):
    return None
  elif (comp == 's' and mine == 'g'):
    return True
  elif (comp == 'w' and  mine == 's'):
    return True
  elif (comp == 'g' and mine == 'w'):
    return True
  else:
    return False

choice = ('s', 'w', 'g')
comp = random.randint(0,2)
comp = choice[comp]
mine = input("Please select S, W or G: ")

win = swg(comp, mine)
print(f"You have chosen {mine} and the computer chosen {comp}")
if win is None:
  print("Draw")
elif win is True:
  print("Won")
else:
  print("Lost")


