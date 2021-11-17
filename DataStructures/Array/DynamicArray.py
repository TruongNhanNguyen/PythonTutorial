import ctypes


class DynamicArray:
    """ A dynamic array class akin to a simplified Python list """

    def __init__(self):
        """ Create an empty array """
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """ Return number of elements stored in the array """
        return self._n

    def __getitem__(self, k):
        """ Return element at index k """
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]                           # retrive from array

    def append(self, obj):
        """ Add object to the end of the array """
        if self._n == self._capacity:               # no enough room
            self._resize(2 * self._capacity)        # so double capacity
        self._A[self._n] = obj
        self._n += 1                                # increase actual number of elements

    def insert(self, k, value):
        """ Insert value at index k, shifting subsequent values rightward. """
        # For simplicity, we assume 0 <= k <= n in this version
        if self._n == self._capacity:               # not enough room
            self._resize(2 * self._capacity)        # so double capacity
        for j in range(self._n, k, -1):              # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value                          # store newest element
        self._n += 1

    def pop(self):
        """ Remove the last element of the array """
        self._A[self._n - 1] = None
        self._n -= 1

    def remove(self, value):
        """ Remove first occurrence of the value (or Raising ValueError) """
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('Value not found!')

    def _resize(self, c):                           # non public utility
        """ Resize internal array to capacity c """
        B = self._make_array(c)                     # new bigger array
        for k in range(self._n):                    # for each existing value
            B[k] = self._A[k]
        self._A = B                                 # use bigger array
        self._capacity = c

    def _make_array(self, c):                       # non public utility
        """ Return new array with capacity c """    # see ctypes documentation
        return (c * ctypes.py_object)()

    def __str__(self):                              # overide print() for dynamic array obj
        return str([self._A[k] for k in range(self.__len__())])


a = DynamicArray()
a.append(1)
a.append(2)
a.append(3)
a.append(7)
a.append('a')
a.append(10)
print(a)
a.insert(3, 4)
a.pop()
a.append(11)
a.remove(2)
print(a)
