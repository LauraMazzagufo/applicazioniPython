# Let's make an agenda for today
import os, time
myAgenda = []

def printList():
  for i in myAgenda:
    print(i)
    time.sleep(1)
    print()

while True:
  menu = input("Add or remove event?: ")
  if menu == "add" or menu == "Add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
    os.system("clear")
    printList()
  elif menu == "remove" or menu == "Remove":
    removedItem = input("What do you want to remove?: ")
    myAgenda.remove(removedItem)
    os.system("clear")
    printList()
