# DU P2 larose



#make a list of numbers
#make a function that squares a number
#use map to square all numbers in the list
#turn the map into a regular list
#loop through both lists together
#print each original number with its squared number


numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

def square_number(num):
    return num * num

squared_map = map(square_number, numbers)

squared_list = list(squared_map)

for i in range(len(numbers)):
    print("Original:", numbers[i], "Squared:", squared_list[i])
