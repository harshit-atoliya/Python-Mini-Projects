# Import randint to generate a random number.
from random import randint

# Generate a secret number between 0 and 100.
secret_number = randint(0, 100)

# Track how many attempts the player has made.
attempts = 0

# The game is not over yet.
game = False

# Keep running the loop until the player guesses correctly.
while not game:
    # Increase the attempt counter each time the loop runs.
    attempts += 1

    try:
        # Ask the user to enter a number between 0 and 100.
        user_guess = int(input("Enter a number between 0-100: "))
    except ValueError:
        # Handle invalid input that is not a number.
        print("Please enter a valid number.")
        continue

    # Reject values outside the allowed range.
    if not 0 <= user_guess <= 100:
        print("Please enter a number between 0 and 100.")
        continue

    # If the guess is too high, tell the player to choose a lower number.
    if user_guess > secret_number:
        print("Lower Number Please")
    # If the guess is too low, tell the player to choose a higher number.
    elif user_guess < secret_number:
        print("Higher Number Please")
    else:
        # If the guess is correct, print the result and end the loop.
        print(f"Correct Guess in {attempts} attempts, the number was: {secret_number}")
        game = True