from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("""Benvenuti al gioco SASSO-CARTA-FORBICI!

Ecco cosa fare: a turno, scrivete:
S per SASSO
C per CARTA
F per FORBICI
e scoprite chi ha vinto!
PS: non crediamo che F per FUOCO sia parte di questo gioco. Non ci piacciono queste trovate moderne!""")
print()
player_1 = input("Giocatore 1, cosa scegli? > ")
player_2 = input("Giocatore 2, cosa scegli? > ")

if (player_1 == "S") and (player_2 == "S"):
  print("Avete scelto entrambi SASSO! Parità!")
elif (player_1 == "C") and (player_2 == "C"):
  print("Avete scelto entrambi CARTA! Parità!")
elif (player_1 == "F") and (player_2 == "F"):
  print("Avete scelto entrambi FORBICI! Parità!")
elif (player_1 == "S"):
  if player_2 == "C":
    print("Giocatore 2, hai vinto! CARTA batte SASSO!")
  elif player_2 == "F":
    print("Giocatore 1, hai vinto! SASSO batte FORBICI!")
elif (player_1 == "C"):
  if player_2 == "S":
    print("Giocatore 1, hai vinto! CARTA batte SASSO!")
  elif player_2 == "F":
    print("Giocatore 2, hai vinto! FORBICI batte CARTA!")
elif (player_1 == "F"):
  if player_2 == "C":
    print("Giocatore 1, hai vinto! FORBICI batte CARTA!")
  elif player_2 == "S":
    print("Giocatore 2, hai vinto! SASSO batte FORBICI!")
else:
  print("Errore nella selezione. Ricorda che puoi rispondere solo S, C o F: hai usato le maiuscole? Riprova!")