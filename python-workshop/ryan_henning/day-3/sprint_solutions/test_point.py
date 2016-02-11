import nose.tools as n
from point import Point, Triangle


def get_message(expected, actual):
    message = 'Incorrect result. You returned {1} instead of {0}.'
    return message.format(expected, actual)


def test_repr():
    p = Point(6, 2)
    expected = 'Point: 6, 2'
    actual = repr(p)
    n.assert_equal(expected, actual, get_message(expected, actual))


def test_length():
    p = Point(3, 4)
    expected = 5.0
    actual = p.length()
    n.assert_almost_equal(expected, actual, msg=get_message(expected, actual))


def test_eq():
    p1 = Point(6, 2)
    p2 = Point(6, 2)
    p3 = Point(6, 3)
    n.assert_equal(p1, p2, 'expected {0} equal to {1}'.format(p1, p2))
    n.assert_not_equal(p1, p3, 'expected {0} not equal to {1}'.format(p1, p3))


def test_add():
    p1 = Point(2, 5)
    p2 = Point(6, 7)
    actual = p1 + p2
    n.assert_equal(8, actual.x, get_message(8, actual.x))
    n.assert_equal(12, actual.y, get_message(12, actual.y))


def test_sub():
    p1 = Point(2, 5)
    p2 = Point(6, 7)
    actual = p2 - p1
    n.assert_equal(4, actual.x, get_message(4, actual.x))
    n.assert_equal(2, actual.y, get_message(2, actual.y))


def test_mul():
    p1 = Point(2, 5)
    actual = p1 * 3
    n.assert_equal(6, actual.x, get_message(6, actual.x))
    n.assert_equal(15, actual.y, get_message(15, actual.y))


def test_dist():
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    actual = p1.dist(p2)
    expected = 5.0
    n.assert_almost_equal(expected, actual, msg=get_message(expected, actual))


def test_perimeter_and_area():
    p1 = Point(2, 2)
    p2 = Point(2, 7)
    p3 = Point(5, 4)
    triange = Triangle(p1, p2, p3)
    actual = triange.perimeter()
    expected = 12.8481919626
    n.assert_almost_equal(expected, actual, msg=get_message(expected, actual))
    actual = triange.area()
    expected = 7.49999999999
    n.assert_almost_equal(expected, actual, msg=get_message(expected, actual))
