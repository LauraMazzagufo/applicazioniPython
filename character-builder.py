#Welcome to your first video game creation. 
#You will create a video game that creates a character's health and attack stats...
#along with an epic name for your character.

import random, os, time

def rollDice(sides):
  number = random.randint(1, sides)
  return number

def character_name():
  name = input("Name Your Legend: > ")
  type = input("Character Type (Human, Elf, Wiard, Orc): > ")
  print()
  print(name)
  time.sleep(1)
  print(type)
  time.sleep(1)

def character_health():
  dice1 = rollDice(6)
  dice2 = rollDice(12)
  health = ((dice1*dice2)/2)+10
  return health

def character_strength():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,12)
  strenght = ((dice1*dice2)/2)+12
  return strenght


while True:
  os.system("clear")
  print("Character Builder")
  print()
  time.sleep(1)
  character_name()
  health = int(character_health())
  strenght = int(character_strength())
  print("HEALTH: ", health)
  time.sleep(1)
  print("STRENGTH: ", strenght)
  time.sleep(1)
  print("May your name go down in Legend...")
  time.sleep(2)
  go_on = input("Do you want to create another character (yes/no): > ")
  if go_on == "yes":
    continue
  elif go_on == "no":
    break
  else:
    print("Invalid answer.")
    break
print("Bye!")
