# Binary Trees

A ***binary tree*** is an ordered tree with the following properties

- Every node has at most two children.
- Each child node is labeled as being either a ***left child*** or a ***right child***.
- A left child precedes a right child in the order of children of a node.

The subtree rooted at a left or right child of an internal node `v` is called a ***left subtree*** or ***right subtree***, respectively, of `v`. A binary tree is ***proper*** if each node has either zero or two children. Some people also refer to such trees as being ***full*** binary trees. Thus, in a proper binary tree, every internal node has exactly two children. A binary tree that is not proper is ***improper***.

🎯 **A Recursive Binary Tree Definition**
Incidentally, we can also define a binary tree in a recursive way such that a binary
tree is either empty or consists of

- A node `r`, called the root of `T`, that stores an element.
- A binary tree (possibly empty), called the left subtree of `T`.
- A binary tree (possibly empty), called the right subtree of `T`.

## The Binary Tree Abstract Data Type

As an abstract data type, a binary tree is a specialization of a tree that supports three
additional accessor methods

- `T.left(p)`: Return the position that represents the left child of `p`, or `None` if `p` has no left child.
- `T.right(p)`: Return the position that represents the right child of `p`, or `None` if `p` has no right child.
- `T.sibling(p)`: Return the position that represents the sibling of `p`, or `None` if `p` has no sibling.

We do not define specialized update methods for binary trees here. Instead, we will consider some possible update methods when we describe specific implementations and applications of binary trees.

### The BinaryTree Abstract Base Class in Python

Just as `Tree` was defined as an abstract base class in [Tree](../README.md), we define a
new `BinaryTree` class associated with the binary tree ADT. We rely on inheritance to define the `BinaryTree` class based upon the existing `Tree` class. However, our `BinaryTree` class remains *abstract*, as we still do not provide complete specifications for how such a structure will be represented internally, nor implementations for some necessary behaviors.

By using inheritance, a binary tree supports all the functionality that was defined for general trees (e.g., `parent`, `is_leaf`, `root`). Our new class also inherits the
nested `Position` class that was originally defined within the `Tree` class definition.
In addition, the new class provides declarations for new abstract methods `left` and
`right` that should be supported by concrete subclasses of `BinaryTree`.

Our new class also provides two concrete implementations of methods. The new `sibling` method is derived from the combination of `left`, `right`, and `parent`. Typically, we identify the sibling of a position `p` as the “other” child of `p`’s parent. However, if `p` is the root, it has no parent, and thus no sibling. Also, `p` may be the only child of its parent, and thus does not have a sibling.

Finally, we provides a concrete implementation of the `children` method; this method is abstract in the `Tree` class. Although we have still not specified how the children of a node will be stored, we derive a generator for the ordered children based upon the implied behavior of abstract methods `left` and `right`.

### Properties of Binary Trees

May be updated later 😎
