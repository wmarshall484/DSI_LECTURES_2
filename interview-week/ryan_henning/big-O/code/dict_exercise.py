def dict_to_str(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is separated by a new
    line.

    For example:
    a: 1
    b: 2

    For nice pythonic code, use iteritems!

    Note: it's possible to do this in 1 line using list comprehensions and the
    join method.
    '''
    return "\n".join("{}: {}".format(key, value) for key, value in d.iteritems())


def dict_to_str_sorted(d):
    '''
    INPUT: dict
    OUTPUT: str

    Return a str containing each key and value in dict d. Keys and values are
    separated by a colon and a space. Each key-value pair is sorted in ascending order by key.
    This is sorted version of dict_to_str().

    Note: This one is also doable in one line!
    '''
    return "\n".join("{}: {}".format(key, value) for key, value in sorted(d.iteritems()))


def dict_difference(d1, d2):
    '''
    INPUT: dict, dict
    OUTPUT: dict

    Combine the two dictionaryies, d1 and d2 as follows. They keys are the union of the keys
    from each dictionary. If the keys are in both dictionaries then the values should be the
    absolute value of the difference between the two values. If a value is only in one dictionary, the
    value should be the absolute value of that value.
    '''
    diff = {}
    for k in set(d1.keys()) | set(d2.keys()):
        diff[k] = abs(d1.get(k, 0) - d2.get(k, 0))
    return diff
