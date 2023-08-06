#Create subroutines that will roll a dice 
#with any number of sides (essentially as big of a number as you like). 
#Write one subroutine with one parameter that allows us 
#to call a function (such as rollDice).

import random
print("Infinity Dice 🎲")

sides = int(input("How many sides?"))
answer = "yes"
 
def rollDice(sides):
  number = random.randint(1, sides)
  print("You rolled", number)
  print()

while answer == "yes": 
  rollDice(sides)
  answer = input("Roll again? ")

print("Ok, bye!")