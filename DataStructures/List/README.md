# The Positional List ADT

## Abstraction

The abstract data types that I have considered thus far in this repository, namely **stacks**, **queues**, and **double-ended queues**, only allow update operations that occur at one end of a sequence or the other. We wish to have a more general abstraction. For example, although we motivated the **FIFO** semantics of a queue as a model for customers who are waiting to speak with a customer service representative, or fans who are waiting in line to buy tickets to a show, the queue ADT is too limiting. What if a waiting customer decides to hang up before reaching the front of the customer service queue? Or what if someone who is waiting in line to buy tickets allows a friend to “cut” into line at that position? We would like to design an abstract data type that provides a user a way to refer to elements anywhere in a sequence, and to perform arbitrary insertions and deletions.

When working with **array-based sequences** (such as a ***Python list***), integer indices provide an excellent means for describing the location of an element, or the
location at which an insertion or deletion should take place. However, numeric indices are not a good choice for describing positions within a linked list because we cannot efficiently access an entry knowing only its index; finding an element at a given index within a linked list requires traversing the list incrementally from its beginning or end, counting elements as we go.

Furthermore, indices are not a good abstraction for describing a local position in some applications, because the index of an entry changes over time due to insertions or deletions that happen earlier in the sequence.

## A Node Reference as a Position?

One of the great benefits of a linked list structure is that it is possible to perform
`O(1)-time` insertions and deletions at arbitrary positions of the list, as long as we
are given a reference to a relevant node of the list. It is therefore very tempting to
develop an ADT in which a node reference serves as the mechanism for describing a position. In fact, our `_DoublyLinkedBase` class (see [here](PositionalList(ADT).py)) has methods `_insert_between` and `_delete_node` that accept node references as parameters.

However, such direct use of nodes would violate the **object-oriented design principles** of **abstraction** and **encapsulation**. There are several reasons to prefer that we encapsulate the nodes of a linked list, for both our sake and for the benefit of users of our abstraction.

- [x] It will be simpler for users of our data structure if they are not bothered with unnecessary details of our implementation, such as low-level manipulation of nodes, or our reliance on the use of sentinel nodes. Notice that to use the `_insert_between` method of our `_DoublyLinkedBase` class to add a node at the beginning of a sequence, the header sentinel must be sent as a parameter.
- [x] We can provide a more robust data structure if we do not permit users to directly access or manipulate the nodes. In that way, we ensure that users cannot invalidate the consistency of a list by mismanaging the linking of nodes. A more subtle problem arises if a user were allowed to call the `_insert_between` or `_delete_node` method of our `_DoublyLinkedBase` class, sending a node that does not belong to the given list as a parameter.
- [x] By better encapsulating the internal details of our implementation, we have greater flexibility to redesign the data structure and improve its performance. In fact, with a well-designed abstraction, we can provide a notion of a non numeric position, even if using an array-based sequence.

For these reasons, instead of relying directly on nodes, we introduce an independent position abstraction to denote the location of an element within a list, and then a complete positional list ADT that can encapsulate a doubly linked list.

## The Positional List Abstract Data Type

To provide for a general abstraction of a sequence of elements with the ability to
identify the location of an element, we define a ***positional list ADT*** as well as a
simpler ***position*** abstract data type to describe a location within a list. A position acts as a marker or token within the broader positional list. A position *p* is unaffected by changes elsewhere in a list; the only way in which a position becomes
invalid is if an explicit command is issued to delete it.

A position instance is a simple object, supporting only the following method

- `p.element()`: Return the element stored at position `p`.

In the context of the positional list ADT, positions serve as parameters to some
methods and as return values from other methods. In describing the behaviors of a
positional list, we being by presenting the accessor methods supported by a list `L`

- `L.first()`: Return the position of the first element of L, or `None` if `L` is empty.
- `L.last()`: Return the position of the last element of L, or `None` if `L` is empty.
- `L.before(p)`: Return the position of `L` immediately before position `p`, or `None` if `p` is the first position.
- `L.after(p)`: Return the position of `L` immediately after position `p`, or `None` if `p` is the last position.
- `L.is_empty()`: Return `True` if list `L` does not contain any elements.
- `len(L)`: Return the number of elements in the list.
- `iter(L)`: Return a forward iterator for the *elements* of the list

The positional list ADT also includes the following ***update*** methods

- `L.add_first(e)`: Insert a new element `e` at the front of `L`, returning the position of the new element.
- `L.add_last(e)`: Insert a new element `e` at the back of `L`, returning the position of the new element.
- `L.add_before(p, e)`: Insert a new element `e` just before position `p` in `L`, returning the position of the new element.
- `L.add_after(p, e)`: Insert a new element `e` just after position `p` in `L`, returning the position of the new element.
- `L.replace(p, e)`: Replace the element at position `p` with `e`
- `L.delete(p)`: Remove and return the element at position `p` in `L`, invalidating the position

For those methods of the ADT that accept a position p as a parameter, an error
occurs if `p` is not a valid position for list `L`.

Note well that the `first()` and `last()` methods of the positional list ADT return
the associated positions, not the elements. The first element of a positional list
can be determined by subsequently invoking the element method on that position,
as `L.first().element()`. The advantage of receiving a position as a return value is
that we can use that position to navigate the list. For example, the following code
fragment prints all elements of a positional list named data.

```python
cursor = data.first()
while cursor is not None:
    print(cursor.element())         # print the element stored at the position
    cursor = data.after(cursor)     # advance to the next position (if any)
```

This code relies on the stated convention that the None object is returned when after is called upon the last position. That return value is clearly distinguishable from any legitimate position. The positional list ADT similarly indicates that the None value is returned when the before method is invoked at the front of the list, or
when first or last methods are called upon an empty list. Therefore, the above code
fragment works correctly even if the data list is empty.

Because the ADT includes support for **Python’s** `iter` function, users may rely on the traditional `for-loop` syntax for such a forward traversal of a list named `data`.

```python
for e in data:
    print(e)
```

More general navigational and update methods of the positional list ADT are shown
in the following table

| **Operation** | **Return Values** | `L` |
| --- | --- | --- |
| `L.add_last(8)` | p | 8_p |
| `L.first()` | p | 8_p |
| `L.add_after(p, 5)` | q | 8_p, 5_q |
| `L.before(q)` | p | 8_p, 5_q |
| `L.add_before(q, 3)` | r | 8p, 3r, 5q |
| `r.element()` | 3 | 8p, 3r, 5q |
| `L.after(p)` | r | 8p, 3r, 5q |
| `L.before(p)` | `None` | 8p, 3r, 5q |
| `L.add_first(9)` | s | 9s, 8p, 3r, 5q |
| `L.delete(L.last())` | 5 | 9s, 8p, 3r |
| `L.replace(p, 7)` | 8 | 9s, 7p, 3r |

## Doubly Linked List Implementation

We present a complete implementation of a PositionalList class using a doubly linked list that satisfies the following important proposition.

We rely on the `_DoublyLinkedBase` class for our low-level representation; the primary responsibility of our new class is to provide a public interface in accordance with the positional list ADT. We begin our class definition with the definition of the public `Position` class, nested within our `PositionalList` class. Position instances will be used to represent the locations of elements within the list. Our various `PositionalList` methods may end up creating redundant Position instances that reference the same underlying node (for example, when `first` and `last` are the same). For that reason, our Position class defines the `__eq__` and `__ne__` special methods so that a test such as `p == q` evaluates to `True` when two positions refer to the same node.

### Validating Positions

Each time a method of the `PositionalList` class accepts a position as a parameter,
we want to verify that the position is valid, and if so, to determine the underlying
node associated with the position. This functionality is implemented by a nonpublic method named `_validate`. Internally, a position maintains a reference to the associated node of the linked list, and also a reference to the list instance that contains the specified node. With the container reference, we can robustly detect when
a caller sends a position instance that does not belong to the indicated list.

We are also able to detect a position instance that belongs to the list, but that
refers to a node that is no longer part of that list. Recall that the `_delete_node` of
the base class sets the previous and next references of a deleted node to `None`; we
can recognize that condition to detect a deprecated node.

### Access and Update Methods

The access methods of the `PositionalList` class and the update methods are given [here](PositionalList(ADT).py). All of these methods trivially adapt the underlying doubly linked list implementation to support the public interface of the positional list ADT. Those methods rely on the validate utility to “unwrap” any position that is sent. They also rely on a make position utility to “wrap” nodes as Position instances to return to the user, making sure never to return a position referencing a sentinel. For convenience, we have overridden the inherited `_insert_between` utility method so that ours returns a *position* associated with the newly created node (whereas the inherited version returns the node itself).

## Sorting a Positional List

We introduced the ***insertion-sort*** algorithm, in the context of an array-based sequence (see [here](../../Algorithms/Sorting%20Algorithms.py)). In this section, we develop an implementation that operates
on a PositionalList, relying on the same high-level algorithm in which each element
is placed relative to a growing collection of previously sorted elements.

We maintain a variable named `marker` that represents the rightmost position of
the currently sorted portion of a list. During each pass, we consider the position just
past the marker as the `pivot` and consider where the `pivot’s element` belongs relative to the sorted portion; we use another variable, named `walk`, to move leftward from the marker, as long as there remains a preceding element with value larger than the pivot’s.

Code Sample:

```python
def insertion_sort(L):
    """Sort PositionalList of comparable elements into non decreasing order."""
    if len(L) > 1:                           # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)          # next item to place
            value = pivot.element()
            if value > marker.element():     # pivot is already sorted
                marker = pivot               # pivot becomes new marker
            else:                            # must relocate pivot
                walk = marker                # find leftmost item greater than value
                while walk != L.first( ) and L.before(walk).element( ) > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)    # reinsert value before walk
```

## Case Study: Maintaining Access Frequencies @Favorite List
