"""
WordGuess game implementation.

@author Leigh Durham
@version 1.0.0
@date 7/13/26
"""

import random

from person import Person


class WordGuess():
    """WordGuess game class - ready for implementation."""
    def __init__(self):  #stores the starting game data
        # The word the player is trying to guess
        self.secret_word = "HELLO"
        self.guessed_letters = ["H", "O"] #Temporary guesses to test the display
        self.max_attempts = 6
        self.wrong_guesses = 0

    def display_word(self):
        #Show the word with blanks for unguessed letters
        display = []  #build and return the word with blanks for unguessed letters.

        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
                
        return " ".join(display)
    
    def display_game(self):  # display the current game information

        print("Word: ", self.display_word())
        print("Guessed letters: ", self.guessed_letters)
        print("Wrong guesses: ", self.wrong_guesses)

    def play(self):   #Phase 2 of the game.
        print("Welcome to Word Guess!")
        print()

        self.display_game()

def main():
    # Core execution logic goes here        
    game = WordGuess() # Create a new game object
    game.play()

if __name__ == "__main__":       
    main()