'''
This scripts brings all these concepts together. Here's how to
use multiprocessing and multithreading together: first create
several processes, then in each of those create several threads.
This is just a template.

When would creating several processes be a good idea? Here's a
few reasons:
    - If one process dies, it doesn't destroy all the other processes.
      This is NOT the case if you use threads. Btw, most browsers will
      create one process to run each tab for this very reason; you don't
      want an error in one of your tabs to bring down the whole browser!
    - This next point is true ONLY FOR PYTHON: The implementation of python we
      all use (CPython) has what they call the Global Interpreter Lock (GIL)
      that prevents more than one thread of a single process from executing
      python code concurrently. So... if you want your python code to be
      executed concurrently... you gotta use multiple processes (multiprocessing).

When would creating several threads be a good idea? Here's a
few reasons:
    - If you need to create/destroy many threads quickly in a loop. Thread
      creation and destruction has less overhead than process creation and
      destruction.
    - If you need easy & fast access to shared memory. This is needed when
      your threads need to coordinate to get things done.

By the way, multiprocessing and multithreading is hard! E.g. Look at all the
warnings just about using multiprocessing.Queue on this page:
    https://docs.python.org/2/library/multiprocessing.html#pipes-and-queues

Keep in mind Donald Knuth's quote:
    "The real problem is that programmers have spent far too much time worrying
     about efficiency in the wrong places and at the wrong times; premature
     optimization is the root of all evil (or at least most of it) in programming."
        - https://en.wikiquote.org/wiki/Donald_Knuth

Translation: Don't worry about multiprocessing and multithreading until you NEED to.
'''

import os
import time
import threading
from threading import Thread
from multiprocessing import Process


num_processes = 3
num_threads_per_process = 5


def thread_main():
    info = "thread_main: PID={} thread_id={}".format(
            os.getpid(), threading.current_thread())
    print(info)
    time.sleep(30.0)


def process_main():
    threads = [Thread(target=thread_main) for i in range(num_threads_per_process)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    processes = [Process(target=process_main) for i in range(num_processes)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

