'''
This script also starts 5 threads and then joins with them (same as 2.py).

The point of this script is to let you see what happens in Activity Monitor
(assuming you're on a Mac) while this script is running.

Notice that activity monitor shows one python process that has 6 threads.
Why 6 instead of 5?
'''

import os
import time
from threading import Thread


def do_stuff(arg1, arg2):

    time.sleep(30.0)


if __name__ == '__main__':

    print "PID={}".format(os.getpid())
    print "Look at Activity Monitor!"

    threads = [Thread(target=do_stuff, args=['bla', i]) for i in xrange(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

