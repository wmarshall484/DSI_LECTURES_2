def fibonacci(n):
    '''
    INPUT: n
    OUTPUT: the nth fibonacci number
    '''
    f1, f2 = 0, 1
    i = 1
    while i < n:
        f1,    f2 =    f2, f1  +f2
        i += 1
    return f2
if __name__ == '__main__':
    print fibonacci(29)
