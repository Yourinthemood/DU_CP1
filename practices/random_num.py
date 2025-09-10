import random


print(random.randint(67, 67))
 

print("this is called the mason 67 game")

print("Press Enter to start the game")
    

print("you have 3 tries to guess the number"   
      " between 1 and 100")

number = random.randint(1, 100)

tries = 0
while tries < 3:

    guess = int(input("Enter your guess: "))
    tries += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number!")
        break

while tries == 3:
    print(f"Sorry, you've used all your tries. The number was {number}.")
    break   
print("Thank you for playing the Mason 67 game!")

while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number = random.randint(1, 100)
        tries = 0
        print("New game started! You have 3 tries to guess the number between 1 and 100.")
        while tries < 3:
            guess = int(input("Enter your guess: "))
            tries += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Congratulations! You've guessed the number!")
                break
        if tries == 3:
            print(f"Sorry, you've used all your tries. The number was {number}.")
        print("Thank you for playing the Mason 67 game!")
    elif play_again == "no":
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")