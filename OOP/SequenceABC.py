from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """ Our own version of collections.Sequence abstract base class """

    @abstractmethod
    def __len__(self):
        """ Return the length of the Sequence """
    @abstractmethod
    def __getitem__(self, index):
        """ Return the element at given index of the sequence """

    def __contains__(self, val):
        """ Return True if val found in the sequence, False otherwise """
        for index in range(len(self)):
            if self[index] == val:                 # found match
                return True
        return False

    def index(self, val):
        """ Return leftmost index at which val is found (or raise ValueError) """
        for index in range(len(self)):
            if self[index] == val:                 # leftmost match
                return index
        raise ValueError("Value not in sequence")  # never found a match

    def count(self, val):
        """ Return the number of elements equal to given value """
        result = 0
        for index in range(len(self)):
            if(self[index]) == val:                # found a match
                result += 1
        return result