#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     14/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

# Hangman drawing stages
HANGMAN_PICS = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Word list
WORDS = ["python", "java", "kotlin", "javascript", "ruby", "swift", "golang"]

def play_hangman():
    word = random.choice(WORDS)
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 0

    while attempts < len(HANGMAN_PICS) - 1:
        print(HANGMAN_PICS[attempts])  # Show hangman state
        print("Word: " + " ".join(guessed_word))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts += 1

        if "_" not in guessed_word:
            print("\n🎉 YOU WIN! The word was:", word)
            return

    print(HANGMAN_PICS[attempts])
    print("\n💀 YOU LOSE! The word was:", word)

if __name__ == "__main__":
    play_hangman()
