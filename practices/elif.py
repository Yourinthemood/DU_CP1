# FL class Shopping List Manager

#Put your shopping list variable here
shopping_list = []

while True:
    action = input("What would you like to do? (add/view/exit) ")
    if action == "add":
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(f"Added {item} to the shopping list.")
    elif action == "view":
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    elif action == "exit":
        break