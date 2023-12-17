# Create your Phrase class logic here.
class Phrase():
    

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.placeholder = len(phrase)
        
    def __str__(self):
        return(f"{self.phrase}")

    def __iter__(self):
        return self

def display(Phrase):
    for letter in Phrase:
        if not " ":
            print(_)

def check_letter():
    pass

def check_complete():
    pass

