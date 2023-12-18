# Create your Game class logic in here.
class Game():
    def __init__(self):
        missed = 0
        phrases = 5
        active_phrase = none
        guesses = []

    def start():
        #calls the welcome method, creates the game loop, calls the get_guess method
        #adds the users guess to guesses
        #increments missed by 1 if missed
        #calls game over if 5 misses occur
        #set active phrase to phrase object returned from get_random_phrase() method
        pass

    def get_random_phrase():
        #selects random phrase from a list of five phrases
        pass

    def welcome():
        print("Welcome to the Phrase Hunter game!")
        print("A random phrase will be picked")
        print("You will have five guesses")
        print("Good Luck")

    def get_guess():
        #this metod gets the guess from the user and records it in the guesses list
        pass

    def game_over():
        #displaysa friendly win or loss message at the end of game
        pass
