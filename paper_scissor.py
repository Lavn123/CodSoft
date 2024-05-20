import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
def main():
    print("Rock-Paper-Scissors Game")

    user_score = 0
    computer_score = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
