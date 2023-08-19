import random, os, time
print("Bingo starts!")

#2Dlist vuota
bingo = []

#funzione che assegna numeri casuali
def ran(): 
  n = random.randint(1,90)
  return n

def createCard():
  global bingo
  
  #lista semplice di numeri (saranno 8)
  numbers = []
  
  #ciclo in cui inserisco numeri casuali nella lista semplice
  for i in range(8):
    numbers.append(ran())
  
  #riordino i numeri nella lista
  numbers.sort()
  
  #assegno ogni numero della lista semplice a una specifica posizione della 2Dlist
  bingo = [ [ numbers[0], numbers[1], numbers[2]],
            [ numbers[3], "BINGO", numbers[4] ],
            [ numbers [5], numbers[6], numbers[7]]
          ]

def printCard():
  print("Here your Bingo Card:")
  print("\n--------------------------------------")
  #stampo bingo in modo che vada a capo ad ogni riga 
  for row in bingo: 
    #loops to the next row when the end of the current one is reached
     for item in row: 
      # item refers to each item in the column for that row
      print(f"{item:^10}", end=" | ") 
        # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.
     print("\n--------------------------------------") 
      # prints a line between rows
  print()

while True:
  #ciclo per scegliere un'altra cartella
  menu = input("Do you want to have a new card? y/n: ").lower()
  if menu == "y":
    os.system("clear")
    createCard()
    printCard()
    continue
  else:
    break

while True:
  # ciclo per estrarre i numeri
  print("Let's draw a number!")
  newNumber = ran()
  print(f"Next number: {newNumber}")
  for row in range(3): # ciclo in ciascuna delle tre righe
    for item in range(3): #ciclo in ciascun item della riga
      if newNumber == bingo[row][item]:
        print("You got it!")
        bingo[row][item] = "X" # sostituisce il numero con una X
        
  printCard()
  counter = 0 # variabile per contare le X
  for row in bingo:
    for item in row:
      if item=="X":
        counter+=1
  if counter == 8:
    print("You have won!")
    break
  time.sleep(3)
  os.system("clear")