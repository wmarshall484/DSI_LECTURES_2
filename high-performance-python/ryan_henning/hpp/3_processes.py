'''
This script uses multiple processes to compute the number of factors of a given
integer. This script does not consider 1 and n to be factors of n (even though
they technically are). We're only interested in finding the number of factors
between 1 and n.

Run the script as: `python 3_processes.py <number_to_factorize> <number_of_worker_processes>`
              E.g. `python 3_processes.py 87178291200 4`

Run this command: for i in {1..100}; do python 3_processes.py 87178291200 2; done
Also try:         for i in {1..100}; do python 3_processes.py 1307674368000 2; done

It prints the correct answer every time now! Notice that we had to use a fancy queue
to get the results from each process.

Try comparing the timings of all these options:
    %timeit %run 3_serial.py 123456787654321 4
    %timeit %run 3_threads.py 123456787654321 4
    %timeit %run 3_processes.py 123456787654321 4
'''

from sys import argv
from math import floor, sqrt
from multiprocessing import Process, Queue


def count_factors(number, start, end, queue):
    total_factors = 0
    for i in xrange(start, end):
        if number % i == 0:
            total_factors += 1
    queue.put(total_factors)


if __name__ == '__main__':

    number = int(argv[1])
    num_processes = int(argv[2])

    start = 2
    end = int(floor(sqrt(number))) + 1  # range is [start, end)

    num_to_test = end - start

    tests_per_process = num_to_test / num_processes
    remainders = num_to_test % num_processes

    queue = Queue()

    processes = []
    for i in xrange(num_processes):
        start_here = start + i * tests_per_process
        end_here = start + (i+1) * tests_per_process
        if i < remainders:
            start_here += i
            end_here += i+1
        else:
            start_here += remainders
            end_here += remainders
        processes.append(Process(target=count_factors, args=(number, start_here, end_here, queue)))

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    total_factors = 0
    while not queue.empty():
        total_factors += queue.get()
    print "# Factors:", total_factors

