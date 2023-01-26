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

print("BATTLE TIME\n")
character_first_name = createCharacter()
character_first_health = createCharacterHealth()
character_first_strength = createCharacterStrength()

print(f"\n{character_first_name}")
print(f"HEALTH: {character_first_health}")
print(f"STRENGTH: {character_first_strength}")
print("\nWho they are battling ?\n")

character_second_name = createCharacter()
character_second_health = createCharacterHealth()
character_second_strength = createCharacterStrength()

print(f"\n{character_second_name}")
print(f"HEALTH: {character_second_health}")
print(f"STRENGTH: {character_second_strength}")
print("")

character_strength_diff = 0
if character_first_strength > character_second_strength:
    character_strength_diff = round(character_first_strength - character_second_strength)
else :
    character_strength_diff = round(character_second_strength - character_first_strength)

battle_round = 1

while True:
    print("BATTLE TIME")
    print(f"The battle begins! Round - {battle_round}")

    character_first_roll_dice = rollDice(6)
    character_second_roll_dice = rollDice(6)

    if character_first_roll_dice > character_second_roll_dice:
        character_second_health = character_second_health - character_strength_diff
        print(f"{character_first_name.split('--')[0]} wins round {battle_round}.")
        print(f"{character_second_name.split('--')[0]} takes a hit with {character_strength_diff} damage")
    else:
        character_first_health = character_first_health - character_strength_diff
        print(f"{character_second_name.split('--')[0]} wins round {battle_round}.")
        print(f"{character_first_name.split('--')[0]} takes a hit with {character_strength_diff} damage")

    if character_first_health < 0:
        print(f"The character {character_second_name} has won the entire battle!")
        break
    elif character_second_health < 0:
        print(f"The character {character_first_name} has won the entire battle!")
        break
    else:
        pass
    time.sleep(2)
    battle_round = battle_round + 1
