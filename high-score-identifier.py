# Create a high score table
# Read in the data from the high.score file
# Identify which of those users had the highest score. Automatically! (Not you doing it!)
# Output the name and score of the winner.

import os
while True:
  f = open("high.score.txt", "a+")
  initials = input("Type your 3 letters initials: > ").upper()
  score = int(input("Type your score: > "))
  f.write(f"{initials}\t{score}\n")
  f.close()
  menu = input("Added to high score table. Have you finished entering data? (Y/N) > ").upper()
  if menu == "Y":
    break
  else:
    os.system("clear")
    continue
print("File generated!")

f = open("high.score.txt", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != [] :
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore, "points.")  