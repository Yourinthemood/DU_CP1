# DU, Period 2, String Methods Assignment


name = input("Enter your full name: ")
phone = input("Enter your phone number: ")
gpa = input("Enter your GPA: ")

formatted_name = name.title()

formatted_phone = phone[:3] + " " + phone[3:6] + " " + phone[6:]

formatted_gpa = round(float(gpa), 1)

print("\nFormatted Information:")
print("name:", formatted_name)
print("phone:", formatted_phone)
print("GPA:", formatted_gpa)
