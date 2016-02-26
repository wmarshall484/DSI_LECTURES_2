def gcd(a, b):
    '''
    INPUT: int, int
    OUTPUT: int

    Return the greatest common divisor of the two integers given.
    '''
    while a != 0:
        c = a
        a = b % a
        b = c
    return b


class Fraction(object):
    '''
    A fraction class.
    '''

    def __init__(self, num, denom):
        '''
        Initialize a fraction with the given numerator and denominator.
        '''
        self.num = num
        self.denom = denom
        self._reduce()

    def _reduce(self):
        '''
        Put the fraction in reduced form.
        '''
        if self.num == 0:
            self.denom = 1
        else:
            d = gcd(self.num, self.denom)
            self.num, self.denom = self.num / d, self.denom / d
        return self

    def __add__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the sum of this fraction and other.
        '''
        return Fraction(self.num * other.denom + other.num * self.denom,
                        self.denom * other.denom)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return a fraction that is the difference of this fraction and other.
        '''
        return Fraction(self.num * other.denom - other.num * self.denom,
                        self.denom * other.denom)

    def __mul__(self, other):
        '''
        INTPUT:
            - other: Fraction or int
        Return a fraction that is the product of this fraction and other.
        '''
        if isinstance(other, int):
            return Fraction(self.num * other, self.denom)
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __cmp__(self, other):
        '''
        INPUT:
            - other: Fraction
        Return 0 if equal, -1 if self < other, +1 if self > other
        '''
        return cmp((self - other).num, 0)

    def __repr__(self):
        '''
        Return a string representation of the fraction.
        '''
        whole_part = self.num / self.denom
        if whole_part != 0:
            return "{2} {0}/{1}".format(self.num - whole_part * self.denom, self.denom, whole_part)
        else:
            return "{0}/{1}".format(self.num, self.denom)
