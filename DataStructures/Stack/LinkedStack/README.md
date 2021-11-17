# Stack

## Implementing a Stack with a Singly Linked List

We demonstrate use of a singly linked list by providing a complete Python implementation of the stack ADT. In designing such an implementation, we need to decide whether to model the top of the stack at the head or at the tail of the list. There is clearly a best choice here; we can efficiently insert and delete elements in constant time only at the head. Since all stack operations affect the top, we orient the top of the stack at the head of our list.

To represent individual nodes of the list, we develop a lightweight **`Node`** class.
This class will never be directly exposed to the user of our stack class, so we will formally define it as a nonpublic, nested class of our eventual **LinkedStack** class. The definition of the **`Node`** class is shown in Code Fragment below:

```Python
class _Node:
    """ Lightweight, nonpublic class for storing a singly linked node. """
    __slots__ = '_element', '_next'  # streamline memory usage

    def __init__(self, element, next):
        """ Initialize node's fields. """
        self._element = element   # reference to user's element
        self._next = next # reference to next node
```

A node has only two instance variables: **`_element`** and **`_next`**. We intentionally
define **`__slots__`** to streamline the memory usage, because there may potentially be many node instances in a single list. The constructor of the
**`_Node`** class is designed for our convenience, allowing us to specify initial values for both fields of a newly created node.

A complete implementation of our LinkedStack class is given **[here](https://github.com/TruongNhanNguyen/PythonBasic/blob/main/DataStructures/Stack/stack(linked_version).py)**. Each stack instance maintains two variables. The
**`_head`** member is a reference to the node at the head of the list (or **`None`**, if the stack is empty). We keep track of the current number of elements with the **`_size`** instance variable,
for otherwise we would be forced to traverse the entire list to count the number of elements when reporting the size of the stack.

The implementation of **`push`** essentially mirrors the pseudo-code for insertion at the head of a singly linked list. When we push a new element **`e`** onto the stack, we accomplish the necessary changes to the linked structure by invoking the constructor of the **`_Node`** class as follows:

```Python
self._head = self._Node(e, self._head)  # create and link a new node
```

Note that the **`_next`** field of the new node is set to the existing top node, and then **`self._head`** is reassigned to the new node.

When implementing the **`top`** method, the goal is to return the element that is at the top of the stack. When the stack is empty, we raise an **`Empty exception`**, as originally defined in **[ArrayBasedStack](https://github.com/TruongNhanNguyen/PythonBasic/blob/main/DataStructures/Stack/stack.py)** implementation.
When the stack is nonempty, **`self._head`** is a reference to the first node of the linked list. The top element can be identified as **`self._head._element`**.

In the implementation of pop, we maintain a local reference to the element that is stored at the node that is being removed, and we return that element to the caller of pop.

## Analyzing the Linked-Based Stack Implementation

The analysis of our LinkedStack operations is given in Table below. We see that all of the methods complete in worst-case constant time `O(1)`.

| **Operation** | **Running Time** |
| --- | --- |
| **`S.push(e)`** | **`O(1)`** |
| **`S.pop()`** | **`O(1)`** |
| **`S.top()`** | **`O(1)`** |
| **`len(S)`** | **`O(1)`** |
| **`S.is_empty()`** | **`O(1)`** |
