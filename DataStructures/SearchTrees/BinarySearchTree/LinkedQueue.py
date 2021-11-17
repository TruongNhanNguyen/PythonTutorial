class Empty(Exception):
    """ Error attemping to access element from the empty stack """
    pass


class LinkedQueue():
    """ FIFO queue implementation using a singly linked list for storage """

    class _Node:
        """ Lightweight and nonpublic class for storing a singly linked node """
        __slot__ = '_element', '_next'                          # streamline memory usage

        def __init__(self, element, next):
            """ Initialize node's fields """                    
            self._element = element                             # reference to user element
            self._next = next                                   # reference to next node

    def __init__(self):
        """ Create an empty queue """
        self._head = None                                       # reference to head node
        self._tail = None                                       # reference to tail node
        self._size = 0                                          # number of queue's element

    def __len__(self):
        """ Return the number of queue elements """
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty """
        return self._size == 0

    def first(self):
        """ Return (but not remove) the element at the front of the queue """
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._head._element                              # front aligned with head of list

    def enqueue(self, e):
        """ Add an element at the back of the queue """
        newest = self._Node(e, None)                            # node will be tail node
        if self.is_empty():                                     
            self._head = newest                                 # special case: previously empty
        else:
            self._tail._next = newest                           # set new node as tail node
        self._tail = newest                                     # update reference to tail node
        self._size += 1

    def dequeue(self):
        """ Return and remove the element at the front of the queue (i.e, FIFO) 
            Raise Empty error if the queue is empty """
        if self.is_empty():
            raise Empty('Queue is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                                     # special case as queue is empty
            self._tail = None                                   # removed head had been the tail
        return answer
    
    def __iter__(self):
        """ Generate a backward iteration of the elements of the queue according principle of queue FIFO """
        cursor = self._head                             # begin traversal at the head of the list
        while cursor is not None:                       # stop at the tail
            yield cursor._element                       # generate node's element
            cursor = cursor._next