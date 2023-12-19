from phrasehunter.phrase import Phrase

import random
import sys


class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = ['HELLO world', 'Monkey BusIness', 'pOTato chips', 'chocolate mACRoons', 'tomATo sauce']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.get_random_phrase()
        self.welcome()
        
        while self.missed < 6:

            game_status = self.active_phrase.check_complete()

            if game_status == (True):
                self.game_over()
                new_game = input("Would you like to play again? (Type YES or NO))").lower()
                if new_game == "yes":
                    new_game_instance.start()
                else:
                    break
            elif self.missed == 5:
                self.game_over()
                new_game = input("Would you like to play again? (Type YES or NO))").lower()
                if new_game == "yes":
                    new_game_instance.start()
                else:
                    break
            else:
                self.active_phrase.display()
                print("\n")
                print(f"Wrong Guesses = {self.missed}\n")
                print("Your Guesses so far are...")
                print(f"{self.guesses}\n")
                print(game_status)
                guess = self.get_guess()
                self.active_phrase.check_letter(guess)
                if guess not in self.active_phrase:
                    self.missed +=1


        #increments missed by 1 if missed
        #calls game over if 5 misses occur
        #set active phrase to phrase object returned from get_random_phrase() method
        pass

    def get_random_phrase(self):
        self.active_phrase = Phrase(random.choice(self.phrases))

    def welcome(self):
        print("--Welcome to the Phrase Hunter game!--")
        print("----A random phrase will be picked..----")
        print("-You will have only five missed guesses!-")
        print("--------------Good Luck------------------\n")

    def get_guess(self):
        #this method gets the guess from the user and records it in the guesses list
        guess = input("What is your guess? (Letter from A-Z)  ").lower()
        self.guesses.append(guess)
        return (guess)

    def game_over(self):
        if self.missed == 5:
            print("\nGame over!")
        elif (self.active_phrase).check_complete() == (True):
            print("\nYou win!!")
        else:
            print("Games still on")
        

game_instance = Game()
new_game_instance = Game()