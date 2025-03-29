import random

print('''
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗███████╗███████╗███████╗███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝███████╗███████║███████║███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝''')

print("Welcome to Number Guessing!")

# Global variables
lives = 0  # Lives will be set in difficulty()
number_list = random.randint(1, 100)  # Random number between 1 and 100
print(number_list)
print("I am thinking of a number from 1 to 100, can you guess it?")


def difficulty():
    """Set the difficulty level by assigning the global variable `lives`."""
    global lives
    qdiff = input("Choose a difficulty: Type Easy or Hard\n").lower()
    if qdiff == "easy":
        lives = 10
        print("You have 10 attempts remaining to guess the number.")
    else:
        lives = 5
        print("You have 5 attempts remaining to guess the number.")


def make_a_guess():
    """Handles the guessing logic with the global `lives` variable."""
    global lives
    while lives > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_list:
            print("Congratulations! You guessed the number correctly!")
            return

        lives -= 1
        if guess > number_list:
            print("Your guess was too high.")
        else:
            print("Your guess was too low.")

        if lives > 0:
            print(f"Guess again! You have {lives} attempts left.")
        else:
            print(f"You've run out of attempts. The correct number was {number_list}. You lose!")


def play_game():
    """Starts the game by setting difficulty and handling guesses."""
    difficulty()
    make_a_guess()


# Start the game
play_game()