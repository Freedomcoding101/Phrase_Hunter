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
        print(''.join(self.phrazed))
        #display guessed letters instead of placeholders
        #update as the user guesses
        

    def check_letter(self, guess):
        if guess in self.letters:
            for i in range(len(self.letters)):
                if self.letters[i] == guess:
                    self.phrazed[i] = guess


    def check_complete(self):
        #check if the phrase has been guessed (All the blanks filled in)
        if self.letters == self.phrazed:
            print("True")
        else:
            print("False")
        

phrase1 = Phrase("Hello WoRlD")
guess1 = "A"
guess2 = "O"