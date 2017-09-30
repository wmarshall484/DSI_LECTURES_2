from Point import Point


class Origin(Point):
    def __init__(self):
        self._x = 0
        self._y = 0

    def __str__(self):
        return "Origin->" + super(Origin, self).__str__()

    def transpose(self, dx=0, dy=0):
        raise ValueError("Cannot transpose the origin")