from MapBase import MapBase

class SortedTableMap(MapBase):
    """ Map implementation using a sorted table """

    # nonpublic behaviors
    def _find_index(self, k, low, high):
        """ Return idx of the leftmost item with key greater than or equal to k.
        Return high + 1 if no such item qualifies.
        That is, idx will be returned such that:
           all items of slice table[low:idx] have key < k
           all items of slice table[idx:high+1] have key >= k
        """
        if high < low:
            return high + 1         # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                # note: may return mid
                return self._find_index(k, low, mid - 1)
            else:
                # answer is right for mid
                return self._find_index(k, mid + 1, high)   

    # public behaviors
    def __init__(self):
        """ Create an empty map """
        self._table = []

    def __len__(self):
        """ Return number of items in the map """
        return len(self._table)

    def __getitem__(self, k):
        """ Return value associated with key k (raise KeyError if not found) """
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx == len(self._table) or self._table[idx]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[idx]._value

    def __setitem__(self, k, v):
        """ Assign value v to key k, overwritting existing value if present """
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx < len(self._table) and self._table[idx]._key == k:
            self._table[idx]._value = v                       # reassign value
        else:
            self._table.insert(idx, self._Item(k, v))         # add new item

    def __delitem__(self, k):
        """ Remove item associated with key k (raise KeyError if not found) """
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx == len(self._table) and self._table[idx]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(idx)                                  # del item

    def __iter__(self):
        """ Generate keys of the map ordered from minimum to maximum """
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """ Generate keys of the map ordered from maximum to minimum """
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """ Return (key, value) pair with minimum key (or None if empty) """
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """ Return (key, value) pair with maximum key (or None if empty) """
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """ Return (key, value) pair with least key greater than or equal to k """
        idx = self._find_index(k, 0, len(self._table) - 1)  # idx's key >= k
        if idx < len(self._table):
            return (self._table[idx]._key, self._table[idx]._value)
        else:
            return None

    def find_lt(self, k):
        """ Return (key, value) pair with greatest key strictly less than k """
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx > 0:
            # note use of idx - 1
            return (self._table[idx - 1]._key, self._table[idx - 1]._value)
        else:
            return None

    def find_gt(self, k):
        """ Return (key, value) pair with least key strictly greater than k """
        idx = self._find_index(k, 0, len(self._table) - 1)
        if idx < len(self._table) and self._table[idx]._key == k:
            idx += 1
        if idx < len(self._table):
            return (self._table[idx]._key, self._table[idx]._value)
        else:
            return None

    def find_range(self, start, stop):
        """ Iterate all (key, value) pairs such that start <= key < stop.
        If start is None, iteration begin with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            idx = 0
        else:
            # find first result
            idx = self._find_index(start, 0, len(self._table) - 1)
        while idx < len(self._table) and (
            stop is None or self._table[idx]._key < stop):
            yield (self._table[idx]._key, self._table[idx]._value)
            idx += 1


events = {
    570: 'Birth of Prophet Mohammed',
    622: 'Emigration of Mohammed to Madina, Beginning of Hijri era',
    632: 'Death of Prophet Mohammed',
    1349: 'Black Death, most devastating pandemic in Europe killed over 100 million people',
    1215: 'Magna Carta, first document limiting the powers of King of England was signed',
    1588: 'Defeat of Spanish Armada also know as Invincible Fleet by England',
    1492: 'Christopher Columbus discover the New World',
    1339: '100 years war between England and France',
    1498: 'Vasco da Gama discovers the sea route from Europe to India',
    1665: 'Great Plague of London which killed about 1 million people in the city',
    1666: 'Great fire of London with destroyed about 70000 homes in the city',
    1815: 'Battle of Waterloo in which Napoleon was defeated',
    1859: 'On the Origin of Species by Charles Darwin published',
    1896: 'First modern Olympic Games held at Athens',
    1912: 'Republic of China is established, Titanic sinks',
    1911: 'Roald Amundsen reached the South Pole',
    1914: '1st World War',
    1939: '2nd World War',
    1957: 'Launch of Sputnik 1, marking the beginning of space age',
    1945: 'Dropping of Atom Bombs on Hiroshima and Nagasaki',
    1969: 'Landing of Apollo 11 with Neil Armstrong on the surface of the moon',
    1986: 'Chernobyl disaster',
    1990: 'World Wide Web invented, Reunification of Germany',
    1991: 'Dissolution of USSR',
    2001: '9/11 attack on World Trade Center'
}

MapOfEvents = SortedTableMap()

for year, event in events.items():
    MapOfEvents[year] = event

print('Year of events: ')
for year in MapOfEvents:
    print(year, end=' ')

print('\nYear of events (reversed): ')
for key in reversed(MapOfEvents):
    print(key, end=' ')

print('\nNumber of events: ', len(MapOfEvents))
print('Event occurred in 1945 or immediately later: ', MapOfEvents.find_ge(1945))
print('Event occurred immediately after 1910: ', MapOfEvents.find_gt(1910))
print('Event occurred immediately before 1897', MapOfEvents.find_lt(1897))
print('Event occurred earliest: ', MapOfEvents.find_min())
print('Event occurred latest: ', MapOfEvents.find_max())

print('Events occurred in years between 500 and 1900: ')
for event in MapOfEvents.find_range(500, 1900):
    print(event)

