#!/usr/bin/env python
"""
main class specific tests
"""

import sys,os,unittest
from Dice import BaseDie, LightedDie

## test class for the main window function
class DieTest(unittest.TestCase):
    """
    test the essential functionality
    """

    def setUp(self):
        """
        setup is used when significant setup is required
        this is not needed for the die example
        """

        pass
        
    def testRoll(self):
        """
        ensure roll functionality works
        """
        
        nsides=3
        die = BaseDie(nsides)
        lighted_die = LightedDie(nsides,colors={1:'blue',2:'yellow',3:'gold'})

        self.assertEqual(die.last_roll,None)

        die.roll()
        lighted_die.roll()

        for d in [die,lighted_die]:
            self.assertTrue(d.last_roll>0 and d.last_roll <= nsides)

    def testEquality(self):
        """
        ensure that the == operator works
        die1 == die2
        lighted_die1 == lighted_die2
        die2 == lighted_die1
        die1 == die2 == die3
        """
        pass

    def tearDown(self):
        """
        remove the stuff that you built in setUp (e.g. directories)
        not needed for Die classes
        """
        pass
    
### Run the tests
if __name__ == '__main__':
    unittest.main()
