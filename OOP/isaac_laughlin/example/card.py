
class Card():
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        self.card_values = {'A':13, 'K':12, 'Q':11, 'J':10, '7': 6}

    def value(self):
        return self.card_values[self.num]

    def __gt__(self, other):
        return self.value() > other.value()

    def __eq__(self, other):
        return self.value() == other.value()