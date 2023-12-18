from phrase import Phrase

import random


class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = ['HELLO world', 'mINIture donkey', 'pOTato chips', 'chocolate mACRoons', 'tomATo sauce']
        self.active_phrase = None
        self.guesses = []

    def start(self):
        game_instance.get_random_phrase()
        game_instance.welcome()
        while self.missed < 5:
            self.active_phrase.display()
            game_instance.get_guess()

            

        #increments missed by 1 if missed
        #calls game over if 5 misses occur
        #set active phrase to phrase object returned from get_random_phrase() method
        pass

    def get_random_phrase(self):
        self.active_phrase = Phrase(random.choice(self.phrases))
        print(self.active_phrase)
        

    def welcome(self):
        print("--Welcome to the Phrase Hunter game!--")
        print("----A random phrase will be picked..----")
        print("-You will have only five missed guesses!-")
        print("--------------Good Luck------------------")

    def get_guess(self):
        #this method gets the guess from the user and records it in the guesses list
        guess = input("What is your guess? (Letter from A-Z)  ").lower()
        self.guesses.append(guess)
        print(self.guesses)

    def game_over(self):
        if self.missed > 5:
            print("Game over motherfucker")
        elif (self.active_phrase).check_complete() == True:
            print("You win motherfucker!!")
        pass

game_instance = Game()