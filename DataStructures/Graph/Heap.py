from PriorityQueueBase import PriorityQueueBase

class Empty(Exception):
    """ Error attemping to access an empty priority queue """
    pass


class HeapPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with a binary heap """

    # nonpublic behaviors
    def _parent(self, j):
        return (j - 1) // 2
    
    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)                  # index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """ Swap elements at indices i and j of array """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _up_heap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._up_heap(parent)                               # recur at position of parent
    
    def _down_heap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left                                  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._down_heap(small_child)                    # recur at position of small child

    # public behaviors
    def __init__(self):
        """ Create a new empty Priority Queue """
        self._data = []

    def __init__(self, contents=()):
        """ Create a new priority queue.
            By default, queue will be empty. If contents is 
            given, it should be as an iterable sequence of (k, v)
            tuples specifying the initial contents """

        self._data = [self._Item(k, v) for k, v in contents]    # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)                     # start at Parent of last leaf
        for j in range(start, -1, -1):                          # going to and including the root
            self._down_heap(j)

    def __len__(self):
        """ Return the number of items in the priority queue """
        return len(self._data)

    def add(self, key, value):
        """ Add a key value-pair to the priority queue """
        self._data.append(self._Item(key, value))
        self._up_heap(len(self._data) - 1)                      # up heap newly added position

    def min(self):
        """ Return but do not remove (k, v) tuple with minimum
            key. Raise Empty exception if empty """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k, v) tuple with minimum key. 
            Raise Empty exception if empty """
        
        if self.is_empty():
            raise Empty('Priority queue is empty')
        self._swap(0, len(self._data) - 1)                      # put minimum item at the end
        item = self._data.pop()                                 # and remove it from the list
        self._down_heap(0)                                      # then fix new root
        return (item._key, item._value)


H = HeapPriorityQueue(
    [(3, 'A'), (11, 'B'), (4, 'C'), (9, 'D'),
     (5, 'E'), (7, 'F'), (20, 'G'), (8, 'H') 
    ]
)

print('Current min: ', H.min())
print('Heap\'s size: ', len(H))
print('Remove current min: ', H.remove_min())
print('Now current min: ', H.min())
print('I will add new item: (0, \'Z\')')
H.add(0, 'Z')
print('Current min: ', H.min())
