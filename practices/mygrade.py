grade_percent = int(input("whats ur percentage in your class?: "))


aGRADE = 95 >= grade_percent <= 100
aMINUS = 90 >= grade_percent < 95  
bPLUS = 89 >= grade_percent < 90
bGRADE = 86 >= grade_percent < 89
bMINUS = 84 >= grade_percent < 86
cPLUS = 79 >= grade_percent < 84
cGRADE = 76 >= grade_percent < 79
cMINUS = 74 >= grade_percent < 76
dPLUS = 69 >= grade_percent < 74
dGRADE = 66 >= grade_percent < 69
dMINUS = 64 >= grade_percent < 66
fGRADE = 59 >= grade_percent < 64


if grade_percent > 100: 
    print("your lying brochacho")
elif grade_percent >= 95:
    print("you have an A")
elif grade_percent >= 90:
    print("you have an A-")
elif grade_percent >= 89:
    print("you have a B+")
elif grade_percent >= 86:
    print("you have a B")
elif grade_percent >= 84:
    print("you have a B-")
elif grade_percent >= 79:
    print("you have a C+")
elif grade_percent >= 76:
    print("you have a C")
elif grade_percent >= 74:
    print("you have a C-")
elif grade_percent >= 69:
    print("you have a D+") 
elif grade_percent >= 66:
    print("you have a D")
elif grade_percent >= 64:
    print("you have a D-")
elif grade_percent >= 59:
    print("you have an F")
else: print("put the dang input corectly next time")
