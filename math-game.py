#Test your family and friends on their multiplication knowledge
print("Math Game!")
print()
score = 0
number = int(input("Name your multiples: > "))
print()
for i in range(1, 11):
  correct_answer = number*i
  print(i, "X", number, "= ?")
  user_answer = int(input(" > "))
  if user_answer == correct_answer:
    print("Correct! You gained a point!")
    print()
    score +=1
  else:
    print("Nope. The answer was ", correct_answer)
    print()
print("---")
print("You scored", score, "out of 10.")
if score == 10:
  print("🥳")
