#### Find the treasure ####

print("Welcome to the Treasure Island!")
print( "Your mission is to find the treasure")

      
choice1 = input("You are at the crossroad. Where do you want to go? \n Type 'left' or 'right'. ").lower()

if choice1 == "left":
    choice2 = input("You are at the crossroad. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n" ).lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One read, one yellow, one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It is a room full of fire. GAME OVER!")
        elif choice3 == "yellow":
            print("You found the treasure! YOU WIN!")
        elif choice3 == "blue":
            print("It is a room full of water. GAME OVER!")
        else:
            print("You choose a door that does not exist!") 
    else:
        print("You got attacked. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")
