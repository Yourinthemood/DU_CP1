money = float(input("enter how much money the pirates earned:" ))
priates_count = int(input("how many pirates are there:" ))

captain_divide = 7

first_mate_divide = 3

crews_share = 1

total_shares = captain_divide + first_mate_divide + (crews_share * (priates_count - 2))
share_value = money / total_shares  
captain_money = share_value * captain_divide
first_mate_money = share_value * first_mate_divide
crew_money = share_value * crews_share + 500 - 1000
print("captain gets:", captain_money)
print("first mate gets:", first_mate_money)
print("each crew still needs:", crew_money)

