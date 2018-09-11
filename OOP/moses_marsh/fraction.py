class Fraction:
    '''
    This class represents a fractional value, e.g., 1/10
    '''

    def __init__(self, numerator, denominator):
        '''
        Initialize this fraction to numerator over denominator
        '''

        if denominator == 0:
            raise ZeroDivisionError('Denominator is zero')

        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return '{} / {}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        '''
        return the sum of two fractions
        '''

        sum_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        sum_denominator = self.denominator * other.denominator
        return Fraction(sum_numerator, sum_denominator)


def gcd(self, a, b):
    '''
    Return the greatest common divisor of two integers
    '''

    while a != 0:
        (a, b) = (b % a, a)
    return b
