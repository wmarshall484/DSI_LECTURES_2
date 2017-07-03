def merge(a, b):
    '''
    Merge two pre-sorted lists: a and b.
    Return a merged (still sorted) lists.
    '''

    i, j = 0, 0

    res = []

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < len(a):
        res.append(a[i])
        i += 1

    while j < len(b):
        res.append(b[j])
        j += 1

    return res


def merge_sort(values):

    if len(values) <= 1:
        return values

    mid_index = len(values) / 2

    left_sorted_values = merge_sort(values[:mid_index])
    right_sorted_values = merge_sort(values[mid_index:])

    return merge(left_sorted_values, right_sorted_values)


if __name__ == '__main__':

    import sys

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    lines_sorted = merge_sort(lines)

    print ''.join(lines_sorted)
