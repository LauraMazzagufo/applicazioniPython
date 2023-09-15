import os, time
orders = []

try:  
  f = open("pizza-shop.txt","r")
  orders = eval(f.read())
  f.close()
except Exception as err:
  print("ERROR: Unable to load. No existing pizza list, using a blank list")
  print("(", err, ")")
  print()

#subrutine per aggiungere una pizza alla lista
def add():
  time.sleep(1)
  os.system("clear")
  name = input("Type your name, please: > ")
  
  while True:
    try:
      quantity = int(input("How many pizzas? > "))
      break
    except:
      print("You must input a numerical character, try again.")
      continue

  price = 0
  size = input("What size (S-M-L)? > ").capitalize()
  if size == "S":
    price = 5
  elif size == "M":
    price = 7
  else:
    price = 10

  cost = price * quantity
  row = [name, quantity, size, cost]
  orders.append(row)


def view():
  i1 = "Name"
  i2 = "Quantity"
  i3 = "Size"
  i4 = "Total cost"
  print(f"{i1:^15}{i2:^15}{i3:^15}{i4:^20}")
  for row in orders:
    print(f"{row[0]:^15}{row[1]:^15}{row[2]:^15}{row[3]:^20}")
  time.sleep(4)
  

print("🌟Dave's Dodgy Pizzas🌟")

while True:
  menu = input("1: Add a pizza\n2: View Pizzas list\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    print("Uncorrect answer, please type '1' or '2'\n> ")
    continue

  time.sleep(1)
  os.system("clear")

  ###### Salvataggio su file ####
  f = open("pizza-shop.txt", "w")
  f.write(str(orders))
  f.close()
