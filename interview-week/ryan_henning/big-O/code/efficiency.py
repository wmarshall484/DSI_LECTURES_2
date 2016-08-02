from string import punctuation
from collections import Counter


def invalid_words(wordlist, document_filename):
    '''
    INPUT: list, str
    OUTPUT: int

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    '''
    # Use a set instead of a list. Make sure to do this at the beginning since
    # the conversation takes time and you don't want to do it inside of the for
    # loop.
    wordset = set(wordlist)
    with open(document_filename) as doc:
        result = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                if word.lower().strip(punctuation) not in wordset:
                    result.append(word)
        return result


def common_characters(s, num):
    '''
    INPUT: str, int
    OUTPUT: list of chars

    Return the list of characters which appear in the string s more than num
    times.
    '''
    char_counts = Counter(s)
    return [elem for elem, cnt in char_counts.iteritems() if cnt > num]


def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''
    # 0 is a special case since we can repeat the element
    if lst.count(0) >= 2:
        return 0, 0
    # use a set to look up the element!
    s = set(lst)
    for item in lst:
        if -item in s:
            return item, -item
