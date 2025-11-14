# DU P2 order up

#dictionary for Detaco Elcasa 
menu = {
    "drinks": {
        "soda": 2.50,
        "juice": 3.00,
        "water": 1.50,
        "lemonade": 2.75
    },
    "main_courses": {
        "beef taco": 4.50,
        "chicken taco": 4.25,
        "fish taco": 5.00,
        "vegetarian taco": 3.75
    },
    "side_dishes": {
        "chips": 2.00,
        "guacamole": 3.50,
        "beans": 2.25,
        "rice": 2.25
    }
}

# Welcome message
print("Welcome to DeTaco ElCasa!")
print("=" * 30)

# Display menu options
print("\nHere's our menu:")
print("DRINKS:")
for drink, price in menu["drinks"].items():
    print("  " + drink.title() + " - $" + str(price))

print("\nMAIN COURSES:")
for main, price in menu["main_courses"].items():
    print("  " + main.title() + " - $" + str(price))

print("\nSIDE DISHES:")
for side, price in menu["side_dishes"].items():
    print("  " + side.title() + " - $" + str(price))

print("\n" + "=" * 30)

# Get drink order
while True:
    drink_choice = input("\nPlease choose a drink: ").lower()
    if drink_choice in menu["drinks"]:
        drink_price = menu["drinks"][drink_choice]
        break
    else:
        print("Sorry, that's not on our drink menu. Please choose from: soda, juice, water, or lemonade.")

# Get main course order
while True:
    main_choice = input("Please choose a main course: ").lower()
    if main_choice in menu["main_courses"]:
        main_price = menu["main_courses"][main_choice]
        break
    else:
        print("Sorry, that's not on our main course menu. Please choose from: beef taco, chicken taco, fish taco, or vegetarian taco.")

# Get first side dish
while True:
    side1_choice = input("Please choose your first side dish: ").lower()
    if side1_choice in menu["side_dishes"]:
        side1_price = menu["side_dishes"][side1_choice]
        break
    else:
        print("Sorry, that's not on our side dish menu. Please choose from: chips, guacamole, beans, or rice.")

# Get second side dish
while True:
    side2_choice = input("Please choose your second side dish: ").lower()
    if side2_choice in menu["side_dishes"]:
        side2_price = menu["side_dishes"][side2_choice]
        break
    else:
        print("Sorry, that's not on our side dish menu. Please choose from: chips, guacamole, beans, or rice.")

# Calculate total cost
total_cost = drink_price + main_price + side1_price + side2_price

# Display order summary
print("\n" + "=" * 30)
print("Your order:")
print("=" * 30)
print("Drink: " + drink_choice.title())
print("Main Course: " + main_choice.title())
print("Side Dishes:")
print("  " + side1_choice.title())
print("  " + side2_choice.title())
print("Total Cost: $" + str(total_cost))
print("\nThank you for ordering from DeTaco ElCasa!")
