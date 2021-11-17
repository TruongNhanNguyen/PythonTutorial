# Progression

## Hierarchy of Numeric Progressions

We develop a hierarchy of classes for iterating numeric progressions. A numeric progression is a sequence of numbers, where each number depends on one or more of the previous numbers. For example, an ***arithmetic progression*** determines the next number by adding a fixed constant
to the previous value, and a ***geometric progression*** determines the next number by  multiplying the previous value by a fixed constant. In general, a progression requires a first value, and a way of identifying a new value based on one or more previous values.

To maximize reusability of code, we develop a hierarchy of classes stemming from a general base class that we name `Progression`. Technically, the `Progression` class produces the progression of whole numbers: 0, 1, 2, ... However, this class is designed to serve as the base class for other progression types, providing as much common functionality as possible, and thereby minimizing the burden on the subclasses.

The constructor for this class accepts a starting value for the progression (0 by default), and initializes a data member, `self._current`, to that value.

The `Progression` class implements the conventions of a ***Python iterator***, namely the special `__next__` and `__iter__` methods. If a user of the class creates a progression as `seq = Progression()`, each call to `next(seq)` will return a subsequent element of the progression sequence. It would also be possible to use a for-loop syntax, `for value in seq:`, although we note that our default progression is defined as an infinite sequence.

To better separate the mechanics of the iterator convention from the core logic of advancing the progression, our framework relies on a nonpublic method named `_advance` to update the value of the `self._current` field. In the default implementation, `_advance` adds one to the current value, but our intent is that subclasses will override `_advance` to provide a different rule for computing the next entry.

For convenience, the `Progression` class also provides a utility method, named `print_progression`, that displays the next `n` values of the progression.

## An Arithmetic Progression Class

Our first example of a specialized progression is an arithmetic progression. While the default progression increases its value by one in each step, an arithmetic progression adds a fixed constant to one term of the progression to produce the next. For example, using an increment of 4 for an arithmetic progression that starts at 0 results in the sequence 0,4,8,12,... .

We will implement an `ArithmeticProgression` class, which relies on `Progression` as its base class. The constructor for this new class accepts both an increment value and a starting value as parameters, although default values for each are provided. By our convention, `ArithmeticProgression(4)` produces the sequence 0,4,8,12,... , and `ArithmeticProgression(4, 1)` produces the sequence 1,5,9,13,... .

The body of the `ArithmeticProgression` constructor calls the super constructor to initialize the `_current` data member to the desired start value. Then it directly establishes the new
`_increment` data member for the arithmetic progression. The only remaining detail in our implementation is to override the `_advance` method so as to add the increment to the current value.

## A Geometric Progression Class

Our second example of a specialized progression is a geometric progression, in which each value is produced by multiplying the preceding value by a fixed constant, known as the ***base*** of the geometric progression. The starting point of a geometric progression is traditionally 1, rather than 0, because multiplying 0 by any factor results in 0. As an example, a geometric progression with base 2 proceeds as 1,2,4,8,16,... .

The constructor uses 2 as a default base and 1 as a default starting value, but either of those can be varied using optional parameters.

## A Fibonacci Progression Class

As our final example, we demonstrate how to use our progression framework to produce a ***Fibonacci progression***. Each value of a Fibonacci series is the sum of the two most recent values. To begin the series, the first two values are conventionally 0 and 1, leading to the Fibonacci series 0,1,1,2,3,5,8,... . More generally, such a series can be generated from any two starting values. For example, if we start with values 4 and 6, the series proceeds as 4,6,10,16,26,42,... .

We use our progression framework to define a new `FibonacciProgression` class. This class is markedly different from those for the arithmetic and geometric progressions because we cannot determine the next value of a Fibonacci series solely from the current one. We must maintain knowledge of the two most recent values. The base `Progression` class already provides storage
of the most recent value as the `_current` data member. Our `FibonacciProgression` class introduces a new member, named `_prev`, to store the value that proceeded the current one.

With both previous values stored, the implementation of `_advance` is relatively straightforward. However, the question arises as to how to initialize the previous value in the constructor. The desired first and second values are provided as parameters to the
constructor. The first should be stored as `_current` so that it becomes the first one that is reported. Looking ahead, once the first value is reported, we will do an assignment to set the new current value (which will be the second value reported), equal to the first value plus the "previous". By initializing the previous value to `(second − first)`, the initial advancement will set the new current value to `first + (second − first) = second`, as desired.

## Testing Progression

```python
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

    print("Geometric progression with base 5 and start 2:")
    GeometricProgression(5, 2).printProgression(10)

    print("Fibonacci progression with default start values:")
    FibonacciProgression().printProgression(15)

    print("Fibonacci progression with start values 1 and 1:")
    FibonacciProgression(1, 1).printProgression(15)

    print("Fibonacci progression with start values 2 and 3:")
    FibonacciProgression(2, 3).printProgression(15)
```

```sh
Default progression:
0 1 2 3 4 5 6 7 8 9
Arithmetic progression with increment 5:
0 5 10 15 20 25 30 35 40 45
Arithmetic progression with increment 5 and start 3:      
3 8 13 18 23 28 33 38 43 48
Geometric progression with default base and default start:
1 2 4 8 16 32 64 128 256 512
Geometric progression with base 5 and default start:      
1 5 25 125 625 3125 15625 78125 390625 1953125
Geometric progression with base 5 and start 2:
2 10 50 250 1250 6250 31250 156250 781250 3906250
Fibonacci progression with default start values:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Fibonacci progression with start values 1 and 1:
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
Fibonacci progression with start values 2 and 3:
2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```
