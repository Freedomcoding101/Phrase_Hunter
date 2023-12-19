# Create your Phrase class logic here.
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.letters = [letter for letter in self.phrase]
        self.phrazed = ["_" if letter != " " else " " for letter in self.phrase]

    def __str__(self):
        return(f"{self.phrase}")

    def __iter__(self):
        return iter(self.phrase)

    def __eq__(self, other):
        pass

    def display(self):
        print("\n-----------Your Phrase is!!--------------\n")
        print(''.join(self.phrazed))
        #display guessed letters instead of placeholders
        #update as the user guesses
        

    def check_letter(self, guess):
        if guess.lower() in self.letters:
            for i in range(len(self.letters)):
                if self.letters[i] == guess.lower():
                    self.phrazed[i] = guess.lower()


    def check_complete(self):
        #check if the phrase has been guessed (All the blanks filled in)
        if self.letters == self.phrazed:
            return(True)
        else:
            return(False)