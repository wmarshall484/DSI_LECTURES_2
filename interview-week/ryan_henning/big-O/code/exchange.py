from collections import defaultdict, Counter
from dict_exercise import dict_to_str_sorted
import sys
import os


def read_data(filename):
    '''
    INPUT: string
    OUTPUT: Counter, defaultdict

    Given a filename of the exchange data, return a tuple of two things:
        - a Counter of the number of times each increase/decrease occurs
        - a defaultdict with the list of dates on which each increase/decrease
            occurred
    '''
    cnt = Counter()
    d = defaultdict(list)
    last_val = None
    with open(filename) as f:
        for line in f:
            data = line.split(',')
            if len(data) < 4 or not data[2][0].isdigit():
                continue
            val = float(data[2])
            date = data[0]
            if last_val is not None:
                diff = round(val - last_val, 10)
                cnt[diff] += 1
                d[diff].append(date)
            last_val = val
    return cnt, d


def days_with_the_biggest_gain(d):
    '''
    INPUT: dict
    OUTPUT: int/float, list

    Return the value of the largest increase in exchange rate and a list of the
    dates that correspond to it.
    '''
    m = max(d)
    return m, d[m]


def histogram(cnt, decimals=2):
    '''
    INPUT: Counter, int
    OUTPUT: Counter

    Given a Counter, return a new Counter which rounds the keys to 2 decimal
    places. If multiple keys get rounded to the same number, sum their values.
    '''
    new_cnt = Counter()
    for k, v in cnt.iteritems():
        new_cnt[round(k, decimals)] += v
    return new_cnt


def main(filename):
    '''
    INPUT: string
    OUTPUT: None

    Read in the exchange data from the filename and output the count of the
    number of times each increase or decrease occurs, with the difference
    values rounded to 2 decimal places.

    '''
    cnt, d = read_data(filename)
    new_cnt = histogram(cnt)
    print dict_to_str_sorted(new_cnt)
    val, days = days_with_the_biggest_gain(d)
    print "Day(s) with biggest gain ({0}): {1}".format(val, ','.join(days)) 


if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
        print "Usage: python exchange.py filename.csv"
        exit()
    main(sys.argv[1])
