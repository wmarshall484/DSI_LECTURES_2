
class Fruit(object):

    def __init__(self, weight):
        self.weight = weight

    def grow(self):
        print "I'm growing!"

    def eat(self):
        print "I'm being eaten!\n"


class Banana(Fruit):

    def __init__(self, weight):
        super(Banana, self).__init__(weight)

    def peel(self, percentage):
        print "Peeling to", percentage, "%..."


class Orange(Fruit):

    def __init__(self, weight):
        super(Orange, self).__init__(weight)

    def peel(self):
        print "Peeling..."


class Apple(Fruit):

    def __init__(self, weight):
        super(Apple, self).__init__(weight)

    def wash(self):
        print "Washing..."



if __name__ == '__main__':

    print "Banana:"
    banana = Banana(4.3)
    banana.grow()
    banana.eat()

    print "Orange:"
    orange = Orange(7.4)
    orange.grow()
    orange.eat()

    print "Apple:"
    apple = Apple(6.5)
    apple.grow()
    apple.eat()
