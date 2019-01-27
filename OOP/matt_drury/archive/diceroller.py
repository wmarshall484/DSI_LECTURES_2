import random

class DiceRoller:
    """Rolls a number of dice, and returns the sum of the faces.
    
    Attributes
    ----------
    n_dice: int
      The number of dice to roll.

    n_sides: int
      The number of sides on each die.

    Usage
    -----
    $ dr = DiceRoller(n_dice=2, n_sides=6)
    $ dr.roll()
    5
    $ dr.roll()
    7
    """
    def __init__(self, n_dice=9, n_sides=6):
        self.n_dice = n_dice
        self.n_sides = n_sides

    def roll(self):
        rolls = [random.randint(1, self.n_sides + 1)
                 for _ in range(self.n_dice)]
        return sum(rolls)
