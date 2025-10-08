# DU Period 2 Rock Paper Scissors larose
import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Welcome to Rock Paper Scissors!")
print("Type 'quit' to exit the game")

while True:
    print(f"\nScore - You: {player_score} | Computer: {computer_score}")
    user_choice = input("Enter rock, paper, or scissors: ").lower().strip()
    
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print(f"Final Score - You: {player_score} | Computer: {computer_score}")
