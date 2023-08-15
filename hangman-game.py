#hangman
import random

print("🌟Hangman🌟")
print()
print("""
  +---+
  |   |
      |
      |
      |
      |
=========""")

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "downton"]
letterPicked = []
counter = 0

wordChosen = random.choice(listOfWords)

while True:
  print()
  myLetter = input("Choose a letter: > ").lower()
  if myLetter in letterPicked:
    print("You've tried that letter before!")
    continue
  letterPicked.append(myLetter)
  if myLetter in wordChosen:
    print()
    print(f"Correct! Letter {myLetter} is in the word:")
  else: 
    print()
    print(f"Nope! No letter {myLetter} in the word!")
    counter +=1
    if counter == 1:
      print("""
        +---+
        |   |
        O   |
            |
            |
            |
      =========
      """)
    elif counter == 2:
      print("""
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
      """)
    elif counter == 3:
      print("""
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
      """)
    elif counter == 4:
      print("""
        +---+
        |   |
        O   |
       /|\  |
            |
            |
      =========
      """)
    elif counter == 5:
      print("""
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
      =========
      """)
      
  allLetters = True
  for i in wordChosen:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  
  if counter < 6 and allLetters == False:
    print()
    print("You've already used the following letters: ", letterPicked)
    continue
  elif counter < 6 and allLetters == True:
    print("YOU WON!")
    break
  elif counter == 6:
    print(f"You lose! The word was: {wordChosen}")
    print("""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
      =========
      """)
    break

