# DU, Period 2, user_signin.py



correct_username = "pro-gamer2"
correct_password = "passwordisthehard"


username = input("Enter your username: ")
password = input("Enter your password: ")


if username == correct_username and password == correct_password:
    print("Welcome, " + correct_username )
else:
    print("incorrect password or username")
    
