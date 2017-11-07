class OrderedDict(object):

    def __init__(self, dictionary=None):
        if dictionary:
            self.data = dictionary
        else:
            self.data = {}
        self.order = self.data.keys()

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            self.data[key] = self.default()
            return self.data[key]
    
    def __setitem__(self, key, value):
        if key not in self.order:
            self.order.append(key)
        self.data[key] = value

    def __delitem__(self, key):
        """This defines the del keyword as in `del x['a']`"""
        try:
            idx = self.order.index(key)
            _ = self.order.pop(idx)
            del self.data[key]
        # The key is not yet in the data.
        except ValueError, KeyError:
            raise KeyError(key)
            
    def __len__(self):
        return len(self.data)
        
    def __contains__(self, key):
        return key in self.data
    
    def __iter__(self):
        for key in self.order:
            yield key

    def itervalues(self):
        for key in self.order:
            yield self.data[key]

    def iteritems(self):
        for key in self.order:
            yield key, self.data[key]
