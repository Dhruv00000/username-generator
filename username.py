# Importing the necessary functions from modules.
from random import choice, randint

# Initializing the output string.
username = ""

# Getting the adjectives and nouns.
with open("./english-adjectives.txt", "r") as a:

    adjs = a.readlines()

with open("./english-nouns.txt", "r") as b:

    nouns = b.readlines()

# Getting all the config inputs from the user.
caps = input("Enter yes if you want the 2 words to be capitalized and no if you don't: ").lower()
under = input("Enter yes if you want an underscore between the 2 words: ").lower()
nums = input("Enter yes if you want numbers at the end of the username: ").lower()

# Adding onto the empty string according to the user input.
if caps != "no":

    adj, noun = choice(adjs).capitalize(), choice(nouns).capitalize()

else:

    adj, noun = choice(adjs), choice(nouns)

username += adj
username += f"_{noun}" if under == "yes" else noun

if nums != "no":

    try:

        # Adding random numbers of the length that the user wants next to the username.
        digits = int(input("Enter the number of digits that you want the number at the end of your username should be of: "))
        username += "".join(str(randint(0,10)) for _ in range(digits))

    # Preventing the crash if the user enters a string instead of an integer.
    except ValueError:

        print("Please enter a valid value.")

# Output
print(username)