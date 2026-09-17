# Import 'choice' to select a random word from our list
from random import choice

# Define a list of words for the game
words = ["Nolan", "Sparrow", "Thor", 'rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Select a random word and convert it to lowercase for case-insensitive matching
secret_word = choice(words).lower()

# Set the maximum number of incorrect guesses allowed
attempts = 6

# Track letters the player has already guessed to prevent duplicate penalties
guessed_letters = []

# Flag to control the main game loop
game = True

# Create a list of underscores matching the length of the secret word to show progress
display_word = list("_" * len(secret_word))

# Main game loop: continues until the player wins or runs out of attempts
while game:
    
    # Display the current state of the word (e.g., "_ _ _ r")
    print(" ".join(display_word))
    
    # Prompt the user for a guess and convert it to lowercase
    guess = input("Guess a letter: ").lower()
    
    # Validate input: Ensure the user entered exactly one character
    if len(guess) == 1:
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You Already Guessed That Letter")
        
        # Handle incorrect guesses
        elif guess not in secret_word:
            attempts -= 1
            print(f"Wrong Guess!, Attempts Left: {attempts}")
             
        # Handle correct guesses
        else:
            # Iterate through the secret word to find all occurrences of the guessed letter
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    # Reveal the letter in the display word at the correct position
                    display_word[i] = guess
                    print(f"You Guessed A Right Letter : {guess}")
                    
        # Record the valid guess so it can't be used again
        guessed_letters.append(guess) 
        
        # Check for a loss condition: 0 attempts remaining                 
        if attempts == 0:
            game = False
            print("Game Over The Secret Word Was :", secret_word)
        
        # Check for a win condition: no more underscores left to guess
        if "_" not in display_word:
            game = False
            print("You Won The game, The Secret Word Was :", secret_word)
    
    # Handle empty input (user just pressed Enter)      
    elif len(guess) == 0:
        print("No Value was given, Please Enter A Value")
    
    # Handle input containing more than one character
    else:
        print("Please Enter A Single Value")