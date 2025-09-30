yes = True 

import datetime
today = datetime.date.today()
print("todays date is: ", today)
while today.weekday() != 4:  # 4 represents Friday
    today += datetime.timedelta(days=1)
    while yes:
        print("It's not Friday yet.")
        loop = 1
        loop += 1
time = datetime.datetime.now()
print("current time is: ", time)