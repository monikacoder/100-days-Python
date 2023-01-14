correct_number = 1000
count_attempts = 0

while True:
  guess_number =  int(input("guess the number?:"))
  count_attempts += 1

  if guess_number == correct_number:
    print("correct")
    break
  elif guess_number < correct_number:
    if (correct_number - guess_number ) >200:
      print("too much low")
    elif (correct_number - guess_number ) >100:  
      print("too low")
    elif (correct_number - guess_number ) >10:  
      print("lower")  
  elif guess_number > correct_number:
    if ( guess_number - correct_number ) >200:
      print("too much high")
    elif ( guess_number - correct_number ) >100:  
      print("too high")
    elif ( guess_number - correct_number ) >10:  
      print("higher")
    
print(f"You have taken {count_attempts} attempts" )    
