#Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.
#For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

print("30 Days Down")
print()
day=1
while day < 31:
  feeling = input(f"What do you think about day {day} of the 30 day of challenges so far?")
  print()
  print(f"""Day {day}:
  {feeling}
  \t \t \t \t \t You thought Day {day} was {feeling}.""")
  print()
  day +=1
print("Thank you! Bye!")

### 2nd answer:

print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()
