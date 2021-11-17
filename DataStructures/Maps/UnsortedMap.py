from MapBase import MapBase

class UnsortedTableMap(MapBase):
    """ Map implementation using an unordered list """

    def __init__(self):
        """ Create an empty map """
        self._table = []                            # list of _Item's

    def __getitem__(self, k):
        """ Return value associated with key k (raise KeyError if not found) """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """ Assign value v to key k, overwriting existing value if present """
        for item in self._table:
            if k == item._key:                      # found a match
                item._value = v                     # reassign value
                return                              # and quit
        self._table.append(self._Item(k, v))        # did not find match for key

    def __delitem__(self, k):
        """ Remove item associated with key k (raise KeyError if not found) """
        for j in range(len(self._table)):
            if k == self._table[j]._key:            # found a match 
                self._table.pop(j)                  # remove item
                return                              # and quit
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """ Return number of items in the map """
        return len(self._table)

    def __iter__(self):
        """ Generate iteration of the map's item's key """
        for item in self._table:
            yield item._key


# M = UnsortedTableMap()
# M['VietNam'] = 'HaNoi'
# M['France'] = 'Paris'
# M['USA'] = 'Washington'
# M['China'] = 'Beijing'
# M['Korea'] = 'Seoul'
# M['Singapore'] = 'Singapore'
# M['Cuba'] = 'La Habana'
# M['Canada'] = 'Ottawa'
# M['Brasil'] = 'Brasilia'
# M['Australia'] = 'Canberra'

# print(len(M))
# print(M['France'])
# for country in M:
#     print(country)

