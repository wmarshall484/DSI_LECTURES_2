import nose.tools as n
import substring


def get_message(result, expected):
    message = 'Incorrect result. You returned {0} instead of {1}.'
    return message.format(result, expected)


def run_substring(func):
    words = ['elephant', 'lion', 'giraffe', 'zebra']
    substrings = ['ion', 'pig', 'eta', 'raz', 'lep']
    result = substring.substring_old(words, substrings)
    expected = ['ion', 'lep']
    n.assert_true(isinstance(result, list), get_message(result, expected))
    n.assert_equal(set(result), set(expected), get_message(result, expected))


def test_subtring_old():
    run_substring(substring.substring_old)


def test_subtring_new():
    run_substring(substring.substring_new)
