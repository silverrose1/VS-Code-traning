
clues = {
    "PYTHON": "A popular programming language",
    "LOOP": "A code structure that repeats"
}

correct_guesses = 0

for word, clue in clues.items():
    print(f"Clue: {clue}")
    guess = input("Your guess: ").upper()

    if guess == word:
        print("Correct!")
        correct_guesses += 1
    else:
        print("Try again.")

if correct_guesses == len(clues):
    print("You solved the crossword puzzle!")
else:
    print("Keep trying!")
