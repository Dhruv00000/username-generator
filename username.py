# Importing the necessary functions from modules.
from random import choice, randint

# Initializing an empty list for all the parts of the username.
username = []

# Getting the lists of adjectives and nouns from the txt files.
with open("./english-adjectives.txt", "r") as a:    adjs = a.readlines()
with open("./english-nouns.txt", "r") as b:    nouns = b.readlines()

# Getting the user input.
caps = input("Enter yes if you want the 2 words to be capitalized and no if you don't: ").lower()
under = input("Enter yes if you want an underscore between the 2 words: ").lower()
nums = input("Enter yes if you want numbers at the end of the username: ").lower()

# Generating the username part-by-part according to the user input.
if caps != "no":

    adj, noun = choice(adjs).capitalize(), choice(nouns).capitalize()

else:

    adj, noun = choice(adjs), choice(nouns)

username.append(adj)
username.append(f"_{noun}" if under == "yes" else noun)

if nums != "no":

    try:

        digits = int(input("Enter the number of digits that you want the number at the end of your username should be of: "))
        username.append("".join(str(randint(0,10)) for _ in range(digits)))

    # If the user enters a string instead of an integer, this message is printed out instead of the program crashing with an error.
    except ValueError:

        print("Please enter a valid value.")

# Output.
for item in username:

    print(item.strip("\n"), end="")

print()