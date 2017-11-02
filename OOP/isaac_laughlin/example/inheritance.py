class Card():
    def __init__(self, *args):
        pass

class Deck():
    def __init__(self):
        self.cards = []
        for suit in 'cshd':
            for num in range(13):
                self.cards.append(Card(suit, num))

    def shuffle(self):
        pass

    def draw(self):
        pass

class FancyDeck(Deck):
    def __init__(self, back='bicycle'):
        self.back = back
        super().__init__()


fd = FancyDeck()

print(fd.cards, fd.back)
