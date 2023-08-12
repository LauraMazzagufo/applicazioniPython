#Create a list that stores greetings in different languages. Start with the language you speak.
import random
greetings = ["ciao!", "hello!", "salut!", "hallo!", "hola!", "yassou!"]
number = int(random.randint(0,5))
print(f"I'll say to you: {greetings[number]}")