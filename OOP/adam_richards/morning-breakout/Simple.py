#!/usr/bin/env python
"""
A generic template
"""

__author__ = "Mr. Baggins"

class SomeClass():
    """
    A generic class
    """

    def __init__(self):
        """
        Constructor
        """

    def __str__(self):
        """
        Identifing string
        """
        
        return("some class itentifier")


if __name__ == "__main__":
    print("\nRunning...")
    sc = SomeClass()
    print(sc)
    print(sc.__doc__)


    print(dir(sc))
