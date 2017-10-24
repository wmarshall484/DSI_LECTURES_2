class Line:
    def __init__(self, point1, point2): #change arguments to include 2 points
        if point1 == point2:
            raise.ValueError("Points must be distinct!")
        self._slope = (point2.get_y() - point1.get_y())/(point2.get_x() - point1._x)

        self._intercept = point2

    def __str__(self):
        return "Line with slope {0:.2f} and intercept {1:.2f}".format(self.slope(), self.intercept())

    def get_slope(self):
        pass

    def get_intercept(self):
        pass

    def on_line(self, p):
        pass
