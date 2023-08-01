print("WELCOME TO THE 🪄  G U E S S  T H E  N U M B E R 🪄  GAME!")
print()
print("Please, pick a number between 0 and 1,000,000")
number = int(input("> "))
counter = 0
while True:
  if (number < 556920) and (number > 0):
    print("The number is too low. Please try again.")
    counter +=1
    number = int(input("> "))
  elif (number > 556920) and (number < 1000000):
    print("The number is too high. Please try again.")
    counter +=1
    number = int(input("> "))
  elif number==556920:
    print("You guessed it! 💫 Great job!")
    break
  else:
    print("Did you type a number between 0 and 1000000? Please try again!")
    number = int(input("> "))
print("You guessed the number in only", counter, "attempts!")  