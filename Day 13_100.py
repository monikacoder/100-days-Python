#This exercise is to understand the "if-else with and" conditions effectively

test_name = input("Enter the name of the test?:")
test_max_score = int(input("Enter the test max score?:"))
test_your_point = int(input("Enter your test point?:"))

your_percent = round(test_your_point/test_max_score * 100,2)
print("Your percentage is:",your_percent)
your_grade = ""
if your_percent >=90 and your_percent <=100:
  your_grade = "A+"
elif your_percent >= 80 and your_percent <= 89:
  your_grade = "A"
elif your_percent >= 70 and your_grade <= 79:
  your_grade = "B"
elif your_percent >= 60 and your_percent <= 69:
  your_grade = "C"
elif your_percent >= 50 and your_grade <= 59:
  your_grade = "D"
else:
  your_grade ="U"

print(f"Your grade is: {your_grade}")
