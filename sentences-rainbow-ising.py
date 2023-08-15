#Code the rainbow!
#Ask the user to input any sentence (string).
#Now we'll rainbow-ize (nope, me neither) it.
#As soon as the string contains an 'r', every letter from that point on should be red.
#When the computer encounters a 'b', 'g', 'p' or 'y', from there the output should be blue for 'b', green for 'g'...you get the idea.
#Loop through the string and output it (so the color continues through the loop).
#The output should change color every time it encounters a new r,g,b,p or y.

myString = input("What sentence do you wanr rainbow-ising? > \n")

for letter in myString:
  if letter.lower() == "r":
    print('\033[31m', end='') #red
  elif letter.lower() == "b":
    print('\033[34m', end='') #blue
  elif letter.lower() == "g":
    print('\033[32m', end='') #green
  elif letter.lower() == "p":
    print('\033[35m', end='') #purple
  elif letter.lower() == "y":
    print('\033[33m', end='') #yellow
  print(letter, end='')
  if letter == " ":
    print('\033[0m', end='') #back to default
