#password strength check DU p2 larose


#display greeting and show criteria required for said password

#define it all in a function so its easily able to like re do it
#ask user for a password
#check the password against the criteria
def new_check():
    print("Welcome to the Password Strength Checker!")
    #initialize strength variable
    #set it to 0 at start

    pass_strength = 0
    special_characters = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','\'','"',',','.','<','>','/','?','`','~']

    #define a function to show the criteria and make it easy to redo
    #if the password is weak

    print("A strong password must meet the following criteria:")
    print("1. At least 8 characters long")
    print("2. Contains at least one number")
    print("3. Contains at least one uppercase letter")
    print("4. Contains at least one lowercase letter")
    print("5. Contains a special character")
    print("if your password doesnt fit all criteria it is not strong.")
    password = input("Please enter your password: ")

    #check the password against the criteria
    #use if statements to check each criteria
    #for each criteria met, increase the strength by 1

    password_length = len(password)
    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if password_length >= 8:
        pass_strength += 1
    if has_number:
        pass_strength += 1
    if has_upper:
        pass_strength += 1
    if has_lower:
        pass_strength += 1


    if any(char in special_characters for char in password):
        pass_strength += 1
    #print a progress bar
    #based on how many criteria the password meets
    # 5 criteria = very strong
    # 4 criteria = strong
    # 3 criteria = moderate
    # 2 criteria = weak
    # 1 criteria = very weak

    #if statements to check how many criteria the password meets

    #print out the strength of the password based on how many criteria it meets
    #and print out a progress bar to visually show the strength of the password

    if pass_strength == 5:
        print("Your password is very strong.")
        print('''
        [####################] 100%
        ''')


    elif pass_strength >= 4:
        print("Your password is strong.")
        print('''
        [##################  ] 90%
        ''')
    elif pass_strength >= 3:
        print("Your password is moderate.")
        print('''
        [###############     ] 70%
        ''')
    elif pass_strength >= 2:
        print("Your password is weak.")
        print('''
        [############         ] 50%
        ''')
    elif pass_strength >= 1:
        print("Your password is rly bad but atleast you have one.")
        print('''
        [##                  ] 10%
        ''')
    print("Thank you for using the Password Strength Checker!")
    #ask if they want to check another password
    retry = input("Do you want to check another password? (yes/no): ").lower()
    if retry == 'yes':
        new_check()
    else:
        print("Goodbye!")

new_check()
        
