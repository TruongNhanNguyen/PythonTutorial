class Empty(Exception):
    """ Error attemping to access element from the empty stack """
    pass


class LinkedQueue():
    """ FIFO queue implementation using a singly linked list for storage """

    class _Node:
        """ Lightweight and nonpublic class for storing a singly linked node """
        __slot__ = '_element', '_next'          # streamline memory usage

        def __init__(self, element, next):
            """ Initialize node's fields """                    
            self._element = element             # reference to user element
            self._next = next                   # reference to next node

    def __init__(self):
        """ Create an empty queue """
        self._head = None                       # reference to head node
        self._tail = None                       # reference to tail node
        self._size = 0                          # number of queue's element

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
        return self._head._element              # front aligned with head of list

    def enqueue(self, e):
        """ Add an element at the back of the queue """
        newest = self._Node(e, None)            # node will be tail node
        if self.is_empty():                                     
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest           # set new node as tail node
        self._tail = newest                     # update reference to tail node
        self._size += 1

    def dequeue(self):
        """ Return and remove the element at the front of the queue (i.e, FIFO) 
            Raise Empty error if the queue is empty """
        if self.is_empty():
            raise Empty('Queue is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():              # special case as queue is empty
            self._tail = None            # removed head had been the tail
        return answer
    
    def __iter__(self):
        """ Generate a backward iteration of the elements of the queue according principle of queue FIFO """
        cursor = self._head         # begin traversal at the head of the list
        while cursor is not None:   # stop at the tail
            yield cursor._element   # generate node's element
            cursor = cursor._next
    
# implementation of merge sort in linked list
def merge(S1, S2, S):
    """ Merge two sort queue instance S1, S2 into empty queue S """
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())     # move remaining elements of S1 to S
    while not S2.is_empty():
        S.enqueue(S2.dequeue())     # move remaining elements of S2 to S

def merge_sort(S):
    """ Sort the elements of queue S using the merge sort algorithm """
    if len(S) < 2:
        return                      # list is already sorted
    # divide
    S1 = LinkedQueue()                                  
    S2 = LinkedQueue()
    while len(S1) < len(S) // 2:    # move the first n // 2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())     # move the rest to S2
    # conquer (with recursion)
    merge_sort(S1)
    merge_sort(S2)
    # merge results
    merge(S1, S2, S)                # merge sorted halves back into S

def quick_sort(S):
    """ Sort the elements of queue using the quick sort algorithm """
    if len(S) < 2:
        return              # queue is already sorted
    # divide
    p = S.first()           # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty(): # divide S into L, E, G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:               # S.first() must be equal pivot
            E.enqueue(S.dequeue())
    # conquer (with recursion)
    quick_sort(L)           # sort elements less than p
    quick_sort(G)           # sort elements greater than p
    # concenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


# demo
S = LinkedQueue()
L = [11, 4, 5, 8, 2, 25, 24, 12, 19, 18, 22, 9, 3]

for item in L:
    S.enqueue(item)

# merge_sort(S)
quick_sort(S)

for item in S:
    print(item, end=' ')

