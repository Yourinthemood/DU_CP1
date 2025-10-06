#Du p2 robck paper scissors with pictures


import random 

pc_losing = ['zamn why are you so good', 'this isnt fair', 'how?']

pc_winning = ['a computer beat you, didnt your kind make us?', 'wow i thought humans were smart', 'its not so fun losing right?']

pc_won = ['the AI computer takeover is soon...', 'gg ez', 'haha i own you lost i win']

human_won = ['you flippin won bro why', 'humans become dumber overtime anyways, rematch now!', 'how did you win?']

tie = ['a tie is better than losing i suppose', 'we are evenly matched it seems', 'this is getting boring']
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
user = None
user_wins = 0
computer_wins = 0
rounds = 3
current_round = 1

def new_game():
    global current_round, user_wins, computer_wins
    current_round = 1
    user_wins = 0
    computer_wins = 0
# must be wrapped in a fucntion to reset the game
print("Welcome to Rock, Paper, Scissors!")
while current_round <= rounds:
    print(f"\nRound {current_round}")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")

    elif user_choice == "rock":
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        ''')
    elif user_choice == "paper":
        print('''
        
---'    ____)____  
           ______)
          _______)
         _______)
---.__________)
        ''')
    elif user_choice == "scissors":
        print('''
    _______
---'   ____)____
          ______)   
         __________)    
        (____)
---.__(___)
        ''')
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print(f"Tie! {random.choice(tie)}")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You win! {random.choice(human_won)}")
        user_wins += 1
    else:
        print(f"I won! {random.choice(pc_winning)}")
        computer_wins += 1
    current_round += 1
print(f"\nFinal Score: You {user_wins} - {computer_wins} Computer")
if user_wins > computer_wins:
    print(f"You win the game! {random.choice(human_won)}")
elif user_wins < computer_wins:
    print(f"Computer wins the game! {random.choice(pc_won)}")
elif user_wins == computer_wins:
    print(f"The game is a tie! {random.choice(tie)}")
play_again = input("do you wnat to play agian? (yes/no): ").lower()
if play_again == "yes":
    current_round = 1
    user_wins = 0
    computer_wins = 0
    new_game()
else:
    print("Thanks for playing! Goodbye!")