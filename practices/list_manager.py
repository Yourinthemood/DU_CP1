# DU P2 class Shopping List Manager


shopping_list = []

while True:
    action = input("What would you like to do? (add/view/remove/exit) ")
    if action == "add":
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(f"Added {item} to the shopping list.")
    elif action == "view":
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    elif  action == "remove":
        item = input("Enter the item you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item} from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
    elif action == "exit":
        break