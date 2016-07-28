import collections
words = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star']


def anagrams1(lst):
    result = []
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 and sorted(word1) == sorted(word2):
                result.append(word1)
                break
    return result


def anagrams2(lst):
    result = []
    d = collections.defaultdict(list)
    for word in lst:
        d[tuple(sorted(word))].append(word)
    for key, value in d.iteritems():
        if len(value) > 1:
            result.extend(value)
    return result
