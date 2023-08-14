#Create your own to do list manager.

import os, time
list = []

def view():
  print()
  counter = 1
  for i in list:
    print(counter, f". {i}\n")
    counter += 1

print("TO DO LIST")
print()

while True:
  menu = input(" Do you want to view, add or remove items? > ").lower() #aggiungo questa funzione per evitare problemi con eventuali lettere maiuscole inserite dall'utente (così add = Add = ADD)

  if menu == "add":
    item = input("What imput do you want to add? > ")
    if item in list:
      print(f"{item} is already in the list!")
    else:
      list.append(item)
      print(f"Item {item} added.")
    time.sleep(2)
    os.system("clear")
  elif menu == "remove":
    item = input("What imput do you want to remove? (type 'all' to remove all items) > ")
    if item in list:
      check = input(f"Are you sure you want to remove {item}? (y/n) > ")
      if check == "y" or check == "yes":
        list.remove(item)
        print(f"Item {item} cancelled.")
      elif check == "n" or check == "no":
        print(f"{item} still present on your list.")
      time.sleep(2)
      os.system("clear")
    elif item == "all":
      list = []
      print("All items cancelled.")
      time.sleep(2)
      os.system("clear")
    else:
      print(f"No item {item} found.")
      time.sleep(2)
      os.system("clear")
  elif menu == "view":
    view()
    time.sleep(2)
    os.system("clear")
  else:
    print("Invalid answer.")
    time.sleep(2)
    os.system("clear")
    continue
    else:
      continue
time.sleep(2)
os.system("clear")
print("Bye!")
