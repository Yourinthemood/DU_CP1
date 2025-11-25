
#DU P2 Fact-calc*TM
# Ask the user for a number
num = input("What number do you want the factorial of: ")

# Check if it's a real number
if num.isdigit():
    n = int(num)
    
    # Make sure it's not negative
    if n < 0:
        print("Please enter a non-negative number")
    else:
        # Calculate the factorial
        if n == 0:
            answer = 1
        else:
            answer = 1
            # Multiply all the numbers from n down to 1
            for i in range(n, 0, -1):
                answer = answer * i
        
        # Show the answer in the right format
        if n == 0:
            print("0 = 1")
        else:
            # Build the equation string like "5 × 4 × 3 × 2 × 1"
            equation = ""
            for i in range(n, 0, -1):
                equation += str(i)
                if i > 1:
                    equation += " × "
            print(f"{equation} = {answer}")
        
else:
    print("Please enter a valid integer")
