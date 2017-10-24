class Point:
    """A class for describing a 2 dimentional cartesian point.

    Examples
    --------
    >>> my_point = Point(4, 1)
    >>> my_point.transpose(dy=-2)
    >>> my_point.get()
    (4, -1)
    """

    def __init__(self, x, y):
        """
        Initialize Point

        Parameters
        ----------
        x : float
        y : float
        """
        self._x = x
        self._y = y

    def __str__(self):
        """Provide a string representation for pretty print"""
        return "(x=" + self._x.__str__() + ", y=" + self._y.__str__() + ")"

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

    def get(self):
        """Return a Tuple version of the point"""
        return (self._x, self._y)

    def get_x(self):
        """Provide access to the X variable"""
        return self._x

    def get_y(self):
        """Provide access to the Y variable"""
        return self._y

    def transpose(self, dx=0, dy=0):
        """Allow the point to be transposed within the X-Y plane"""
        self._x = self._x + dx
        self._y = self._y + dy

