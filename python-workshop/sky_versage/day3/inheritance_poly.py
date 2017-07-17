class Animal(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sleep(self):
        print('zZZzzZZ')

    def make_noise(self):
        raise NotImplementedError


class Dog(Animal):

    def __init__(self, name, color, breed):
        Animal.__init__(self, name, color)
        self.breed = breed

    def make_noise(self):
        print('woof')

    def wag_tale(self):
        print('wag wag')

class Cat(Animal):

    def __init__(self, name, color, vertical_leap):
        Animal.__init__(self, name, color)
        self.vertical_leap = vertical_leap

    def jump(self):
        return '{} jumped {} inches into the air'.format(self.name,
                                                  self.vertical_leap)



if __name__ == '__main__':
    ralph = Dog(name='ralph',
                color='red',
                breed='lab')

    garfield = Cat(name='Garf',
                   color='Orange',
                   vertical_leap=4)

    #Notice what happens when you call garfield.make_noise
