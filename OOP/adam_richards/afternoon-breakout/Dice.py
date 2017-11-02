#!/usr/bin/env python
"""
create an n-sided die

attributes
    total_sides
    last_roll

methods
    return sides
    roll

questions
    how many sides does it have
    what number is face up

Python3
"""

import numpy as np

class BaseDie():
    """
    A base class for a die
    """

    def __init__(self,n_sides,name='generic'):
        """
        Constructor
        """
        ## error checking
        if n_sides <=1:
            raise Exception("not enough sides")
        
        self.n_sides = n_sides
        self.last_roll = None
        self.name = name
        
    def get_sides(self):
        return(self.n_sides)

    def get_current_side(self):
        if self.last_roll:
            return(self.last_roll)
        else:
            return("you have not rolled yet")
        
    def __str__(self):
        return("My name is: %s I have %s sides"%(self.name,self.n_sides))
        
    def __add__(self,other):
        return(self.n_sides+other.n_sides)

    def __gt__(self,other):
        if self.n_sides > other.n_sides:
            return(True)
        else:
            return(False)
    def __eq__(self,other1,other2=None):
        if not other2 and self.n_sides == other1.n_sides:
            return(True)
        else:
            return(False)

        if other2:
            if self.n_sides == other1.n_sides and self.n_sides == other2.n_sides:
                return(True)
            else:
                return(False)

    def __add__(self,other,other2=None):
        return(self.n_sides+other.n_sides)

    def roll(self):
        self.last_roll = np.random.randint(1,self.n_sides+1)
    
class LightedDie(BaseDie):
    """
    A die that shows a diffent color for each side
    """

    def __init__(self, n_sides,colors=None):

        self.n_sides = n_sides
        
        ## imput error checking
        if colors and type(colors)==type({}):
            if len(colors) != self.n_sides:
                raise Exception("improper length color dict imput")
            self.colors = colors
        else:
            self.colors = None

    def get_current_color(self):
       """
       return the current color
       """
       if self.colors:
           if self.n_sides not in self.colors:
               raise Exception("colors does not have side %s"%self.n_sides)
           return(self.colors[self.n_sides])
       else:
           return("colors were not specified")    
       
if __name__ == "__main__":

    ## make a 3 way comparison
    print("\nthree way comparison...")
    die1 = BaseDie(4)
    die2 = BaseDie(4)
    die3 = BaseDie(4)
    print(die1==die2==die3)
    
    ## roll the die
    print("\nrolling the die...")
    print(die1.last_roll)
    die1.roll()
    print(die1.last_roll)
    die1.roll()
    print(die1.last_roll)

    ## lighted die
    lighted_die = LightedDie(4,colors={1:'blue',2:'yellow',3:'cyan',4:'gold'})
    lighted_die.roll()
    ccolor = lighted_die.get_current_color()
    print("current side: %s, current color: %s"%(lighted_die.last_roll,ccolor))
    
