import random

class Bag:

    def __init__(self, dice):
        """
        Args:
            dice (list): list of die objects
        """
        self.dice = dice.copy()
    
    def pick_random(self, replace=True):
        die = random.choice(self.dice)
        if not replace:
            self.dice.remove(die)
        return die

    def remove_n_die(self, n):
        for i in range(n):
            self.pick_random(replace=False)

    def sum_n_times(self, n):
        sum_of_rolls = 0
        for i in range(n):
            sum_of_rolls += self.pick_random().roll()
        return sum_of_rolls


class Die:

    def __init__(self, n_sides):
        self.n_sides = n_sides

    def roll(self):
        return random.randint(1,self.n_sides)
