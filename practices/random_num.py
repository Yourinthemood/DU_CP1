money = float(input("enter how much money the pirates earned:" ))
priates_count = int(input("how many pirates are there:" ))

captain_divide = 7

first_mate_divide = 3

crews_share = 1
 

#crew members get the rest of the shares divided equaly
rest = money - (money / (captain_divide + first_mate_divide + (crews_share * (priates_count - 2)))) * (captain_divide + first_mate_divide)
crew_member_share = rest / (priates_count - 2)  



# we need round it to the second pplace
print("each crew member gets: ", round((crew_member_share - 500), 2)) 
print("first mate gets: ", round(crew_member_share * first_mate_divide, 2))
print("captain gets: ", round(crew_member_share * captain_divide, 2))