# Trees

## General Trees

Tree structures are indeed a breakthrough in data organization, for they allow us to implement a host of algorithms much faster than when using linear data structures, such as array-based lists or linked lists. Trees also provide a natural organization for data, and consequently have become ubiquitous structures in file systems, graphical user interfaces, databases, Web sites, and other computer systems.

### Tree Definitions and Properties

A ***tree*** is an abstract data type that stores elements hierarchically. With the exception of the top element, each element in a tree has a ***parent*** element and zero or more ***children*** elements. A tree is usually visualized by placing elements inside ovals or rectangles, and by drawing the connections between parents and children
with straight lines. We typically call the top element the ***root*** of the tree, but it is drawn as the highest element.

#### Formal Tree Definition

Formally, we define a ***tree*** `T` as a set of ***nodes*** storing elements such that the nodes have a ***parent-child*** relationship that satisfies the following properties

- If `T` is nonempty, it has a special node, called the ***root*** of `T`, that has no parent.
- Each node `v` of `T` different from the root has a unique ***parent*** node `w`; every node with parent `w` is a ***child*** of `w`.

Note that according to our definition, a tree can be empty, meaning that it does not
have any nodes. This convention also allows us to define a tree recursively such
that a tree `T` is either empty or consists of a node `r`, called the root of `T`, and a (possibly empty) set of subtrees whose roots are the children of `r`.

#### Other Node Relationships

Two nodes that are children of the same parent are *siblings*. A node `v` is external if `v` has no children. A node `v` is ***internal*** if it has one or more children. ***External*** nodes are also known as ***leaves***.

A node `u` is an ***ancestor*** of a node `v` if `u = v` or `u` is an ancestor of the parent of `v`. Conversely, we say that a node `v` is a ***descendant*** of a node `u`  if `u` is an ancestor of `v`.

#### Edge and Path in Trees

An ***edge*** of tree `T` is a pair of nodes `(u,v)` such that `u` is the parent of `v`, or vice versa. A ***path*** of `T` is a sequence of nodes such that any two consecutive nodes in the sequence form an edge.

#### Ordered Trees

A tree is ***ordered*** if there is a meaningful linear order among the children of each node; that is, we purposefully identify the children of a node as being the first,
second, third, and so on. Such an order is usually visualized by arranging siblings
left to right, according to their order.

- [x] Examples:
  - The components of a structured document, such as a book, are hierarchically organized as a tree whose internal nodes are parts, chapters, and sections, and whose leaves are paragraphs, tables, figures, and so on.
  - A family tree that describes generational relationships is often modeled as an ordered tree, with siblings ordered according to their birth.

### The Tree Abstract Data Type

As we did with [positional lists](../List/README.md), we define a tree ADT using the
concept of a ***position*** as an abstraction for a node of a tree. An element is stored at each position, and positions satisfy parent-child relationships that define the tree structure. A position object for a tree supports the method

- `p.element()`: Return the element stored at position p.

The tree ADT then supports the following ***accessor methods***, allowing a user to
navigate the various positions of a tree

- `T.root()`: Return the position of the ***root*** of tree `T`, or `None` if `T` is empty.
- `T.is_root(p)`: Return `True` if position `p` is the `root` of Tree `T`.
- `T.parent(p)`: Return the position of the parent of position `p`, or `None` if `p` is the root of `T`.
- `T.num_children(p)`: Return the number of children of position `p`.
- `T.children(p)`: Generate an iteration of the children of position `p`.
- `T.is_leaf(p)`: Return `True` if position `p` does not have any children.
- `len(T)`: Return the number of positions (and hence elements) that are contained in tree `T`.
- `T.is_empty()`: Return `True` if tree `T` does not contain any positions.
- `T.positions()`: Generate an iteration of all *positions* of tree `T`.
- `iter(T)`: Generate an iteration of all *elements* stored within tree `T`.

Any of the above methods that accepts a position as an argument should generate a
`ValueError` if that position is invalid for `T`.

If a tree `T` is ordered, then `T.children(p)` reports the children of `p` in the natural order. If `p` is a leaf, then `T.children(p)` generates an empty iteration. In similar regard, if tree `T` is empty, then both `T.positions()` and `iter(T)` generate empty iterations. We will discuss general means for iterating through all positions of a tree in [Traversal Algorithms](#tree-traversal-algorithms)

We do not define any methods for creating or modifying trees at this point. We prefer to describe different tree update methods in conjunction with specific implementations of the tree interface, and specific applications of trees.

#### A Tree Abstract Base Class Class in Python

We noted that a public interface for an abstract data type is often managed in Python via ***duck typing***. A more formal mechanism to designate the relationships between different implementations of the same abstraction is through the definition of one class that serves as an ***abstract base class***, via inheritance, for one or more ***concrete classes***.

We choose to define a `Tree` class, that serves as an abstract base class corresponding to the tree ADT. Our reason for doing so is that there is quite a bit of useful code that we can provide, even at this level of abstraction, allowing greater code reuse in the concrete tree implementations we later define. The `Tree` class  provides a definition of a nested `Position` class (which is also abstract), and declarations of many of the accessor methods included in the tree ADT.

However, our `Tree` class does not define any internal representation for storing a tree, and five of the methods given in the code fragment remain ***abstract*** (`root`, `parent`, `num_children`, `children`, and `__len__`); each of these methods raises a
`NotImplementedError`. (A more formal approach for defining abstract base classes
and abstract methods, using Python’s `abc` module) The subclasses are responsible for overriding abstract methods, such as children, to provide a working implementation for each behavior, based on their chosen internal representation.

Although the `Tree` class is an abstract base class, it includes several ***concrete***
methods with implementations that rely on calls to the abstract methods of the class.
In defining the tree ADT in the previous section, we declare ten accessor methods. Five of those are the ones we left as abstract, the other five can be implemented based on the former. We provides concrete implementations for methods `is_root`, `is_leaf`, and `is_empty`. In [Tree Traversal Algorithms](#tree-traversal-algorithms), we will
explore general algorithms for traversing a tree that can be used to provide concrete
implementations of the positions and `__iter__` methods within the `Tree` class. The
beauty of this design is that the concrete methods defined within the Tree abstract
base class will be inherited by all subclasses. This promotes greater code reuse, as
there will be no need for those subclasses to re-implement such behaviors.

We note that, with the `Tree` class being abstract, there is no reason to create a
direct instance of it, nor would such an instance be useful. The class exists to serve
as a base for inheritance, and users will create instances of concrete subclasses.

### Computing Depth and Height

#### Depth

Let `p` be the position of a node of a tree `T`. The depth of `p` is the number of
ancestors of `p`, excluding `p` itself. Note that this definition implies that the depth of the `root` of `T` is 0. The depth of `p` can also be recursively defined as follows:

- If `p` is the root, then the depth of `p` is 0.
- Otherwise, the depth of `p` is one plus the depth of the parent of `p`.

Based on this definition, we present a simple, recursive algorithm, `depth`, in Code
Fragment below, for computing the depth of a position `p` in Tree `T`. This method calls
itself recursively on the parent of `p`, and adds 1 to the value returned.

```python
def depth(self, p):
    """Return the number of levels separating Position p from the root"""
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))
```

The running time of `T.depth(p)` for position `p` is `O(dp +1)`, where `d_p` denotes
the depth of `p` in the tree `T`, because the algorithm performs a constant-time recursive step for each ancestor of `p`. Thus, algorithm `T.depth(p)` runs in `O(n)` worst-case time, where `n` is the total number of positions of `T`, because a position of `T` may have depth `n − 1` if all nodes form a single branch. Although such a running
time is a function of the input size, it is more informative to characterize the running
time in terms of the parameter `d_p`, as this parameter may be much smaller than `n`.

#### Height

The height of a position `p` in a tree `T` is also defined recursively:

- If `p` is a leaf, then the height of `p` is 0.
- Otherwise, the height of `p` is one more than the maximum of the heights of `p`'s children.

The height of a nonempty tree `T` is the height of the root of `T`. In addition, height can also be viewed as follows.

> **Proposition 1**: The height of a nonempty tree `T` is equal to the maximum of the depths of its leaf positions.
>
> **Proposition 2**: Let `T` be a tree with `n` positions, and let `c_p` denote the number of children of a position `p` of `T`. Then, summing over the positions of `T`, $\Sigma_p c_p = n−1$.

We leave the justification of this fact here.

We can compute the height of a tree efficiently, in `O(n)` worst-case time,
by relying instead on the original recursive definition. To do this, we will parameterize a function based on a position within the tree, and calculate the height of
the subtree rooted at that position. Algorithm `_height_subtree`, shown as nonpublic method `_height_subtree`, computes the height of tree `T` in this way.

```python
def _height_subtree(self, p):
    """Return the height of the subtree rooted at Position p"""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height_subtree(c) for c in self.children(p))
```

Revisiting the public interface for our `Tree` class, the ability to compute heights
of subtrees is beneficial, but a user might expect to be able to compute the height
of the entire tree without explicitly designating the tree root. We can wrap the non-
public `_height_subtree` in our implementation with a public `height` method that provides a default interpretation when invoked on tree `T` with syntax `T.height()`. Such an implementation is given in Code Fragment down there:

```python
def height(self, p=None):
    """Return the height of the subtree rooted at Position p.
    If p is None, return the height of the entire tree."""
    if p is None:
        p = self.root()
    else:
        return self._height_subtree(p)
```

## Binary Tree

See instructions at [Binary Tree](Instructions/BinaryTree.md)

## Implementing Tree

See instructions at [Implementing Tree](Instructions/ImplementingTree.md)

## Tree Traversal Algorithms

See instructions at [Tree Traversal Algos](Instructions/TreeTraversalAlgos.md)
