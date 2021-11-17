from random import randrange


class MultiMap:
    """ A multimap class built upon use of an underlying map for storage """

    _MapType = dict()                                   # Map type can be redefined by subclass

    def __init__(self):
        """ Create a new empty multimap instance """
        self._map = self._MapType                       # create map instace for storage
        self._n = 0
    
    def __len__(self):
        """ Return the number of items in the multimap """
        return self._n

    def num_secondaries(self):
        """ Return the number of secondary map in the multimap """
        return len(self._map)

    def __iter__(self):
        """ Iterate through all (k, v) pairs in multimap """
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        """ Add pair (k, v) to multimap """
        container = self._map.setdefault(k, [])         # create empty list, if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """ Remove and return arbitrary (k, v) with key k (or raise KeyError) """
        secondary = self._map[k]                        # may raise KeyError
        rand_index = randrange(len(secondary))          
        v = secondary.pop(rand_index)
        if len(secondary) == 0:
            del self._map[k]                            # no pairs left
        self._n -= 1
        return (k, v)

    def find(self, k):
        """ Return arbitrary (k, v) pair with given key (or raise KeyError) """
        secondary = self._map[k]
        rand_index = randrange(len(secondary))
        return (k, secondary[rand_index])

    def find_all(self, k):
        """ Generate iteration of all (k, v) pairs with given key """
        secondary = self._map.get(k, [])                # empty list by default
        for v in secondary:
            yield (k, v)

M = MultiMap()

M.add('Fruit', 'Apple')
M.add('Fruit', 'Mango')
M.add('Fruit', 'Banana')
M.add('Fruit', 'Strawberry')
M.add('Fruit', 'Potato')
M.add('Car', 'BMW')
M.add('Car', 'Tesla')
M.add('Car', 'Mercedes-Benz')
M.add('Book', 'Mathemmatic')
M.add('Book', 'Advanced Physic')
M.add('Activity', 'Running')
M.add('Activity', 'Swimming')
M.add('Activity', 'Playing Volleyball')
M.add('Activity', 'Coding')
M.add('Activity', 'Studying')

print(len(M))
print(M.num_secondaries())

print(M.find('Car'))
print(M.find('Fruit'))
print(M.find('Book'))
print(M.find('Activity'))

M.pop('Fruit')

for act in M.find_all('Fruit'):
    print(act)