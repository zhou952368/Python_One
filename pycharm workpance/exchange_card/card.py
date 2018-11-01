class Card:

    def __init__(self, flower, char):
        self.flower = flower
        self.char = char

    def __str__(self):
        return self.flower + self.char

