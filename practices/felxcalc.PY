# DU p2 flex calc


# make a calculator function that can take many numbers
# the function should do different math operations
# ask user what operation they want
# let user enter as many numbers as they want
# show the result
# ask if they want to do another calculation

def calculator(operation, *numbers):
    # check if there are numbers
    if len(numbers) == 0:
        return "you didnt enter any numbers"
    
    # do the operation based on what user wants
    if operation == "sum":
        total = 0
        for num in numbers:
            total += num
        return total
    
    elif operation == "average":
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
    
    elif operation == "max":
        biggest = numbers[0]
        for num in numbers:
            if num > biggest:
                biggest = num
        return biggest
    
    elif operation == "min":
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        return smallest
    
    elif operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result
    
    else:
        return "that doesnt work try again"

# main program
print("welcome to the flexible calculator")
print()

# keep going until user says stop
while True:
    # ask what operation they want and show options
    print("which math function would you like to do")
    print("sum - add all numbers together")
    print("average - find the average of numbers")
    print("max - find the largest number")
    print("min - find the smallest number")
    print("product - multiply all numbers together")
    
    operation = input("enter your choice: ")
    operation = operation.lower()
    
    # check if operation is valid
    valid_operations = ["sum", "average", "max", "min", "product"]
    if operation not in valid_operations:
        print("thats not one of the options try again")
        print()
        continue
    
    # get numbers from user
    numbers_list = []
    print("type your numbers type done when you are finished")
    
    while True:
        user_input = input("number ")
        
        # check if user is done
        if user_input.lower() == "done":
            break
        
        # try to convert to number
        try:
            number = float(user_input)
            numbers_list.append(number)
        except:
            print("thats not a number try again")
    
    # calculate result
    result = calculator(operation, *numbers_list)
    
    # show the calculation
    print(f"doing {operation} with these numbers {numbers_list}")
    print(f"the answer is {result}")
    print()
    
    # ask if they want to go again
    again = input("want to do another one yes or no ")
    if again.lower() != "yes":
        break

print("thanks for using my flex calc")
