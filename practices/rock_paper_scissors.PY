import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        print("\nRock, Paper, Scissors!")
        print("Choose: rock, paper, or scissors")
        user_choice = input("What's your pick? ").lower()
        
        if user_choice == 'quit':
            print("Bye!")
            break
        
        if user_choice not in choices:
            print("Oops! That's not rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"I picked: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("I win!")

rock_paper_scissors()
make it so you cn replay
python
import random

choices = ["rock", "paper", "scissors"]
#DU 2nd larose
while True:
    print("\nRock, Paper, Scissors!")
    user_choice = input("Pick rock, paper, or scissors: ").lower()
    
    if user_choice == 'quit':
        print("Bye!")
        break
    
    if user_choice not in choices:
        print("That's not rock, paper, or scissors!")
        continue
    
    computer_choice = random.choice(choices)
    print(f"I picked: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("I win!")
    
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
