#DU snd period 

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

add = num_1 + num_2
sub = num_1 - num_2 
mul = num_1 * num_2
div = num_1 / num_2 
mod = num_1 % num_2
exp = num_1 ** num_2

what = input("What operation do you want to perform? (+, -, *, /, %, **): ")

if what == "+":
    print(f"{num_1} + {num_2} = {add}")
elif what == "-":
    print(f"{num_1} - {num_2} = {sub}")
elif what == "*":
    print(f"{num_1} * {num_2} = {mul}")
elif what == "/":  
    print(f"{num_1} / {num_2} = {div}")
elif what == "%":
    print(f"{num_1} % {num_2} = {mod}")
elif what == "**":
    print(f"{num_1} ** {num_2} = {exp}")
else:
    print("Invalid operation")

while True:
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again == "yes":
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))
        what = input("What operation do you want to perform? (+, -, *, /, %, **): ")

        if what == "+":
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        elif what == "-":
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
        elif what == "*":
            print(f"{num_1} * {num_2} = {num_1 * num_2}")
        elif what == "/":  
            print(f"{num_1} / {num_2} = {num_1 / num_2}")
        elif what == "%":
            print(f"{num_1} % {num_2} = {num_1 % num_2}")
        elif what == "**":
            print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
        else:
            print("Invalid operation")
    elif again == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")



 