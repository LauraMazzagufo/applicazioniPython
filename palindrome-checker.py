print("🌟Palindrome Checker🌟")

word = str(input("Input a word: > "))

def reverse(word):
  if len(word) >= 1:
  
    if word[0] == word[-1]:
      reverse(word[1:-1])
    else:
      print("This word is not a palindrome!")
  
  else:
    print(f"The word is a palindrome!")

reverse(word)
