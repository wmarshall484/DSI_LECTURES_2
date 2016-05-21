'''
The scenario: Donald Trump becomes president and make the python built-in
              'set' class illegal. What do we do?
'''


class myset:
    '''
    This is a custom set class to rival python's built-in set class.
    '''

    def __init__(self, iterable=None):
        '''
        Create a list initialized with the items in the given iterable.
        '''
        self.p = 113
        self.hash_table = [[] for i in xrange(self.p)]
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        '''
        Add the given item to the set (if it is not already in the set).
        '''
        h = (hash(item) % self.p)
        if item not in self.hash_table[h]:
            self.hash_table[h].append(item)

    def discard(self, item):
        '''
        Remove the given item from the set (if it is in the set).
        '''
        h = (hash(item) % self.p)
        self.hash_table[h].remove(item)

    def to_list(self):
        '''
        Return a list of all the items in this set.
        '''
        return [item for lst in self.hash_table for item in lst]

    def __contains__(self, item):
        '''
        Return True if the given item is in this set, and False otherwise.
        '''
        h = (hash(item) % self.p)
        return (item in self.hash_table[h])

    def __iter__(self):
        '''
        Return an object that has a next() method so that the values
        of this set can be iterated over in a 'for' loop.

        This magic method is called implicitly by the python interpreter
        at the beginning of for loops that want to iterate over this list.

        See: http://stackoverflow.com/questions/19151/how-to-make-class-iterable
        '''
        return self.to_list().__iter__()

    def __or__(self, other):
        '''
        Return the union of the two myset objects.

        This magic method is called when you use the bitwise or
        operator (|) on two myset objects.
        '''
        union = myset()
        for item in self:
            union.add(item)
        for item in other:
            union.add(item)
        return union

    def __and__(self, other):
        '''
        Return the intersection of the two myset objects.

        This magic method is called when you use the bitwise and
        operator (&) on two myset objects.
        '''
        intersection = myset()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __repr__(self):
        '''
        Return a string representation of this set.
        '''
        return '{' + ', '.join(repr(item) for item in self.to_list()) + '}'

