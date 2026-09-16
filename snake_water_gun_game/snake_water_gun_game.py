# Import the random module to let the computer choose a move.
import random

# Define a function that plays one round of Snake-Water-Gun.
def snake_game(a):
    # Normalize the user input so it works even if extra spaces or uppercase letters are used.
    a = a.lower().strip()
    # The computer randomly picks one of the valid choices.
    b = random.choice(["snake", "water", "gun"])

    # Store all valid choices for input validation.
    valid_words = ["snake", "water", "gun"]

    # Reject invalid entries before checking the game rules.
    if a not in valid_words or b not in valid_words:
        return "invalid"

    # If both players choose the same option, the round is a tie.
    if a == b:
        return "tie"

    # Check the winning combinations for Player A.
    elif (a == "snake" and b == "water") or \
         (a == "gun" and b == "snake") or \
         (a == "water" and b == "gun"):
        return "A"

    # If the round is valid, not a tie, and A did not win, then B wins.
    else:
        return "B"

# Initialize the score counters before the loop starts.
score_A = 0
score_B = 0

# Keep the game running until the player chooses to exit.
while True:
    # Ask the user for their move or an exit command.
    p1 = input("Enter a word[snake,water,gun] or type exit to quit: ")

    # If the user types exit, end the game and thank them for playing.
    if p1.lower().strip() == "exit":
        print("Thanks for playing!")
        break

    # Run the game logic for one round.
    result = snake_game(p1)

    # Update the score and print the round result based on the outcome.
    if result == "A":
        score_A += 1
        print("\n🎉 Player A wins this round!")
    elif result == "B":
        score_B += 1
        print("\n🎉 Player B wins this round!")
    elif result == "tie":
        print("\n👔 It's a tie!")
    else:
        print("\n❌ Please enter a correct word (snake, water, or gun).")

    # Display the current score after each round.
    print(f"📊 CURRENT SCORE -> Player A: {score_A} | Player B: {score_B}\n")
    print("-" * 40)
