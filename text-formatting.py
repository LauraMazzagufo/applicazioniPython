print("Super Subroutine")
print()

def color_print(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="black":
    print("\033[0;30m", word, sep="", end="")
  elif color=="green":
    print("\033[0;32m", word, sep="", end="")
  elif color=="blue":
    print("\033[0;34m", word, sep="", end="")
  elif color=="yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color=="purple":
    print("\033[0;35m", word, sep="", end="")
  elif color=="brown":
    print("\033[0;33m", word, sep="", end="")
  elif color=="gray":
    print("\033[0;30m", word, sep="", end="")
  else:
    print("[Sorry, I don't know this color.]", end=" ")
    print("\033[0m", word, sep="", end="")
    
color = input("What color do you want to use? > ")
  
print("Write a subroutine that writes ", sep="", end="")
color_print(color, "text in color")
print("\033[0m", ". All it will do is print out the text in ", sep="", end="")
color_print(color, "that color")
print("\033[0m", "and turn the color back to normal when it's finished.", end=" ") 
print("Control 'end' and 'sep' so there are not random symbols or spaces.\n Remember: by default, at the end of every print statement, the computer clicks 'enter', so you can change this with the content of 'end'. \t By 'sep', instead, you insert short separator to avoid double spaces.", sep="")