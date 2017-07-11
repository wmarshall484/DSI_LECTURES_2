class Animal(object):
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        raise NotImplementedError

    def drink_water(self):
        print('Gulp, gulp, gulp')


class Dog(Animal):
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed

    def make_noise(self):
        print('Ruff!')



if __name__ == '__main__':
    WALDO = Dog('Waldo', 'Big Red Dog')
    WALDO.make_noise()
    WALDO.drink_water()
