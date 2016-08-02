import nose.tools as n
import exchange
from collections import defaultdict, Counter


def get_message(result, expected):
    message = 'Incorrect result. You returned {0} instead of {1}.'
    return message.format(result, expected)


def test_read_data():
    result = exchange.read_data('data/test_exchange.csv')
    cnt = Counter({0.1:2, -0.05: 1})
    d = defaultdict(list)
    d.update({0.1: ['2014-12-30', '2014-12-28'], -0.05: ['2014-12-29']})
    n.assert_equal(result[0], cnt, get_message(result[0], cnt))
    n.assert_equal(result[1], d, get_message(result[1], d))


def test_days_with_the_biggest_gain():
    d = defaultdict(list)
    d.update({0.1: ['2014-12-30', '2014-12-28'], -0.05: '2014-12-29'})
    result = exchange.days_with_the_biggest_gain(d)
    m = 0.1
    n.assert_equal(result[0], m, get_message(result[0], m))
    n.assert_equal(result[1], d[m], get_message(result[1], d[m]))

def test_histogram():
    cnt = Counter({0.017: 3, 0.097: 1, 0.104: 4})
    expected = Counter({0.02: 3, 0.10: 5})
    result = exchange.histogram(cnt, 2)
    n.assert_equal(expected, result, get_message(result, expected))
