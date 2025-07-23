import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    user_input = input("Your choice: ").lower()
    if user_input in ["rock", "paper", "scissors"]:
        return user_input
    else:
        print("Invalid input. Try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

def play():
    print("🪨📄✂️ Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)
play()