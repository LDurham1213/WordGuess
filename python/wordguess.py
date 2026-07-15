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

        self.player = None

        self.categories = {
            "1": {"name": "Animals",
                  "words": ["TIGER", "ZEBRA", "HORSE", "ELEPHANT"]
                  },
            "2": {"name": "Technology",
                  "words": ["PYTHON", "MAINFRAME", "COBOL", "CODING"]
                  },
            "3": {"name": "Food",
                  "words": ["PIZZA", "SHRIMP", "PASTA", "LOBSTER"]
                  }
        }
        self.category_name = ""
        self.secret_word = ""
        self.guessed_letters = []  
        self.max_attempts = 6
        self.wrong_guesses = 0

    def create_player(self):

        print("WELCOME TO WORD GUESS!")
        print()

        first_name = input("ENTER YOUR FIRST NAME: ").strip()
        last_name =  input("ENTER YOUR LAST NAME: ").strip()

        while True:
            try:
                age = int(input("ENTER YOUR AGE: "))

                if age <= 0:
                    print("PLEASE ENTER AN AGE GREATER THAN ZERO.")
                    continue
                break

            except ValueError:
                print("PLEASE ENTER YOUR AGE AS A WHOLE NUMBER.")

        self.player = Person()
        self.player.set_first_name(first_name)
        self.player.set_last_name(last_name)
        self.player.set_age(age)

        print()
        print(f"Welcome, {self.player.get_first_name()}!")
        
    def choose_category(self):
        print()
        print("CHOOSE A CATEGORY:")

        for category_number, category_data in self.categories.items():
            print(category_number, "-", category_data["name"])

        while True:
            choice = input("ENTER CATEGORY NUMBER: ").strip()

            if choice in self.categories:
                self.category_name = self.categories[choice]["name"]

                word_list = self.categories[choice]["words"]
                self.secret_word = random.choice(word_list)

                break
            print("Invalid category. Please enter 1, 2, or 3.")

    def reset_game(self):
        """ Resets the game before beginning a new game """

        self.guessed_letters = []
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
    
    def display_game(self):
        # displays the current game information

        attempts_remaining = self.max_attempts - self.wrong_guesses

        print()
        print("-----------------------------------------")
        print("Category: ", self.category_name)
        print("Word: ", self.display_word())

        if len(self.guessed_letters) == 0:
            print("Guessed letters: None")
        else:
            print("Guessed letters: ", ", ".join(self.guessed_letters))

        print("Attempts remaining: ", attempts_remaining)
        print("------------------------------------------------")

    def get_guess(self):
        #get and validate one letter from the player.

        while True:
            guess = input(
                "Enter one letter or type 'quit' to exit: "
            ).strip().upper()

            if guess == "QUIT":
                return guess
            
            if len(guess) != 1:
                print("Please enter exactly one letter.")
                continue

            if not guess.isalpha():
                print("Numbers and symbols are not allowed.")
                continue

            if guess in self.guessed_letters:
                print("uh uh - you already guess that letter.")
                continue

            return guess

    def check_guess(self,guess):
        # Check if the guessed letter is in the secret word.

        self.guessed_letters.append(guess)

        if guess in self.secret_word:
            letter_count = self.secret_word.count(guess)

            if letter_count > 1:
                print(f"Awesome! The letter {guess} apears "
                        f"{letter_count} times."
                )
            else:
                print(f"Awesome! The letter {guess} is in the word.")                      
        else:
            self.wrong_guesses += 1
            print(f"Oh no! Letter {guess} is not in the word.")

    def has_won(self):
        #return true when each letter is guessed correct
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
            
        return True
    
    def has_lost(self):
        # return true when the player has used all wrong guesses.

        return self.wrong_guesses >= self.max_attempts
    
    def play(self):
        """Run the game until the player wins, loses, or quits."""

        self.create_player()
        assert self.player is not None
        self.choose_category()
        self.reset_game()

        while True:
            self.display_game()

            guess = self.get_guess()

            if guess == "QUIT":
                print("Thanks for playing - Enjoy your day!")
                print("The secret word was:", self.secret_word)
                break

            self.check_guess(guess)

            if self.has_won():
                print()
                print("Word:", self.display_word())
                print(
                    f"Congratulations, "
                    f"{self.player.get_first_name()}! "
                    "You guessed the word!"
                )
                break

            if self.has_lost():
                print()
                print("You have no more guesses!")
                print("The secret word was:", self.secret_word)
                break

def main():
    # Core execution logic goes here        
    game = WordGuess() # Create a new game object
    game.play()

if __name__ == "__main__":       
    main()