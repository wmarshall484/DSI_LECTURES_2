
class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def make_sound(self):
        pass


class Dog(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def make_sound(self):
        print self.name, "says: RUFF RUFF!"

    def roll_over(self):
        print self.name, "is rolling over..."


class Cat(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def make_sound(self):
        print self.name, "says: MEOW!"
