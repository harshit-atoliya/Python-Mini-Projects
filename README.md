# Python Mini Projects

A collection of small Python projects built while learning the language.

## Projects

### Snake Water Gun
A classic Snake-Water-Gun game played against the computer.
**Concepts:** functions, conditionals, loops, and the `random` module

Run it with:

```bash
cd snake_water_gun_game
python snake_water_gun_game.py
```

### Rock Paper Scissors
A score-tracking Rock-Paper-Scissors game with input validation and an exit command.
**Concepts:** functions, conditionals, loops, and the `random` module

Run it with:

```bash
cd "rock_paper_scissor _game"
python "rock_paper_scissor _game.py"
```

### Number Guessing Game
Guess a randomly generated number between 0 and 100.
**Concepts:** loops, conditionals, input validation, and the `random` module

Run it with:

```bash
cd number_guessing_game
python number_guessing_game.py
```

### Word Guessing Game
Guess the letters in a randomly selected word before the attempts run out.
**Concepts:** lists, loops, strings, and the `random` module

Run it with:

```bash
cd word_guessing_game
python word_guessing_game.py
```

### File Comparison
Compares the contents of two sample files using SHA-1 hashes.
**Concepts:** functions, file handling, binary file reading, and the `hashlib` module

Run it with:

```bash
cd file_comparison_app
python file_comparison_app.py
```

### Date Calculator
Calculates the difference between two dates in days, months, and years.
**Concepts:** the `datetime` module, `strptime`, and `try`/`except` input validation

Run it with:

```bash
cd days_calculator
python day_calculator.py
```

### Friday Voice Assistant
A Windows voice assistant that listens for a wake command, reads daily tasks, opens configured tools, and gives a spoken briefing. See the [Friday README](friday_ai_assistant/README.md) for setup requirements and configuration details.

Run it with:

```powershell
cd friday_ai_assistant
python friday.py
```

Friday requires Windows, a microphone, and additional Python packages. Follow its project README before running it.

## How to Run

Open a terminal in the repository root, change into a project folder, and run its Python script. The examples above use the actual folder and file names in this repository.

## Structure

```text
Python-Mini-Projects/
├── days_calculator/
│   └── day_calculator.py
├── file_comparison_app/
│   ├── file_comparison_app.py
│   ├── text.txt
│   └── text1.txt
├── friday_ai_assistant/
│   ├── friday.py
│   ├── tasks.txt
│   └── README.md
├── number_guessing_game/
│   └── number_guessing_game.py
├── rock_paper_scissor _game/
│   └── rock_paper_scissor _game.py
├── snake_water_gun_game/
│   └── snake_water_gun_game.py
└── word_guessing_game/
    └── word_guessing_game.py
```
