from Point import Point
from Origin import Origin
from PointCollection import PointCollection
from Polygon import Polygon

def main():
    # Define points
    p1 = Point(4, 2)
    p2 = Origin()
    p3 = Point(2, 1)
    l_points = [p1, p2, p3]

    pc = PointCollection(p1, p2, p3)
    print(pc.rightmost())

    # or by defrefrencing a list
    pc = PointCollection(*l_points)
    print(pc.leftmost())

    # you can pass to kwargs by derefferencing a dict
    inp = {"ptype": 'line"', "points": l_points}
    poly = Polygon(**inp)

    # Use a static method
    poly.describe()

    # Use a class method
    poly.print_origin()

if __name__ == "__main__":
    main()