def sum_to_zero(lst):
    '''
    INPUT: list of ints
    OUTPUT: tuple of two ints

    Return a tuple of two values from the input list that sum to zero.
    If none exist, return None.
    '''

    # Let:
    #  n = len(lst)



    # Bad solution:                            COST of each line of code:

    for i, item1 in enumerate(lst):          # n
        for item2 in lst[i + 1:]:            # n * (n-1) / 2
            if item1 + item2 == 0:           # n * (n-1) / 2
                return item1, item2          # 0 or 1
    return None                              # 0 or 1

                                      # TOTAL: n + n*(n-1) + 1
                                      #      = n^2 + 1



    # Good solution:                           COST of each line of code:

    counter = defaultdict(int)               # 1
    for item in lst:                         # n
        counter[item] += 1                   # n * 1

    if counter[0] >= 2:                      # 1
        return (0, 0)                        # 0 or 1

    for item in lst:                         # n
        if -item in counter:                 # n * 1
            return item, -item               # 0 or 1

    return None                              # 0 or 1

                                      # TOTAL: 1 + n + (n*1) + 1 + n + (n*1) + 1
                                      #      = 4*n + 3


