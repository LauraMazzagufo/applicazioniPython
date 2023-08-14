#This is the challenge you're looking for. This program will generate your Star Wars Name.
print("🌟Star Wars Name Generator🌟")
print()

first_name = input("Type your first name: > ")
last_name = input("Type your last name: > ")
cut_first_name = (first_name[0:3:1]).strip().capitalize()
cut_last_name = (last_name[0:3:1]).strip().lower()
starwars_first_name = f"{cut_first_name}{cut_last_name}"

mother_name = input("Type your mother's maiden name: > ")
place_name = input("Type the name of the city where you were born: > ")
cut_mother_name = (mother_name[0:2:1]).strip().capitalize()
cut_place_name = (place_name[-3::1]).strip().lower()
starwars_last_name = f"{cut_mother_name}{cut_place_name}"

print()
print(f"Your Star Wars name is {starwars_first_name} {starwars_last_name}.")
