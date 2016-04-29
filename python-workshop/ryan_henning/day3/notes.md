These are my notes for when I lecture on day3 of the week-0 python-workshop. See the python-workshop repo as well.

These notes are messy. But cleaning them up will have to wait... :(

# Morning

## Objectives (write on board)

- OOP: Object-Oriented Programming
- Why OOP?
- OOP Terminology
- In Python:
    - define classes
    - instantiate use classes

In this lecture we will begin abstract (talking about the real-world, human concepts) then we will move toward the concrete (by writing some actual code).


## Introduction

Our world is filled with objects... we will say that every object has State
and Behavior.

Here is an object: my mug. What is its state? What is its behavior?

It is not the only mug in the world, it is just ONE of many mugs. But there is only one concept of a "mug".

So, we might say that "Mug" is a certain class. Each individual mug is just one instance of the "Mug" concept.

Mug is the class. Individual mugs are just objects.

A class is a blueprint for creating an object. You can use the one blueprint to create as many objects as you want.

Another example of a class: Library. (Write on the board) What is the state that a library must keep? What is the behavior of a library?

State is information. Behavior is algorithmic (to manipulate the state). Tip: Usually the class name and the state are nouns, and each behavior is a verb.

## OOP

So what is Object-Oriented Programming? It is a certain programming paradigm (or pattern) where we define classes in code and use those classes to create objects.

This does not give us extra power, but it does help us organize our code in a way that makes logical sense to humans. Goal is to write code that is:
- split into logical components
- easy to understand
- easy to use
- easy to modify
- easy to maintain

We are employing the concept of "encapsulation". The idea is that we will write classes that hide away the complexity of the code. Each class defines high-level behavior that manipulates hidden state.

## Built-in Python types

Now we will get more concrete. Let's write some code. First, you have already been using classes and objects in python. `list` is a class. Each list that you create is an object. When you call `append`, `extend`, `pop`, etc, those are methods.

Live-code this example:
```python
x = list()
x.append(8)
x.extend([4, 5, 6])
print x
```

Mention that list is a build-in type (no need to import it). `list` is the name of the class. `x` is one instance of the `list` class. `x` is an object.

The list is being created by calling the list constructor. `append` and `extend` are methods (i.e. behavior). Calling these methods manipulates the state of the list.

The state is hidden from us, but that is a good thing! Because we do not need to worry about it!

## Write the Library class

(All live-coding:)

Write `morning_code/main1.py` first. This will motivate how we write the `Library` class. Then implement the library class. Run `main1.py` after every method to see it work more-and-more each time.

Take a side note and talk about who floating point is weird. Motivate it with the example of 1/3 represented in base 10-floating point. Then talk about how 1/10 cannot be represented precisely in base-2 floating point. Give this example:
```python
x = 0.0
while x != 1.0:
    print "%.20f" % x
    x += 0.1
```

That floating point side note motivates the Fraction class.

Live code `morning_code/main2.py` and then implement the `Fraction` class.

## Morning Sprint

Send them out to the morning sprint. Give them a little heads-up about it first.

# Afternoon

## Objectives (write on board)

- The concept of is-a vs has-a
- Python example of inheritance (is-a)
- Python example of composition (has-a)

## Introduction

As humans, in our world, we have the concept of 'is-a' and 'has-a'.

E.g. Dog is-a Animal. Cat is-a Animal.

E.g. House has Rooms. Room has walls. Wall has doors. Doors have Knobs.
Library has Books. Library has Customers.

## OOP

We can represent the is-a relationship in our code by using inheritance.

Live-code Animal, Dog, Cat example.

We can represent the has-a relationship in our code by using composition.

Live-code Library, Book, Customer example.

## Terminology

OOP: Object-Oriented Programming

Class: A blueprint for stamping out new objects.

Object: An instance that has its own copy of its state.

State is stored in what we call: Instance variables, member variables, attributes, properties, or fields (pick your favorite name)

Behavior is written as methods.

Use inheritance to capture the is-a relationship.

Base Class -> Subclass (aka, derived class)

Use composition to capture the has-a relationship.

Polymorphism is the ability to redefine behavior in subclasses. Allows us to make each subclass behave differently (if appropriate).

## Afternoon Sprint

Give them a heads-up.

# Next-morning Review:

## Traingle test notes

use points (2, 7), (2, 2), (5, 4)

perimeter = 12.8481919626

area = 7.499999999
