# Queues Implementation

## Queues

## Abstraction

One of the fundamental data structure is the ***queue***. It is a close "cousin" of the ***stack***, as a queue is a collection of objects that are inserted and removed according to the ***first-in, first-out (FIFO)*** principle. That is, elements can be inserted at any time, but only the element that has been in the queue the longest can be next removed.

We usually say that elements enter a queue at the back and are removed from the front. A metaphor for this terminology is a line of people waiting to get on an amusement park ride. People waiting for such a ride enter at the back of the line and get on the ride from the front of the line. There are many other applications of queues. Stores, theaters, reservation centers, and other similar services typically process customer requests according to the FIFO principle. A queue would therefore be a logical choice for a data structure to handle calls to a customer service center, or a wait-list at a restaurant. FIFO queues are also used by many computing devices, such as a networked printer, or a Web server responding to requests.

### The Queue Abstract Data Type

Formally, the queue abstract data type defines a collection that keeps objects in a sequence, where element access and deletion are restricted to the ***first*** element in the queue, and element insertion is restricted to the back of the sequence. This restriction enforces the rule that items are inserted and deleted in a queue according to the first-in, first-out (FIFO) principle. The ***queue*** abstract data type (ADT) supports the following two fundamental methods for a queue `Q`

- [x] `Q.enqueue(e)`: Add element `e` to the back of queue `Q`.
- [x] `Q.dequeue()`: Remove and return the first element from queue `Q`; an error occurs if the queue is empty.

The queue ADT also includes the following supporting methods (with `first` being
analogous to the stack’s `top` method)

- [x] `Q.first()`: Return a reference to the element at the front of queue `Q`, without removing it; an error occurs if the queue is empty.
- [x] `Q.is_empty()`: Return `True` if queue `Q` does not contain any elements.
- [x] `len(Q)`: Return the number of elements in queue `Q`; in Python, we implement this with the special method `__len__`

By convention, we assume that a newly created queue is empty, and that there is no a priori bound on the capacity of the queue. Elements added to the queue can have arbitrary type.

### Array-Based Queue Implementation

#### @Using A Circular Array

In developing a more robust queue implementation, we allow the front of the queue to drift rightward, and we allow the contents of the queue to “wrap around” the end of an underlying array. We assume that our underlying array has fixed length `N` that is greater that the actual number of elements in the queue. New elements are enqueued toward the “end” of the current queue, progressing from the front to index `N − 1` and continuing at index 0, then 1. Figure 6.6 illustrates such a queue with first element `E` and last element `M`.

Implementing this circular view is not difficult. When we dequeue an element and want to “advance” the front index, we use the arithmetic `f = (f + 1) % N`. Recall that the `%` operator in Python denotes the modulo operator, which is computed by taking the remainder after an integral division. For example, 14 divided by 3 has a quotient of 4 with remainder 2, that is, `14/3 = 4 + 2/3`. So in Python, `14 // 3` evaluates to the quotient 4, while `14 % 3` evaluates to the remainder 2. The modulo operator is ideal for treating an array circularly. As a concrete example, if we have a list of length 10, and a front index 7, we can advance the front by formally computing `(7+1) % 10`, which is simply 8, as 8 divided by 10 is 0 with a remainder of 8. Similarly, advancing index 8 results in index 9. But when we advance from index 9 (the last one in the array), we compute `(9+1) % 10`, which evaluates to index 0 (as 10 divided by 10 has a remainder of zero)

#### Python Queue Implementation

Internally, the queue class maintains the following three instance variables

- `_data`: is a reference to a list instance with a fixed capacity.
- `size`: is an integer representing the current number of elements stored in the queue (as opposed to the length of the `_data` list).
- `front`: is an integer that represents the index within `_data` of the first element of the queue (assuming the queue is not empty)

We initially reserve a list of moderate size for storing data, although the queue formally has size zero. As a technicality, we initialize the `_front` index to zero.
When front or dequeue are called with no elements in the queue, we raise an instance of the `Empty` exception.

[Code Sample](queue.py)

#### Adding and Removing Elements

The goal of the `enqueue` method is to add a new element to the back of the queue. We need to determine the proper index at which to place the new element. Although we do not explicitly maintain an instance variable for the back of the queue, we compute the location of the next opening based on the formula.

```math
avail = (self._front + self._size) % len(self._data)
```

Note that we are using the size of the queue as it exists prior to the addition of the
new element. For example, consider a queue with capacity 10, current size 3, and first element at index 5. The three elements of such a queue are stored at indices 5, 6, and 7. The new element should be placed at index `(front + size) = 8`. In a case with wrap-around, the use of the modular arithmetic achieves the desired circular semantics. For example, if our hypothetical queue had 3 elements with the first at
index 8, our computation of `(8+3) % 10` evaluates to 1, which is perfect since the
three existing elements occupy indices 8, 9, and 0.

When the dequeue method is called, the current value of `self._front` designates the index of the value that is to be removed and returned. We keep a local reference to the element that will be returned, setting `answer = self._data[self._front]` just prior to removing the reference to that object from the list, with the assignment
`self._data[self._front] = None`. Our reason for the assignment to `None` relates to
Python’s mechanism for reclaiming unused space. Internally, Python maintains a count of the number of references that exist to each object. If that count reaches zero, the object is effectively inaccessible, thus the system may reclaim that memory for future use. Since we are no longer responsible for storing a dequeued element, we remove the reference to it from our list so as to reduce that element’s reference count.

The second significant responsibility of the `dequeue` method is to update the
value of `_front` to reflect the removal of the element, and the presumed promotion
of the second element to become the new first. In most cases, we simply want to increment the index by one, but because of the possibility of a wrap-around configuration, we rely on modular arithmetic as originally described.

#### Resizing the Queue

When `enqueue` is called at a time when the size of the queue equals the size of the
underlying list, we rely on a standard technique of doubling the storage capacity of
the underlying list. In this way, our approach is similar to the one used when we
implemented a `DynamicArray`.

However, more care is needed in the queue’s `_resize` utility than was needed in
the corresponding method of the `DynamicArray` class. After creating a temporary
reference to the old list of values, we allocate a new list that is twice the size and
copy references from the old list to the new list. While transferring the contents, we
intentionally realign the front of the queue with index 0 in the new array. This realignment is not purely cosmetic. Since the modular arithmetic depends on the size of the array, our state would be flawed had we transferred each element to its same index in the new array.

#### Shrinking the Underlying Array

A desirable property of a queue implementation is to have its space usage be `Θ(n)`
where `n` is the current number of elements in the queue. Our ArrayQueue implementation, does not have this property. It expands the underlying array when `enqueue` is called with the queue at full capacity, but the `dequeue` implementation never shrinks the underlying array. As a consequence, the capacity of the underlying array is proportional to the maximum number of elements that have ever been stored in the queue, not the current number of elements.

#### Analyzing the Array-Based Queue Implementation 📊

Performance of an array-based implementation of a queue. The bounds for `enqueue` and `dequeue` are amortized due to the resizing of the array. The space usage is `O(n)`, where `n` is the current number of elements in the queue.

| **Operation** | **Running Time** |
| --- | --- |
| `Q.enqueue(e)` | `O(1)` |
| `Q.dequeue()` | `O(1)` |
| `Q.first()` | `O(1)` |
| `Q.is_empty()` | `O(1)` |
| `len(Q)` | `O(1)` |

### Implementing a Queue with a Circularly Linked List

To implement the queue ADT using a circularly linked list, we rely on the intuition
that in which the queue has a ***head*** and a ***tail***, but with the next reference of the ***tail*** linked to the ***head***. Given such a model, there is no need for us to explicitly store references to both the ***head*** and the ***tail***; as long as we keep a reference to the ***tail***, we can always find the ***head*** by  following the tail’s next reference.

The only two instance variables are `_tail`, which is a reference to the tail node (or `None` when empty), and `_size`, which is the current number of elements in the queue. When an operation involves the front of the queue, we recognize `self._tail._next` as the head of the queue. When `enqueue` is called, a new node is placed just after the tail but before the current head, and then the new node becomes the tail.

In addition to the traditional queue operations, the `CircularQueue` class supports
a rotate method that more efficiently enacts the combination of removing the front
element and reinserting it at the back of the queue. With the circular representation,
we simply set `self._tail = self._tail._next` to make the old (with the node after the old head becoming the new head).

### Doubly Linked List

In a singly linked list, each node maintains a reference to the node that is immediately after it. We have demonstrated the usefulness of such a representation when
managing a sequence of elements. However, there are limitations that stem from
the asymmetry of a singly linked list. We emphasized that we can efficiently insert a node at either end of a singly linked list, and can delete a node at the head of a list, but we are unable to efficiently delete a node at the tail of the list. More generally, we cannot efficiently delete an arbitrary node from an interior position of the list if only given a reference to that node, because we cannot determine the node that immediately *precedes* the node to be deleted (yet, that node needs to have its next reference updated).

To provide greater symmetry, we define a linked list in which each node keeps an explicit reference to the node before it and a reference to the node after it. Such
a structure is known as a ***doubly linked list***. These lists allow a greater variety of
`O(1)-time` update operations, including insertions and deletions at arbitrary positions within the list. We continue to use the term “next” for the reference to the
node that follows another, and we introduce the term “prev” for the reference to the
node that precedes it.

#### Header and Trailer Sentinels

In order to avoid some special cases when operating near the boundaries of a doubly
linked list, it helps to add special nodes at both ends of the list: a ***header*** node at the beginning of the list, and a ***trailer*** node at the end of the list. These “dummy” nodes are known as ***sentinels*** (or guards), and they do not store elements of the primary sequence.

When using sentinel nodes, an empty list is initialized so that the `next` field of
the header points to the trailer, and the `prev` field of the trailer points to the header; the remaining fields of the sentinels are irrelevant (presumably `None`, in Python). For a nonempty list, the header’s `next` will refer to a node containing the first real element of a sequence, just as the trailer’s `prev` references the node containing the last element of a sequence.

#### Advantages of Using Sentinels

Although we could implement a doubly linked list without sentinel nodes, the slight extra space devoted to the sentinels greatly simplifies the logic of our operations. Most notably, the header and trailer nodes never change—only the nodes between them change. Furthermore, we can treat all insertions in a unified manner, because a new node will always be placed between a pair of existing nodes. In similar fashion, every element that is to be deleted is guaranteed to be stored in a node that has neighbors on each side.

#### Inserting and Deleting with a Doubly Linked List

For contrast, look back at our [LinkedQueue](linked_queue.py) implementation. Its `enqueue` method, adds a new node to the end of the list. However, its implementation required a conditional to manage the special case of inserting into an empty list. In the general case, the new node was linked after the existing tail. But when adding to an empty list, there is no existing tail; instead it is necessary to reassign `self._head` to reference the new node. The use of a sentinel node in that implementation would eliminate the special case, as there would always be an existing node (possibly the header) before a new node.

Every insertion into our doubly linked list representation will take place between
a pair of existing nodes. For example, when a new element is inserted at the front of the sequence, we will simply add the new node between the header and the node that is currently after the header.

The deletion of a node proceeds in the opposite fashion of an insertion. The two neighbors of the node to be deleted are linked directly to each other, thereby bypassing the original node. As a result, that node will no longer be considered part of the list and it can be reclaimed by the system. Because of our use of sentinels, the same implementation can be used when deleting the first or the last element of a sequence, because even such an element will be stored at a node that lies between two others.

#### Basic Implementation of a Doubly Linked List

We begin by providing a preliminary implementation of a doubly linked list, in the
form of a class named `_DoublyLinkedBase`. We intentionally name the class with
a leading underscore because we do not intend for it to provide a coherent public
interface for general use. We will see that linked lists can support general insertions
and deletions in `O(1)` worst-case time, but only if the location of an operation can be succinctly identified. With array-based sequences, an integer index was a  convenient means for describing a position within a sequence. However, an index is not convenient for linked lists as there is no efficient way to find the jth element; it would seem to require a traversal of a portion of the list.

When working with a linked list, the most direct way to describe the location of an operation is by identifying a relevant node of the list. However, we prefer to encapsulate the inner workings of our data structure to avoid having users directly access nodes of a list. In the remainder of this subject, we will develop two public classes that inherit from our `_DoublyLinkedBase` class to provide more coherent abstractions. We provide a [LinkedDeque](linked_deque.py) class that implements the double-ended queue ADT that class only supports operations at the ends of the queue, so there is no need for a user to identify an interior position within the list and introduce a new [PositionalList](../List/PositionalList(ADT).py) abstraction that provides a public interface that allows arbitrary insertions and deletions from a list.

Our low-level `_DoublyLinkedBase` class relies on the use of a nonpublic `_Node` class that is similar to that for a singly linked list, as given in Code Fragment down there,
except that the doubly linked version includes a `_prev` attribute, in addition to the
`_next` and `_element` attributes, as shown below:

```python
class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'        # streamline memory
    def __init__(self, element, prev, next):        # initialize node’s fields
        self._element = element                     # user’s element
        self._prev = prev                           # previous node reference
        self._next = next                           # next node reference
```

The remainder of our `_DoublyLinkedBase` class is given in Code Fragment below. The constructor instantiates the two sentinel nodes and links them directly to each other. We maintain a `_size` member and provide public support for `__len__` and is empty so that these behaviors can be directly inherited by the subclasses.

```python
class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation """

    class _Node:
        """ Lightweight and nonpublic class for storing a doubly linked node """

        __slot__ = '_element', '_prev', '_next'                 # streamline memory usage

        def __init__(self, element, prev, next):
            """ Initialize node's fields """
            self._element = element                             # node's element
            self._prev = prev                                   # previous node reference
            self._next = next                                   # next node reference

    def __init__(self):
        """ Create an empty list """
        self._header = self._Node(None, None, None)             # header sentinel
        self._trailer = self._Node(None, None, None)            # trailer sentinels
        self._header._next = self._trailer                      # trailer is after heder
        self._trailer._prev = self._header                      # header is before trailer
        self._size = 0                                          # number of list elements

    def __len__(self):
        """ Return number of list elements """
        return self._size

    def is_empty(self):
        """ Return true if the list is empty """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """ Add an element between two existing nodes and return new node """
        newest = self._Node(e, predecessor, successor)          # linked to neighbors
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
        element = node._element                                 # record deleted element
        node._element = node._prev = node._next = None          # deprecated node
        return element                                          # return deleted element
```

The other two methods of our class are the nonpublic utilities, `_insert_between` and
`_delete_node`. These provide generic support for insertions and deletions, respectively, but require one or more node references as parameters. The implementation of the `_insert_between` method is modeled upon the algorithm that was previously portrayed in Code Fragment. It creates a new node, with that node’s fields initialized to link to the specified neighboring nodes. Then the fields of the neighboring nodes are updated to include the newest node in the list. For later convenience, the method returns a reference to the newly created node.

The implementation of the `_delete_node` method is modeled upon the algorithm portrayed in Code Fragment. The neighbors of the node to be deleted are linked directly
to each other, thereby bypassing the deleted node from the list. As a formality, we intentionally reset the `_prev`, `_next`, and `_element` fields of the deleted node to
`None` (after recording the element to be returned). Although the deleted node will be ignored by the rest of the list, setting its fields to None is advantageous as it may help Python’s garbage collection, since unnecessary links to the other nodes and the stored element are eliminated. We will also rely on this configuration to recognize a node as “deprecated” when it is no longer part of the list.

### Implementing a Deque with a Doubly Linked List

We provide an implementation of a `LinkedDeque` class [@Code Fragment](linked_deque.py)
that inherits from the `_DoublyLinkedBase` class of the preceding section. We do
not provide an explicit `__init__` method for the `LinkedDeque` class, as the inherited
version of that method suffices to initialize a new instance. We also rely on the
inherited methods `__len__` and is empty in meeting the deque ADT.

With the use of sentinels, the key to our implementation is to remember that the header does not store the first element of the deque—it is the node just *after* the
header that stores the first element (assuming the deque is non empty). Similarly,
the node just *before* the trailer stores the last element of the deque.

We use the inherited `_insert_between` method to insert at either end of the deque. To insert an element at the front of the deque, we place it immediately between the header and the node just after the header. An insertion at the end of deque is placed immediately before the trailer node. Note that these operations succeed, even when the deque is empty; in such a situation, the new node is placed between the two sentinels. When deleting an element from a nonempty deque, we rely upon the inherited `_delete_node` method, knowing that the designated node is assured to have neighbors on each side.
