from random import randint
secret_number = randint(0, 100)
attempts = 0
game = False

while not game:
    attempts += 1

    try:
        user_guess = int(input("Enter a number between 0-100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not 0 <= user_guess <= 100:
        print("Please enter a number between 0 and 100.")
        continue

    if user_guess >secret_number:
        print("Lower Number Please")
    elif user_guess <secret_number:
        print("Higher Number Please")
    else:
        print(f"Correct Guess in {attempts} attempts, the number was: {secret_number}")
        game = True