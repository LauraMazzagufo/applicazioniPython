import random

print("WELCOME TO THE 🪄  G U E S S  T H E  N U M B E R 🪄  GAME!")
print()

counter = 0
startagain = "run"

while startagain=="run":
  correct_number = random.randint(1, 100)
  print("Please, pick a number between 0 and 100")
  number = int(input("> "))
  
  while True:
    if (number < correct_number) and (number > 0):
      print("The number is too low. Please try again.")
      counter +=1
      number = int(input("> "))
    elif (number > correct_number) and (number < 100):
      print("The number is too high. Please try again.")
      counter +=1
      number = int(input("> "))
    elif number==correct_number:
      print("You guessed it! 💫 Great job!")
      break
    else:
      print("Did you type a number between 0 and 100? Please try again!")
      number = int(input("> "))
  print("You guessed the number in only", counter, "attempts!") 
  print()
  startagain = input("Type 'run' to try again with a different number. > ")
  continue
print("Ok, bye!")
