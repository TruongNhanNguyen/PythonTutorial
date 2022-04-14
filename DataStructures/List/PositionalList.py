class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation """

    class _Node:
        """ Lightweight and nonpublic class for storing a doubly linked node """

        __slot__ = '_element', '_prev', '_next'     # streamline memory usage

        def __init__(self, element, prev, next):
            """ Initialize node's fields """
            self._element = element     # node's element
            self._prev = prev           # previous node reference
            self._next = next           # next node reference

    def __init__(self):
        """ Create an empty list """
        self._header = self._Node(
            None, None, None)       # header sentinel
        # trailer sentinels
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer      # trailer is after heder
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
        newest = self._Node(
            e, predecessor, successor)          # linked to neighbors
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
        # recore deleted element
        element = node._element
        node._element = node._prev = node._next = None  # deprecated node
        return element                                  # return deleted element


class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access  """

    # nested Position class
    class Position:
        """ An abstraction represtenting the location of the single element """

        def __init__(self, container, node):
            """ Constructor should not be invoked by user """

            __slot__ = '_container', '_node'
            # reference to the list contains node's position
            self._container = container
            self._node = node           # reference to current node

        def element(self):
            """ Return the element stored at this position """
            return self._node._element  # node's element

        def __eq__(self, other):
            """ Return True if orther is a Position representing the same location """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """ Return True if other dose not represent the same location """
            return not (self == other)  # opposite of __eq__

    # utility methods
    def _validate(self, p):
        """ Return position's node, or raise appropriate error if valid """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:       # convention for deprecated node
            raise ValueError('p is not longer valid')
        return p._node

    def _make_position(self, node):
        """ Return Position instance for given node (or None if sentinels) """
        if node is self._header or node is self._trailer:   # boundary violation
            return None
        else:
            # legitimate position
            return self.Position(self, node)

    # accessors
    def first(self):
        """ Return the first Position in the list (or None if list is empty) """
        return self._make_position(self._header._next)

    def last(self):
        """ Return the last Position int hte list (or None if list is empty) """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """ Return the Position just before the Position p (or None if p is first) """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """ Return the Position just after the Position p (or None if p is last) """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list """
        cursor = self.first()   # begin from the head of the list
        while cursor is not None:   # iterate forward through the list
            # print node's element at current position
            yield cursor.element()
            # advance cursor
            cursor = self.after(cursor)

    # mutator
    # override inherited version to return Position, rether than Node
    def _insert_between(self, e, predecessor, successor):
        """ Add element e between existing nodes and return new Position """
        # call inherited method
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """ Insert element e at the front of the list and return new Position """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """ Insert element e at the back of the list and return new Position """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """ Insert element e into the list before Position p and return new Position """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """ Insert element e into the list after Position p and return new Position """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """ Remove and return the element at Position p """
        original = self._validate(p)
        # inherited method returns element
        return self._delete_node(original)

    def replace(self, p, e):
        """ Replace the element at hte Position p with e.
            Return the element formerly at Position p  """
        original = self._validate(p)        # temporarily store old element
        # replace with new element
        old_value = original._element
        # return the old element value
        original._element = e
        return old_value

    def sort(self, * ,reverse = False):
        """ Sort Positional list of comparable elements into appropriate order """
        if len(self) > 1:                                               # otherwise, no need to sort it
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)                              # next item to place
                value = pivot.element()
                if reverse == False:                                    # sort in nondecreasing order
                    if value > marker.element():                        # pivot is already sorted
                        marker = pivot                                  # pivot become new marker
                    else:                                               # must reallocate pivot
                        walk = marker                                   # find leftmost item greater than value
                        while walk != self.first() and self.before(walk).element() > value:
                            walk = self.before(walk)
                        self.delete(pivot)
                        self.add_before(walk, value)                    # reinsert value before walk
                else:                                                   # if reverse = True sort in nonincreasing order
                    if value < marker.element():                        # pivot is already sorted
                        marker = pivot                                  # pivot become new marker
                    else:                                               # must reallocate pivot
                        walk = marker                                   # find leftmost item lesser than value
                        while walk != self.first() and self.before(walk).element() < value:
                            walk = self.before(walk)
                        self.delete(pivot)
                        self.add_before(walk, value)                    # reinsert value before walk



p = PositionalList()
p_1 = p.add_first(1)
p_0 = p.add_first(0)
p_2 = p.add_last(9)
p_8 = p.add_last(7)
p_4 = p.add_after(p_2, 10)
p_3 = p.add_before(p_4, 11)
p_6 = p.add_after(p_4, 2)
p_5 = p.add_before(p_6, 3)
p_7 = p.add_before(p_8, 8)
p_9 = p.add_after(p_8, 9)
p.replace(p_9, 100)

print('List before sorted: ')
for elem in p:
    print(elem, end=' ')

p.sort()

print('\nList after sorted in nondecreasing order: ')
for elem in p:
    print(elem, end=' ')

p.sort(reverse=True)

print('\nList after sorted in nonincreasing order: ')
for elem in p:
    print(elem, end=' ')

