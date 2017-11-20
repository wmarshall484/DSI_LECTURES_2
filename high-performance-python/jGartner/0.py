'''
Before you begin, look at your Mac's "About this Mac" -> "System Report" to
see details about your Mac's processor. Run `sysctl -n machdep.cpu.brand_string`
to see more specifically which processor your Mac has.

Now open Activity Monitor and double-click the CPU history graph at the bottom
to open a floating CPU history graph. How many cores does it show? If it shows
more than what the "System Report" said, that means your cores are hyperthreaded,
meaning each core /pretends/ to be more than one core. Hyperthreaded cores are
mostly just a facade to the OS--they don't provide much gain over non-hyperthreaded
cores.

Note: Run this with environment variable OMP_NUM_THREADS=1 so that numpy doesn't
launch its own OpenMP threads in the background. That's normally fine, but for this
we want to have full control over the threads that are launched so that we can see
what's happening in Activity Monitor.

I'm being a little sneaky here to avoid a very common situation where CPython's GIL
screws up multi-threading performance. I'm avoiding the GIL issue by calling down
into numpy to do heavy computation--numpy will release the GIL before doing that
heavy computation, so we will actually be able to get good parallel performance using
threads in python (a very rare event, really).

Note: Use `killall python` if you want to quickly kill a bunch of processes
you've forked all at once.
'''
from random import random
import numpy as np
import multiprocessing, time
from threading import Thread

def do_stuff():
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    for i in range(1000):
        C = A.dot(B)

def do_stuff_not_numpy():
    A = [[random() for j in range(1000)] for i in range(1000)]
    B = [[random() for j in range(1000)] for i in range(1000)]
    for aaa in range(100):
        C = 0
        for i in range(len(A)):
            for j in range(len(B)):
                C += A[i][j]*B[j][i]


if __name__ == '__main__':
    then = time.time()
    # If I dare say that python is wrong... then I'd say that the name of this
    # function is wrong. What this function returns is the number of cores,
    # not the number of CPUs. Even more specifically, it returns the number of
    # hyperthreaded cores.

    print("# cores =", multiprocessing.cpu_count())

    #do_stuff()
    #do_stuff_not_numpy()

    #threads = [Thread(target=do_stuff) for i in range(2)]
    threads = [Thread(target=do_stuff_not_numpy) for i in range(2)]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    print("Runtime: {}".format(time.time()-then))