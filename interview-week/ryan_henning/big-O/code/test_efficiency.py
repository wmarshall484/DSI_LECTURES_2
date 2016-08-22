import nose.tools as n
import efficiency
from collections import Counter


def test_count_invalid_words():
    words = ['a', 'b', 'c']
    expected = ['d', 'd', 'e']
    actual = efficiency.invalid_words(words, 'data/tiny.txt')
    n.assert_equal(type(actual), list, 'Need to return a list.')
    n.assert_equal(Counter(actual), Counter(expected), 'Incorrect result.')


def test_common_characters():
    s = 'abcaabbdad'
    num = 2
    expected = ['a', 'b']
    actual = efficiency.common_characters(s, num)
    n.assert_equal(type(actual), list, 'Need to return a list.')
    n.assert_equal(sorted(actual), sorted(expected), 'Incorrect result.')


def test_sum_to_zero():
    lst = [9, 4, -5, 8, -4, 7, 3]
    expected = (-4, 4)
    actual = efficiency.sum_to_zero(lst)
    n.assert_equal(type(actual), tuple, 'Need to return a tuple.')
    n.assert_equal(set(actual), set(expected), 'Incorrect result.')
