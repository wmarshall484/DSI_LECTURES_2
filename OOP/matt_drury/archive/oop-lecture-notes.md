# Python Workshop: Classes and Objects

Today we will add a very important skill to our toolbox: the ability to create our own data types.

We have already seen how useful having many data types can be:
  - Lists store ordered collections of data.
  - Dictionaries create mappings between one type of data and another.

To create our own datatypes, we will need to introduce two new primary concepts:

  - **Objects** is (are?) a word we have been using informally up to now.  An object is the most generic name for a piece of data manipulated within a computer program.  Everything we have studied so far is an object.  After today we will be able to create our own custom objects and inject them with whatever behaviour is appropriate to the problem we are solving.

  - **Classes** are object templates.  They are a sort of design document for manufacturing objects of a custom type.  They are also used to define the behaviour of a new type of object, and also serve as factories to create them.

Classes and objects are powerful, subtle tools.  It takes many years of practice to master their use.

## Outline

#### Objects

  - The primary objects: lists, sets, dictionaries, tuples, strings, numeric types
  - An example custom object: `StringStamper`
  - Creating objects
  - Looking inside an object: `dir`
  - Picking apart objects: attributes
  - Picking apart objects: methods

#### Classes and Methods

  - The `StringStamper` class.
  - The `class` keyword
  - Constructing new objects: the `__init__` method
  - `self` and self-reference
  - Methods.
  - `self` and self reference
  
## Objects

**Object** is a generic term for data inside a computer program.  This data can come in many forms, don't think of just tables or spreadsheets.  Think numbers, strings, and collections of them.

### The primary objects: lists, sets, dictionaries, tuples, strings, numeric types.

These primary objects are provided by python itself, and will serve as building blocks for all of our further exploration.  Because they are so fundamental, it is imperative that any python programmer is skilled in manipulating these objects.

  - Objects can contain other objects.

I.e., dictionaries can contain lists which in turn contain dictionaries.  You can make this as complex as you wish, but be careful, you still need to understand what you've done!

### An example custom object: `StringStamper`

We've provided a very simple custom object template (what we will call a **class** very soon) in `stringstamper.py`.  To use it in your python environment, use the `import` statement like this:

```python
$ from stringstamper import StringStamper
```

### Creating objects: The Construction Pattern

The `StringStamper` we imported serves as a template for creating new object.  Here's how you can use it to create a new object.

```python
$ ss = StringStamper("Property of Matt.")
```

Now `ss` is an object of type `StringStamper`.  We have a new **type** of object to play with.

```python
$ type(ss)
stringstamper.StringStamper
```

#### Exercise: Two Objects
Create two `StringSampler` objects containing different messages.

### Looking inside an object: `dir`

One you have an object to play with, the `dir` function will show all its contents, options, bells and whistles.

```python
$ dir(ss)
```

We will leave the weird contents that begin with double underscores as a topic for tomorrow. 

### Picking apart objects: attributes

When you called `dir` on the `ss` object hopefully you saw something like this:

```python
$ dir(ss)
[...,
 'message',
 'stamp']
```

Let's look at what `message` is all about.

```python
$ ss.message
'Property of Matt.'
```

#### Question:

Where did this come from?

It looks like what has happened is this:
  - When we *created* the `StringStamper` object, we supplied it with a message.
  - The resulting `StringStamper` object has stored the message internally.
  - We can access this stored message with a dot notation: `ss.message`.

This kind of *internal storage box* on an object is called an **attribute**.

#### Exercise: Two Objects

Look inside your two different string sampler objects.  Are the messages the same?  Are the messages stored independently?

#### Exercise: Changing an Attribute

Try to figure out how to *change the value of an attribute*, then verify that it has actually changed.

### Picking apart objects: methods

There's another attribute of the object, the `stamp` attribute.  This one is a bit special.  Instead of just storing data, it is actually a function.

```python
$ ss.stamp("The Elements of Statistical Learning.")
'The Elements of Statistical Learning. Property of Matt.'
```

### Discussion: Ok, what just happened?


### Exercise: Using `stamp`

Call the `stamp` method on different strings.  What stays the same and what changes?

### Exercise: Changing Attributes Revisited

Change the `message` attribute of your `StringStamper` object a few times, and call `stamp` before and afterwards.  What stays the same and what has changed?

### Exercise: Explore Die Roller

Import the `DiceRoller` class

```python
from diceroller import DiceRoller
```

Create some `DiceRoller`s and investigate their attributes and methods.  Call the methods on your dice roller objects.

### Methods

A function attached to an object like this is called a **method**.  Methods use the data attached to an object (its attributes) to do some computations.


## Classes

### The String Stamper Class

#### Exercise: Archaeology.
You know what the `StringStamper` class is supposed to do now.  Spend five minuets looking at the code for the `StringStamper` class.  Take notes on its curious features, and form some hypothesises about what the different parts do.
  
###  The `class` keyword

A custom data type in python is called a **class**, and you create one with the `class` keyword.

Let's summarize what we know classes can do, so we can structure our thoughts about how to get them to do it.

  - You can use a class to create a new object.
  - That new object needs to be able to store some data, so we need a way to feed data into the class.
  - Objects can have functions attached (methods), these need access to the data stored on the object.

###  Constructing new objects: the `__init__` method

Our first task is to learn how to construct new objects.  This is done using the `__init__` method.  **Every class needs to have an __init__ method!**

```python
class EveryClassYouEverWrite:

    def __init__(self, ...)  # <- They all start like this.
```

When writing the `__init__` method for a class, you need to ask yourself: **What data does this class need to store?**

#### Example: StringStamper `__init__`

The `__init__` method for `StringStamper` looks like this:

```python
def __init__(self, message):
    self.message = message
```

We needed to store a `message` attribute, so:

  - We added a `message` argument to `__init__` to get the message data into the function.
  - We used a pattern `self.thing = data` to store the data on the resulting object.

We will have more to say about what `self` is soon.  For now, just think of `self.thing = data` as a pattern that means **store `data` on the new object in attribute `thing`**


#### Exercise: Prefix and Suffix `__init__`
Create a `PrefixAndSuffix` class that is like the `StringStamper`, but stamps *both* a prefix and suffix on the string.  For now

  1. Think about what data a `PrefixAndSuffixStamper` object needs to store.
  2. Write the `__init__` method to accept and store that data.
  3. Create some objects and verify that they work as intended.

Note that you do *not* yet have to create the `stamp` method, but if you think you can figure out how to do that, go for it.

###  `self` and self-reference

Yah, so what is this `self` thing?

`self` is a keyword that refers to the **object currently being created or manipulated**.  So

```python
self.message = message
   # ^         ^
   # |         This is a piece of data we are storing.
   # This is an attribute name, it is where we are storing the data
```

**literally** means, store that data `message` on an attribute of the object being created named `message`.

It is very common to name parameters of `__init__`, and the attributes where we store the corresponding argument, by the same name.  This can be confusing at first, but you should get used to it quickly.

###  Methods.

**Methods** are functions attached to object, which are defined inside of classes.  

There is one difference between our functions from last week, and the methods of this week:  **methods have access to all of the attributes of the object they are attached to!**.

```python
def stamp(self, string):
    return string + " " + self.message
    #                     ^
    #                     The stamp method can access the message attribute!
```

#### Exercise: Prefix and Suffix

Update your `PrefixAndSuffixStamper` class to include a method `stamp` which takes a string as input, and returns the string with the prefix and suffix appended.


#### Exercise: Reverse Indexer

Don't forget that you can use any type of data as attributes for a class! In this example, you will store a list as a attribute of a class.

Write a `ReverseList` class.  When you create a `ReverseList` object, it should store a supplied list as an attribute.

Provide `ReverseList` with an `index` method, which looks up an element in the stored list in *reverse order*.  So, you should be able to use your object like this:

```python
$ rev_list = ReverseList([1, 2, 3, 4])
$ rev_list.index(0)
4
$ rev_list.index(3)
1
$ rev_list.index(1)
3
```

#### Exercise: SymmetricDict

Ok, this is our final example.  This is a class I have actually used a few times in my own day to day work.

Create a `SymmetricDict` class.  When you add a key, value pair, you should be able to use the key to lookup the value, or use the value to lookup the key!

Here's an example of what we are gong for:

```python
$ sym_dict = SymmerticDict()
$ sym_dict.add_key_value('Matt', 'Data Scientist')
$ sym_dict.add_key_value('Jack', 'Physicist')
$ sym_dict.lookup('Matt')
'Data Scientist'
$ sym_dict.lookup('Jack')
'Physicist'
$ sym_dict.lookup('Data Scientist')
'Matt'
$ sym_dict.lookup('Physicist')
'Jack'
```
