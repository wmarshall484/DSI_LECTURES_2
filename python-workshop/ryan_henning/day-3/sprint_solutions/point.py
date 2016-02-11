from math import sqrt


class Point(object):
    '''
    A 2d point class
    '''
    def __init__(self, x, y):
        '''
        Initialize a point with the given x and y coordinate values.
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Return a string representation of the point.
        '''
        return "Point: {0}, {1}".format(self.x, self.y)

    def __eq__(self, other):
        '''
        INPUT:
            - other: Point
        Return True iff this is the same point as other.
        '''
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which adds the x and y coordinates of the two points
        together.
        '''
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which subtracts the x and y coordinates of the second
        point from the first.
        '''
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        '''
        INPUT:
            - other: int/float
        Return a new Point which multiplies both the x and y coordinate values
        by the given value.
        '''
        return Point(self.x * other, self.y * other)

    def length(self):
        '''
        Return the length of the vector (squareroot of the two values squared)
        '''
        return sqrt(self.x * self.x + self.y * self.y)

    def dist(self, other):
        '''
        Return the distance (float) between this point and the other point given.

        Hint: You should use subtract and len!
        '''
        return (self - other).length()


class Triangle(object):
    '''
    A class to represent a 2d triangle
    '''

    def __init__(self, a, b, c):
        '''
        INPUT:
            - points: an iterable of Point objects
        Constructs a triangle that is defined by the given three points.
        '''
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        '''
        Computes and returns the perimeter of this triangle.
        '''
        a, b, c = self.a, self.b, self.c
        return a.dist(b) + b.dist(c) + c.dist(a)

    def area(self):
        '''
        Computes and returns the area of this triangle.
        '''
        a, b, c = self.a, self.b, self.c
        x = a.dist(b)
        y = b.dist(c)
        z = c.dist(a)
        s = (x + y + z) / 2.0
        return sqrt(s * (s - x) * (s - y) * (s - z))
