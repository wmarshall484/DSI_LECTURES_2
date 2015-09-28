# Object Oriented Programming in Python

In programming, there are typically two dominant paradigms to structure code: Functional and Object Oriented.  Functional programming eschews mutable state, i.e. variables, and passes information/logic through the input and output of functions. OO programming on the other hand embraces state (i.e. remembering) in the form of variables and objects.  For example, if I wanted to write a program that calculates some mathematical results, I might pass intermediate values from one function to the next through an internal variable.  

Often a language chooses to focus on one, [Java](http://docs.oracle.com/javase/tutorial/java/concepts/) is almost purely OO (although that is changing with recent versions) in that you cannot even write a function outside of a class.  Others are purely functional in that you are prevented from creating variables.  Many language leverage the strengths of both of these paradigms, Python included.

In Python, we have a bunch of built-in classes that we use every day. For example, Lists, Strings and Dictionaries are examples. We can create an instance of them and then use methods to operate on them.

We can create a new list or dictionary with what we call a *constructor*:

```python
d = dict()

L = list()

# a more pythonic way of initializing an empty list:
L = []
```

We have methods that allow us to do things with and to the list. A *method* is a function which acts on a class. `append`, `pop` and `extend` are examples of *methods*.

```python
In [1]: L = []

In [2]: L.append('a')

In [3]: L.pop()
Out[3]: 'a'

In [4]: L.extend(['x', 'y', 'z'])

In [5]: L.pop(1)
Out[5]: 'y'
```

The built-in types are very generic and have many uses. However, sometimes we would like to define our own types that fit our specific scenario.

## Primer on Classes

Think of a class as a blueprint.  It is a scaffold for an house we would like to build.  And since we might want to create many houses that all are very similar (though might have a few properties that differ such as color, siding, porch, etc.) we want to remember how to easily build more houses.  The class is this blueprint and an object instantiation is an individual physical house.

## Data and Computation (Nouns and Verbs)

### Object Oriented

In OO programming, Objects are the 'first class citizen' which encapsulate both data (state) and computation.  These are separated as variables and methods.  Programs are simply a collection of objects that pass state around through 'messages' (i.e. method calls).  Methods are functions that operate on state (data) to mutate an object.  Let us unpack that a bit.

![messages](http://2.bp.blogspot.com/-N2sHRubepUE/T3rFv_IjeYI/AAAAAAAAABc/qyetT9SvixU/s1600/OOP000%5B1%5D.jpg)

In plain English... when you call a method on an object, you send a message to it through its arguments (or lack thereof) to update its internal state (variables).  `mean()` in the code above tells the `Variance` object to update its internal state: `self.total_length` and `self.mean`.

## Card Games as an OOP problem

The example we will be looking at today is creating card games. In this scenario, it's very helpful to have classes to represent a playing card and a deck of cards.

Here is the syntax for creating a card class:

```python
class Card(object):
    def __init__(self, number, suit):
        self.suit = suit
        self.number = number
```

Here the `suit` and `number` are what we call *instance variables*. That means that they are variables that are specific to each *instance* of the class (each card that you create will have its own values for suit and number).

The `__init__` function is the *constructor*. It is called when you run the following code:

```python
card = Card('5', 'C')
```

Look at the deck class for an example where we also create *methods*.

```python
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        for num in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            for suit in 'cdhs':
                self.cards.append(Card(num, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.isempty():
            return self.cards.pop()

    def add_cards(self, cards):
        self.cards.extend(cards)

    def isempty(self):
        return self.cards == []
```

Now we can use our `Deck` class:

```python
In [1]: deck = Deck()

In [2]: deck.draw_card()
Out[2]: AS

In [3]: deck.draw_card()
Out[3]: AH

In [4]: deck.shuffle()

In [5]: deck.draw_card()
Out[5]: QC

In [6]: deck.isempty()
Out[6]: False
```

(Note that with this implementation, the cards go in order until you shuffle the deck.)


## Magic methods

In python, there are what we call *magic methods*.

#### Length function

Notice how you can use the `len` function on most built-in types to get the length (length of a list, number of items in a dictionary, length of a string). If you'd like to be able to do the same with your own class, you can implement the `__len__` method.

You can add the following to the `Deck` class:

```python
    def __len__(self):
        return len(self.cards)
```

This enables you to use `len(deck)` and it will give you the number of cards in your deck.

#### Comparisons

You also may want to be able to compare two cards to see which is larger or if they have the same value. You can get this functionality by implementing the '__cmp__' function. 

Here is an implementation of this function for the `Card` class:

```python
   def __cmp__(self, other):
       return cmp(self.value_dict[self.number], self.value_dict[other.number])
```

You can now run the following code:

```python
In [1]: card1 = Card('5', 'c')
In [2]: card2 = Card('7', 'd')
In [3]: card3 = Card('7', 'h')

In [4]: card1 > card2
Out[4]: False

In [5]: card2 == card3
Out[5]: True
```

#### String representation

If you try to print your object, you will get something like this:

```python
In [1]: card = Card('A', 'd')

In [2]: print card
<Card object at 0x10a2ce210>
```

If you would like to be able to print out your object in a human-readable form, you need to create the `__repr__` method which will give the string representation. Here is an example repr method for the `Card` class:

```python
    def __repr__(self):
        return "%s%s" % (self.number, self.suit)
```

Now, this will happen when you try to print the card:

```python
In [1]: card = Card('A', 'd')

In [2]: print card
Ad
```

You can of course modify the output however you'd like, putting a space or symbol between the number and suit:

```python
        return "|%s|%s|" % (self.number, self.suit)
```

This gives an output like this: `|A|d|`.

***For a full list of magic methods, take a look at [this blog post](http://www.rafekettler.com/magicmethods.html).***

#### Card and Deck implementations

You can find the code for the `Card` and `Deck` classes in [deck.py](code/deck.py).


## How to structure your classes

The hardest part of Object Oriented Programming is figuring out how to structure your classes and what methods you need.

The general rules of thumb are:

* nouns should become classes
* verbs should become methods

## Example: War Card Game

We'll demonstrate how to do this by implementing the children's card game [war](http://en.wikipedia.org/wiki/War_(card_game)).

If you're unfamiliar with the game, read the link or just play the game by running: `python war.py`

It is a complete game of chance, so you will never have to make a decision.

### Classes

We've already created classes for a card and a deck.

The other classes we will need are:

* player
* game

#### The player class

Let's look at the player class. First, what *instance variables* does it need? What does a player need to keep track of?

* `hand`: a list of cards in the player's current deck
* `discard`: a list of cards in the player's discard pile
* `name`: the player's name (not essential)

And what *methods* does the player class need?

* `receive_card`
* `play_card`

The player class is implemented in [war_player.py](code/war_player.py). There are a couple other instance variables and methods there that turned out to be useful that aren't as essential as the ones noted above.

#### The game class

These are the important instance variables:

* `player1` and `player2` (two instances of the `Player` class)
* `pot`: the cards that are currently in play (they will be won by one of the two players at the end of the round)
* `winner`: the player that has won, which will be `None` until the end of the game (this is not the only way to keep track of this information)


These are the important methods:

* `deal`: gives each player their starting decks
* `play_round`: goes through one round of the game (each player plays a card, highest card wins. If they tie, each player plays 3 cards and then they try again.)
* `play_game`: starts the game and calls `play_round` repeatedly until one player gets all the cards and is declared the winner.

When you look at the code in [war.py](code/war.py), you'll notice there are a bunch of other functions. One thing you'll notice is that all of the displaying of the game was separated into separate methods (`display_play`, `display_receive`, `display_war` and `display_winner`). It's nice to separate out the display functions in case later you want to create a fancy UI. Then you don't have to modify any of the game functionality, just the display.

You'll also notice that a few helper methods like `draw_card`, `draw_cards`, `war` and `give_cards` were created to simplify the code for the `play_round` method.


## Testing!

We will be using `nose` to test our code. The syntax is very simple. Basically, you need to write a function for each test you want to run. The challenge is to determine what the necessary tests are.

When writing tests, you want to think about all the edge cases and make sure your code won't break. For example, for the `Card` and `Deck` classes, you want to test the following things:

* Initializing a card sets the number and suit correctly
* You get the correct string representation of a card
* Comparisons work correctly (<, >, ==)
* The deck is initialized correctly (has 52 unique cards)
* Drawing a card works (you get a card and now the deck has one less card)

You can use tests to make sure that you are implementing your code correctly and also to make sure that when you implement additional features you don't break anything.

You can find test examples in [test_deck.py](code/test_deck.py) and [test_war.py](code/test_war.py).

# Scope

Scope can be thought of as the lifetime of a reference (i.e. variables, objects, and methods).  Python scope can take some getting used to but here is a quick cheatsheet on what the rules are for looking up a value.  Python uses lexical scoping and binds scope on declaration of a variable/reference (rather than on function execution).  The difference between lexical (static) and dynamic scope is beyond the scope of this course, but the wikipedia page has a concise [explanation][1].

```bash
x=1
function g () { echo $x ; x=2 ; }
function f () { local x=3 ; g ; }
f # does this print 1, or 3?
echo $x # does this print 1, or 2?
```

### Rules

__LEGB Rule__

![scope][2]

__L: Local.__ (Names assigned in any way within a function (def or lambda)), and not declared global in that function.

__E: Enclosing function locals.__ (Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

__G: Global (module).__ Names assigned at the top-level of a module file, or declared global in a def within the file.

__B: Built-in (Python).__ Names preassigned in the built-in names module : open,range,SyntaxError,...

Python uses lexical scoping and a variable is __bound__ when it is defined (or assigned to).  When in doubt always jump into a debugger (`ipdb.set_trace()`) at the point of you program in which you are uncertain and inspect the variables.  In Python, the `locals()` method tells you exactly what is in the local scope, and the globals() tells you everything that is in the global scope.

```python
def foo(arg): 
    x = 1
    print locals()

foo(7)
#=> {'arg': 7, 'x': 1}

foo('bar')
#=> {'arg': 'bar', 'x': 1}
```

### Creating Scope

In Python, you can create new scope by defining a function (`def ... or lambda`) or creating a class.  Think of each of these as adding layers to a wonderful scope onion (or maybe Russian dolls are a better analogy).

![matroyska dolls][4]

You can never look down scope but can most always look up (unless you shadow a variable).  For example:

```python
x = "global"

def new_scope(x):
    print x
    y = "I'm just hiding"
    x = "shadow variable"
    return x

print x #=> "global"
new_scope("argument") #=> "argument"

print x #=> "global"

print new_scope("argument") 
    #=> "argument"
    #=> "shadow variable"

print y #=> NameError: name 'y' is not defined
```

### How do I get into the Scope club (with a velvet rope)

#### Pass-by-reference vs. pass-by-value

Most languages are either pass by reference or pass by value.  The difference being in pass-by-reference the argument can be mutated and it effects that variable up scope, whereas in pass-by-value creates a 'copy'.  Unfortunately Python is a mixture of these in something called 'pass-by-object-reference'.  Or rather:

>Object references are passed by value

But that may not make more sense. If you ever have a question, it is often best to try it out in a python interpreter:

```python

x = "global"

def do_nothing(ll):
    print x
    return ll

def return_list(ll):
    ll = ["assign", "a", "list"]
    return ll

def mutate_list(ll):
    ll.append("Messin with my list")
    return ll

new_list = ['foo', 'bar']

print do_nothing(new_list) #=> "global" 
                           #=> ['foo', 'bar']
print return_list(new_list) #=> ["assign", "a", "list"]
print mutate_list(new_list) #=> ['foo', 'bar', "Messin with my list"]
```

I just showed you how to get into the scope club, to get out you can either mutate a object passed in, or the safest option is to return variables.

This is a common source of confusion for people new to Python but the worst offender of breaking some of these conventions is `pandas`.  You should always read the docs of a new library to understand its own semantics and nuances.

__[More info][3]__

### What is that `self` thing you keep using

```python
# from above...
class Animal(object):
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion

    def speak(self):
        print "My name is " + self.name

    # self is replaced by the object
    # the method is called on
    def eat(self, food):
        print "I " + self.emotion + " " + food

frank = Animal("Frank", "adore")
frank.speak() #=> "My name is Frank"

# object is passed as first argument to a method call
frank.eat("bananas") #-> Animal.eat(frank, "bananas")
    #=> "I adore bananas"
```

The object a method is called on is always passed as the first argument (`self`).  In this case, the object `frank` of the class `Animal` is passed as the first argument to the method call `eat(...)`.  This ensures that we always explicitly have access to the object the method belongs to.  When we create a new object instantiation of the class `Animal`, we bind the variable `self` to the object created.  In this case, the call to `Animal("Frank")` binds the variable `self` to the returned object.  This instantialion also runs the code in the class's `__init__()` method implicitly.  `__init()__` is just a function though and we can (though it is very bad practice to) call it once a object has been created.

```python
class Person(object):
    def __init__(self, name):
        self.name = name
        print "I am alive"

jon = Person("Jon") #=> I am alive

jon #=> <__main__.Person instance at 0x105addc20>

jon.name #=> 'Jon'

jon.__init__("Susie") #=> I am alive

jon.name #=> 'Susie'
```

_More info: [http://freepythontips.wordpress.com/2013/08/07/the-self-variable-in-python-explained/](http://freepythontips.wordpress.com/2013/08/07/the-self-variable-in-python-explained/)_

# Appendix

Another handy tool when learning about scope and stacks is the [stack visualization tool](http://pythontutor.com) at pythontutor.com.  Here is a great [tutorial](http://cscircles.cemc.uwaterloo.ca/11b-how-functions-work/) on visually exploring variable scope in Python as you execute a program.  Scope gets more specific as you go down, i.e. the top of the image (`Global Frame`) is the top most scope and `sum_squared_error` is the most specific.  Each box on the left represents a different scope (created when we call a function).  The nested scopes can look up/out but the outer scopes cannot look in.  For example, `sum_squared_error` can access anything defined in any scope above it (unless it is shielded by another function or class) but the global scope cannot peek into the `sum_squared_error` function and its variables.  To move data/values/variables between scope you either pass arguments and return values: __function arguments -> down/into scope :: return values -> up/out scope__

### Functional vs. OOP

In functional programming, state never changes (programs are stateless).  Functions are 'first class citizens' and can actually be passed around like variables, used as arguments to a function, etc. (think `map()`, `reduce()`, `filter()`). Functions (and a program at large) is a series of operation to perform on an immutable data source. And functions can be passed around like data!

### (Functional) Python
```python
def mean(data):
    return reduce(float.__add__, data)/len(data)

def sum_squared_error(data, mean):
    return reduce(float.__add__, [ math.pow(num - mean, 2) for num in data])/len(data)

def variance(data):
    return sum_squared_error(data, mean(data))

variance([1.,2.,3.,4.]) #=> 1.25
```

### (Object Oriented) Python
```python
class Variance(object):
    def __init__(self, input_list):
        self.data = input_list
        self.total_length = 0
        self.difference_sum = 0

    def mean(self):
        total = 0.0
        for num in self.data:
            total += num
            self.total_length += 1
        self.mean = total/self.total_length

    def sum_squared_error(self):
        for num in self.data:
            self.difference_sum += math.pow(num - self.mean, 2)
        self.variance = self.difference_sum / self.total_length

    def compute_variance(self):
        return self.variance

variance_object = Variance([1.,2.,3.,4.])
variance_object.mean()
variance_object.sum_squared_error()
variance_object.compute_variance() #=> 1.25
```

__NOTE: There is no wrong paradigm, they both have their strengths and weaknesses__

## Three principles of OO programming (or something)

I think that any rigid formalism around the 'tenets' of proper OO design is a little contrived... but people often refer to the 3 principles (read: benefits) of design:

1. Encapsulation
2. Polymorphism
3. Inheritance

_source: [https://python.g-node.org/python-summerschool-2013/_media/wiki/oop/oo_design_2013.pdf](https://python.g-node.org/python-summerschool-2013/_media/wiki/oop/oo_design_2013.pdf)_

### Encapsulation

Encapsulation allows you to create proper abstractions and abstractions are _THE_ most powerful concept of computer science.  Encapsulation is the practice of only exposing what is necessary to the outside world (i.e. code outside of your class).  Think of the methods and instance variables as the interface into the code contained within the object.  This lets the programmer dictate how their code is used and actually can force people to think differently.  One of my favorite examples of good OO design principles is within the `scikit-learn` library.  Do not worry if you do not understand any of the code here or the algorithms implemented... that is the joy of OO design and proper encapsulation.

All you have to understand is the following concepts:

> A machine learning model is an interface.  It takes data and labels.  From these data and labels it learns what patterns are associated with what labels.  This process is called fitting (or training) a model.  If you then give it data without labels, it can predict what those labels should be.  This is all we need to know and the library has properly abstracted all the messy details from us.


```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

# get data and labels
X, y = iris.data, iris.target

# create a classifier object.  
clf = KNeighborsClassifier(n_neighbors=1)

# Initialization state == number of neighbors.
# this takes some domain knowledge of the internals of
# the object.  Most libraries use sane defaults however
# 
# clf = KNeighborsClassifier()

# Train our classifier model (change internal state)
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)
```

Notice how `.fit()` did not return any value?  If this were a functional interface, data would go in and a trained model would come out.  `scikit-learn` adheres to many principles of good OO design and because of this, `.fit()` simply mutates the internal state of the classifier.  It is in this internal state (variables) that the trained model (and its parameters) resides.

### Inheritance (extensibility)

![inheritance](http://techsharer.com/wp-content/uploads/2013/11/TIJ308.png)

Inheritance is the ability of one class to override behavior of its 'parent' class to allow for customized behavior.  With inheritance, a 'child' class has all of the features and functionality (methods) of its 'parent' unless explicitly overriden.  Stepping away from our `scikit-learn` example for a second here, I will demonstrate inheritance with a much simpler example.

```python
class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print "My name is " + self.name

    def eat(self, food):
        print "I love " + food

frank = Animal("Frank")
frank.speak() #=> "My name is Frank"
frank.eat("bananas") #=> "I love bananas"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def eat(self):
        print "I like biscuits!"

fido = Dog("Fido")
fido.speak() #=> "My name is Fido"
fido.eat() #=> "I like biscuits!"
```

### Polymorphism

Related to (empowered by) inheritance, polymorphism enables us to use a shared interface for similar objects, while still allowing each object to have its own specialized behavior. It does this through inheritance of a common parent and subclassing.

> Polymorphism refers to a programming language's ability to process objects differently depending on their data type or class. More specifically, it is the ability to redefine methods for derived classes.

For `scikit-learn` this simply means that the internals of the model you are training can be drastically different (i.e. kNN vs. Decision Tree) but the methods you call for each are identical.

```python
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

# get data and labels
X, y = iris.data, iris.target

# create a kNN classifier object.  
clf = KNeighborsClassifier(n_neighbors=1)

# Train our classifier model
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)

# Decide we want to experiment with a DecisionTree
clf = tree.DecisionTreeClassifier()

# Train our classifier model
clf.fit(X, y)

# predict on new values
y_pred = clf.predict(new_data)
```
Notice that since a DecisionTree model and kNN model both have a `fit()` method defined that takes the same inputs (or many of the same), we can optimistically call `fit()` on whatever type of model the `clf` variable references.  This allows us to do some pretty powerful things with our models (i.e. GridSearch parameter optimization) which we will see later in the course.


<!-- References -->
[1]: http://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scoping_vs._dynamic_scoping
[2]: http://developer.nokia.com/community/wiki/images/b/b5/Figure2-1.png?20101129095437
[3]: http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
[4]: http://www.sciencephotography.com/xrayfish/xray%20jan24-06/Russian-doll1.jpg

<!-- Easter Eggs -->
[gotchas]: http://docs.python-guide.org/en/latest/writing/gotchas/

