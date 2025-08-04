import random
import os
import time

# Word list
WORDS = [
    'python', 'javascript', 'hangman', 'challenge', 'function', 'variable',
    'keyboard', 'internet', 'programmer', 'terminal', 'debugging', 'compiler',
    'execute', 'recursion', 'syntax', 'loop', 'integer', 'boolean', 'class'
]

# ASCII Hangman Stages
HANGMAN = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========="""
]

# Game logic
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    return random.choice(WORDS).upper()

def display_game(word, guessed, tries):
    clear()
    print(HANGMAN[tries])
    print("\nWord: ", end="")
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(f"\n\nGuessed Letters: {' '.join(guessed)}")
    print(f"Tries Left: {6 - tries}")

def play():
    word = get_word()
    guessed_letters = []
    tries = 0
    won = False

    while tries < 6:
        display_game(word, guessed_letters, tries)
        guess = input("\nGuess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter a valid single letter.")
            time.sleep(1)
            continue

        if guess in guessed_letters:
            print("Already guessed.")
            time.sleep(1)
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries += 1
        else:
            if all(letter in guessed_letters for letter in word):
                won = True
                break

    display_game(word, guessed_letters, tries)
    if won:
        print("\n🎉 YOU WON! The word was:", word)
    else:
        print("\n💀 YOU LOST! The word was:", word)

def main():
    while True:
        play()
        again = input("\nWanna play again? (y/n): ").lower()
        if again != 'y':
            print("Peace out, code cowboy 🤠")
            break

if __name__ == "__main__":
    main()
