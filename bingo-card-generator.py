import random

#2Dlist vuota
bingo = []

#funzione che assegna numeri casuali
def ran(): 
  n = random.randint(1,90)
  return n

#lista semplice di numeri (saranno 8)
numbers = []

#ciclo in cui inserisco numeri casuali nella lista semplice
for i in range(8):
  numbers.append(ran())
#counter = 0
#while counter < 8:
#    numbers.append(ran())
#    counter +=1

#riordino i numeri nella lista
numbers.sort()

#assegno ogni numero della lista semplice a una specifica posizione della 2Dlist
bingo = [ [ numbers[0], numbers[1], numbers[2]],
          [ numbers[3], "BINGO", numbers[4] ],
          [ numbers [5], numbers[6], numbers[7]]
        ]
#stampo bingo in modo che vada a capo ad ogni riga
#for row in bingo:
#  print(row)
print(f"""{bingo[0][0]}\t|  {bingo[0][1]}\t| {bingo[0][2]}
----------------
{bingo[1][0]}\t| {bingo[1][1]}\t| {bingo[1][2]}
----------------
{bingo[2][0]}\t|  {bingo[2][1]}\t| {bingo[2][2]}""")