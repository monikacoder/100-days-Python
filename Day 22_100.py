import random


correct_number = random.randint(1,1000)
count_attempts = 0

while True:
    guess_number = int(input("guess the number?:"))
    count_attempts += 1

    if guess_number == correct_number:
        print("correct")
        break
    elif guess_number < correct_number:
        if (correct_number - guess_number) > 200:
            print("too much low")
        elif (correct_number - guess_number) > 100:
            print("too low")
        elif (correct_number - guess_number) > 10:
            print("lower")
        elif (correct_number - guess_number) > 0:
            print("lower but closer")
    elif guess_number > correct_number:
        if (guess_number - correct_number) > 200:
            print("too much high")
        elif (guess_number - correct_number) > 100:
            print("too high")
        elif (guess_number - correct_number) > 10:
            print("higher")
        elif (guess_number - correct_number) > 0:
            print("higher but closer")

print(f"You have taken {count_attempts} attempts")
