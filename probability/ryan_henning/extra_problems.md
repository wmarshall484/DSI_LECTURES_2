# Extra Problems

### Problem #1

Let's say we play a game where I keep flipping a coin until I get heads. If the first time I get heads is on the nth coin, then I pay you 2n-1 dollars. How much would you pay me to play this game for us to break even in the long term? Show your work.

Write a program to simulate the game and verify that your answer is correct.

([ref](https://github.com/gSchool/dsi-warmups/blob/master/probability.md))

### Problem #2

A hunter has two hunting dogs. One day, on the trail of some animal, the hunter comes to a place where the road diverges into two paths. He knows that each dog, independent of the other, will choose the correct path with probability p. The hunter decides to let each dog choose a path, and if they agree, he takes that one, and if they disagree, he randomly picks a path. Is his strategy better than just letting one of the two dogs decide on a path? Explain why or why not.

([ref](https://github.com/gSchool/dsi-warmups/blob/master/probability2.md))

### Problem #3

You have a stream of items of large and unknown length that you can only iterate over once. Assume that the stream is _so large_ that you can't hold all the items in memory at once.

**For example:** Perhaps you are streaming tweets from the Twitter "fire hose" over a 24-hour period. You don't know how many tweets you'll get during that time, but you know it will be more than you can hold in memory.

1. Given a data stream of unknown length `n`, write a function that picks an item uniformly at random. This is, each item has a `1/n` chance of being chosen.

    ```python
    def random_element(stream):
        '''
        Return a random element from the generator `stream`.

        Notes:
            - You can't use `len` on this generator.
            - You can only iterate through it once.
            - You don't have enough memory to store every
              element from the generator.
        '''
    ```

2. Extend the algorithm to pick `k` samples from this stream such that each item is equally likely to be selected.

([ref](https://github.com/gSchool/dsi-warmups/blob/master/python_random_element.md))

