# Ideas storage system
# Your idea storage system should:
#1. Prompt the user to add an idea, or load a random one.
#2. Choosing 'Add an idea' results in:
# - A prompt for the user to input their idea.
# - Add the idea to a text file called 'my.ideas'.
# - Add the idea in append mode, with every new idea on a brand new line.
#3. Choosing 'Load random' results in:
# - Load the list of ideas.
# - Choose one at random.
# - Display it on screen for a few seconds.
# - Return to the menu.

import os, time, random

def create_idea():
  print("Creating new idea to storage.")
  idea = input("Please, type your idea: > ")
  f = open("my.ideas.txt", "a+")
  f.write(f"- {idea}\n")
  f.close()
  print("Nice! Your idea has been stored.")
  time.sleep(2)
  os.system("clear")

def read_ideas():
  print("Loading the list of ideas...")
  time.sleep(1)
  f = open("my.ideas.txt", "r")
  list_ideas = f.read().split("\n")
  f.close()
  max = len(list_ideas)-1
  n = random.randint(0,max)
  idea = list_ideas[n]
  print(f"Your random idea is:\n{idea}")
  time.sleep(4)
  os.system("clear")

print("🌟Idea Storage🌟\nWelcome to ideas storage system!")
print()
while True:
  menu = input("Make your choice:\n1 = Add an idea\n2 = Load a random one\n3 = Exit\n > ")
  if menu == "1":
    create_idea()
    continue
  elif menu == "2":
    read_ideas()
    continue
  elif menu == "3":
    print("Ok, bye bye!")
    break
  else:
    print("Incorrect answer, please type '1', '2' or '3'.") 
    time.sleep(2)
    os.system("clear")
    continue