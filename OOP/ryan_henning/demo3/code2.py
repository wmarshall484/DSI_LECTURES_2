
class Fruit(object):

    def __init__(self, weight):
        self.weight = weight

    def grow(self):
        print "Fruit is grown!"

    def eat(self):
        print "Fruit is eaten!"


class Banana(Fruit):

    def __init__(self, weight):
        super(Banana, self).__init__(weight)

    def peel(self, percentage):
        print "Banana is peeled", percentage, "%"


class Orange(Fruit):

    def __init__(self, weight):
        super(Orange, self).__init__(weight)

    def peel(self):
        print "Orange is peeled fully."


class Apple(Fruit):

    def __init__(self, weight):
        super(Apple, self).__init__(weight)

    def wash(self):
        print "Apple is washed."



if __name__ == '__main__':

    print "Banana:"
    banana = Banana(4.3)
    banana.grow()
    banana.eat()
    print

    print "Orange:"
    orange = Orange(7.4)
    orange.grow()
    orange.eat()
    print

    print "Apple:"
    apple = Apple(6.5)
    apple.grow()
    apple.eat()
    print
