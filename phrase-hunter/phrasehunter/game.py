from phrasehunter.phrase import Phrase

import random
import sys

# initiates game class with five phrases and all necessary variables
class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = ['HELLO world', 'Monkey BusIness', 'pOTato chips', 'chocolate mACRoons', 'tomATo sauce']
        self.active_phrase = None
        self.guesses = []

# pulls all functions together to create working game
    def start(self):
        self.get_random_phrase()
        self.welcome()

        while self.missed < 6:
            game_status = self.active_phrase.check_complete()

            if game_status == (True):
                self.active_phrase.display()
                self.game_over()
                self.new_game()

            elif self.missed == 5:
                self.game_over()
                self.new_game()
            else:
                self.active_phrase.display()
                print("\n")
                print(f"Wrong Guesses = {self.missed}\n")
                print("Your Guesses so far are...")
                print(f"{self.guesses}\n")
                guess = self.get_guess()
                self.active_phrase.check_letter(guess)
                if guess not in self.active_phrase:
                    self.missed += 1

# grabs a random phrase from phrases list
    def get_random_phrase(self):
        self.active_phrase = Phrase(random.choice(self.phrases))

# welcomes the user to the game
    def welcome(self):
        print("--Welcome to the Phrase Hunter game!--")
        print("----A random phrase will be picked..----")
        print("-You will have only five missed guesses!-")
        print("--------------Good Luck------------------\n")

# queries the user for input, checks if input valid and if it is appends it to guesses
    def get_guess(self):
        try:
            guess = input("What is your guess? (Letter from A-Z)  ").lower()
            if len(guess) != 1 or not guess.isalpha():
                raise TypeError("Please enter a letter from A-Z")
            elif len(guess) == 1 and guess.isalpha():
                self.guesses.append(guess)
        except TypeError:
            print("That is not a valid guess, please enter a letter from A-Z")
        return (guess)

# checks game condition to see if user has won, or lost
    def game_over(self):
        if self.missed == 5:
            print("\nGame over!\n")
        elif (self.active_phrase).check_complete():
            print("\nYou win!!\n")
        else:
            print("Games still on")

# asks the user to play again. Handles exceptions
    def new_game(self):
        while True:
            try:
                new_game = input("Would you like to play again? (Type YES or NO))").lower()
                if new_game == "yes":
                    game_instance = Game()
                    game_instance.start()
                elif new_game == "no":
                    print("\nThanks for playing!!\n")
                    sys.exit()
                else:
                    raise ValueError("That is not a valid choice")
            except ValueError as e:
                print(f"\n{e}\n")
