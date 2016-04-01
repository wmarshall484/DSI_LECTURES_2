'''
This script demonstrates how to create 5 threads, start the 5 threads (via
the start() method), and then wait for the 5 threads to terminate (via the
join() method). It also shows how to pass arguments to each thread.
This script will terminate AFTER all 5 threads that it starts have terminated.

Notice how each of the 5 threads have the same PID, but their args and their
thread IDs differ.
'''

import os
import threading
from threading import Thread


def do_stuff(arg1, arg2):

    info = "args=({},{}), PID={} thread_id={}".format(arg1, arg2,
            os.getpid(), threading.current_thread())
    print info


if __name__ == '__main__':

    threads = [Thread(target=do_stuff, args=['hello', i]) for i in xrange(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print "All threads have terminated, so we'll let the main script terminate now."

