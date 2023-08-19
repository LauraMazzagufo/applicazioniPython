def prettyPrint():
  print() 
  # Puts a blank row at the top
  for row in listOfShame: 
    #loops to the next row when the end of the current one is reached
     for item in row: 
      # item refers to each item in the column for that row
      print(f"{item:^10}", end=" | ") 
        # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.
     print() 
    # prints a blank line between rows

listOfShame = [] 
# Creates an empty list.

while True: 
# Starts a never ending loop (until we end it)
  menu = input("Add or Remove? a/r: ") 
  # Gives the user a choice prompt and stores their input.
  if(menu.strip().lower()[0]=="a"): 
   # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    # Get the user input.
  
    row = [name, age, pref] 
    # Assigns the 3 variables into a single row.
  
    listOfShame.append(row) 
    # Adds the contents of the row variable at the end of the list

  elif(menu.strip().lower()[0]=="r"): 
    # If the user doesn't choose 'a', run this new remove code instead.
    name = input("What is the name of the record to delete?") # Get the input of a name
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  else:
    print("Please, type 'a' or 'r' only.")
    continue
    
  exit = input("Exit? y/n: ") 
  # Get user choice to quit, yes or no?

  if (exit.strip().lower()[0] == "y"): 
    # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
    break # break ends a loop and jumps to the next line of code that is not part of the loop.
    
prettyPrint() 
# Call the prettyPrint subroutine instead of printing the list directly.