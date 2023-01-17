
dict_users = {
    "david" : "bald",
    "john"  : "bird"
}

def login():
    while True:
      user_name = input("enter your name?:")
      user_password = input("enter your password?:")
      if user_name in dict_users and dict_users[user_name] == user_password:
        print("Welcome to Replit! Enjoy your day!!!")
        break
      elif user_name in dict_users and dict_users[user_name] != user_password:
        print("Whoops! I don't recognize that username or password. Try again!")

      elif user_name not in dict_users:
        print("user not found, try again")


login()
