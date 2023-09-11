#  create a high score table
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