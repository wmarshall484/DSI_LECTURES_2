class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "(x=" + self._x.__str__() + ", y=" + self._y.__str__() + ")"

    def get(self):
        return (self._x, self_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def transpose(self, dx=0, dy=0):
        self._x = self._x + dx
        self._y = self._y + dy

