import matplotlib.pyplot as plt
import numpy as np


class Fruit(object):

    def __init__(self, weight):
        self.weight = weight

    def grow():
        print "I'm growing!"

    def set_weight(self, weight):
        self.weight = weight

    def calculate_price(self):
        return 2.5 * self.weight


class Banana(Fruit):

    def __init__(self, weight=0):
        super(Banana, self).__init__(weight)

    def peel(self):
        print "I'm peeling!"

    def calculate_price(self):
        return 0.85 * self.weight


class Orange(Fruit):

    def __init__(self, weight=0):
        super(Orange, self).__init__(weight)

    def peel(self):
        print "I'm peeling!"


class Apple(Fruit):

    def __init__(self, weight=0, color=(255, 0, 0)):
        super(Apple, self).__init__(weight)
        self.color = color

    def calculate_price(self):
        return 0.4 * self.weight ** 2



def plot_fruit_prices(fruit, weight_min, weight_max):
    range_ = np.linspace(weight_min, weight_max, 100)
    price = []
    for weight in range_:
        fruit.set_weight(weight)
        price.append(fruit.calculate_price())
    plt.plot(range_, price)



banana = Banana()
orange = Orange()
apple  = Apple()

plot_fruit_prices(banana, 0, 20)
plot_fruit_prices(orange, 0, 20)
plot_fruit_prices(apple,  0, 20)

plt.show()

