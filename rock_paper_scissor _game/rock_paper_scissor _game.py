# Import the random module to let the computer choose a move.
import random

# Store the computer's latest choice so it can be displayed after the round result is calculated.
computer_guess = ""

# Define a function that plays one round of the Rock-Paper-Scissors game.
def rock_game(a):
    # Use global so the chosen computer move is available outside this function.
    global computer_guess

    # Normalize the user input so it works even if extra spaces or uppercase letters are used.
    a = a.lower().strip()

    # Store all valid choices for input validation.
    valid_words = ["rock", "scissor", "paper"]

    # Reject invalid entries before checking the game rules.
    if a not in valid_words:
        computer_guess = "invalid"
        return "invalid", computer_guess

    # The computer randomly picks one of the valid choices.
    b = random.choice(valid_words)
    computer_guess = b

    # If both players choose the same option, the round is a tie.
    if a == b:
        return "tie", computer_guess

    # Check the winning combinations for the player.
    # rock beats scissor, paper beats rock, scissor beats paper.
    if (a == "rock" and b == "scissor") or \
       (a == "paper" and b == "rock") or \
       (a == "scissor" and b == "paper"):
        return "A", computer_guess

    # If the round is valid, not a tie, and the player did not win, the computer wins.
    return "B", computer_guess

# Initialize the score counters before the loop starts.
score_A = 0
score_B = 0

# Keep the game running until the player chooses to exit.
while True:
    # Ask the user for their move or an exit command.
    p1 = input("Enter a word[rock,paper,scissor] or type exit to quit: ")

    # If the user types exit, end the game and thank them for playing.
    if p1.lower().strip() == "exit":
        print("Thanks for playing!")
        break

    # Run the game logic for one round and get the result plus the computer move.
    result, computer_guess = rock_game(p1)

    # Show both choices after the computer move has been generated.
    print(f"\nYou Choose : {p1} And Computer Choose : {computer_guess} ")

    # Update the score and print the round result based on the outcome.
    if result == "A":
        score_A += 1
        print("\n🎉 You wins this round!")
    elif result == "B":
        score_B += 1
        print("\n🎉 Computer wins this round!")
    elif result == "tie":
        print("\n👔 It's a tie!")
    else:
        print("\n❌ Please enter a correct word (rock, paper, or scissor).")

    # Display the current score after each round.
    print(f"📊 CURRENT SCORE -> You : {score_A} | Computer : {score_B}\n")

    # Separate each round visually in the terminal.
    print("-" * 40)
