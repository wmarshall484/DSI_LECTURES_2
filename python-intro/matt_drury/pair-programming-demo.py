"""Template class for a pair programming demo."""


class Vector(object):

    def __init__(self, lst):
        self.lst = lst

    def __add__(self, other):
        """Componentwise addition of two vectors."""
        pass

    def __sub__(self, other):
        """Componentwise subtraction of two vectors."""
        pass

    def dot(self, other):
        """Dot product of two vectors."""
        pass

    def angle(self, other):
        """Signed angle between two vectors (in radians)."""
        pass

    def proj(self, other):
       """Projection of other onto self."""
       pass
