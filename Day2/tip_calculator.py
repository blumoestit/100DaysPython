#### If the bill was $150.00, split between 5 people, with 12% tip. ####

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 percent? "))
people = int(input("how many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
bill_per_person = round(bill_with_tip / people, 2)

bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${bill_per_person}")

#### END ####