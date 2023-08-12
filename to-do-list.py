#Create your own to do list manager.

import os, time
print("To Do List Manager")
myList = []

def printList():
  print() 
  for item in myList:
    print(item)
  print()

while True:
  menu = input("Do you want to view, add, or edit your to do list?: ")
  if menu == "add" or menu == "Add":
    item = input("Who should I add to the list?: ")
    myList.append(item)
  elif menu == "edit" or menu == "Edit":
    item = input("What item did you complete?: ")
    if item in myList:
      myList.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu == "view" or menu == "View":
    os.system("clear")
    print("TO DO LIST:")
    printList()
    exit = input("Exit?: ")
    if exit == "yes":
       break
    else:
      continue
time.sleep(2)
os.system("clear")
print("Bye!")