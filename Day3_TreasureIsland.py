def treasureIsland():
    # print('''
    # *******************************************************************************
    #           |                   |                  |                     |
    #  _________|________________.=""_;=.______________|_____________________|_______
    # |                   |  ,-"_,=""     `"=.|                  |
    # |___________________|__"=._o`"-._        `"=.______________|___________________
    #           |                `"=._o`"=._      _`"=._                     |
    #  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    # |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    # |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
    #           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    #  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    # |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    # |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    # ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    # /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    # ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    # /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    # ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    # /______/______/______/______/______/______/______/______/______/______/_____ /
    # *******************************************************************************
    # ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    input1 = input("You approach a fork in the road. Go left or right? Type 'left' or 'right' to proceed.\n").lower()
    if input1.lower() == "left":
        input2 = input("You go left. You find a river in front of you. Swim across or wait for a boat to arrive? Type 'swim' or 'wait' to proceed.\n").lower()
        if input2.lower() == "wait":
            input3 = input("Across the river, you come across a house with three doors, colored red, yellow, or blue. Which door will you enter? Type 'red', yellow', or 'blue' to proceed.\n").lower()
            if input3.lower() == 'red':
                print("The room was filled with lava! You've been burned. Game over!")
            elif input3.lower() == "blue":
                print("The room was filled with angry bees. You're allergic to bees. You've been stung! Game over!")
            elif input3.lower() == "yellow":
                print("You've discovered a treasure chest! You open it and inside you find it overflowing with gold. You win!")
        else:
            print("The rapid current of the river takes you under. You are attacked by a school of hungry trout. Game over!")
    else:
        print("You go right. You notice a huntsman's trap in front of you, and carefully go around it. While doing so, you step in a different trap. Game Over!")

while True:
    print('')
    start_game = input("Would you like to play Treasure Island? type 'y' to begin!\n").lower()
    if start_game == 'y':
        treasureIsland()