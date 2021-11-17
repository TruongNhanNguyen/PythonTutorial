# Tree Traversal Algorithms

A ***traversal*** of a tree `T` is a systematic way of accessing, or "visiting" all the positions of `T`. The specific action associated with the "visit" of a position `p` depends on the application of this traversal, and could involve anything from incrementing a counter to performing some complex computation for `p`. In this section, we describe several common traversal schemes for trees, implement them in the con-
text of our various tree classes, and discuss several common applications of tree
traversals.

## Pre-order and Post-order Traversals of General Trees

### Post-order Traversal

In a ***pre-order traversal*** of a tree `T`, the root of `T` is visited first and then the subtrees rooted at its children are traversed recursively. If the tree is ordered, then the subtrees are traversed according to the order of the children. The pseudo-code
for the pre-order traversal of the subtree rooted at a position `p` is shown in **Code
Fragment** below

```python
Algorithm preorder(T, p):
    perform the “visit” action for position p
    for each child c in T.children(p) do
    preorder(T, c)                    {recursively traverse the subtree rooted at c}
```

### Pre-order Traversal

Another important tree traversal algorithm is the ***postorder traversal***. In some
sense, this algorithm can be viewed as the opposite of the preorder traversal, because it recursively traverses the subtrees rooted at the children of the root first, and
then visits the root (hence, the name "postorder"). Pseudo-code for the postorder
traversal is given in Code Fragment below

```python
Algorithm postorder(T, p):
    for each child c in T.children(p) do
        postorder(T, c)                 {recursively traverse the subtree rooted at c}
    perform the “visit” action for position p
```

🎯 **Running-Time Analysis**

Both preorder and postorder traversal algorithms are efficient ways to access all the
positions of a tree. The analysis of either of these traversal algorithms is similar to
that of algorithm `_height_subtree`, given in [Depth and Height](../README.md). At each
position `p`, the non recursive part of the traversal algorithm requires time `O(c_p +1)`, where `c_p` is the number of children of `p`, under the assumption that the "visit" itself takes `O(1)` time. By [Proposition 2](../README.md), the overall running time for the traversal of tree `T` is `O(n)`, where `n` is the number of positions in the tree. This running time is asymptotically optimal since the traversal must visit all the `n` positions of the tree.

## Breadth-First Tree Traversal

Although the preorder and postorder traversals are common ways of visiting the positions of a tree, another common approach is to traverse a tree so that we visit all the positions at depth `d` before we visit the positions at depth `d + 1`. Such an algorithm is known as a ***breadth-first traversal***.

Pseudo-code for a breadth-first traversal is given in **Code Fragment** below. The
process is not recursive, since we are not traversing entire subtrees at once. We use
a queue to produce a FIFO (i.e., first-in first-out) semantics for the order in which
we visit nodes. The overall running time is `O(n)`, due to the `n` calls to `enqueue` and
`n` calls to `dequeue`.

```python
Algorithm breadthfirst(T):
    Initialize queue Q to contain T.root()
    while Q not empty do
    p = Q.dequeue()                         {p is the oldest entry in the queue}
    perform the "visit" action for position p
    for each child c in T.children(p) do
        Q.enqueue(c)          {add p’s children to the end of the queue for later visits}
```

## Inorder Traversal of a Binary Tree

The standard preorder, postorder, and breadth-first traversals that were introduced for general trees, can be directly applied to binary trees. In this section, we introduce another common traversal algorithm specifically for a binary tree.

During an ***inorder traversal***, we visit a position between the recursive traversals of its left and right subtrees. The inorder traversal of a binary tree `T` can be informally viewed as visiting the nodes of `T` "from left to right". Indeed, for every
position `p`, the inorder traversal visits `p` after all the positions in the left subtree of `p` and before all the positions in the right subtree of `p`. Pseudo-code for the inorder traversal algorithm is given in **Code Fragment** below

```python
Algorithm inorder(p):
    if p has a left child lc then
        inorder(lc)              {recursively traverse the left subtree of p}
    perform the "visit" action for position p
    if p has a right child rc then
        inorder(rc)              {recursively traverse the right subtree of p}
```

The inorder traversal algorithm has several important applications. When using a binary tree to represent an arithmetic expression, the inorder traversal visits positions in a consistent order with the standard representation of the expression, as in `3+1×3/9−5+2...` (albeit without parentheses).

## Implementing Tree Traversals in Python

When first defining the tree ADT, we stated that tree `T` should include support for the following methods

- `T.positions()`: Generate an iteration of all *positions* of tree `T`.
- `iter(T)`: Generate an iteration of all *elements* stored within tree `T`.

At that time, we did not make any assumption about the order in which these iterations report their results. In this section, we demonstrate how any of the tree traversal algorithms we have introduced could be used to produce these iterations.

To begin, we note that it is easy to produce an iteration of all elements of a tree, if we rely on a presumed iteration of all positions. Therefore, support for the `iter(T)` syntax can be formally provided by a concrete implementation of the special method
`__iter__` within the abstract base class `Tree`. We rely on Python’s ***generator*** syntax as the mechanism for producing iterations. Our implementation of `Tree.__iter__`
is given in Code Fragment below

```python
def __iter__(self):
    """Generate an iteration of the tree's elements"""
    for p in self.positions():      # use same order as positions()
        yield p.element()           # but yield each element
```

To implement the positions method, we have a choice of tree traversal algorithms. Given that there are advantages to each of those traversal orders, we will provide independent implementations of each strategy that can be called directly by a user of our class. We can then trivially adapt one of those as a default order for the positions method of the tree ADT.

### Pre-order

We begin by considering the preorder traversal algorithm. We will support a public method with calling signature `T.preorder()` for tree `T`, which generates a preorder iteration of all positions within the tree. However, the recursive algorithm for generating a preorder traversal, must be parameterized by a specific position within the tree that serves as the root of a subtree to traverse. A standard solution for such a circumstance is to define a non public utility method with the desired recursive parameterization, and then to have the public method preorder invoke the nonpublic method upon the root of the tree.

Our implementation of such a design is given in **Code Fragment** below

```python
def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()):   # start recursion
            yield p

def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p                                         # visit p before its subtrees
    for c in self.children(p):                      # for each child c
        for other in self._subtree_preorder(c):     # do preorder of c’s subtree
            yield other                             # yielding each to our caller
```

Formally, both `preorder` and the utility `_subtree_preorder` are generators. Rather
than perform a "visit" action from within this code, we yield each position to the
caller and let the caller decide what action to perform at that position.

The `_subtree_preorder` method is the recursive one. However, because we are relying on generators rather than traditional functions, the recursion has a slightly different form. In order to yield all *positions* within the subtree of child `c`, we loop over the positions yielded by the recursive call `self._subtree_preorder(c)`, and re `yield` each position in the outer context. Note that if `p` is a leaf, the for loop over `self.children(p)` is trivial (this is the base case for our recursion).

We rely on a similar technique in the public preorder method to re-yield all positions that are generated by the recursive process starting at the root of the tree; if the tree is empty, nothing is yielded. At this point, we have provided full support for the preorder generator. A user of the class can therefore write code such as

```python
for p in T.preorder():
    # "visit" position p
```

The official tree ADT requires that all trees support a `positions` method as well. To
use a preorder traversal as the default order of iteration, we include the definition
shown in Code Fragment below within our `Tree` class. Rather than loop over the results returned by the preorder call, we return the entire iteration as an object.

```python
def position(self):
    """Generate an iteration of the tree's positions."""
    return self.preorder()          # return entire preorder iteration
```

### Post-order

We can implement a postorder traversal using very similar technique as with a
preorder traversal. The only difference is that within the recursive utility for a post-
order we wait to yield position `p` until *after* we have recursively yield the positions
in its subtrees. An implementation is given in **Code Fragment** below

```python
def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty():                         # start recursion
        for p in self._subtree_postorder(self.root()):
            yield p

def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in the tree rooted at position p"""
    for c in self.children(p):                      # for each child c
        for other in self._subtree_postorder(c):    # do postorder of c’s subtree
            yield other                             # yielding each to our caller
    yield p                                         # visit p after its subtrees
```

### Breadth-First Traversal

In **Code Fragment** below, we provide an implementation of the breadth-first traversal
algorithm in the context of our Tree class. Recall that the breadth-first traversal
algorithm is not recursive; it relies on a queue of positions to manage the traversal process

```python
def breadthfirst(self):
    """Generate a breath first iteration of positions in the tree."""
    if not self.is_empty():
        fringe = LinkedQueue()              # known positions not yet yielded
        fringe.enqueue(self.root())         # starting with the root
        while not fringe.is_empty():
            p = fringe.dequeue()            # remove from front of the queue
            yield p                         # report this position
            for c in self.children(p):
                fringe.enqueue(c)           # add children to back of queue
```

### Inorder Traversal for Binary Trees

The preorder, postorder, and breadth-first traversal algorithms are applicable to all trees, and so we include their implementations within the `Tree` abstract base class. Those methods are inherited by the abstract `BinaryTree` class, the concrete `LinkedBinaryTree` class, and any other dependent tree classes we might develop.

The inorder traversal algorithm, because it explicitly relies on the notion of a
left and right child of a node, only applies to binary trees. We therefore include its
definition within the body of the `BinaryTree` class. We use a similar technique to
implement an inorder traversal (**Code Fragmen**t below) as we did with preorder and
postorder traversals.

```python
def inorder(self):
    """Generate an inorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p

def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in the tree rooted at position p."""
    if self.left(p) is not None:            # if left child exists, traverse its subtree
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p                                 # visit p between its subtrees
    if self.right(p) is not None:
        for other in self._subtree_inorder(self.right(p)):
            yield other                     # if right child exists, traverse its subtree
```

For many applications of binary trees, an inorder traversal provides a natural iteration. We could make it the default for the `BinaryTree` class by overriding the
positions method that was inherited from the `Tree` class (see **Code Fragment** below)

```python
def positions(self):
    """Generate an an iteration of tree's positions."""
    return self.inorder()       # make inorder the default
```
