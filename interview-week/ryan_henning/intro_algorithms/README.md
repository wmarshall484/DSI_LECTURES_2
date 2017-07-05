# Outline

- What is a program?
- What is an algorithm?
- Examples of algorithms:
  - bubble sort
  - fibonacci sequential
  - fibonacci recursive
  - fibonacci memoization
  - merge two sorted lists
  - mergesort

# What is a program?

> data + algorithm

Talk about it:
- Why is it not useful to have data only?
- Why is it not useful to have algorithms only?

> input -> process -> output

Talk about it:
- The "process" is one or more algorithms.
- The input/output is data.

# What is an algorithm

We will write:
 - bubble sort
 - fibonacci sequential
 - fibonacci recursive
 - fibonacci memoization
 - merge two sorted lists
 - mergesort

### Bubble Sort

Motivate the algorithm with little labeld cups.

Write live:

```python
def bubble_sort(numbers):
    while True:
        did_swap_something = False
        for i in range(len(numbers)-1):
            curr_num = numbers[i]
            next_num = numbers[i+1]
            if curr_num > next_num:
                numbers[i+1], numbers[i] = curr_num, next_num
                did_swap_something = True
        if not did_swap_something:
            break
    return numbers

my_list_of_things = [3, 4, 7, 1, 2, 8, 9, 3, 5, 6]
print my_list_of_things

print bubble_sort(my_list_of_things)

print sorted(my_list_of_things)
```

Btw, in real life, don't write your own sorting functions!

### Fibonacci Sequence

Review the sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Begin by leading them through the sequential solution, then the recursive, then the memoized.

```python
def fib_sequential(n):

    if n == 1 or n == 2:
        return 1

    prev, prev_prev = 1, 1

    for i in range(3, n):
        curr_in_sequence = prev + prev_prev
        prev, prev_prev = curr_in_sequence, prev

    return prev + prev_prev

print fib_sequential(500)

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

print fib_recursive(37)
```

Talk about why the fib_recursive is so bad! Draw the call tree.

Fix with this:

```python
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

print fib_recursive(37)
```

### Merge

Demo the code below, then send it to them and give them 10 minutes of self-study on it.

```python
def merge(a, b):
    '''
    Merge two pre-sorted lists: a and b.
    Return a merged (still sorted) list.
    '''

    i, j = 0, 0

    res = []

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < len(a):
        res.append(a[i])
        i += 1

    while j < len(b):
        res.append(b[j])
        j += 1

    return res


print merge([1, 4, 7, 9, 12], [5, 8, 9, 9, 10, 30])
```

### Mergesort

Write this live.

```python
def mergesort(numbers):

    if len(numbers) <= 1:
        return numbers

    mid_index = len(numbers) / 2

    left_numbers = numbers[0:mid_index]
    right_numbers = numbers[mid_index:]

    left_numbers = mergesort(left_numbers)
    right_numbers = mergesort(right_numbers)

    merged = merge(left_numbers, right_numbers)

    return merged


print mergesort([4, 9, 2, 4, 9, 0, 10, 299, 4, -3, 4])
```
