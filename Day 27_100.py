import random
import time

def rollDice(sides_of_dice):
    return random.randint(1,sides_of_dice)

def createCharacter():
    characterName = input("Name Your Legend: ")
    characterType = input("Character Type (Human, Elf, Wiard, Orc): ")
    return characterName + "--" + characterType

def createCharacterHealth():
    characterHealth = ( rollDice(6) * rollDice(12) ) / 2  + 10
    return characterHealth

def createCharacterStrength():
    characterStrength = ( rollDice(6) * rollDice(12) ) / 2  + 12
    return characterStrength

while True:
    print("Character Builder\n")
    character_NameAndType = createCharacter()
    print()
    print(f"{character_NameAndType.split('--')[0]}")
    print(f"HEALTH: {createCharacterHealth()}")
    print(f"STRENGTH: {createCharacterStrength()}")
    time.sleep(5)
    choice = input("Do you want to continue: ?")
    if choice == "no":
        break

