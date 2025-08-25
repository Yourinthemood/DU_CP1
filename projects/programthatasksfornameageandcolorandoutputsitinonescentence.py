#DU 2nd Project
print("hello friend!")

import time 
time.sleep(2)

name = input("what is your name: ")
print("hi",name)

time.sleep(1)

age = input("what is your age?: ")

time.sleep(1)

color = input("what is you favorite color?: ")

time.sleep(1)

print("your",name + " your about", age + " years old." + " and your favorite color is",color + "is that correct?")

time.sleep(1)

answer = input("is that information correct? (yes/no): ")

if answer == "no":
    print("oops, i must've done something wrong then")
if answer == "yes":
    print("thats good to hear")
