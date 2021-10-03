from random import choice, randint

username = []

with open("./english-adjectives.txt", "r") as a:    adjs = a.readlines()
with open("./english-nouns.txt", "r") as b:    nouns = b.readlines()

caps = input("Enter yes if you want the 2 words to be capitalized and no if you don't: ").lower()
under = input("Enter yes if you want an underscore between the 2 words: ").lower()
nums = input("Enter yes if you want numbers at the end of the username: ").lower()

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

    except ValueError:

        print("Please enter a valid value.")

for item in username:

    print(item.strip("\n"), end="")

print()