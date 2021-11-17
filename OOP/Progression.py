class Progression:
    """ Iterator producing a generic progression
    Default iterator produces the whole numbers 0, 1, 2, ->...
    """

    def __init__(self, start=0):
        """ Initialize current to the first value of the progression """
        self._current = start

    def _advance(self):
        """ Update self._current to a new value
        This should be overridden by a subclass to customize progression

        By convention, if current is set to None, this designate the 
        end of a infinite progression
         """

        self._current += 1

    def __next__(self):
        """ Return the next element, or else raise StopIteration error. """
        if self._current is None:                # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current               # record current value to return
            self._advance()                      # advance to prepare for next time
            return answer                        # return the answer

    def __iter__(self):
        """ By convention an iterator must be return itself as an iterator """
        return self

    def printProgression(self, n):
        """ Print next n values of the progression """
        print(' '.join(str(next(self)) for index in range(n)))


# inherit from class Progression
class ArithmeticProgression(Progression):
    """ Iterator producing an arithmetic progression. """

    def __init__(self, increment=1, start=0):
        """ Create a new arithmetic progression

        increment   the fixed constant to add to each term (default 1)
        start       the first item of the progression (default 0)
         """

        super().__init__(start)                  # initialize from base class
        self._increment = increment

    def _advance(self):                          # overide inherited method
        """ Update current value by adding the fixed increment """
        self._current += self._increment


# inherit from Progression class
class GeometricProgression(Progression):
    """ Iterator producing a geometric progression. """

    def __init__(self, base=2, start=1):
        """ Create a new geometric progression

        base        the fixed constant multiplied to each term (default 2)
        start       the first item of the progression (default 1)
         """

        super().__init__(start)
        self._base = base

    def _advance(self):
        """ Update current value by multiplying it by the base value """
        self._current *= self._base


# inherit from Progression class
class FibonacciProgression(Progression):
    """ Iterator producing a generalized Fibonacci progression. """

    def __init__(self, first=0, second=1):
        """ Create a new Fibonacci progression

        first        the first term of the progression (default 0)
        second       the second term of the progression (default 1)
         """

        super().__init__(first)                  # start progeression at first
        self._prev = second - first              # fictitious value preceding the first

    def _advance(self):
        """ Update current value by taking sum of previous two """
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print("Default progression:")
    Progression().printProgression(10)

    print("Arithmetic progression with increment 5:")
    ArithmeticProgression(5).printProgression(10)

    print("Arithmetic progression with increment 5 and start 3:")
    ArithmeticProgression(5, 3).printProgression(10)

    print("Geometric progression with default base and default start:")
    GeometricProgression().printProgression(10)

    print("Geometric progression with base 5 and default start:")
    GeometricProgression(5).printProgression(10)

    print("Geometric progreeion with base 5 and start 2:")
    GeometricProgression(5, 2).printProgression(10)

    print("Fibonacci progression with default start values:")
    FibonacciProgression().printProgression(15)

    print("Fibonacci progression with start values 1 and 1:")
    FibonacciProgression(1, 1).printProgression(15)

    print("Fibonacci progression with start values 2 and 3:")
    FibonacciProgression(2, 3).printProgression(15)
    