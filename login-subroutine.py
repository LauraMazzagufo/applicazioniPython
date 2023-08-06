def login():
  while True:
    user = input("What is your username?: >")
    pw = input("What is your password?: >")
    if (user == "david") and (pw == "baldies4life"):
      print("Welcome, David!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

print("Login System")
login()
print(":-)")
