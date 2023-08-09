#Welcome to your first video game creation. 
#You will create a video game that creates a character's health and attack stats...
#along with an epic name for your character.
#Then, use the character generator to build an automated game battle system!

import random, os, time

def rollDice(sides):
  number = random.randint(1, sides)
  return number

def character_name():
  name = input("Name Your Legend: > ")
  return name

def character_type():
  type = input("Character Type (Human, Elf, Wiard, Orc): > ")
  return type

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
  print("⚔️ Character Builder ⚔️")
  print()
  time.sleep(1)
  name1 = character_name()
  type1 = character_type()
  print()
  print(name1)
  time.sleep(1)
  print(type1)
  time.sleep(1)
  health1 = int(character_health())
  strenght1 = int(character_strength())
  print("HEALTH: ", health1)
  time.sleep(1)
  print("STRENGTH: ", strenght1)
  time.sleep(1)

  print()
  print("Who are they battling?")
  
  print()
  time.sleep(1)
  name2 = character_name()
  type2 = character_type()
  print()
  print(name2)
  time.sleep(1)
  print(type2)
  time.sleep(1)
  health2 = int(character_health())
  strenght2 = int(character_strength())
  print("HEALTH: ", health2)
  time.sleep(1)
  print("STRENGTH: ", strenght2)
  time.sleep(2)
  
  print()
  go_on = input("Do you want to re-create another character (yes/no): > ")
  if go_on == "yes":
    continue
  elif go_on == "no":
    break
  else:
    print("Invalid answer.")
    break

print()
print("⚔️ BATTLE TIME ⚔️!")
time.sleep(1)
print()
print("The battle begins!")
time.sleep(1)
print()
rounds = 0
while True:
  score1 = rollDice(6)
  score2 = rollDice(6)
  if strenght1 >= strenght2:
    damage = strenght1 - strenght2
  else:
    damage = strenght2 - strenght1
  
  if score1 > score2:
    print(name1, "wins the blow")
    print(name2, "takes a hit, with", damage, "damage")
    print()
    time.sleep(1)
    health2 = health2-damage
  elif score2 > score1:
    print(name2, "wins the blow")
    print(name1, "takes a hit, with", damage, "damage")
    print()
    time.sleep(1)
    health1 = health1-damage
  elif score1==score2:
    print("Same score!")
    print()
    time.sleep(1)
  print(name1, "> HEALTH: ", health1)
  print(name2, "> HEALTH: ", health2)
  print()
  time.sleep(1)
  if health1 > 0 and health2 > 0:
    print("And they're both standing for the next round!")
    print("The battle continues!")
    print()
    time.sleep(1)
    rounds +=1
    continue
  else:
    if health1 <= 0:
      print("Oh no", name1, "has died!")
      print(name2, "destroyed", name1, "in", rounds, "rounds!")
      break
    elif health2 <= 0:
      print("Oh no", name2, "has died!")
      print(name1, "destroyed", name2, "in", rounds, "rounds!")
      break
print("Bye!")