class Empty(Exception):
    """ Error attemping to access element from an empty deque """
    pass


class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation """

    class _Node:
        """ Lightweight and nonpublic class for storing a doubly linked node """

        __slot__ = '_element', '_prev', '_next'     # streamline memory usage

        def __init__(self, element, prev, next):
            """ Initialize node's fields """
            self._element = element                 # node's element
            self._prev = prev                       # previous node reference
            self._next = next                       # next node reference

    def __init__(self):
        """ Create an empty list """
        self._header = self._Node(None, None, None)     # header sentinel
        self._trailer = self._Node(None, None, None)    # trailer sentinels
        self._header._next = self._trailer              # trailer is after heder
        self._trailer._prev = self._header      # header is before trailer
        self._size = 0                          # number of list elements

    def __len__(self):
        """ Return number of list elements """
        return self._size

    def is_empty(self):
        """ Return true if the list is empty """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """ Add an element between two existing nodes and return new node """
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """ Delete nonsentinel node from the list and return its element """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1                                         
        element = node._element     # recore deleted element
        node._element = node._prev = node._next = None  # deprecated node
        return element              # return deleted element


class LinkedDeque(_DoublyLinkedBase):
    """ Doubly_ended queue implementation based on doubly linked list """
    
    def first(self):
        """ Return (but do not remove) the element at the front of the deque """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._header._next._element  # real item just after the header

    def last(self):
        """ Return (but not remove) the element at the back of the deque """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._trailer._prev._element # real item just before the header

    def insert_first(self, e):
        """ Add an element to the front of the deque """
        self._insert_between(e, self._header, self._header._next) # after header

    def insert_last(self, e):
        """ Add an element to the back of the deque """
        # before trailer
        self._insert_between(e, self._trailer._prev, self._prev)

    def delete_first(self):
        """ Remove and return the element from the front of the queue """
        if self.is_empty():
            raise Empty('Deque is empty!')
        self._delete_node(self._header._next)   # use inherited method
    
    def delete_last(self):
        """ Remove and return the element from the back of the queue """
        if self.is_empty():
            raise Empty('Deque is empty!')
        self._delete_node(self._trailer._prev)  # use inherited method
