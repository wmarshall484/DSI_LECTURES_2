from Origin import Origin
from PointCollection import PointCollection


class Polygon(PointCollection):
    origin = Origin()

    def __init__(self, **kwargs):
        # Type of polygon
        if 'ptype' in kwargs:
            self.ptype_ = kwargs['ptype']
        else:
            self.ptype_ = 'polygon'

        # Get polygon points
        if 'points' in kwargs:
            if type(kwargs["points"]) != type([]):
                raise AttributeError("'points' object must be a list of points")
            # Here, we derefference the points list
            super(Polygon, self).__init__(self, *kwargs["points"])
        else:
            raise AttributeError("Must pass a list of points")

        # See if polygon can be made from points
        if self.size_of() < 3:
            raise AttributeError("Polygon must have at least 3 points")
            # if self.pc_.colinear() is True:
            #    raise AttributeError("Polygon points are all colinear")

    @classmethod
    def print_origin(cls):
        print(cls.origin)

    @staticmethod
    def describe():
        print('''
        Polygons are collections of points, created either from list of points using the keyword "points", or a 
        PointCollection object called "point_collection".  It has built in check to determine if it's a potentially
        valid colleciton.
        ''')