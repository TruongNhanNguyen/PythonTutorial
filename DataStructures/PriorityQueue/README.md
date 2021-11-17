# Priority Queue

## The Priority Queue Abstract Data Type

### Priorities

We introduce a new abstract data type known as a ***priority queue***. This is a collection of prioritized elements that allows arbitrary element insertion, and allows the removal of the element that has first priority. When an element is added to a priority queue, the user designates its priority by providing an associated ***key***.
The element with the *minimum* key will be the next to be removed from the queue (thus, an element with key 1 will be given priority over an element with key 2). Although it is quite common for priorities to be expressed numerically, any Python object may be used as a key, as long as the object type supports a consistent meaning for the test `a < b`, for any instances `a` and `b`, so as to define a natural order of the keys. With such generality, applications may develop their own notion of priority for each element.

### The Priority Queue ADT

Formally, we model an element and its priority as a ***key-value pair***. We define the
priority queue ADT to support the following methods for a priority queue `P`:

- `P.add(k, v)`: Insert an item with key `k` and value `v` into priority queue `P`.
- `P.min()`: Return a tuple, `(k,v)`, representing the key and value of an item in priority queue `P` with minimum key (but do not remove the item); an error occurs if the priority queue is empty.
- `P.remove_min()`: Remove an item with minimum key from priority queue `P`, and return a tuple, `(k,v)`, representing the key and value of the removed item; an error occurs if the priority queue is empty.
- `P.is_empty()`: Return `True` if priority queue `P` does not contain any items.
- `len(P)`: Return the number of items in priority queue `P`.

## Implementing a Priority Queue

In this section, we show how to implement a priority queue by storing its entries in
a positional list `L`. We provide two realizations, depending on whether or not we keep the entries in `L` sorted by key.

### The Composition Design Pattern

One challenge in implementing a priority queue is that we must keep track of both an element and its key, even as items are relocated within our data structure. To solve this problem,  we introduced the ***composition design pattern***, defining an `_Item` class that assured that each element remained paired with its associated count in our primary data structure.

For priority queues, we will use composition to store items internally as pairs consisting of a key `k` and a value `v`. To implement this concept for all priority queue
implementations, we provide a `PriorityQueueBase` class (see below **Code Fragment**)
that includes a definition for a nested class named `_Item`. We define the syntax `a < b`, for item instances `a` and `b`, to be based upon the keys.

```python
class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys

    def is_empty(self):                         # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0
```

For convenience, we provide a concrete implementation of `is_empty` that is based on a presumed `__len__` implementation.

### Implementation with an Unsorted List

In our first concrete implementation of a priority queue, we store entries within
an *unsorted list*. Our `UnsortedPriorityQueue` class is given in the [Code Fragment](UnsortedPriorityQueue.py), inheriting from the `PriorityQueueBase` class introduced in the above **Code Fragment** internal storage, key-value pairs are represented as composites, using instances of the inherited `_Item` class. These items are stored within a `PositionalList`, identified as the data member of our class. We assume that the positional list is implemented with a doubly-linked list, as in [here](../List/README.md), so that all operations of that ADT execute in `O(1)` time.

We begin with an empty list when a new priority queue is constructed. At all times, the size of the list equals the number of key-value pairs currently stored in the priority queue. For this reason, our priority queue `__len__` method simply returns the length of the internal `_data` list. By the design of our `PriorityQueueBase` class, we inherit a concrete implementation of the `is_empty` method that relies on a call to our `__len__`
method.

Each time a key-value pair is added to the priority queue, via the `add` method, we create a new `_Item` composite for the given key and value, and add that item to the end of the list. Such an implementation takes `O(1)` time.

The remaining challenge is that when `min` or `remove_min` is called, we must locate the item with minimum key. Because the items are not sorted, we must inspect all entries to find one with a minimum key. For convenience, we define a nonpublic `_find_min` utility that returns the position of an item with minimum key. Knowledge of the position allows the `remove_min` method to invoke the `delete` method on the positional list. The min method simply uses the position to retrieve the item when preparing a key-value tuple to return. Due to the loop for finding the minimum key, both `min` and `remove_min` methods run in `O(n)` time, where `n` is the number of entries in the priority queue.

A summary of the running times for the UnsortedPriorityQueue class is given
in below Table 📊

| **Operation** | **Running Time** |
| --- | --- |
| `len` | `O(1)` |
| `is_empty` | `O(1)` |
| `add` | `O(1)` |
| `min` | `O(n)` |
| `remove_min` | `O(n)` |

### Implementation with a Sorted List

An alternative implementation of a priority queue uses a positional list, yet maintaining entries sorted by non decreasing keys. This ensures that the first element of
the list is an entry with the smallest key.

The implementation of `min` and `remove_min` are rather straightforward given knowledge that the first element of a list has a minimum key. We rely on the `first` method of the positional list to find the position of the first item, and the `delete` method to  remove the entry from the list. Assuming that the list is implemented with a doubly linked list, operations `min` and `remove_min` take `O(1)` time.

This benefit comes at a cost, however, for method `add` now requires that we scan
the list to find the appropriate position to insert the new item. Our implementation
starts at the end of the list, walking backward until the new key is smaller than
an existing item; in the worst case, it progresses until reaching the front of the
list. Therefore, the add method takes `O(n)` worst-case time, where `n` is the number
of entries in the priority queue at the time the method is executed. In summary,
when using a sorted list to implement a priority queue, insertion runs in linear time,
whereas finding and removing the minimum can be done in constant time.

### Comparing the Two List-Based Implementations

Table 📊 below compares the running times of the methods of a priority queue realized
by means of a sorted and unsorted list, respectively. We see an interesting trade-off when we use a list to implement the priority queue ADT. An unsorted list supports fast insertions but slow queries and deletions, whereas a sorted list allows fast queries and deletions, but slow insertions.

| **Operation** | **Unsorted List** | **Sorted List** |
| --- | --- | --- |
| `len` | `O(1)` | `O(1)` |
| `is_empty` | `O(1)` | `O(1)` |
| `add` | `O(1)` | `O(n)` |
| `min` | `O(n)` | `O(1)` |
| `remove_min` | `O(n)` | `O(1)` |

## Heap

The two strategies for implementing a priority queue ADT in the previous section
demonstrate an interesting trade-off. When using an unsorted list to store entries,
we can perform insertions in `O(1)` time, but finding or removing an element with
minimum key requires an `O(n)`-time loop through the entire collection. In contrast,
if using a sorted list, we can trivially find or remove the minimum element in `O(1)`
time, but adding a new element to the queue may require `O(n)`-time to restore the
sorted order.

In this section, we provide a more efficient realization of a priority queue using
a data structure called a ***binary heap***. This data structure allows us to perform both insertions and removals in logarithmic time, which is a significant improvement
over the list-based implementations discussed in [Implementing a Priority Queue](#implementing-a-priority-queue). The fundamental way the heap achieves this improvement is to use the structure of a binary tree to find a compromise between elements being entirely unsorted and perfectly sorted.

### The Heap Data Structure

A heap is a ***binary tree*** `T` that stores a collection of items at its positions and that satisfies two additional properties: a relational property defined in terms of the way keys are stored in `T` and a structural property defined in terms of the shape of `T` itself. The relational property is the following

> ***Heap-Order Property***: In a heap `T`, for every position `p` other than the `root`    , the key stored at `p` is greater than or equal to the key stored at `p`’s parent.

As a consequence of the heap-order property, the keys encountered on a path from
the root to a leaf of `T` are in non decreasing order. Also, a minimum key is always
stored at the root of `T`. This makes it easy to locate such an item when min or
`remove_min` is called, as it is informally said to be "at the top of the heap" (hence,
the name "heap" for the data structure). By the way, the heap data structure defined
here has nothing to do with the memory heap used in the run-time environment supporting a programming language like Python.

For the sake of efficiency, as will become clear later, we want the heap `T` to have
as small a *height* as possible. We enforce this requirement by insisting that the heap
`T` satisfy an additional structural property—it must be what we term ***complete***.

> ***Complete Binary Tree Property***: A heap `T` with height `h` is a complete binary tree if levels `0,1,2,...,h − 1` of `T` have the maximum number of nodes possible (namely, level `i` has `2i` nodes, for `0 <= i <= h − 1`) and the remaining nodes at level `h` reside in the leftmost possible positions at that level.

A complete binary tree with `n` elements is one that has positions with level numbering `0` through `n − 1`. For example, in an array-based representation of the above tree, its `13` entries would be stored consecutively from `A[0]` to `A[12]`.

#### The Height of a Heap

Let `h` denote the height of `T`. Insisting that `T` be complete also has an important
consequence, as shown in below Proposition.

> ***Height of the Heap***: A heap `T` storing `n` entries has height `h=floor(log(n))`

### Implementing a Priority Queue with a Heap

Proposition ***Height of the Heap*** has an important consequence, for it implies that if we can perform update operations on a heap in time proportional to its height, then those operations will run in logarithmic time. Let us therefore turn to the problem of how to efficiently perform various priority queue methods using a heap.

We will use the composition pattern from [The Composition Pattern](#the-composition-design-pattern) to store key-value pairs as items in the heap. The `len` and `is_empty` methods can be implemented based on examination of the tree, and the `min` operation is equally trivial because the heap property assures that the element at the root of the tree has a minimum key. The interesting algorithms are those for implementing the add and `remove_min` methods.

#### Adding an Item to the Heap

Let us consider how to perform `add(k,v)` on a priority queue implemented with a heap `T`. We store the pair `(k,v)` as an item at a new node of the tree. To maintain the ***complete binary tree property***, that new node should be placed at a position `p` just beyond the rightmost node at the bottom level of the tree, or as the leftmost position of a new level, if the bottom level is already full (or if the heap is empty).

#### Up-Heap Bubbling After an Insertion

After this action, the tree `T` is complete, but it may violate the ***heap-order property***. Hence, unless position `p` is the root of `T` (that is, the priority queue was empty before the insertion), we compare the key at position `p` to that of `p`’s parent, which we denote as `q`. If key `k_p >= k_q`, the heap-order property is satisfied and the algorithm terminates. If instead `k_p < k_q`, then we need to restore the heap-order property, which can be locally achieved by swapping the entries stored at positions `p` and `q`. This swap causes the new item to move up one level. Again, the heap-order property may be violated, so we repeat the process, going up in `T` until no violation of the heap-order property occurs.

The upward movement of the newly inserted entry by means of swaps is conventionally called ***up-heap bubbling***. A swap either resolves the violation of the heap-order property or propagates it one level up in the heap. In the worst case, up-heap bubbling causes the new entry to move all the way up to the root of heap `T`. Thus, in the worst case, the number of swaps performed in the execution of method `add` is equal to the height of `T`. By Proposition ***Height of the Heap***, that bound is `floor(log(n))`.

#### Removing the Item with Minimum Key

Let us now turn to method `remove_min` of the priority queue ADT. We know that an entry with the smallest key is stored at the root `r` of `T` (even if there is more than one entry with smallest key). However, in general we cannot simply delete node `r`, because this would leave two disconnected subtrees. Instead, we ensure that the shape of the heap respects the ***complete binary tree*** property by deleting the leaf at the *last* position `p` of `T`, defined as the rightmost position at the bottommost level of the tree. To preserve the item from the last position `p`, we copy it to the root `r` (in place of the item with minimum key that is being removed by the operation).

#### Down-Heap Bubbling After a Removal

We are not yet done, however, for even though `T` is now complete, it likely violates
the ***heap-order property***. If `T` has only one node (the root), then the heap-order
property is trivially satisfied and the algorithm terminates. Otherwise, we distinguish two cases, where `p` initially denotes the root of `T`

- If `p` has no right child, let `c` be the left child of `p`.
- Otherwise (`p` has both children), let `c` be a child of `p` with minimal key.

If key `k_p <= k_c`, the heap-order property is satisfied and the algorithm terminates. If instead `k_p > k_c`, then we need to restore the heap-order property. This can be locally achieved by swapping the entries stored at `p` and `c`. It is worth noting that when `p` has two children, we intentionally consider the smaller key of the two  children. Not only is the key of `c` smaller than that of `p`, it is at least as small as the key at `c`’s sibling. This ensures that the heap-order property is locally restored when that smaller key is promoted above the key that had been at `p` and that at `c`’s sibling.

Having restored the heap-order property for node `p` relative to its children, there may be a violation of this property at `c`; hence, we may have to continue swapping down `T` until no violation of the heap-order property occurs. This downward swapping process is called ***down-heap bubbling***. A swap either resolves the violation of the heap-order property or propagates it one level down in the heap. In the worst case, an entry moves all the way down to the bottom level. Thus, the number of swaps performed in the execution of method `remove_min` is, in the worst case, equal to the height of heap `T`, that is, it is `floor(log(n))`.

### Array-Based Representation of a Complete Binary Tree

The array-based representation of a binary tree is especially suitable for a complete binary tree `T`. We recall that in this implementation, the elements of `T` are stored in an array-based list `A` such that the element at position `p` in `T` is stored in `A` with index equal to the level number `f(p)` of `p`, defined as follows

- If `p` is the root of `T`, then `f(p) = 0`.
- If `p` is the left child of position `q`, then `f(p) = 2f(q)+1`.
- If `p` is the right child of position `q`, then `f(p) = 2f(q)+2`.

With this implementation, the elements of `T` have contiguous indices in the range `[0, n − 1]` and the last position of `T` is always at index `n − 1`, where `n` is the number
of positions of `T`.

Implementing a priority queue using an array-based heap representation allows us to avoid some complexities of a node-based tree structure. In particular, the `add` and `remove_min` operations of a priority queue both depend on locating the last
index of a heap of size `n`. With the array-based representation, the last position
is at index `n − 1` of the array. Locating the last position of a complete binary tree
implemented with a linked structure requires more effort.

If the size of a priority queue is not known in advance, use of an array-based representation does introduce the need to dynamically resize the array on occasion,
as is done with a Python list. The space usage of such an array-based representation
of a complete binary tree with `n` nodes is `O(n)`, and the time bounds of methods for
adding or removing elements become ***amortized***.

### Python Heap Implementation

We use an array-based representation, maintaining a Python list of item composites. Although we do not formally use the binary tree ADT,source code includes nonpublic utility functions that compute the level numbering of a parent or child of another. This allows us to describe the rest of our algorithms using tree-like terminology of `parent`, `left`, and `right`. However, the relevant variables are integer indexes (not "position" objects). We use recursion to implement the repetition in the `_upheap` and
`_downheap` utilities.

### Analysis of a Heap-Based Priority Queue

📊 Table below shows the running time of the priority queue ADT methods for the heap
implementation of a priority queue, assuming that two keys can be compared in `O(1)` time and that the heap `T` is implemented with an array-based or linked-based tree representation.

In short, each of the priority queue ADT methods can be performed in `O(1)` or
in `O(log(n))` time, where n is the number of entries at the time the method is executed. The analysis of the running time of the methods is based on the following

- The heap `T` has `n` nodes, each storing a reference to a key-value pair.
- The height of heap `T` is `O(log(n))`, since `T` is complete.
- The `min` operation runs in `O(1)` because the root of the tree contains such an element.
- Locating the last position of a heap, as required for add and `remove_min`, can be performed in `O(1)` time for an array-based representation, or `O(log(n))` time for a linked-tree representation.
- In the worst case, up-heap and down-heap bubbling perform a number of swaps equal to the height of `T`.

| **Operation** | **Running Time** |
| --- | --- |
| `len(P)`, `P.is_empty()` | `O(1)` |
| `P.min()` | `O(1)` |
| `P.add()` | `O(log(n))` |
| `P.remove_min` | `O(log(n))` |

We conclude that the heap data structure is a very efficient realization of the priority queue ADT, independent of whether the heap is implemented with a linked structure or an array. The heap-based implementation achieves fast running times for both insertion and removal, unlike the implementations that were based on using an unsorted or sorted list.

### Bottom-Up Heap Construction 🌟

If we start with an initially empty heap, `n` successive calls to the add operation will
run in `O(n.log(n))` time in the worst case. However, if all `n` key-value pairs to be
stored in the heap are given in advance, such as during the first phase of the heap-
sort algorithm, there is an alternative ***bottom-up*** construction method that runs in
`O(n)` time.

In this section, we describe the bottom-up heap construction, and provide an implementation that can be used by the constructor of a heap-based priority queue.

For simplicity of exposition, we describe this bottom-up heap construction assuming the number of keys, `n`, is an integer such that `n = 2^(h + 1) − 1`. That is, the heap is a complete binary tree with every level being full, so the heap has height `h = log(n + 1) − 1`. Viewed non-recursively, bottom-up heap construction consists of the following `h + 1 = log(n + 1)` steps

1. In the first step, we construct `(n + 1)/2` elementary heaps storing one entry each.
2. In the second step, we form `(n + 1)/4` heaps, each storing three entries, by joining pairs of elementary heaps and adding a new entry. The new entry is placed at the root and may have to be swapped with the entry stored at a child to preserve the heap-order property.
3. In the third step, we form `(n + 1)/8` heaps, each storing 7 entries, by joining pairs of 3-entry heaps (constructed in the previous step) and adding a new entry. The new entry is placed initially at the root, but may have to move down with a down-heap bubbling to preserve the heap-order property.

...

i. In the generic `i-th` step, `2 <= i <= h`, we form `(n + 1)/2i` heaps, each storing `2i − 1` entries, by joining pairs of heaps storing `(2i − 1 − 1)` entries (constructed in the previous step) and adding a new entry. The new entry is placed initially at
the root, but may have to move down with a down-heap bubbling to preserve the heap-order property.

...

h + 1. In the last, we form the final heap, storing all the `n` entries, by joining two heaps storing `(n − 1)/2` entries (constructed in the previous step) and adding a new entry. The new entry is placed initially at the root, but may have to move down with a down-heap bubbling to preserve the heap-order property.

#### Python Implementation of a Bottom-Up Heap Construction

Implementing a bottom-up heap construction is quite easy, given the existence of a "down-heap" utility function. The "merging" of two equally sized heaps that are subtrees of a common position `p`, as described in the opening of this section, can be accomplished simply by down-heaping `p`’s entry.

With our array-based representation of a heap, if we initially store all `n` items in
arbitrary order within the array, we can implement the bottom-up heap construction
process with a single loop that makes a call to `_downheap` from each position of the tree, as long as those calls are ordered starting with the deepest level and ending with the root of the tree. In fact, that loop can start with the deepest non-leaf, since
there is no effect when down-heap is called at a leaf position.

In below **Code Fragment**, we augment the original `HeapPriorityQueue` class to provide support for the bottom-up construction of an initial collection. We introduce a non-public utility method, `_heapify`, that calls `_downheap` on each non-leaf position, beginning with the deepest and concluding with a call at the root of the tree. We have redesigned the constructor of the class to accept an optional parameter that can be any sequence of `(k,v)` tuples. Rather than initializing `self._data` to an empty list, we use a list comprehension syntax to create an initial list of item composites based on the given contents. We declare an empty sequence as the default parameter value so that the default syntax `HeapPriorityQueue()` continues to result in an empty priority queue.

```python
def __init__(self):
        """ Create a new empty Priority Queue """
        self._data = []

    def __init__(self, contents=()):
        """ Create a new priority queue.
            By default, queue will be empty. If contents is 
            given, it should be as an iterable sequence of (k, v)
            tuples specifying the initial contents """

        self._data = [self._Item(k, v) for k, v in contents]    # empty by default
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)                     # start at Parent of last leaf
        for j in range(start, -1, -1):                          # going to and including the root
            self._down_heap(j)
```
