'''
This script computes the number of factors of a given integer. This script
does not consider 1 and n to be factors of n (even though they technically
are). We're only interested in finding the number of factors between 1 and n.
'''

from sys import argv
from math import floor, sqrt


def count_factors(number, start, end):
    total_factors = 0
    for i in xrange(start, end):
        if number % i == 0:
            total_factors += 1
    return total_factors


if __name__ == '__main__':

    number = int(argv[1])

    start = 2
    end = int(floor(sqrt(number))) + 1  # range is [start, end)

    print "# Factors:", count_factors(number, start, end)

