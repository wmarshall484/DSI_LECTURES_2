#!/usr/bin/env python
"""
A generic inheritance template
Python3
"""

class Fruit():
    """
    A base class fruit
    """

    def __init__(self,n_fruit):
        """
        Constructor
        """
        
        self.n_fruit = n_fruit
        self.l = []

    def count_fruit(self):
        return(self.n_fruit)

    def __str__(self):
        return("Num fruit: %s"%self.n_fruit)
        
    def __add__(self,other,other2=None):
        return(self.n_fruit+other.n_fruit)
        
class Apple(Fruit):
    """
    An apple class based on the Fruit class
    """

    def __init__(self, n_fruit,colors=None):
        #super(self.__class__, self).__init__(n_fruit)
        self.colors = colors
        
    def sort_apples_by_color(self):
        pass
            
if __name__ == "__main__":
    
    fruit1 = Fruit(4)
    fruit2 = Fruit(2)
    
    ## demonstrate magic functions
    print("combined", fruit1+fruit2)
    
    ## inherited class
    apple1 = Apple(4,colors=['g','g','r','r'])
    print(dir(apple1))
