import random

dice_sides = int(input("how many sides of dice ?"))
choice = "yes"

def rollDice(sides_of_dice):

    while True:
        print(f"you rolled {random.randint(1,sides_of_dice)}")
        choice = input("Roll again ?")
        if choice == "no":
            break


rollDice(dice_sides)
