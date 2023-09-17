#videogame inventory
import os, time

inventory = []
try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except Exception as err:
  #print("ERROR: file not found. Creating new file.")
  #print(err)
  pass

def add():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to add: > ").capitalize()
  inventory.append(item)
  print(f"{item} has been added to your inventory.")
  #save to file
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()

def remove():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to remove: > ").capitalize()
  if item in inventory:
    inventory.remove(item)
    print(f"{item} has been removed from your inventory.")
  else:
    print(f"No {item} found in the inventory.")
  #save to file
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()

def view():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to view: > ").capitalize()
  if item in inventory:
    #counter = 0
    #for i in inventory:
      #if i == item:
        #counter += 1
    counter = inventory.count(item)
    print(f"You have {counter} {item}")
  else:
    print(f"No {item} found in the inventory.")
  #save to file
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()

while True:
  time.sleep(1)
  os.system("clear")
  print("🌟RPG Inventory🌟")
  menu = input("1: Add\n2: Remove\n3: View\n4: Exit\n> ")
  if menu == "1":
    add()
    continue
  elif menu =="2":
    remove()
    continue
  elif menu =="3":
    view()
    continue
  elif menu == "4":
    break
  else:
    print("Invalid selection. Please try again.")
    continue
print()
print("Bye!")
    

