import random

def rollDice(sides_of_dice):
    return random.randint(1,sides_of_dice)

def rollDice_six_eight():
    roll_six = rollDice(6)
    roll_eight = rollDice(8)
    health_stats = roll_six * roll_eight
    return health_stats

for i in range(1,3):
    name = input("name your character")
    print(f"their health is {rollDice_six_eight()}")
