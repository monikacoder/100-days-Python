user_year = int(input("enter the year?:"))

days_leap_year = 366
days_non_leap_year = 365
seconds_in_day = 24 * 60 * 60

if user_year % 4 == 0:  # its a leap year
     seconds_year = days_leap_year * seconds_in_day
else:  # it is not a leap year
     seconds_year = days_non_leap_year * seconds_in_day

print(f"Number of seconds in year {user_year} are :{seconds_year} seconds")


