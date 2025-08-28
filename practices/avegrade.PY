
one = float(input("what is your grade in your Math class? (0.0 - 4.0): "))

two = float(input("what is your grade in your computer science class? (0.0 - 4.0): "))

three = float(input("what is your grade in your english class? (0.0 - 4.0): "))

four = float(input("what is your grade in your advisory class? (0.0 - 4.0): "))

five = float(input("what is your grade in your drawing class? (0.0 - 4.0): "))

six = float(input("what is your grade in your history class? (0.0 - 4.0): "))

seven = float(input("what is your grade in your biology class? (0.0 - 4.0): "))


average_gpa = (one + two + three + four + five + six + seven) / 7

print("your average GPA is", average_gpa)

if any(grade > 4.0 or grade < 0.0 for grade in [one, two, three, four, five, six, seven]):
    print("that's not a valid GPA! Grades must be between 0.0 and 4.0")
    
    #idk why its not working in w3 schools when it worked at the computer lab
