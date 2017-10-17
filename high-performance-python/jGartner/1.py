'''
This script prints its process id (PID), and then it waits for
user input before terminating. It waits so that you have time to
look in Activity Monitor (assuming you're on a Mac) to verify that
the PID is correct!

Notice that the PID changes every time you run this script.
'''

import os


if __name__ == '__main__':

    print("I am process id (PID):", os.getpid())

    bla = input("Look at Activity Monitor! (Press enter to exit...)")

