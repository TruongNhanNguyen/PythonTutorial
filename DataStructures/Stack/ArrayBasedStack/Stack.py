class Empty(Exception):
    """ Error attemping to access an element from an empty stack """
    pass


class ArrayStack:
    """ LIFO stack implementation using Python list as underlying storage """

    def __init__(self):
        """ Create an empty stack """
        self._data = []                         # non public list instance

    def __len__(self):
        """ Return number of elements in the stack """
        return len(self._data)

    def is_empty(self):
        """ Check if the stack is empty """
        return len(self._data) == 0

    def push(self, obj):
        """ Add element at the top of the stack """
        self._data.append(obj)                  # new item is stored at the end of the list

    def top(self):
        """ Return (but not remove) the element at the top of the stack
            Raise Empty exception if the stack is empty """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._data[-1]                   # last item in the list

    def pop(self):
        """ Remove and return the element from the top of the stack (i.e LIFO)
            Raise Empty exception if stack is empty """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._data.pop()                 # remove the last item from the list

    def __str__(self):
        """ Print the stack's content """
        return str(self._data)


def reverse_file(filename):
    """ Overwrite given file with its content line by line reversed """
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))               # we will reinsert new line when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')                # reopening file overwrite original
    while not S.is_empty():
        output.write(S.pop() + '\n')            # re-insert new line character
    output.close()

S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
print(S)
