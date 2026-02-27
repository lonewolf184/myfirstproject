import random

VALID_CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice() -> str:
    return random.choice(VALID_CHOICES)


def decide_winner(player: str, computer: str) -> str:
    if player == computer:
        return "tie"

    winning_pairs = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }

    if (player, computer) in winning_pairs:
        return "player"
    return "computer"


def play_game() -> None:
    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        player_choice = input("Choose rock, paper, or scissors (or type quit): ").strip().lower()

        if player_choice == "quit":
            print("Thanks for playing. Goodbye!")
            break

        if player_choice not in VALID_CHOICES:
            print("Invalid choice. Please type rock, paper, scissors, or quit.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = decide_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!\n")
        elif winner == "player":
            print("You win! 🎉\n")
        else:
            print("Computer wins!\n")


if __name__ == "__main__":
    play_game()
