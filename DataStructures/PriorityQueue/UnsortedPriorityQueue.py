from PositionalList import PositionalList, Empty
from PriorityQueueBase import PriorityQueueBase

class UnsortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with an unsorted list """
    
    # constructor
    def __init__(self):
        """ Create a new empty Priority Queue """
        self._data = PositionalList()

    # nonpublic utility
    def _find_min(self):
        """ Return Position of item with minimum key """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __len__(self):
        """ Return the number of items in the priority queue """
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair """
        self._data.add_last(self._Item(key, value))

    def min(self):
        """ Return but not remove (k, v) tuple with minimum key """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k, v) tuple with minimum key """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
    

P = UnsortedPriorityQueue()
P.add(5, 'A')
P.add(9, 'C')
P.add(3, 'B')
P.add(7, 'D')
print(P.min())
P.remove_min()
P.remove_min()
print(len(P))
P.remove_min()
P.remove_min()
print(P.is_empty())
P.remove_min()
