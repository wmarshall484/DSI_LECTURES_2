from Point import Point
from Origin import Origin


def main():
    p1 = Point(4, 2)
    p2 = Origin()
    p3 = Point(2, 1)
    l_points = [p1, p2, p3]

    for P in l_points:
        print(P)

    p2.transpose(dx=1)


if __name__ == "__main__":
    main()