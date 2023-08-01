from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("""Benvenuti al gioco SASSO-CARTA-FORBICI!

Ecco cosa fare: a turno, scrivete:
S per SASSO
C per CARTA
F per FORBICI
e scoprite chi ha vinto! Vince la partita chi totalizza per primo 3 punti.
PS: non crediamo che F per FUOCO sia parte di questo gioco. Non ci piacciono queste trovate moderne!""")
print()

punteggio_1 = 0
punteggio_2 = 0
  
while (punteggio_1 < 3) and (punteggio_2 < 3):

  player_1 = input("Giocatore 1, cosa scegli? > ")
  player_2 = input("Giocatore 2, cosa scegli? > ")
  
  if (player_1 == "S") and (player_2 == "S"):
    print("Avete scelto entrambi SASSO! Parità!")
    print()
  elif (player_1 == "C") and (player_2 == "C"):
    print("Avete scelto entrambi CARTA! Parità!")
    print()
  elif (player_1 == "F") and (player_2 == "F"):
    print("Avete scelto entrambi FORBICI! Parità!")
    print()
  elif (player_1 == "S"):
    if player_2 == "C":
      print("Giocatore 2, hai vinto questo round! CARTA batte SASSO!")
      punteggio_2 +=1
      print()
    elif player_2 == "F":
      print("Giocatore 1, hai vinto questo round! SASSO batte FORBICI!")
      punteggio_1 +=1
      print()
  elif (player_1 == "C"):
    if player_2 == "S":
      print("Giocatore 1, hai vinto questo round! CARTA batte SASSO!")
      punteggio_1 +=1
      print()
    elif player_2 == "F":
      print("Giocatore 2, hai vinto questo round! FORBICI batte CARTA!")
      punteggio_2 +=1
      print()
  elif (player_1 == "F"):
    if player_2 == "C":
      print("Giocatore 1, hai vinto questo round! FORBICI batte CARTA!")
      punteggio_1 +=1
      print()
    elif player_2 == "S":
      print("Giocatore 2, hai vinto questo round! SASSO batte FORBICI!")
      punteggio_2 +=1
      print()
  else:
    print("Errore nella selezione. Ricorda che puoi rispondere solo S, C o F: hai usato le maiuscole? Riprova!")
    continue
print("Abbiamo un vincitore!")
if punteggio_1==3:
  print("Giocatore 1, hai vinto la partita!")
else:
  print("Giocatore 2, hai vinto la partita!")