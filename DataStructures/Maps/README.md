# Maps and Hash Tables

## Maps and Dictionaries

Python’s **dict** class is arguably the most significant data structure in the language. It represents an abstraction known as a ***dictionary*** in which unique ***keys*** are mapped to associated ***values***. Because of the relationship they express between keys and values, dictionaries are commonly known as ***associative array***s or ***maps***. We use the term *dictionary* when specifically discussing Python’s `dict` class, and the term `map` when discussing the more general notion of the abstract data type.

A map from the names of countries to their associated units of currency is a simple example.

We note that the keys (the country names) are assumed to be unique, but the values
(the currency units) are not necessarily unique. For example, we note that Spain and Greece both use the euro for currency. Maps use an array-like syntax for indexing, such as `currency['Greece']` to access a value associated with a given key or `currency['Greece'] = 'Drachma'` to remap it to a new value. Unlike a standard array, indices for a map need not be consecutive nor even numeric. Common applications of maps include the following

- A university’s information system relies on some form of a student ID as a key that is mapped to that student’s associated record (such as the student’s name, address, and course grades) serving as the value.
- The domain-name system (**DNS**) maps a host name, such as [www.wiley.com](https://www.wiley.com), to an Internet-Protocol (**IP**) address, such as `208.215.179.146`.
- A social media site typically relies on a (nonnumeric) username as a key that can be efficiently mapped to a particular user’s associated information.
- A computer graphics system may map a color name, such as 'turquoise', to the triple of numbers that describes the color’s RGB (red-green-blue) representation, such as `(64,224,208)`
- Python uses a dictionary to represent each namespace, mapping an identifying string, such as `pi` , to an associated object, such as `3.14159`.

### The Map ADT

In this section, we introduce the map ADT, and define its behaviors to be consistent with those of Python’s built-in dict class. We begin by listing what we consider the most significant five behaviors of a map M as follows

- `M[k]`: Return the value `v` associated with key `k` in map `M`, if one exists; otherwise raise a `KeyError`. In Python, this is implemented with the special method `__getitem__`.
- `M[k] = v`: Associate value `v` with key `k` in map `M`, replacing the existing value if the map already contains an item with key equal to `k`. In Python, this is implemented with the special method `__setitem__`.
- `del M[k]`: Remove from map `M` the item with key equal to `k`; if `M` has no such item, then raise a `KeyError`. In Python, this is implemented with the special method `__delitem__`.
- `len(M)`: Return the number of items in map `M`. In Python, this is implemented with the special method `__len__`.
- `iter(M)`: The default iteration for a map generates a sequence of *keys* in the map. In Python, this is implemented with the special method `__iter__`, and it allows loops of the form, `for k in M`.

We have highlighted the above five behaviors because they demonstrate the core functionality of a map—namely, the ability to query, add, modify, or delete a key-value pair, and the ability to report all such pairs. For additional convenience, map `M` should also support the following behaviors

- `k in M`: Return `True` if the map contains an item with key `k`. In Python, this is implemented with the special `__contains__` method.
- `M.get(k, d=None)`: Return `M[k]` if key `k` exists in the map; otherwise return default value `d`. This provides a form to query `M[k]` without risk of a `KeyError`.
- `M.setdefault(k, d)`: If key `k` exists in the map, simply return `M[k]`; if key `k` does not exist, set `M[k] = d` and return that value.
- `M.pop(k, d=None)`: Remove the item associated with key `k` from the map and return its associated value `v`. If key `k` is not in the map, return default value `d` (or raise `KeyError` if parameter `d` is `None`).
- `M.popitem()`: Remove an arbitrary key-value pair from the map, and return a `(k,v)` tuple representing the removed pair. If map is empty, raise a `KeyError`.
- `M.clear()`: Remove all key-value pairs from the map.
- `M.keys()`: Return a set-like view of all keys of `M`.
- `M.values()`: Return a set-like view of all values of `M`.
- `M.items()`: Return a set-like view of `(k,v)` tuples for all entries of `M`.
- `M.update(M2)`: Assign `M[k] = v` for every `(k,v)` pair in map `M2`.
- `M == M2`: Return `True` if maps `M` and `M2` have identical key-value associations.
- `M != M2`: Return `True` if maps `M` and `M2` do not have identical key-value associations.

### Python’s MutableMapping Abstract Base Class

The previous section provides an introduction to the concept of an ***abstract base class*** and the role of such classes in Python’s `collections` module. Methods that are declared to be abstract in such a base class must be implemented by concrete subclasses. However, an abstract base class may provide *concrete* implementation of other methods that depend upon use of the presumed abstract methods. (This is an example of the ***template method design pattern***).

The `collections` module provides two abstract base classes that are relevant to
our current discussion: the `Mapping` and `MutableMapping` classes. The `Mapping`
class includes all non-mutating methods supported by Python’s `dict` class, while the
`MutableMapping` class extends that to include the mutating methods. What we define as the map ADT in the previous section is akin to the `MutableMapping` abstract base class in Python’s `collections` module.

The significance of these abstract base classes is that they provide a framework
to assist in creating a user-defined map class. In particular, the MutableMapping
class provides concrete implementations for all behaviors other than the first five
outlined in the previous section: `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, and `__iter__`. As we implement the map abstraction with various data structures, as long as we provide the five core behaviors, we can inherit all other derived behaviors by simply declaring `MutableMapping` as a parent class.

### Our MapBase Class

We will be providing many different implementations of the map ADT, in the remainder of this chapter and next, using a variety of data structures demonstrating a trade-off of advantages and disadvantages. The `MutableMapping` abstract base class, from Python’s `collections` module and discussed in the preceding sections, is a valuable tool when implementing a map. However, in the interest of greater code reuse, we define our own `MapBase` class, which is itself a subclass of the `MutableMapping` class. Our MapBase class provides additional support for the ***composition design pattern***. This is a technique we introduced when implementing a priority queue (see ***composition design pattern***) in order to group a key-value pair as a single instance for internal use.

More formally, our `MapBase` class, extending the existing `MutableMapping` abstract base class so that we inherit the many useful concrete methods that class provides. We then define a nonpublic nested `_Item` class, whose instances are able to store both a key and value. This nested class is reasonably similar in design to the `_Item` class that was defined within our `PriorityQueueBase` class in ***composition design pattern***, except that for a map we provide support for both equality tests and comparisons, both of which rely on the item’s key. The notion of equality is necessary for all of our map implementations, as a way to determine whether a key given as a parameter is equivalent to one that is already stored in the map. The notion of comparisons between keys, using the `<` operator, will become relevant when we later introduce a ***sorted map ADT***.

### Simple Unsorted Map Implementation

We demonstrate the use of the `MapBase` class with a very simple concrete implementation of the map ADT. An `UnsortedTableMap` class that relies on storing key-value pairs in arbitrary order within a Python `list`.

An empty table is initialized as `self._table` within the constructor for our map. When a new key is entered into the map, `__setitem__` method, we create a new instance of the nested `_Item` class, which is inherited from our `MapBase` class.

This list-based map implementation is simple, but it is not particularly efficient.
Each of the fundamental methods, `__getitem__`, `__setitem__`, and `__delitem__`, relies on a for loop to scan the underlying list of items in search of a matching key. In a best-case scenario, such a match may be found near the beginning of the list, in which case the loop terminates; in the worst case, the entire list will be examined. Therefore, each of these methods runs in `O(n)` time on a map with `n` items.

## Hash Table

In this section, we introduce one of the most practical data structures for implementing a map, and the one that is used by Python’s own implementation of the `dict` class. This structure is known as a ***hash table***.

Intuitively, a map `M` supports the abstraction of using keys as indices with a syntax such as `M[k]`. As a mental warm-up, consider a restricted setting in which a map with `n` items uses keys that are known to be integers in a range from `0` to `N − 1` for some `N >= n`. In this case, we can represent the map using a ***lookup table*** of length `N`.

In this representation, we store the value associated with key `k` at index `k` of the
table (presuming that we have a distinct way to represent an empty slot). Basic map operations of `__getitem__`, `__setitem__`, and `__delitem__` can be implemented in
`O(1)` worst-case time.

There are two challenges in extending this framework to the more general set-
ting of a map. First, we may not wish to devote an array of length `N` if it is the case
that `N >> n`. Second, we do not in general require that a map’s keys be integers.
The novel concept for a hash table is the use of a ***hash function*** to map general
keys to corresponding indices in a table. Ideally, keys will be well distributed in the
range from `0` to `N − 1` by a hash function, but in practice there may be two or more
distinct keys that get mapped to the same index. As a result, we will conceptualize
our table as a ***bucket array***, in which each bucket may manage a collection of items that are sent to a specific index by the hash function. (To save space, an empty bucket may be replaced by `None`).

### Hash Functions

The goal of a hash function, `h`, is to map each key `k` to an integer in the range
`[0,N − 1]`, where `N` is the capacity of the bucket array for a hash table. Equipped
with such a hash function, `h`, the main idea of this approach is to use the hash function value, `h(k)`, as an index into our bucket array, `A`, instead of the key `k`
(which may not be appropriate for direct use as an index). That is, we store the item `(k,v)` in the bucket `A[h(k)]`.

If there are two or more keys with the same hash value, then two different items
will be mapped to the same bucket in `A`. In this case, we say that a ***collision*** has
occurred. To be sure, there are ways of dealing with collisions, which we will discuss later, but the best strategy is to try to avoid them in the first place. We say
that a hash function is "good" if it maps the keys in our map so as to sufficiently
minimize collisions. For practical reasons, we also would like a hash function to
be fast and easy to compute.

It is common to view the evaluation of a hash function, `h(k)`, as consisting of two portions—a hash code that maps a key `k` to an integer, and a compression function that maps the hash code to an integer within a range of indices, `[0,N − 1]`, for a bucket array.

The advantage of separating the hash function into two such components is that the ***hash code*** portion of that computation is independent of a specific hash table size. This allows the development of a general hash code for each object that can be used for a hash table of any size; only the ***compression function*** depends upon the table size. This is particularly convenient, because the underlying bucket array for a hash table may be dynamically resized, depending on the number of items currently stored in the map.

### Collision-Handling Schemes

The main idea of a hash table is to take a bucket array, `A`, and a hash function, `h`, and use them to implement a map by storing each item `(k,v)` in the "bucket" `A[h(k)]`.
This simple idea is challenged, however, when we have two distinct keys, `k_1` and `k_2`,
such that `h(k_1) = h(k_2)`. The existence of such collisions prevents us from simply
inserting a new item `(k,v)` directly into the bucket `A[h(k)]`. It also complicates our
procedure for performing insertion, search, and deletion operations.

#### Separate Chaining Resolutions

A simple and efficient way for dealing with collisions is to have each bucket `A[j]`
store its own secondary container, holding items `(k,v)` such that `h(k) = j`. A natural
choice for the secondary container is a small map instance implemented using a list,
. This collision resolution rule is known as separate chaining.

In the worst case, operations on an individual bucket take time proportional to
the size of the bucket. Assuming we use a good hash function to index the `n` items
of our map in a bucket array of capacity `N`, the expected size of a bucket is `n/N`.
Therefore, if given a good hash function, the core map operations run in `O(cell(n/N))`.
The ratio `lambda = n/N`, called the ***load factor*** of the hash table, should be bounded by a small constant, preferably below `1`. As long as ***lambda*** is `O(1)`, the core operations on the hash table run in `O(1)` expected time.

#### Open Addressing

The separate chaining rule has many nice properties, such as affording simple  implementations of map operations, but it nevertheless has one slight disadvantage:
It requires the use of an auxiliary data structure—a list—to hold items with colliding keys. If space is at a premium (for example, if we are writing a program for a small handheld device), then we can use the alternative approach of always storing each item directly in a table slot. This approach saves space because no auxiliary structures are employed, but it requires a bit more complexity to deal with collisions. There are several variants of this approach, collectively referred to as ***open addressing*** schemes, which we discuss next. Open addressing requires that the load factor is always at most 1 and that items are stored directly in the cells of the bucket array itself.

#### Linear Probing and Its Variants

A simple method for collision handling with open addressing is ***linear probing***. With this approach, if we try to insert an item `(k,v)` into a bucket `A[j]` that is already occupied, where `j = h(k)`, then we next try `A[(j + 1) mod N]`. If `A[(j + 1) mod N]` is also occupied, then we try `A[(j + 2) mod N]`, and so on, until we find an empty bucket that can accept the new item. Once this bucket is located, we simply insert the item there. Of course, this collision resolution strategy requires that we change the implementation when searching for an existing key—the first step of all `__getitem__`
, `__setitem__`, or `__delitem__` operations. In particular, to attempt to locate an item with key equal to k, we must examine consecutive slots, starting from `A[h(k)]`, until we either find an item with that key or we find an empty bucket. The name "linear probing" comes from the fact that accessing a cell of the bucket array can be viewed as a "probe".

To implement a deletion, we cannot simply remove a found item from its slot in the array.
A typical way to get around this difficulty is to replace a deleted item with a special "available" marker object. With this special marker possibly occupying spaces in our hash table, we modify our search algorithm so that the search for a key `k` will skip over cells containing the available marker and continue probing until reaching the desired item or an empty bucket (or returning back to where we started from). Additionally, our algorithm for `__setitem__` should remember an available cell encountered during the search for `k`, since this is a valid place to put a new item `(k,v)`, if no existing item is found.

Although use of an open addressing scheme can save space, linear probing suffers from an additional disadvantage. It tends to cluster the items of a map into contiguous runs, which may even overlap (particularly if more than half of the cells in the hash table are occupied). Such contiguous runs of occupied hash cells cause searches to slow down considerably.

Another open addressing strategy, known as quadratic probing, iteratively tries the buckets `A[(h(k) + f(i)) mod N]`, for `i = 0,1,2,...,` where `f(i) = i^2`, until finding
an empty bucket. As with linear probing, the quadratic probing strategy complicates the removal operation, but it does avoid the kinds of clustering patterns that occur with linear probing. Nevertheless, it creates its own kind of clustering, called ***secondary clustering***, where the set of filled array cells still has a non-uniform pattern, even if we assume that the original hash codes are distributed uniformly. When `N` is prime and the bucket array is less than half full, the quadratic probing strategy is guaranteed to find an empty slot.

### Python Hash Table Implementation

In this section, we develop two implementations of a hash table, one using separate chaining and the other using open addressing with linear probing. While these approaches to collision resolution are quite different, there are a great many commonalities to the hashing algorithms. For that reason, we extend the `MapBase` class, to define a new `HashMapBase` class, providing much of the common functionality to our two hash table
implementations. The main design elements of the `HashMapBase` class are

- The bucket array is represented as a Python list, named `self._table`, with all entries initialized to `None`.
- We maintain an instance variable `self._n` that represents the number of distinct items that are currently stored in the hash table.
- If the load factor of the table increases beyond 0.5, we double the size of the table and rehash all items into the new table.
- We define a `_hash_function` utility method that relies on Python’s built-in hash function to produce hash codes for keys, and a randomized ***Multiply-Add-and-Divide*** (***MAD***) formula for the compression function.

What is not implemented in the base class is any notion of how a "bucket" should be represented. With separate chaining, each bucket will be an independent structure. With open addressing, however, there is no tangible container for each bucket; the "buckets" are effectively interleaved due to the probing sequences.

In our design, the `HashMapBase` class presumes the following to be abstract methods, which must be implemented by each concrete subclass

- `_bucket_getitem(j, k)`: This method should search bucket `j` for an item having key `k`, returning the associated value, if found, or else raising a `KeyError`.
- `_bucket_setitem(j, k, v)`: This method should modify bucket `j` so that key `k` becomes associated with value `v`. If the key already exists, the new value overwrites the existing value. Otherwise, a new item is inserted and *this method is responsible for incrementing* `self._n`.
- `_bucket_delitem(j, k)`: This method should remove the item from bucket `j` having key `k`, or raise a `KeyError` if no such item exists. (`self._n` is decremented after this method).
- `__iter__`: This is the standard map method to iterate through all keys of the map. Our base class does not delegate this on a per-bucket basis because "buckets" in open addressing are not inherently disjoint.

#### Separate Chaining

The first three methods in the class use index `j` to access the potential bucket in
the bucket array, and a check for the special case in which that table entry is `None`.
The only time we need a new bucket structure is when `_bucket_setitem` is called on
an otherwise empty slot. The remaining functionality relies on map behaviors that are already supported by the individual `UnsortedTableMap` instances. We need a bit of forethought to determine whether the application of `__setitem__` on the chain causes a net increase in the size of the map (that is, whether the given key is new).

#### Linear Probing

Our implementation of a `ProbeHashMap` class, using open addressing with linear
probing. In order to support deletions, we use a technique described in Section [**Collision-Handling Schemes**](#collision-handling-schemes) in which we place a special marker in a table location at which an item has been deleted, so that we can distinguish between it and a location that has always been empty. In our implementation, we declare a class-level attribute, `_AVAIL`, as a sentinel. (We use an instance of the
built-in object class because we do not care about any behaviors of the sentinel,
just our ability to differentiate it from other objects).

The most challenging aspect of open addressing is to properly trace the series of probes when collisions occur during an insertion or search for an item. To this end, we define a nonpublic utility, `_find_slot`, that searches for an item with key `k` in "bucket" `j` (that is, where `j` is the index returned by the hash function for key `k`).

The three primary map operations each rely on the `_find_slot` utility. When attempting to retrieve the value associated with a given key, we must continue probing until we find the key, or until we reach a table slot with the `None` value. We cannot stop the search upon reaching an `_AVAIL` sentinel, because it represents a location that may have been filled when the desired item was once inserted.

When a key-value pair is being assigned in the map, we must attempt to find an existing item with the given key, so that we might overwrite its value, before adding a new item to the map. Therefore, we must search beyond any occurrences of the `_AVAIL` sentinel when inserting. However, if no match is found, we prefer to repurpose the first slot marked with `_AVAIL`, if any, when placing the new element in the table. The `_find_slot` method enacts this logic, continuing the search until a truly empty slot, but returning the index of the first available slot for an insertion.

When deleting an existing item within `_bucket_delitem`, we intentionally set the table entry to the `_AVAIL` sentinel in accordance with our strategy.

## Sorted Map

The traditional map ADT allows a user to look up the value associated with a given key, but the search for that key is a form known as an ***exact search***.

For example, computer systems often maintain information about events that have occurred (such as financial transactions), organizing such events based upon what are known as ***time stamps***. If we can assume that time stamps are unique for a particular system, then we might organize a map with a time stamp serving as the key, and a record about the event that occurred at that time as the value. A particular time stamp could serve as a reference ID for an event, in which case we can quickly retrieve information about that event from the map. However, the map ADT does not provide any way to get a list of all events ordered by the time at which they occur, or to search for which event occurred closest to a particular time. In fact, the fast performance of hash-based implementations of the map ADT relies on the intentionally scattering of keys that may seem very "near" to each other in the original domain, so that they are more uniformly distributed in a hash table.

In this section, we introduce an extension known as the ***sorted map*** ADT that includes all behaviors of the standard map, plus the following

- `M.find_min()`: Return the (key,value) pair with minimum key (or `None`, if map is empty).
- `M.find_max()`: Return the (key,value) pair with maximum key (or `None`, if map is empty).
- `M.find_lt(k)`: Return the (key,value) pair with the greatest key that is strictly less than `k` (or `None`, if no such item exists).
- `M.find_le(k)`: Return the (key,value) pair with the greatest key that is less than or equal to `k` (or `None`, if no such item exists).
- `M.find_gt(k)`: Return the (key,value) pair with the least key that is strictly greater than `k` (or `None`, if no such item exists).
- `M.find_ge(k)`: Return the (key,value) pair with the least key that is greater than or equal to `k` (or `None`, if no such item).
- `M.find_range(start, stop)`: Iterate all (key,value) pairs with `start <= key < stop`. If `start` is `None`, iteration begins with minimum key; if `stop` is `None`, iteration concludes with maximum key.
- `iter(M)`: Iterate all keys of the map according to their natural order, from smallest to largest.
- `reversed(M)`: Iterate all keys of the map in reverse order; in Python, this is implemented with the `__reversed__` method.

### Sorted Search Tables

In this section, we begin by exploring a simple implementation of a sorted map. We store the map’s items in an array-based sequence A so that they are in increasing order of
their keys, assuming the keys have a naturally defined order. We refer to this implementation of a map as a ***sorted search table***.

As was the case with the unsorted table map of Section [**Simple Unsorted Map**](#simple-unsorted-map-implementation), the sorted search table has a space requirement that is `O(n)`, assuming we grow and shrink the array to keep its size proportional to the number of items in the map. The primary advantage of this representation, and our reason for insisting that `A` be array-based, is that it allows us to use the ***binary search*** algorithm for a variety of efficient operations.

#### Binary Search and Inexact Searches

We originally know the binary search algorithm, as a means for detecting whether a given target is stored within a sorted sequence. In our original presentation, a `binary search` function returned `True` of `False` to designate whether the desired target was found. While such an approach could be used to implement the `__contains__` method of the map ADT, we can adapt the binary search algorithm to provide far more useful information when performing forms of inexact search in support of the sorted map ADT.

The important realization is that while performing a binary search, we can determine the index at or near where a target might be found. During a successful search, the standard implementation determines the precise index at which the target is found. During an unsuccessful search, although the target is not found, the algorithm will effectively determine a pair of indices designating elements of the collection that are just less than or just greater than the missing target.

#### Implementation

We will present a complete implementation of a class, `SortedTableMap`, that supports the sorted map ADT. The most notable feature of our design is the inclusion of a `_find_index` utility function. This method using the binary search algorithm, but by convention returns the index of the leftmost item in the search interval having key greater than or equal to `k`. Therefore, if the key is present, it will return the index of the item having that key. (Recall that keys are unique in a map.) When the key is missing, the function returns the index of the item in the search interval that is just beyond where the key would have been located. As a technicality, the method returns index `high + 1` to indicate that no items of the interval had a key greater than `k`.

We rely on this utility method when implementing the traditional map operations and the new sorted map operations. The body of each of the `__getitem__`, `__setitem__`, and
`__delitem__` methods begins with a call to `_find_index` to determine a candidate index at which a matching key might be found. For `__getitem__`, we simply check whether that is a valid index containing the target to determine the result. For `__setitem__`, recall that the goal is to replace the value of an existing item, if one with key `k` is found, but otherwise to insert a new item into the map. The index returned by `_find_index` will be the index of the match, if one exists, or otherwise the exact index at which the new item should be inserted. For `__delitem__`, we again rely on the convenience of `_find_index` to determine the location of the item to be popped, if any.

Our `_find_index` utility is equally valuable when implementing the various inexact search methods. For each of the methods `find_lt`, `find_le`, `find_gt`, and `find_ge`, we begin with a call to `_find_index` utility, which locates the first index at which there is an element with `key >= k`, if any. This is precisely what we want for `find_ge`, if valid, and just beyond the index we want for `find_lt`. For `find_gt` and `find_le` we need some extra case analysis to distinguish whether the indicated index has a key equal to `k`. For example, if the indicated item has a matching key, our `find_gt` implementation increments the index before continuing with the process. (We omit the implementation of `find_le`, for brevity.) In all cases, we must properly handle boundary cases, reporting None when unable to find a key with the desired property.

Our strategy for implementing `find_range` is to use the `_find_index` utility to locate the first item with `key >= start` (assuming start is not `None`). With that knowledge, we use a while loop to sequentially report items until reaching one that has a key greater than or equal to the stopping value (or until reaching the end of the table). It is worth noting that the while loop may trivially iterate zero items if the first key that is greater than or equal to start also happens to be greater than or equal to `stop`. This represents an empty range in the map.

#### Analysis (Updating)

We conclude by analyzing the performance of our `SortedTableMap` implementation. A  summary of the running times for all methods of the sorted map ADT (including the traditional map operations) is given in Table below. It should be clear that the `__len__`, `find_min`, and `find_max` methods run in `O(1)` time, and that iterating the keys of the table in either direction can be performed in `O(n)` time.

The analysis for the various forms of search all depend on the fact that a binary search on a table with `n` entries runs in `O(log(n))` time. This claim was originally shown as the complexity of binary search, and that analysis clearly applies to our `_find_index` method as well. We therefore claim an `O(log(n))` worst-case running time for methods
`__getitem__`, `find_lt`, `find_gt`, `find_le`, and `find_ge`. Each of these makes a single call to `_find_index`, followed by a constant number of additional steps to determine the appropriate answer based on the index. The analysis of `find_range` is a bit more interesting. It begins with a binary search to find the first item within the range (if any). After that, it executes a loop that takes `O(1)` time per iteration to report subsequent values until reaching the end of the range. If there are
s items reported in the range, the total running time is `O(s+log(n))`.

In contrast to the efficient search operations, update operations for a sorted table
may take considerable time. Although binary search can help identify the index at
which an update occurs, both insertions and deletions require, in the worst case, that
linearly many existing elements be shifted in order to maintain the sorted order of
the table. Specifically, the potential call to `_table.insert` from within `__setitem__`
and `_table.pop` from within `__delitem__` lead to `O(n)` worst-case time.

In conclusion, sorted tables are primarily used in situations where we expect many  searches but relatively few updates.

📊 Performance of a sorted map, as implemented with `SortedTableMap`. We use `n` to denote the number of items in the map at the time the operation is performed. The space requirement is `O(n)`

| **Operation** | **Running Time** |
| --- | --- |
| `len(M)` | `O(1)` |
| `k in M` | `O(log(n))` |
| `M[k] = v` | `O(n)` worst case; `O(log(n))` if existing `k` |
| `del M[k]` | `O(n)` worst case |
| `M.find_min()`, `M.find_max()` | `O(1)` |
| `M.find_lt(k)`, `M.find_gt(k)`, `M.find_le(k)`, `M.find_ge(k)` | `O(log(n))` |
| `M.find_range(start, stop)` | `O(s + log(n))` where `s` items are reported |
| `iter(M)`, `reversed(M)` | `O(n)` |

## Sets, Multi-sets, and Multi-maps

### The Set ADT

### Python’s MutableSet Abstract Base Class
