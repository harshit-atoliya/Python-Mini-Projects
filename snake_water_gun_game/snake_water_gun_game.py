import random
def snake_game(a):
    a = a.lower().strip()
    b = random.choice(["snake","water","gun"])
    
    # 1. Check for valid inputs first to prevent bugs
    valid_words = ["snake", "water", "gun"]
    if a not in valid_words or b not in valid_words:
        return "invalid"
        
    # 2. Check for a tie
    if a == b:
        return "tie"
        
    # 3. Check if Player A wins
    elif (a == "snake" and b == "water") or \
         (a == "gun" and b == "snake") or \
         (a == "water" and b == "gun"):
        return "A"
        
    # 4. If it's valid, not a tie, and A didn't win, B must have won
    else:
        return "B"

# Initialize score counters outside the loop
score_A = 0
score_B = 0

while True:
    # Use standard input so typing is visible and predictable
    p1 = input("Enter a word[snake,water,gun] or type exit to quit: ")
    if p1.lower().strip() == "exit":
        print("Thanks for playing!")
        break      
    # Run game logic
    result = snake_game(p1)
    
    # Update scores and print results based on the return value
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
        
    # Display the scoreboard
    print(f"📊 CURRENT SCORE -> Player A: {score_A} | Player B: {score_B}\n")
    print("-" * 40)
