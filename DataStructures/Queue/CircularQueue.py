class Empty(Exception):
    """ Error attemping to access element from the empty stack """
    pass


class CircularQueue():
    """ Queue implementation using circular linked list for storage """

    class _Node:
        """ Lightweight and nonpublic class for storing a singly linked node """
        __slot__ = '_element', '_next'          # streamline memory usage

        def __init__(self, element, next):
            """ Initialize node's fields """
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    def __init__(self):
        """ Create an empty queue """
        self._tail = None                       # represent tail of the queue
        self._size = 0                          # number of queue elements

    def __len__(self):
        """ Return number of the elements of the queue """
        return self._size

    def is_empty(self):
        """ Check if the queue is empty """
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front of the queue
            Raise Empty error if the queue is empty """
        if self.is_empty():
            raise Empty('Queue is empty!')
        head = self._tail._next                 # the head being after the tail
        return head._element

    def enqueue(self, e):
        """ Add an element to the back of the queue """
        newest = self._Node(e, None)            # node will be the tail node
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node point to head
            self._tail._next = newest           # old tail point to new node
        self._tail = newest                     # new node now become the tail
        self._size += 1

    def dequeue(self):
        """ Remove and return the element at the front of the queue
            Raise Empty error if the queue is empty """
        if self.is_empty():
            raise Empty('Queue is empty!')
        old_head = self._tail._next
        if self._size == 1:                            # remove only element
            self._tail = None                          # queue becomes empty 
        else:
            self._tail._next = old_head._next          # bypass the old head
        self._size -= 1
        return old_head._element

    def rotate(self):
        """ Rotate front element to the back of the queue """
        if self._size > 0:
            self._tail = self._tail._next       # old head become new tail


q = CircularQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.enqueue(50)
q.rotate()
print(q.first())
