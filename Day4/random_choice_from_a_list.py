#### LISTS ####
import random

names_str = "Dor, Rem, Mif, Fas, Sol, Laa, Sid"
names = names_str.split(", ")

# Chose a person from a list randomly (1)
random_name = random.randint(0, len(names) - 1)
person = names[random_name]
print("Who will pay today: ", person)

# Chose a person from a list randomly (2)
print("Who will pay today: ", random.choice(names))