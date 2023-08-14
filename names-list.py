#Create a list of people's names. Ask for first and last name (surname) separately.
#Strip any extra spaces.
#Store names in a capitalized version.
#Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
#Add those new versions to a list.
#Do not allow duplicates.
#Each time you add a new name, you should print out the full list.

import os

names = []
while True:
  first_name = input("Type the first name: > ").strip().capitalize()
  last_name = input("Type the last name: > ").strip().capitalize()
  name = f"{first_name} {last_name}"
  if name in names:
    print(f"{first_name} {last_name} is already on your list!")
    continue
  else:
    names.append(name)
  os.system("clear")
  for i in names:
    print(i)
    print()
