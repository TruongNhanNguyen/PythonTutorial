# Implementing Trees

The `Tree` and `BinaryTree` classes that we have defined thus far in [Tree](../README.md) and [Binary Tree](BinaryTree.md) are both formally ***abstract base classes***. Although they provide a great deal of support, neither of them can be directly instantiated. We have not yet defined key implementation details for how a tree will be represented internally, and how we can effectively navigate between parents and children. Specifically, a concrete implementation of a tree must provide methods `root`, `parent`, `num_children`, `children`, `__len__`, and in the case of `BinaryTree`, the additional accessors `left` and `right`.

There are several choices for the internal representation of trees. We describe the most common representations in this section. We begin with the case of a ***binary tree***, since its shape is more narrowly defined.

## Linked Structure for Binary Trees

A natural way to realize a binary tree T is to use a ***linked structure***, with a node that maintains references to the element stored at a position `p` and to the nodes associated with the children and parent of `p`. If `p` is the `root` of `T`, then the parent field of `p` is `None`. Likewise, if `p` does not have a left child respectively, right child), the associated field is `None`. The tree itself maintains an instance variable storing a reference to the root node (if any), and a variable, called `size`, that represents the overall number of nodes of `T`

### Python Implementation of a Linked Binary Tree Structure

In this section, we define a concrete `LinkedBinaryTree` class that implements the binary tree ADT by sub-classing the `BinaryTree` class. Our general approach is very similar to what we used when developing the `PositionalList` in [here](../../List/README.md). We define a simple, nonpublic `_Node` class to represent a node, and a public `Position` class that wraps a node. We provide a `_validate` utility for robustly checking the validity of a given position instance when unwrapping it, and a `_make_position` utility for wrapping a node as a position to return to a caller.

As a formality, the new `Position` class is declared to inherit immediately from `BinaryTree.Position`. Technically, the `BinaryTree` class definition, does not formally
declare such a nested class; it trivially inherits it from `Tree.Position`. A minor benefit from this design is that our position class inherits the `__ne__` special method
so that syntax `p != q` is derived appropriately relative to `__eq__`.

Our class definition continues, with a constructor and with concrete implementations for the methods that remain abstract in the `Tree` and `BinaryTree` classes. The constructor creates an empty tree by initializing `_root` to `None` and `_size` to zero. These  accessor methods are implemented with careful use of the `_validate` and `_make_position` utilities to safeguard against boundary cases.

### Operations for Updating a Linked Binary Tree

Thus far, we have provided functionality for examining an existing binary tree. However, the constructor for our `LinkedBinaryTree` class results in an empty tree and we have not provided any means for changing the structure or content of a tree.

We chose not to declare update methods as part of the `Tree` or `BinaryTree` *abstract* base classes for several reasons. First, although the principle of *encapsulation* suggests that the outward behaviors of a class need not depend on the internal representation, the *efficiency* of the operations depends greatly upon the representation. We prefer to have each concrete implementation of a tree class offer the most suitable options for updating a tree.

The second reason we do not provide update methods in the base class is that we may not want such update methods to be part of a public interface. There are many applications of trees, and some forms of update operations that are suitable for one application may be unacceptable in another. However, if we place an update method in a base class, any class that inherits from that base will inherit the update method.

✅ **Consider**, for example, the possibility of a method `T.replace(p, e)` that
replaces the element stored at position `p` with another element `e`. Such a general
method may be unacceptable in the context of an ***arithmetic expression tree***, because we may want to enforce that internal nodes store only operators as elements.

For linked binary trees, a reasonable set of update methods to support for genneral usage are the following

- `T.add_root(e)`: Create a root for an empty tree, storing `e` as the element, and return the position of that root; an error occurs if the tree is not empty.
- `T.add_left(p, e)`: Create a new node storing element `e`, link the node as the left child of position `p`, and return the resulting position; an error occurs if `p` already has a left child.
- `T.add_right(p, e)`: Create a new node storing element `e`, link the node as the right child of position `p`, and return the resulting position; an error occurs if `p` already has a right child.
- `T.replace(p, e)`: Replace the element stored at position `p` with element `e`, and return the previously stored element.
- `T.delete(p)`: Remove the node at position `p`, replacing it with its child, if any, and return the element that had been stored at `p`; an error occurs if `p` has two children.
- `T.attach(p, T1, T2)`: Attach the internal structure of trees `T1` and `T2`, respectively, as the left and right subtrees of leaf position `p` of `T`, and reset `T1` and `T2` to empty trees; an error condition occurs if `p` is not a leaf.

We have specifically chosen this collection of operations because each can be implemented in `O(1)` worst-case time with our linked representation. The most complex of these are delete and attach, due to the case analyses involving the various parent-child relationships and boundary conditions, yet there remains only a constant number of operations to perform.

To avoid the problem of undesirable update methods being inherited by subclasses of `LinkedBinaryTree`, we have chosen an implementation in which none of the above methods are publicly supported. Instead, we provide nonpublic versions of each, for example, providing the underscored `_delete` in lieu of a public `delete`.

### Performance of the Linked Binary Tree Implementation

🎯 To summarize the efficiencies of the linked structure representation, we analyze the
running times of the LinkedBinaryTree methods, including derived methods that
are inherited from the Tree and BinaryTree classes

- [x] The `len` method, implemented in `LinkedBinaryTree`, uses an instance variable storing the number of nodes of `T` and takes `O(1)` time. Method `is_empty`, inherited from `Tree`, relies on a single call to `len` and thus takes `O(1)` time.
- [x] The accessor methods `root`, `left`, `right`, `parent`, and `num_children` are implemented directly in `LinkedBinaryTree` and take `O(1)` time. The `sibling` and `children` methods are derived in `BinaryTree` based on a constant number of calls to these other accessors, so they run in `O(1)` time as well.
- [x] The `is_root` and `is_leaf` methods, from the `Tree` class, both run in `O(1)` time, as `is_root` calls root and then relies on equivalence testing of positions, while `is_leaf` calls `left` and `right` and verifies that `None` is returned by both.
- [x] Methods `depth` and `height` were each analyzed in [Section Depth and Height](../README.md). The `depth` method at position `p` runs in `O(d_p +1)` time where `d_p` is its depth; the `height` method on the root of the tree runs in `O(n)` time.
- [x] The various update methods `add_root`, `add_left`, `add_right`, `replace`, `delete`, and `attach` (that is, their nonpublic implementations) each run in `O(1)` time, as they involve relinking only a constant number of nodes per operation.

Summary table 📑

| **Operation** | **Running Time** |
| --- | --- |
| `len`, `is_empty` | `O(1)` |
| `root`, `parent`, `left`, `right`, `sibling`, `children`, `num_children` | `O(1)` |
| `is_root`, `is_leaf` | `O(1)` |
| `depth(p)` | `O(d_p + 1)` |
| `height` | `O(n)` |
| `add_root`, `add_left`, `add_right`, `replace`, `delete`, `attach` | `O(1)` |

## Linked Structure for General Trees

When representing a binary tree with a linked structure, each node explicitly maintains fields `left` and `right` as references to individual children. For a general tree, there is no a priori limit on the number of children that a node may have. A natural
way to realize a general tree `T` as a linked structure is to have each node store a single *container* of references to its children. For example, a `children` field of a
node can be a Python list of references to the children of the node (if any).

Summarizes the performance of the implementation of a general tree using a linked structure 📑

| **Operation** | **Running Time** |
| --- | --- |
| `len`, `is_empty` | `O(1)` |
| `root`, `parent`, `is_root`, `is_leaf` | `O(1)` |
| `children` | `O(c_p + 1)`|
| `depth(p)` | `O(d_p + 1)` |
| `height` | `O(n)` |

🗒 We let c_p denote the number of children of a position `p`. The space usage is `O(n)`
