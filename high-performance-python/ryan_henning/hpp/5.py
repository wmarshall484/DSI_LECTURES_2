'''
Python tries to be cleaver by giving you a Process class that works
like the Thread class. But that hides what's actually happening under-
the-hood. Processes are not /actually/ launched like threads are launched.

This script demonstrates why it is a little deceiving to have the
Process class work like the Thread class. Run this script and note the
behavior.

The reason for this behavior is that processes are created via the
system call fork(). What does fork() do? Well, fork(), when called,
creates a copy of the calling process. The original is the "parent"
process, and the copy is the "child" process. There is a lot at play
here, but one of the key points is that the parent and the child each
have a copy of all the process's data (e.g. variables).

With that new info, the behavior we see below makes sense now.
'''

from multiprocessing import Process
from threading import Thread

Parallelizer = Thread


x = 1


def do_stuff():
    global x
    x = 2


if __name__ == '__main__':
    p = Parallelizer(target=do_stuff)
    p.start()
    p.join()
    print x

