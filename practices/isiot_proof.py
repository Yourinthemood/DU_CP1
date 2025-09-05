name = input("whats ur full name lil bro:").strip().capitalize().replace("."," ")

phone = input("whats ur phone number lil bro:").strip("-").replace("-"," ").replace("."," ")

if len(phone)!= 10 or not phone.isdigit(10):
print("invalid phone number, setting to default")
    
    


GPA = float(input("whats ur GPA lil bro: "))

rounded_gpa = round(GPA, 1)


print("hello", name)
print("your phone number is", phone)
print("your GPA is", rounded_gpa)