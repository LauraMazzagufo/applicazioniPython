# create a contact card using a dictionary:
#Ask the user to input their name, date of birth, telephone number, email and physical address.
#Store it all in a dictionary.
#Print it out in a nice way once its stored.

print("🌟Contact Card🌟")

contactCard = {"name": "", "date": "", "telephone": "", "email": "", "address": ""}

yourName = input("Input your name > ").strip().capitalize()
yourDate = input("Input your date of birth > ").strip()
yourTelephone = input("Input your telephone number > ")
yourEmail = input("Input your email > ").strip().lower()
yourAddress = input("Input your address > ")

contactCard["name"] = yourName
contactCard["date"] = yourDate
contactCard["telephone"] = yourTelephone
contactCard["email"] = yourEmail
contactCard["address"] = yourAddress

print(f"Hi {contactCard['name']}.\n Our dictionary says that you were born on {contactCard['date']}, we can call you on {contactCard['telephone']}, email {contactCard['email']}, or write to {contactCard['address']}.")