#!/anaconda/bin/python

import time
import sys

def fizz_buzz(i):
    if i%15==0:
        return "fizz-buzz"
    if i%5==0:
        return "Buzz"
    if i%3==0:
        return "fizz"
    return i

if __name__ == "__main__":
    for i in range(100):
        print(fizz_buzz(i))
        sys.stdout.flush()
        #time.sleep(2)
