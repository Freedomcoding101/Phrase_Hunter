# initilize phrase, save it as lowercase and create two lists for comparison
class Phrase():
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.letters = [letter for letter in self.phrase]
        self.phrazed = ["_" if letter != " " else " " for letter in self.phrase]

    def __str__(self):
        return(f"{self.phrase}")

    def __iter__(self):
        return iter(self.phrase)

# joins the _ together and prints to terminal
    def display(self):
        print("\n-----------Your Phrase is!!--------------\n")
        print(' '.join(self.phrazed))

# check to see if guessed letter is in phrase
    def check_letter(self, guess):
        if guess.lower() in self.letters:
            for i in range(len(self.letters)):
                if self.letters[i] == guess.lower():
                    self.phrazed[i] = guess.lower()

# checks to see if game has been won
    def check_complete(self):
        if self.letters == self.phrazed:
            return(True)
        else:
            return(False)
