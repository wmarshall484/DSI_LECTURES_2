# Topics
* [Python Terminal (ipython)](#python-terminal)
* [Advanced Python](#advanced-python)
    * [Generators](#generators)
    * [Looping tools](#looping-tools)
    * [List comprehensions](#list-comprehensions)
    * [Lambda functions](#lambda-functions)
    * [Sets and Dictionaries](#sets-and-dictionaries)
    * [Mutable vs Immutable](#mutable-vs-immutable)
    * [Permutations and Combinations](#permutations-and-Combinations)
    * [File I/O](#file-io)
    * [Exception Handling](#exception-handling)
* [Python Style](#python-style)
* [Python Documentation](#documentation)

# Python Terminal

We recommend using `ipython` rather than the standard python terminal to test out your code. Here are some cool things you can do with `ipython`:

1. View the docstring for any python object using `?object`, this is a shorcut for `help(obj)`.
    ```python
    In [5]: ?map
    Type:        builtin_function_or_method
    String form: <built-in function map>
    Namespace:   Python builtin
    Docstring:
    map(function, sequence[, sequence, ...]) -> list

    Return a list of the results of applying the function to the items of...
```    
1. Use tab completion to list possible completions for keywords, and
object attributes. This is similar to using `dir()`.
    ```python
    In [8]: ma #Press tab...
    %macro       %magic       %man         %matplotlib  map          max
```

1. Press UP to cycle back through previous commands. If you start typing in the command and then press UP, it will only cycle through commands that start with those characters.

1. Use `_` for a variable containing the result of the last executed command:

    ```python
    In [1]: 9 * 54
    Out[1]: 486

    In [2]: _
    Out[2]: 486

    In [3]: x = _

    In [4]: x
    Out[4]: 486
    ```

1. You can re-run a line you've already run:

    ```python
    In [10]: exec _i6
    ```

    This will run the code in line 6.

1. You can edit the line before you re-run it:

    ```python
    In [11]: rep 6
    ```

1. This will run python code from a file:

    ```python
    In [1]: run example.py
    ```

1. You can paste text using this:

    ```python
    In [2]: paste
    ```

1. You can edit a function that you've already defined:

    ```python
    In [3]: edit foo
    ```

    It will open in your chosen editor (defaults to vi)

You can check out the ipython [documentation](http://ipython.org/documentation.html) or a [cheat sheet](http://damontallen.github.io/IPython-quick-ref-sheets/) of all the commands (there are a lot!)


# Advanced Python

## Note
`range`, `zip`, `dictionary.keys` do not make lists in Python 3, while they do in Python 2. 

This is a bunch of syntax and special tools that are available in python that come in very handy.

## Generators

First look at this bit of code:

```python
for i in range(1000):
    print(i)
```

In Python 2, the `range` function will create a list of length 1000 and then we iterate over it. This is very wasteful for space! We don't need to create a list of 1000 elements and store it in memory! We can use a *generator* to save the memory:

```python
# python2 only
for i in xrange(1000):
    print(i)
```

In Python 2, the `xrange` function will generate the next value when it's needed, but won't pre-generate everything like the `range` function.

In Python 3, `xrange` is deprecated and `range` creates a generator by default, already optimized.

You'll see other examples of generators below. For the rest of the assignment, we will work in Python 3.


## Looping tools

There are a couple handy tools in python that help you clean up your code when you're looping through a list. First, when possible, use the most simple pythonic loop:

```python
for item in L:
    print(item)
```

### Enumerate

If you need to know the index, you've probably seen code like this:

```python
for i in range(len(L)):
    print(i, L[i])
```

But you should really use `enumerate` (a generator!):

```python
for i, item in enumerate(L):
    print(i, item)
```

Isn't that cleaner?


### Zip

Let's say you have two lists and you want to loop over both of them at the same time. You could do this:

```python
first_names = ['Giovanna', 'Ryan', 'Jon']
last_names = ['Thron', 'Orban', 'Dinu']

for i in range(len(first_names)):
    print(first_names[i], last_names[i])
```

But python has a handy `zip` function to zip two lists together:

```python
In [3]: zip(first_names, last_names)
Out[3]: [('Giovanna', 'Thron'), ('Ryan', 'Orban'), ('Jon', 'Dinu')]
```



```python
for first, last in zip(first_names, last_names):
    print(first, last)
```

If you want a combination of zip and enumerate, you can do the following and have the index and the values:

```python
for i, first, last in zip(count(), first_names, last_names):
    print(i, first, last)
```


(In Python 2, `zip` returns a list; the generator version is called `izip` and you must import it from `itertools`)

## List comprehensions

For simple things, you can do your for loop on one line. Let's say you want to create a new list that has all the items from the first list doubled. You could do this:

```python
doubled = []
for item in L:
    doubled.append(item * 2)
```

But using a list comprehension, you can do this:

```python
doubled = [item * 2 for item in L]
```

### 2D list comprehensions

You can similarly do a double for loop. This is what it would look like the standard way:

```python
L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
doubled = []
for row in L:
    row2 = []
    for item in row:
        row2.append(item * 2)
    doubled.append(row2)
```

And with a list comprehension:

```python
doubled = [[item * 2 for item in row] for row in L]
```

And if you wanted to flatten a 2-dimesionsional list:

```python
In [1]: L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

In [2]: [item for row in L for item in row]
Out[2]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Note the order of the loop statements.


### If statements in list comprehensions

If statements have a weird syntax in a list comprehension:

```python
In [3]: L = [4, 6, 3, 2, 5]

In [4]: ["even" if item % 2 == 0 else "odd" for item in L]
Out[4]: ['even', 'even', 'odd', 'even', 'odd']
```

You can also use an if statement as a filter, to only include some of the items. Here we include only the even numbers:

```python
In [5]: L = [4, 6, 3, 2, 5]

In [6]: [item for item in L if item % 2 == 0]
Out[6]: [4, 6, 2]
```


### Generator comprehensions

You can make it a generator instead of a list if you're just going to be looping over the result. You do this by using round brackets instead of square ones:

```python
L = ["zack desario", "giovanna thron", "ryan orban", "jonathan dinu"]
for name in (item.split()[0] for item in L):
    print(name)
```

Another example is if you're just going to put the result into another function that can use a generator:

```python
In [1]: L = ["zack desario", "giovanna thron", "ryan orban", "jonathan dinu"]

In [2]: "-".join(item.split()[0] for item in L)
Out[2]: 'zack-giovanna-ryan-jonathan'
```


## Lambda Functions

In Python, you can use `lambda` to define unnamed functions. This is really useful for being able to customize `sort` and use functions like `map`, `filter` and `reduce`.

```python
# Sort by first element of tuple
L = [(2, 4), (5, 3), (6, 8), (4, 1)]
L.sort(key=lambda x: x[0])
```

All things you can do with list comprehensions you can also do with `map`. It's more "Pythonic" to use list comprehensions, but understanding how to write maps is key for numpy and pandas, modules we will be using heavily.

```python
# Double every element of a list
def double_list(L):
    return map(lambda x: x * 2, L)
```

The if statement syntax is very similar to list comprehension syntax. Here's the same example (double positive numbers but not negative numbers):

```python
map(lambda x: x * 2 if x > 0 else x, L)
```

You can also use `map` with already implemented functions, like `abs` (absolute value):

```python
L = [0, 5, -8, 9, -3, -2]
M = map(abs, L)  # [0, 5, 8, 9, 3, 2]
```

The `reduce` function can be used to implement aggregation functions. Here's an implementation of `sum` (if sum wasn't already implemented in python):

```python

def sum(L):
    total = 0
    for x in L:
        total += x
    return total
```

But we can do this so much more simply if we use `reduce`. Here `total` is the running total and `x` is the new element from the list.

```python
from functools import reduce

def sum(L):
    return reduce(lambda total, x: total + x, L)
```

And here's a `len` function. Note that we gave an initial value of 0. The default initial value is the first element of the list, which works fine for `sum`, but not for `len`.

```python
def len(L):
    return reduce(lambda total, x: total + 1, L, 0)
```

(In Python 2, `reduce` is a built-in function. In Python 3, it must be imported from `functools`)

## Sets and Dictionaries

Python has some specialized datatypes that come in very handy!

### Dictionaries

Dictionaries are an implementation of hash tables (like Java's hashmaps if you're familiar with them). It's a way of matching key, value pairs. Here is an example:

```python
homestate = {"giovanna": "maine", "ryan": "california", "katie": "michigan", "zack": "new york"}
```

You can easily lookup a person's homestate like this:

```python
print(homestate['katie'])
```

Dictionaries are more powerful than they first appear. It's import to note that it's always really fast to access a dictionary. In a list, if you want to find an element without having the index, you have to search through the whole list. In a dictionary, you can access an element by key quickly!


#### Looping over dictionaries

Here are a couple ways of iterating through a dictionary:

```python
for k in d:
    # iterations over the keys
```

```python
for k in d.keys():
    # iterations over the keys
```


```python
for k, v in d.items():
    # iterates over key, value pairs
```


(In Python 2, `d.keys()` and `d.items()` return lists. Use `d.iterkeys()` and `d.iteritems()` instead when looping.)


#### Checking membership in a dictionary

If you would like to check if a key is in a dictionary, just do this:

```python
if k in d:
    # do something
```


### Counter and defaultdict

You are very often using dictionaries to count things or where the type is always the same. In the module `collections` there are a couple useful datatypes.

`Counter` and `defaultdict` have default values for keys that haven't been seen before. For a `Counter`, the default value will be 0. For a `defaultdict`, the default value will be dependent on what you give it.

With a standard dictionary, you can't access a new key:

```python
In [1]: d = {}

In [2]: d['abc']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-6-e51fd128be60> in <module>()
----> 1 d['abc']

KeyError: 'abc'
```

But with a `Counter` or `defaultdict`, this would be no problem.

```python
In [1]: from collections import Counter, defaultdict

In [2]: c = Counter()

In [3]: c['abc']
Out[3]: 0

In [4]: d = defaultdict(str)

In [5]: d['abc']
Out[5]: ''
```

Note that `d` here has a default value of an empty string since we gave it the argument `str`. Besides how they deal with new keys, these two datatypes work the same as standard dictionaries.

#### Examples

Let's say you want to get a count of the number of occurrences of each character in a string. You could do this:

```python
letter_count = {}
for char in word:
    letter_count[char] = letter_count.get(char, 0) + 1
```

If you use `Counter`, you can just do this:
```python
from collections import Counter
letter_count = Counter(word)
```

Let's say you have a list. You want to know all the indicies that each value appears on. With a stardard dictionary, you could do this:

```python
lst = ['a', 'b', 'a', 'c', 'd', 'c', 'a']
d = {}
for i, item in enumerate(lst):
    if item in d:
        d[item].append(i)
    else:
        d[item] = [i]
# result: {'a': [0, 2, 6], 'b': [1], 'c': [3, 5], 'd': [4]}
```

A `defaultdict` lets you choose a default type for the values so you don't have to do a special case when it's not already in your dictionary. The following code does the same as above.

```python
from collections import defaultdict
d = defaultdict(list)
for i, item in enumerate(lst):
    d[item].append(i)
```


### Sets

Sets are basically value-less dictionaries. If you have a list that you're going to be regularly checking membership of, you should be using a set.

Here's an example to get all the unique words in a string that are longer than 3 characters:

```python
s = set()
for word in string.split():
    if len(word) > 3:
        s.add(word)
```

You can check membership in a set:

```python
if 'house' in s:
    # do something
```

Adding to and checking membership in a set are fast operations (just like in a dictionary).

Sets are also useful for removing duplicates in a list (if you don't care about order):

```python
L_unique = list(set(L))
```

### Order of dictionaries and sets
Dictionaries and sets are **unordered**. This means that if you iterate through them multiple times you will not necessarily get the items in the same order (though computers are deterministic so it will often be the same order, but it is in no way a guarantee). Usually this doesn't matter. There is an `OrderedDict` datatype in the `collections` module if it is ever important to maintain the order in your dictionary.


## Mutable vs Immutable

Python datatypes can be mutable or immutable.

Mutable datatypes can be modified after they are created. Examples of **mutable** datatypes are:
* lists
* sets
* dictionaries

Immutable datatypes cannot be modified once they are created. Examples of **immutable** datatypes are:
* ints
* floats
* strings
* tuples (like immutable lists)

For example, you can do this with a list:

```python
In [1]: L = [1, 2, 3, 4, 5, 6]

In [2]: L[3] = 100

In [3]: L
Out[3]: [1, 2, 3, 100, 5, 6]
```

However, if you try to do the same thing with an immutable type like a string or a tuple, you will get an error:

```python
In [4]: str = "blah"

In [5]: str[3] = 'z'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-6f44c398cf3c> in <module>()
----> 1 str[3] = 'z'

TypeError: 'str' object does not support item assignment

In [6]: t = (1, 2, 3, 4, 5, 6)  # a tuple

In [7]: t[3] = 100
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-9132167f4634> in <module>()
----> 1 t[3] = 100

TypeError: 'tuple' object does not support item assignment
```

It's generally good form to use a tuple instead of a list if you won't be modifying it. If you're not going to use the full functionality of the list, a tuple will suffice.

### Mutability and dictionary keys

A big use case of immutable types is with dictionaries. At some point you will probably encounter this error:

```python
TypeError: unhashable type: 'list'
```

This comes up if you're trying to make the key of a dictionary a mutable type. If you want to have a list as a key, you'll need to transform it to a tuple or another immutable type.

The same goes for items in a set.


## Permutations and Combinations

The `itertools` module functions for getting all the combinations and permutations of an interable. Both of these functions are generators.

```python
In [1]: from itertools import permutations, combinations

In [2]: L = [1, 2, 3]

In [3]: for perm in permutations(L):
   ...:     print(perm)
   ...:
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)

In [4]: for comb in combinations(L, 2):
   ...:     print(comb)
   ...:
(1, 2)
(1, 3)
(2, 3)
```


## File I/O

Reading from and writing to files in python is pretty simple.

### File Input

There are several ways to read from a file.

The preferred way of reading a file is by looping over the lines:

```python
f = open("myfile.txt")
for line in f:
    # do something
f.close()
```

Don't forget to close the file at the end!

You can also use the `readline` method to get a single line:

```python
f = open("myfile.txt")
line = True
while line:
    line = f.readline()
    # do something
f.close()
```

There are also two functions for reading the whole file at once: `read` (returns the whole file as a string) and `readlines` (returns the file as a list of strings). It is generally bad form to use these. They load the whole file into memory, which will be really costly with a large file.

If you forget to close the file, you can also use this syntax:

```python
with open("myfile.txt") as f:
    # do stuff with the file
```

Sometimes this is nice, but if you have a lot of nested indentations it can make your code hard to read.

### File Output

To write to a file, you just need to add a "w" parameter when you open the file and then use the `write` method:

```python
f = open("out.txt", 'w')
f.write("Hello!\n")
f.close()
```

Note that it won't automatically add new lines.

Using the `'w'` parameter will overwrite the file. If you'd like to add to the end of the file instead, you can use the `'a'` parameter.


## Exception Handling

You can catch exceptions in python with the following syntax:

```python
try:
    f = open(filename)
except IOError:
    print("Couldn't open file {}".format(filename))
```

### Guidelines

1. You should *always* give the type of error that you are excepting. If you just do a blanket `except:`, you could easily except away your silly typo.

2. Keep as little code in the try block as possible. If there's one line of code that could produce an error, that is the only line of code which would be within the try except block. You want to make sure to not accidentally catch a real error.

3. You should also avoid using try excepts whenever possible. For example, I could do the following BAD CODE:

    ```python
    try:
        result = L[i]
    except IndexError:
        result = -1
    ```

    Exception handling is expensive! It takes time. You can tell what condition would make this fail, right? If the index is too large we'll get the error, so let's just use an if statement:

    ```python
    if i < len(L):
        result = L[i]
    else:
        result = -1
    ```

    The times when you should use it are when you need to run the code in order to determine if it will produce an error. Two times you frequently see it coming up are in reading from files and making web requests. You need to actually run the code to know whether there's going to be an issue.


# Python style

Python has some standard guidelines for style. It's worth taking a look at the [pep8 style guidelines](http://legacy.python.org/dev/peps/pep-0008/).

Many companies force you to follow style guidelines. Why? If everyone writes with the same style it makes it much easier to read other people's code. Whenever you're writing code keep in mind: **Code is read more than it is written**.

Lucky for us, anaconda comes with `pep8` so you can just run it on your python file and it will tell you what to change:

```
pep8 myprogram.py
```


# Documentation

Python documentation is really good! Here's some links:

* [Python docs home](https://docs.python.org/2/index.html)
* [Python tutorial](https://docs.python.org/2/tutorial/index.html)
* [Lists, tuples, sets, dictionaries](https://docs.python.org/2/tutorial/datastructures.html)
* [itertools](https://docs.python.org/2/library/itertools.html)
* [collections](https://docs.python.org/2/library/collections.html)
