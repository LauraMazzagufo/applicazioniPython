#Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
myWebsite = {"name": None, "URL": None, "descriprion": None, "rating": None}

#Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
for name,value in myWebsite.items():
  myWebsite[name] = input(f"Type the {name} of your website: > ")

#Finally, output the whole dictionary (keys and values).
print()
for name,value in myWebsite.items():
  print(f"{name}: {value}")