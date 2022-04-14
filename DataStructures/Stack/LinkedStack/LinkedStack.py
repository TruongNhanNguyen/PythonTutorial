class Empty(Exception):
    """ Error attemping to access element from the empty stack """
    pass


class LinkedStack():
    """ LIFO Stack implementation using a singly linked list as underlying storage """

    #--- nested Node class ---
    class _Node():
        """ Lightweight and nonpublic class for storing a singly linked node """
        __slots__ = '_element', '_next' # streamline memory usage

        def __init__(self, element, next):
            """ initialize node's fields """
            self._element = element     # reference to user's element
            self._next = next           # reference to next node

    #--- stack's methods ---
    def __init__(self):
        """ Create an empty stack """
        self._head = None               # reference to the head node
        self._size = 0                  # number of stack elements

    def __len__(self):
        """ Return the numbers of elements in the stack """
        return self._size

    def is_empty(self):
        """ Return True if the stack is empty """
        return self._size == 0

    def push(self, e):
        """ Add element to the top of the stack """
        self._head = self._Node(e, self._head)  # create and link the new node
        self._size += 1

    def top(self):
        """ Return (but not remove) the element at the top of the stack (i.e, LIFO)
            Raise Empty error if the stack is empty """
        if self.is_empty():
            raise Empty('Stack is empty!')
        # top element is at head of list
        return self._head._element

    def pop(self):
        """ Return and remove the element at the top of the stack (i.e, LIFO)
            Raise Empty error if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list """
        cursor = self._head          # begin traversal at the head of the list
        while cursor is not None:    # stop at the tail
            yield cursor._element    # generate node's element
            cursor = cursor._next    # advance cursor to next node

s = LinkedStack()
s.push(1)
s.push(10)
s.push(12)
s.push(14)
s.push(15)
s.push(17)

print('Stack is created: ')
for elem in s:
    print(elem)

s.pop()

print('Stack after first pop operation: ')
for elem in s:
    print(elem)

