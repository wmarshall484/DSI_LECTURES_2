class PointCollection:
    # *args lets you pass in a list of objects instead of
    def __init__(self, *args):
        self.points_ = []
        for p in args:
            self.points_.append(p)

    def leftmost(self):
        return sorted(self.points_, key=lambda x: x.get_x())[0]

    def rightmost(self):
        return sorted(self.points_, key=lambda x: x.get_y())[-1]

    def size_of(self):
        return len(self.points_)

    def get_points(self):
        return self.points_

    def colinear(self):
        line = Line(self.leftmost(), self.rightmost())
        for p in self.points_:
            if line.on_line(p) is False:
                return False
        return True