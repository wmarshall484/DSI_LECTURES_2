# Object Oriented Programming (Classes)

Object Oriented Programming is about how we *organize* our ideas in code.

Programs are made up of two fundamental, conceptual components:
    
  - Data
  - Algorithms to manipulate the data

So to have an expressive and useful programming language, we need ways to both:

  - Create new types of data.
  - Create re-usable algorithms to manipulate that data.

Sometimes the algorithms we need to manipulate data are tied closely to the structure of the data itself, and in this case we would like to:

  - Associate algorithms with specific data structures

Classes are a popular way of accomplishing all of these goals, and it is Python's preferred high level organizational concept.

## Objectives

  - Give basic examples of objects in python (list and dictionaries)
  - Give definitions of object, attribute, and method, along with examples.
  - Create a new datatype using a class.
  - Describe the difference between a class and an object.
  - Describe what `self` is.
  - Add natural behaviour to a class with dunder methods.

## Basic Example: Lists

Python `list`s are a very useful type of data structure, and they have lot's of associated algorithms.  Let's take a closer look a lists and how they work.

### Methods

```python
# Q: Why didn't I call it 'l', why didn't I call it 'list'?
lst = [1, 2, 2, 3, 4, 4, 4]

# Associated algorithm: count
print(lst.count(2))
print(lst.count(3))

print(lst)
```
    #    2
    #    1
    #    [1, 2, 2, 3, 4, 4, 4]

The `count` function is associated with the `list` data type.

Functions that are associated to a specific data type in this way are called *methods*.  So we would say

> `count` is a method of the data type `list`

Methods are (generally) called using the `.` notation:

```python
data_element.method(additional_arguments)
```

### Pure vs. Impure Methods

Some methods actually *change* the data they operate on:

```python
print(lst)

lst.append(5)

print(lst)
```
    #    [1, 2, 2, 3, 4, 4, 4]
    #    [1, 2, 2, 3, 4, 4, 4, 5]

Methods which do **not** change the underlying data (`list.count`) are called **pure methods**, methods that *do* change the underlying data (`list.append`) are called **impure methods**.

Changing the data without giving it a new name (or, at the extreme, copying it first) is called **mutating** the data.  Some data types protect against changing the data in place, they are called **imutable types**.

```python
tup = (1, 2, 3)
tup[2] = 4
```

    #    ---------------------------------------------------------------------------
    #
    #    TypeError                                 Traceback (most recent call last)
    #
    #    <ipython-input-4-584a888776e5> in <module>()
    #          1 tup = (1, 2, 3)
    #    ----> 2 tup[2] = 4
    #    
    #
    #    TypeError: 'tuple' object does not support item assignment


### Magic Methods

Some things that do not look like methods actually are, indexing for example:

```python
print(lst[2])
print(lst.__getitem__(2))
```
    #    2
    #    2

The `__getitem__` is called a **magic method**.  There are spelled with two underscores and can be called with special syntax, which lead to thier other common name: **dunder maethods**.  This one would be pronounced "dunder-get-item".

Other magic methods can be used in place of setting by index, slicing an object, or getting the length of an object.

```python
# lst[2] = 100
lst.__setitem__(2, 100)

# lst[2]
print(lst.__getitem__(2))

# lst[1:5]
print lst.__getslice__(1, 5)

# len(lst)
print(lst.__len__())
```
    #    100
    #    [2, 100, 3, 4]
    #    8


## More Advanced Examples

The python standard library has many examples of additional data types.  We will be re-implementing two of the more useful ones, `defaultdict` and `OrderedDict`.

```python
from collections import defaultdict, OrderedDict
```

### defaultdict

`defautdict` is a simple but effective alternative to a dictionary that adds a touch of extra functionality which can save lots of work in some relatively common situations.

Recall that with a normal dictionary, attempting to lookup a key that does not exist is an error.

```python
D = {'a': 1, 'b': 2}

D['c']
```

    #    ---------------------------------------------------------------------------
    #
    #    KeyError                                  Traceback (most recent call last)
    #
    #    <ipython-input-18-d8c10fe02c26> in <module>()
    #          1 D = {'a': 1, 'b': 2}
    #          2 
    #    ----> 3 D['c']
    #    
    #
    #    KeyError: 'c'

A `defaultdict` allows you to specify a default value to return when a non-existent key lookup is attempted.

```python
def default():
    """A function that returns a default value, called when we attempt to
    access a non-existent key in a default dictionary.
    """
    return 0

D = defaultdict(default, {'a': 1, 'b': 2})
print(D['a'])
print(D['c'])
print(D)
```
    #    1
    #    0
    #    defaultdict(<function <lambda> at 0x104773050>, {'a': 1, 'c': 0, 'b': 2})

Note: In our creation of the default dict above, the line `D = defaultdict(int, {'a': 1, 'b': 2})` is more idomatic.  We chose to write it the way we did above as it makes more explicit what is going on.

Note: It's a bit weird to have to pass in a function that returns the default value instead of the default value itself, but this is needed to avoid weird problems arising from mutable objects like lists.  Passing a function guarentes that this will work:

```python
D = defaultdict(list, {})

print(D['a'])

D['a'].append(1)
D['a'].append(2)
D['b'].append(1)

print(D)
```

    #    []
    #    defaultdict(<type 'list'>, {'a': [1, 2], 'b': [1]})

A more naive implementation would result in the **same** list being shared by all keys.

## Making Your Own Default Dict

Let's implement our own default dictionaries.

**Note:** In practice, we would not do this.  Since the `defaultdict` datatype already exists, there is no benefit in reimplementing it.  But it's instructional to see how we could do this if our needs were for something slightly different.

There are two concepts we need

  - A `class` is a template for a new data type.  It contains information on what data is needed to construct the data type, how to store the data internally, and what algorithms can be applied to the data type.
  - An instance of a class is a concrete object of the new data type.
  
A class is a recipe for constructing instances of that class.

**Question**: In the picture below, what are the classes, and what are the instances of these classes?

![Examples of Objects of Different Classes](classes-and-objects.png)

### Example of a Class: defaultdict

`defaultdict` is a class

```python
from inspect import isclass
isclass(defaultdict)
```

    #    True

Using the class `defaultdict` as a function creates an instance of that class.

Note: The process of using the class itself as a function is called **construction**, and in this context the class is being used as a **constructor**.  The idea is that we are "constructing" a new object whose type is the class.

```python
D = defaultdict(lambda: 0, {'a': 1, 'b': 2})
isinstance(D, defaultdict)
```
    #    True

We usually abbreviate the phrase

> `D` is an instance of class `defaultdict`.

as

> `D` is a `defaultdict`.

In this way, `defaultdict` is thought of as a **type** (or datatype).  This is analagous to the `int`s, `float`s, `string`s, etc that we base all our programs on.

### Creating a Custom Class

The basics of creating a custom class in python is very easy

```python
class MyClass(object):
    pass  # Do nothing.
```

```python
my_instance = MyClass()
isinstance(my_instance, MyClass)
```

    #    True

This is a pretty dumb class as it stands, it cant really *do* anything.  To get something useful we have to add data and behaviour to our class.

# Storing Data In A Class

The first step is to determine what data we need to store.  In this case it's pretty easy, we need

  - The underlying dictionary that we are going to attempt lookups into.
  - The default action to take when a lookup fails.

Let's mimic the way Python's built in default dict works.  We need to add some functionality to **supply and then store** both of these data elements when we create an instance of the class.  This is done using a special *method*, `__init__`.

**Note:** `__init__` is pronounced *dunder-in-it*.

```python
class MyDefaultDict(object):
    """A personal implementation of a default dictionary."""
    
    def __init__(self, default, dictionary):
        self.default = default
        self.dictionary = dictionary
```

There's a lot of new concepts in this code, but let's first see how it works.

```python
MD = MyDefaultDict(lambda: 0, {'a': 1, 'b': 2})
print(MD.default)
print(MD.default())
print(MD.dictionary)
```

    #    <function <lambda> at 0x1046d6aa0>
    #    0
    #    {'a': 1, 'b': 2}

When we use a class like a function

```python
my_instance = MyClass()  # <- Called like a function.
```

it is to create *instances of that class*.  

We will often be working with more than one instance of a single class

```python
MD = MyDefaultDict(lambda: 0, {'a': 1, 'b': 2})
MD2 = MyDefaultDict(lambda: 1, {'a': 2, 'b': 3, 'c': 5})

print(MD.dictionary)
print(MD2.dictionary)
```

    #    {'a': 1, 'b': 2}
    #    {'a': 2, 'c': 5, 'b': 3}

Note the important point: **Both** `MD` and `MD2` are instances of the **same class**, but they contain **different data**; they are **independent objects of the same type**.

### The self Placeholder

Inside of the code defining a class, `self` represents the instance of the class we are manipulating.

A statement like

```
self.default = default
```

creates what is known as an **instance varaible** or **instance data**.  In this specific line, we attach the `default` function to the instance of the class currently being created.

There are two main ways that `self` is used:

  - References to `self` inside the `__init__` method refer to the object **currently being created**.
  - References to `self` in any other method (see more below) refer to the object used to reference a call to this method.

For example, when we call a method like:

```python
some_object.some_method(an_argument, another_argument)
```

any references to `self` inside the definition of `some_method` will refer to `some_object`.

So our use of self in the `__init__` method

```python
def __init__(self, default, dictionary):
    self.default = default
    self.dictionary = dictionary
```

Is setting up our `MyDefaultDict` objects so that, once created, each instance of `MyDefaultDict` stores both `default` and `dictionary` data.

### Adding Methods to Manipulate Data in a Class

Let's implement `__getitem__` and `__setitem__`, which will allow us to index into instances of our class like this

```
MD['a']
# Means the same thing as MD.__getitem__('a')

MD['c'] = 3
# Means the same thing as MD.__setitem__('c', 3)
```

As a first attempt, let's ignore our goal of adding default behaviour, we can add that later on down the line.

```python
class MyDefaultDict(object):
    """A personal implementation of a default dictionary."""
    
    def __init__(self, default, dictionary):
        self.default = default
        self.dictionary = dictionary
        
    def __getitem__(self, key):
        return self.dictionary[key]
    
    def __setitem__(self, key, value):
        self.dictionary[key] = value
```

Let's test it out.


```python
MD = MyDefaultDict(lambda: 0, {'a': 1, 'b': 2})

print(MD['a'])
print(MD['b'])

MD['c'] = 3

print(MD.dictionary)
```

    #    1
    #    2
    #    {'a': 1, 'c': 3, 'b': 2}

Let's deconstruct one of these calls:

```python
MD['a']
```

This is equivalent to the following call to `__getitem__`:

```python
MD.__getitem__('a')
```

In our call, the object `MD` is used to reference the `__getitem__` method, so inside the `__getitem__` definition

```python
def __getitem__(self, key):
    return self.dictionary[key]
```

the `self` parameter refers to `MD`.  The expression `self.dictionary` then refers to the `dictionary` data stored in the `MD` object, which we index in the usual way.


### Adding the Special Default Behaviour

Now lets add in the special behaviour on our indexing, we want to return the default value when an attempt is made to access a key that does not exist in the dictionary.

```python
class MyDefaultDict(object):
    """A personal implementation of a default dictionary."""
    
    def __init__(self, default, dictionary):
        self.default = default
        self.dictionary = dictionary
        
    def __getitem__(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            self.dictionary[key] = self.default()
            return self.dictionary[key]
    
    def __setitem__(self, key, value):
        self.dictionary[key] = value
```

Let's try it out:

```python
MD = MyDefaultDict(lambda: 0, {'a': 1, 'b': 2})

print(MD['a'])
print(MD['b'])

# This next key does not yet exist.
print(MD['c'])

print(MD.dictionary)
```

    #    1
    #    2
    #    0
    #    {'a': 1, 'c': 0, 'b': 2}


### Adding Other Dict-y Things

A few things that should work for dictionaries still don't work for our new datatype

```python
len(MD)
```

    #    ---------------------------------------------------------------------------
    #
    #    TypeError                                 Traceback (most recent call last)
    #
    #    <ipython-input-79-9aab7d873478> in <module>()
    #    ----> 1 len(MD)
    #    
    #
    #    TypeError: object of type 'MyDefaultDict' has no len()

It seems obvious what we should do here, the `len` of our datatype should be the `len` of the dictionary that we stored, but we must *tell* python this is the case.

Additionally, code like

```python
'c' in MD
```

and

```python
for key in MD:
    print key, MD[key]
```

will cause an infinite loop, due to a design error (at least in the author's opinion) in Python itself.

Let's fix that with more magic methods:

```python
class MyDefaultDict(object):
    """A personal implementation of a default dictionary."""
    
    def __init__(self, default, dictionary):
        self.default = default
        self.dictionary = dictionary
        
    def __getitem__(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return self.default()
    
    def __setitem__(self, key, value):
        self.dictionary[key] = value
        
    def __len__(self):
        return len(self.dictionary)
        
    def __contains__(self, key):
        return key in self.dictionary
    
    def __iter__(self):
        for key in self.dictionary:
            yield key
```

We have a few new methods:

  - `__len__` allows our datatype to support calls to `len`.
  - `__contains__` allows our datatype to support the `in` keyword.
  - `__iter__` allows our datatype to support iteration, i.e., for loops.  The `yield` keyword here is new, and it is a powerful feature of python you will see often.  You should find some time to read about it [here](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python).

Let's try out our new features.

```python
MD = MyDefaultDict(lambda: 0, {'a': 1, 'b': 2})
```

```python
print(len(MD))
```

    #    2

```python
print('a' in MD)
```

    #    True

```python
for key in MD:
    print key, MD[key]
```

    #    a 1
    #    b 2

### OrderedDict

The `OrderedDict` type is a dictionary that remembers the order that keys are added.  While a basic dictionary has no order - iterating over a regular dictionary will access the key, values in a random order, iterating through a `OrderedDict` will access the keys in the same order that they were added.

Your task is to **implement an ordered dictionary**.  Here are some questions to ask yourself:

  - What data will you store on each instance.  Clearly you need a `dictionary`, just like in `defaultdict`.  How are you going to remember the order that keys were added to the dictionary?
  - What methods will you need to implement.  Which one is the important one, i.e., the one that adds the new and interesting behaviour?
  - What happens if you add a key twice?  This is an edge case, which your final implementation should account for.

### Non-Magic Methods

It's worth mentioning that not all methods are magic.  Here is a class that represents a simple quadratic polynomial, and has an `evaluate` method, which plugs a number into the polynomial.


```python
class QuadraticPolynomial(object):
    """A class representing a polynomial like:
    
        a_0 + a_1 x + a_2 x^2
    """
    
    def __init__(self, a0, a1, a2):
        self.coefficients = (a0, a1, a2)
        
    def evaluate(self, x):
        a0, a1, a2 = self.coefficients
        return a2 * x * x + a1 * x + a0
```

## Programming Together

1. Use the `__add__` magic method to allow something like `QuadraticPolynomial(1, 1, 1) + QuadraticPolynomial(1, 0, 1)`.  The new method should *return* another `QuadraticPolynomial`.

2. Write a class `LinearPolynomial`.  Add a method `differentiate` to `QuadraticPolynomial` that returns a `LinearPolynomial`.

3. Suppose we create a new `QuadraticPolynomial` like `QuadraticPolynomial(1, 1, 0)`.  Is this really a `QuadraticPolynomial`?  What should it be?  How can you resolve this weird inconsistency in data types?


```python
class QuadraticPolynomial(object):
    """A class representing a polynomial like:
    
        a_0 + a_1 x + a_2 x^2
    """
    
    def __init__(self, a0, a1, a2):
        self.coefficients = (a0, a1, a2)
        
    def evaluate(self, x):
        a0, a1, a2 = self.coefficients
        return a2 * x * x + a1 * x + a0
    
    def __repr__(self):
        return "QuadraticPolynomial({}, {}, {})".format(
            self.coefficients[0],
            self.coefficients[1],
            self.coefficients[2])
    
    def __str__(self):
        return "{}x^2 + {}x + {}".format(
            self.coefficients[2],
            self.coefficients[1],
            self.coefficients[0])
    
    def _apply_operation_to_coefficients(self, other, operation):
        a0 = operation(self.coefficients[0], other.coefficients[0])
        a1 = operation(self.coefficients[1], other.coefficients[1])
        a2 = operation(self.coefficients[2], other.coefficients[2])
        return QuadraticPolynomial(a0, a1, a2)
    
    def __add__(self, other):
        return self._apply_operation_to_coefficients(other, lambda x, y: x + y)
    
    def __sub__(self, other):
        return self._apply_operation_to_coefficients(other, lambda x, y: x - y)
    
    def differentiate(self):
        a0, a1, a2 = self.coefficients
        return LinearPolynomial(a1, 2 * a2)
```

```python
class LinearPolynomial(object):
    
    def __init__(self, a0, a1):
        self.coefficients = (a0, a1)
    
    def __str__(self):
        return "{}x + {}".format(self.coefficients[1], self.coefficients[0])
```

```python
def polynomial_factory(coefficients):
    if coefficients[2] == 0:
        return LinearPolynomial(coefficients[0],
                                coefficients[1])
    else:
        return QuadraticPolynomial(coefficients[0],
                                   coefficients[1],
                                   coefficients[2])
```

## Challange Exercise

Implement a general `Polynomial` class, that can handle any degree polynomial.

  - What extra data will you need to store on each instance?
  - Do we need any new methods to handle this case?
  - What happens if we try to add a `Polynomial` object to another type of object, say an integer?  Should this work?  If not, how can we make it work properly?
