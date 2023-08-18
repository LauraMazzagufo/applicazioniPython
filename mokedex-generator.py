#This challenge is all about using dictionaries to create a game about small creatures that you have captured, enslaved, and forced to fight for your amusement. You monster.

#Create a dictionary to store the details of your, ahem, MokéBeast.
mokedex = {"name": None, "type": None, "Special Move": None, "HP": None, "MP": None}

#Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP. 
for name, value in mokedex.items():
  mokedex[name] = input(f"Type the {name} of your monster: > ").strip().title()

print("MokéBeast")
print()

#Output the beast's details. Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.
if value == "fire" or value == "fuoco":
  print('\033[31m', end='') #red
elif value == "water" or value == "acqua":
  print('\033[34m', end='') #blue
elif value == "earth" or value == "terra":
  print('\033[32m', end='') #green
elif value == "air" or value == "aria":
  print('\033[37m', end='') #grey

for name, value in mokedex.items():
  print(f"{name}: {value}")
