'''
This script uses multiple threads to compute the number of factors of a given
integer. This script does not consider 1 and n to be factors of n (even though
they technically are). We're only interested in finding the number of factors
between 1 and n.

Run the script as: `python 3_threads.py <number_to_factorize> <number_of_worker_threads>`
              E.g. `python 3_threads.py 87178291200 4`

Run this command: for i in {1..100}; do python 3_threads.py 87178291200 2; done
Also try:         for i in {1..100}; do python 3_threads.py 1307674368000 2; done

What happens? (It /hopefully/ will print the wrong answer sometimes. I say /hopefully/ because I'm trying
to prove a point about the dangers of threading. It's possible that if you have a fast computer you will
not see this bug for this particular program.)

Btw: 14! = 87178291200
     15! = 1307674368000
'''

from sys import argv
from math import floor, sqrt
from threading import Thread


TOTAL_FACTORS = 0


def count_factors(number, start, end):
    global TOTAL_FACTORS
    for i in range(start, end):
        if number % i == 0:
            TOTAL_FACTORS += 1


if __name__ == '__main__':

    number = int(argv[1])
    num_threads = int(argv[2])

    start = 2
    end = int(floor(sqrt(number))) + 1  # range is [start, end)

    num_to_test = end - start

    tests_per_thread = int(num_to_test / num_threads)
    remainders = num_to_test % num_threads

    threads = []
    for i in range(num_threads):
        start_here = start + i * tests_per_thread
        end_here = start + (i+1) * tests_per_thread
        if i < remainders:
            start_here += i
            end_here += i+1
        else:
            start_here += remainders
            end_here += remainders
        threads.append(Thread(target=count_factors, args=(number, start_here, end_here)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("# Factors:", TOTAL_FACTORS)

