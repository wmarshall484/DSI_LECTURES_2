from abc import ABC


class Fruit(ABC):
    def __init__(self, color, is_delicious=True):
        self.color = color
        self.delicious = is_delicious


class Apple(Fruit):
    def __init__(self, color, is_delicious=False):
        super(Apple, self).__init__(color, is_delicious=is_delicious)
        self.name = "Apple"


class Kiwi(Fruit):
    def __init__(self, color, is_delicious=True):
        super(Kiwi, self).__init__(color, is_delicious=is_delicious)
        self.name = "Kiwi"

def main():
    my_fruit = [Kiwi('brown'), Apple('green')]
    for fruit in my_fruit:
        print("A {} is delicious: {}".format(fruit.name, fruit.delicious))

if __name__ == "__main__":
    main()