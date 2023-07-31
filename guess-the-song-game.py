print("""Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.""")
print("Never going to ______ you up.")
counter = 0
while True: 
  counter +=1
  word = input("Type the word: > ")
  if word != "give":
    print("Nope, try again.")
  else:
    break
print("Well done! It only took you", counter, "attempts.")