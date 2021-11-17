# Dynamic Array Implementation

## Implementing a Dynamic Array

Although the Python list class provides a highly optimized implementation of dynamic arrays, it is instructive to see how such a dynamic array might be implemented.

The key is to provide means to grow the array A that stores the elements of a list. Of course, we cannot actually grow that array, as its capacity is fixed. If an element is appended to a list at a time when the underlying array is full, we perform the following steps

- [x] Allocate a new array B with larger capacity.
- [x] Set B[i] = A[i], for i = 0,...,n−1, where n denotes current number of items.
- [x] Set A = B, that is, we henceforth use B as the array supporting the list.
- [x] Insert the new element in the new array.

The remaining issue to consider is how large of a new array to create. A commonly used rule is for the new array to have twice the capacity of the existing array that has been filled.

We offer a concrete implementation of dynamic arrays in Python. Our `DynamicArray` class is designed using ideas described up there. While consistent with the interface of a Python list class, we provide only limited functionality in the form of an `append` method, and accessors `__len__` and `__getitem__`. Support for creating low-level arrays is provided by a module named `ctypes`. Because we will not typically use such a low-level structure in the remainder, we omit a detailed explanation of the `ctypes` module. Instead, we wrap the necessary command for declaring the raw array within a private utility method `_make_array`. The hallmark expansion procedure is performed in our nonpublic `_resize` method.

An implementation of a DynamicArray class, using a raw array from the ctypes module as storage [here](dynamic_array.py)

## Amortized Analysis of Dynamic Arrays

May i do not mention this section here 😇
