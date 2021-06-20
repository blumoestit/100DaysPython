#### Pizza Delivery ####
#### Size ####

print("Welcome to Python Pizza Delivery!")

size = input("What pizza size do you want? S, M, or L ")
add_pepperoni = input("Do you wat pepperoni?) Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 6
elif size == "M":
    bill += 12
else:
    bill += 18
    

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        
if extra_cheese == "Y":
    if size == "S":
        bill += 4
    else:
        bill += 6

print(f"Your final bill is ${bill}")
    
