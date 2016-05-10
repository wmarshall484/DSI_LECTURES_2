
def gcd(a, b):
    '''
    Return the greatest common divisor of the two integers given.
    '''
    while a != 0:
        c = a
        a = b % a
        b = c
    return b


class Fraction:
    '''
    This class represents a franctional value.
    E.g. 1/10
    '''

    def __init__(self, numerator, denominator):
        '''
        Initialize this fraction to (numerator / denominator).
        '''
        self.num = numerator
        self.denom = denominator
        if self.denom == 0:
            raise ZeroDivisionError('you cannot divide by zero')
        self._reduce()

    def _reduce(self):
        '''
        Reduce the fraction to its canonical (simplified) form.
        E.g. 2/4 becomes 1/2.
        '''
        d = gcd(self.num, self.denom)
        self.num /= d
        self.denom /= d
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom
        if self.num == 0:
            self.denom = 1

    def to_float(self):
        '''
        Return a floating point object (approximately)
        equal to this fraction.
        '''
        return float(self.num) / self.denom

    def __repr__(self):
        '''
        Return a string represenation of this fraction.
        '''
        return "{0}/{1}".format(self.num, self.denom)

    def __add__(self, other):
        common_denom = self.denom * other.denom
        new_num = self.num * other.denom + other.num * self.denom
        return Fraction(new_num, common_denom)

