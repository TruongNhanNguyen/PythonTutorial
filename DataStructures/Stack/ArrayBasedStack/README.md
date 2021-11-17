# Stack

## The Stack Abstract Data Type

Stacks are the simplest of all data structures, yet they are also among the most important. They are used in a host of different applications, and as a tool for many more sophisticated data structures and algorithms. Formally, a stack is an abstract data type (ADT) such that an instance S supports the following two methods:

- [x] **`S.push(e)`**: Add element e to the top of stack S.
- [x] **`S.pop()`**: Remove and return the top element from the stack S;an error occurs if the stack is empty.

Additionally, let define the following accessor methods for convenience:

- [x] **`S.top()`**: Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
- [x] **`S.is_empty()`**: Return True if stack S does not contain any elements.
- [x] **`len(S)`**: Return the number of elements in stack S; in Python, we implement this with the special method **`__len__`**.

By convention, we assume that a newly created stack is empty, and that there is no a priori bound on the capacity of the stack. Elements added to the stack can have arbitrary type.

**Example :** The following table shows a series of stack operations and their effects on an initially empty stack S of integers.

| **Operation** | **Return Value** | **Stack Contents** |
| --- | --- | --- |
| **`S.push(5)`** | **`None`** | [5] |
| **`S.push(3)`** | **`None`** | [5, 3] |
| **`len(S)`** | 2 | [5, 3] |
| **`S.pop()`** | 3 | [5] |
| **`S.is_empty()`** | **`False`** | [5] |
| **`S.pop()`** | 5 | [] |
| **`S.is_empty()`** | **`True`** | [] |
| **`S.pop()`** | **`Error`** | [] |
| **`S.push(7)`** | **`None`** | [7] |
| **`S.push(9)`** | **`None`** | [7, 9] |
| **`S.top()`** | 9 | [7, 9] |
| **`S.push(4)`** | **`None`** | [7, 9, 4] |
| **`len(S)`** | 3 | [7, 9, 4] |
| **`S.pop()`** | 4 | [7, 9] |
| **`S.push(6)`** | **`None`** | [7, 9, 6] |
| **`S.push(8)`** | **`None`** | [7, 9, 6, 8] |
| **`S.pop()`** | 8 | [7, 9, 6] |

## Simple Array Based Stack Implementation

We can implement a stack quite easily by storing its elements in a Python list. The list class already supports adding an element to the end with the append method, and removing the last element with the pop method, so it is natural to align the top of the stack at the end of the list.

Although a programmer could directly use the list class in place of a formal stack class, lists also include behaviors (e.g., adding or removing elements from arbitrary positions) that would break the abstraction that the stack ADT represents. Also, the terminology used by the list class does not precisely align with traditional nomenclature for a stack ADT, in particular the distinction between append and
push. Instead, we demonstrate how to use a list for internal storage while providing a public interface consistent with a stack.

## The Adapter Pattern

The adapter design pattern applies to any context where we effectively want to modify an existing class so that its methods match those of a related, but different, class or interface. One general way to apply the adapter pattern is to define a new class in such a way that it contains an instance of the existing class as a hidden
field, and then to implement each method of the new class using methods of this hidden instance variable. By applying the adapter pattern in this way, we have created a new class that performs some of the same functions as an existing class,
but repackaged in a more convenient way.

In the context of the stack ADT, we can adapt Python’s list class using the correspondences shown in **Table** below:

| **Stack Methods** | **Realization with Python list** |
| --- | --- |
| **`S.push(e)`** | **L.append(e)** |
| **`S.pop()`** | **`L.pop()`** |
| **`S.top()`** | **`L[-1]`** |
| **`S.is_empty()`** | **`len(L) == 0`** |
| **`len(S)`** | **`len(L)`** |

## Implementing a Stack Using a Python List

We use the adapter design pattern to define an **ArrayStack** class that uses an underlying **Python list** for storage. (We choose the name **ArrayStack** to emphasize that the underlying storage is inherently **array based**.) One question that remains is what our code should do if a user calls pop or top when the stack is empty. Our ADT suggests that an error occurs, but we must decide what type of error. When pop is called on an empty Python list, it formally raises an **IndexError**, as lists are  index-based sequences. That choice does not seem appropriate for a stack, since there is no assumption of indices. Instead, we can define a new exception class that is more appropriate. Code Fragment below defines such an **Empty class** as a trivial **subclass** of the **Python Exception class**.

```Python
class Empty(Exception):
    """ Error attempting to access an element from an empty container. """
    pass
```

The constructor establishes the member **`self.data`** as an initially empty **Python list**,
for internal storage. The rest of the public stack behaviors are implemented, using
the corresponding adaptation that was outlined in Table of Stack methods.

## Code fragment

You can see all detail implementation of Stack **[here](https://github.com/TruongNhanNguyen/PythonBasic/blob/main/DataStructures/Stack/stack.py)**

## Analyzing the Array-Based Stack Implementation

Table below shows the running times for our ArrayStack methods. The implementations for top, is empty, and len use constant time in the worst case. The **`O(1)`** time for push and pop are amortized bounds; a typical call to either of these methods uses constant time, but there is occasionally an **`O(n)-time`** worst case, where n is the current number of elements in the stack, when an operation causes the list to resize its internal array. The space usage for a stack is **`O(n)`**.

| **Operation** | **Running Time** |
| --- | --- |
| **`S.push(e)`** | **`O(1)*`** |
| **`S.pop()`** | **`O(1)*`** |
| **`S.top()`** | **`O(1)`** |
| **`S.is_empty()`** | **`O(1)`** |
| **`len(S)`** | **`O(1)`** |

***Note***: *amortized

## Avoiding Amortization by Reserving Capacity

In some contexts, there may be additional  knowledge that suggests a maximum size that a stack will reach. Our implementation of ArrayStack from **[Code Fragment](https://github.com/TruongNhanNguyen/PythonBasic/blob/main/DataStructures/Stack/stack.py)** begins with an empty list and expands as needed. In the analysis of lists, we emphasized that it is more efficient in practice to construct a list with initial length n than it is to start with an empty list and append n items (even though both approaches run in (`O(n)-time`).
