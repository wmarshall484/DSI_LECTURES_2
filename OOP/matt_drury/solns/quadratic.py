class QuadraticPolynomial(object):
    """A class representing a polynomial like:
    
        a_0 + a_1 x + a_2 x^2
    """
    
    def __init__(self, a0, a1, a2):
        self.coefficients = (a0, a1, a2)
        
    def evaluate(self, x):
        a0, a1, a2 = self.coefficients
        return a2*x*x + a1*x + a0
    
    def __repr__(self):
        return "QuadraticPolynomial({}, {}, {})".format(
            self.coefficients[0],
            self.coefficients[1],
            self.coefficients[2])
    
    def __str__(self):
        return "{}x^2 + {}x + {}".format(
            self.coefficients[2],
            self.coefficients[1],
            self.coefficients[0])
    
    def _apply_operation_to_coefficients(self, other, operation):
        a0 = operation(self.coefficients[0], other.coefficients[0])
        a1 = operation(self.coefficients[1], other.coefficients[1])
        a2 = operation(self.coefficients[2], other.coefficients[2])
        return QuadraticPolynomial(a0, a1, a2)
    
    def __add__(self, other):
        return self._apply_operation_to_coefficients(other, lambda x, y: x + y)
    
    def __sub__(self, other):
        return self._apply_operation_to_coefficients(other, lambda x, y: x - y)
    
    def differentiate(self):
        a0, a1, a2 = self.coefficients
        return LinearPolynomial(a1, 2 * a2)


class LinearPolynomial(object):
    
    def __init__(self, a0, a1):
        self.coefficients = (a0, a1)
    
    def __str__(self):
        return "{}x + {}".format(self.coefficients[1], self.coefficients[0])


def polynomial_factory(coefficients):
    if coefficients[2] == 0:
        return LinearPolynomial(coefficients[0],
                                coefficients[1])
    else:
        return QuadraticPolynomial(coefficients[0],
                                   coefficients[1],
                                   coefficients[2])
