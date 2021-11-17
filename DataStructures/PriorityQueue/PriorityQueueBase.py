class PriorityQueueBase:
    """ Abstract base class for a priority queue """

    class _Item:
        """ Lightweight and nonpublic class to store priority queue items """
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            """ Initialize item's fields """
            self._key = k
            self._value = v

        def __lt__(self, other):
            """ compared items based om their keys """
            return self._key < other._key

    def is_empty(self):
        """ Return True if the priority queue is empty """
        return len(self) == 0