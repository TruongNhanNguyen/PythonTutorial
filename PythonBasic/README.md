# Python Primer

## Python Overview

- [Python Primer](#python-primer)
  - [Python Overview](#python-overview)
    - [The Python Interpreter](#the-python-interpreter)
    - [Preview of a Python Program](#preview-of-a-python-program)
  - [Objects in Python](#objects-in-python)
    - [Identifier, Objects and Assignments](#identifier-objects-and-assignments)
      - [Identifiers](#identifiers)
    - [Creating and Using Objects](#creating-and-using-objects)
      - [Instantiation](#instantiation)
      - [Calling Methods](#calling-methods)
    - [Python Built-in Classes](#python-built-in-classes)
  - [Expressions, Operators and Precedence](#expressions-operators-and-precedence)
    - [Logical Operators](#logical-operators)
    - [Equality Operators](#equality-operators)
    - [Comparison Operators](#comparison-operators)
    - [Arithmetic Operators](#arithmetic-operators)
    - [Bitwise Operators](#bitwise-operators)
    - [Sequence Operators](#sequence-operators)
    - [Operators for Sets and Dictionaries](#operators-for-sets-and-dictionaries)
    - [Extended Operators](#extended-operators)
    - [Compound Expressions and Operator Precedence](#compound-expressions-and-operator-precedence)
  - [Control Flows](#control-flows)
    - [Conditionals](#conditionals)
    - [Loops](#loops)
      - [While Loop](#while-loop)
      - [For Loop](#for-loop)
        - [Index-Based For Loops](#index-based-for-loops)
        - [Break and Continue Statements](#break-and-continue-statements)
  - [Functions](#functions)
    - [Return Statement](#return-statement)
    - [Information Passing](#information-passing)
      - [Mutable Parameters](#mutable-parameters)
      - [Default Parameter Values](#default-parameter-values)
      - [Keyword Parameters](#keyword-parameters)
    - [Python Built-in Functions](#python-built-in-functions)
  - [Simple Input and Output](#simple-input-and-output)
    - [Console Input and Output](#console-input-and-output)
    - [Files](#files)
  - [Exceptions Handling](#exceptions-handling)
    - [Raising an Exception](#raising-an-exception)
    - [Catching an Exception](#catching-an-exception)
  - [Iterators and Generators](#iterators-and-generators)
  - [Additional Python Conveniences](#additional-python-conveniences)
  - [Scope and Namespaces](#scope-and-namespaces)
  - [Modules and the `Import` Statement](#modules-and-the-import-statement)
    - [Existing Modules](#existing-modules)
  - [Object-Oriented Programming](#object-oriented-programming)
  - [Algorithm Analysis](#algorithm-analysis)
  - [Data Structures and Algorithms](#data-structures-and-algorithms)
    - [Data Structures](#data-structures)
    - [Algorithms](#algorithms)

### The Python Interpreter

Python is formally an ***interpreted*** language. Commands are executed through a piece of software known as the ***Python interpreter***. The interpreter receives a command, evaluates that command, and reports the result of the command. While the interpreter can be used interactively (especially when debugging), a programmer typically defines a series of commands in advance and saves those commands in a plain text file known as ***source code*** or a ***script***. For Python, source code is conventionally stored in a file named with the `/py` suffix (e.g., `demo.py`).

On most operating systems, the Python interpreter can be started by typing python from the command line. By default, the interpreter starts in interactive mode with a clean workspace. Commands from a predefined script saved in a file (e.g., `demo.py`) are executed by invoking the interpreter with the filename as an argument (e.g., `python demo.py`), or using an additional `-i` flag in order to execute a script and then enter interactive mode (e.g., `python -i demo.py`).

Many ***integrated development environments*** (IDEs) provide richer software development platforms for Python, including one named IDLE that is included with the standard Python distribution. IDLE provides an embedded text-editor with support for displaying and editing Python code, and a basic debugger, allowing step-by-step execution of a program while examining key variable values.

### Preview of a Python Program

As a simple introduction, ***Code Fragment*** below presents a Python program that computes the grade-point average (GPA) for a student based on letter grades that are entered by a user. Many of the techniques demonstrated in this example will be discussed in the remainder of this chapter. At this point, we draw attention to a few high-level issues, for readers who are new to Python as a programming language.

Python’s syntax relies heavily on the use of ***whitespace***. Individual statements are typically concluded with a newline character, although a command can extend to another line, either with a concluding backslash character (`\`), or if an opening delimiter has not yet been closed, such as the `{` character in defining `value_map`.

Whitespace is also key in delimiting the bodies of control structures in Python. Specifically, a block of code is indented to designate it as the body of a control structure, and nested control structures use increasing amounts of indentation. In the ***Code Fragment***, the body of the `while` loop consists of the subsequent 8 lines, including a nested conditional structure.

Comments are annotations provided for human readers, yet ignored by the Python interpreter. The primary syntax for comments in Python is based on use of the `#` character, which designates the remainder of the line as a comment.

***Code Fragment***: A Python program that computes a grade-point average (GPA)

```python
print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'A+': 4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67,
         'C+':2.33, 'C':2.0, 'C':1.67, 'D':1.33, 'D':1.0, 'F':0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    else if grade not in points:
        print('Unknown grade '{0}' being ignored'.format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_course > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))
```

## Objects in Python

Python is an object-oriented language and classes form the basis for all data types.

### Identifier, Objects and Assignments

The most important of all Python commands is an assignment statement, such as

```python
temperature = 98.6
```

This command establishes temperature as an ***identifier*** (also known as a ***name***), and then associates it with the ***object*** expressed on the right-hand side of the equal sign, in this case a floating-point object with value `98.6`.

#### Identifiers

Identifiers in Python are ***case-sensitive***, so `temperature` and `Temperature` are distinct names. Identifiers can be composed of almost any combination of letters, numerals, and underscore characters (or more general **Unicode** characters). The primary restrictions are that an identifier cannot begin with a numeral (thus `9lives` is an illegal name), and that there are 33 specially reserved words that cannot be used as identifiers, as shown in ***Table*** below.

***Table***: A listing of the ***reserved words*** in Python. These names cannot be used as  identifiers.

```python
False   as      continue    else    from    in      not    return  
None    assert  def         except  global  is      or     try     
del     finally if          lambda  pass    while   and    class   elif
for     import  nonlocal    raise   with    yield   True   break
```

If you were familiar with other programming languages, the semantics of a Python identifier is most similar to a reference variable in Java or a pointer variable in C++. Each identifier is implicitly associated with the ***memory address*** of the object to which it refers. A Python identifier may be assigned to a special object named `None`, serving a similar purpose to a null reference in Java or C++.

Unlike Java and C++, Python is a ***dynamically typed*** language, as there is no advance declaration associating an identifier with a particular data type. An identifier can be associated with any type of object, and it can later be reassigned to another object of the same (or different) type. Although an identifier has no declared type, the object to which it refers has a definite type. In the first example, the characters `98.6` are recognized as a  *floating-point* literal, and thus the identifier `temperature` is associated with an instance of the `float` class having that value.

A programmer can establish an ***alias*** by assigning a second identifier to an existing object.
Once an alias has been established, either name can be used to access the underlying object. If that object supports behaviors that affect its state, changes enacted through one alias will be apparent when using the other alias (because they refer to the same object). However, if one of the *names* is reassigned to a new value using a subsequent assignment statement, that does not affect the aliased object, rather it breaks the alias.

### Creating and Using Objects

#### Instantiation

The process of creating a new instance of a class is known as ***instantiation***. In general, the syntax for instantiating an object is to invoke the constructor of a class. For example, if there were a class named `Widget`, we could create an instance of that class using a syntax such as `w = Widget()`, assuming that the constructor does not require any parameters. If the constructor does require parameters, we might use a syntax such as `Widget(a, b, c)` to construct a new instance.

Many of Python’s built-in classes support what is known as a ***literal*** form for designating new instances. For example, the command `temperature = 98.6` results in the creation of a new instance of the `float` class; the term `98.6`in that expression is a literal form.

From a programmer’s perspective, yet another way to indirectly create a new instance of a class is to call a function that creates and returns such an instance. For example, Python has a built-in function named `sorted` that takes a sequence of comparable elements as a parameter and returns a new instance of the `list` class containing those elements in sorted order.

#### Calling Methods

Python supports traditional functions that are invoked with a syntax such as `sorted(data)`, in which case `data` is a parameter sent to the function. Python’s classes may also define one or more ***methods*** (also known as ***member functions***), which are invoked on a specific instance of a class using the dot (`.`) operator. For example, Python’s `list` class has a method named sort that can be invoked with a syntax such as `data.sort()`. This particular method rearranges the contents of the list so that they are sorted.

The expression to the left of the dot identifies the object upon which the method is invoked. Often, this will be an identifier (e.g., `data`), but we can use the dot operator to invoke a method upon the immediate result of some other operation. For example, if response identifies a string instance (we will discuss strings later in this section), the syntax `response.lower().startswith('y')` first evaluates the method call, `response.lower()`, which itself returns a new string instance, and then the `startswith('y')` method is called on that intermediate string.

When using a method of a class, it is important to understand its behavior. Some methods return information about the state of an object, but do not change that state. These are known as ***accessors***. Other methods, such as the `sort` method of the `list` class, do change the state of an object. These methods are known as ***mutators*** or ***update methods***.

### Python Built-in Classes

***Table*** below provides a summary of commonly used, built-in classes in Python; we take particular note of which classes are mutable and which are ***immutable***. A class is immutable if each object of that class has a fixed value upon instantiation that cannot subsequently be changed. For example, the float class is immutable. Once an instance has been created, its value cannot be changed (although an identifier referencing that object can be reassigned to a different value).

***Table***: Commonly used built-in classes for Python

| **Class** | **Description** | **Immutable** |
| --- | --- | --- |
| `bool` | Boolean value | ✔ |
| `int` | integer (arbitrary magnitude) | ✔ |
| `float` | floating-point number | ✔ |
| `list` | mutable sequence of objects |  |
| `tuple` | immutable sequence of objects | ✔ |
| `str` | character string | ✔ |
| `set` | unordered set of distinct objects |  |
| `frozenset` | immutable form of `set` class | ✔ |
| `dict` | associative mapping (aka dictionary) | |

## Expressions, Operators and Precedence

In the previous section, we demonstrated how names can be used to identify existing objects, and how literals and constructors can be used to create instances of built-in classes. Existing values can be combined into larger syntactic ***expressions*** using a variety of special symbols and keywords known as ***operators***. The semantics of an operator depends upon the type of its operands. For example, when `a` and `b` are numbers, the syntax `a + b` indicates addition, while if `a` and `b` are strings, the operator indicates concatenation. In this section, we describe Python’s operators in various contexts of the built-in types.

We continue, in Section [Compound Expressions and Operator Precedence](#compound-expressions-and-operator-precedence), by discussing compound expressions, such as
`a + b * c`, which rely on the evaluation of two or more operations. The order in which the operations of a compound expression are evaluated can affect the overall value of the expression. For this reason, Python defines a specific order of precedence for evaluating operators, and it allows a programmer to override this order by using explicit parentheses to group sub-expressions.

### Logical Operators

Python supports the following keyword operators for Boolean values

- `not`: unary negation
- `and`: conditional and
- `or`: conditional or

The `and` and `or` operators ***short-circuit***, in that they do not evaluate the second
operand if the result can be determined based on the value of the first operand. This feature is useful when constructing Boolean expressions in which we first test that a certain condition holds (such as a reference not being `None`), and then test a condition that could have otherwise generated an error condition had the prior test not succeeded.

### Equality Operators

Python supports the following operators to test two notions of equality

- `is`: same identity
- `is not`: different identity
- `==`: equivalent
- `!=`: not equivalent

The expression `a is b` evaluates to `True`, precisely when identifiers `a` and `b` are aliases for the same object. The expression `a == b` tests a more general notion of equivalence. If identifiers `a` and `b` refer to the same object, then `a == b` should also evaluate to `True`. Yet `a == b` also evaluates to `True` when the identifiers refer to different objects that happen to have values that are ***deemed equivalent***. The precise notion of equivalence depends on the data type. For example, two strings are considered equivalent if they match character for character. Two sets are equivalent if they have the same contents, irrespective of order. In most programming situations, the equivalence tests `==`and `!=` are the appropriate operators; use of is and is not should be reserved for situations in which it is necessary to detect true aliasing.

### Comparison Operators

Data types may define a natural order via the following operators

- `<`: less than
- `<=`: less than or equal to
- `>`: greater than
- `>=`: greater than or equal to

These operators have expected behavior for numeric types, and are defined *lexicographically*, and *case-sensitively*, for strings. An exception is raised if operands have incomparable types, as with `5 < 'hello'`.

### Arithmetic Operators

Python supports the following arithmetic operators

- `+`: addition
- `-`: subtraction
- `*`: multiplication
- `/`: true division
- `//`: integer division
- `%`: the module operator

The use of addition, subtraction, and multiplication is straightforward, noting that if
both operands have type int, then the result is an int as well; if one or both operands
have type float, the result will be a `float`.

Python takes more care in its treatment of division. We first consider the case in which both operands have type int, for example, the quantity 27 divided by 4. In mathematical notation, `27 ÷ 4 = 6 + 3 / 4 = 6.75`. In Python, the `/` operator designates ***true division***, returning the floating-point result of the computation. Thus, `27 / 4` results in the *float* value `6.75`. Python supports the pair of operators `//` and `%` to perform the integral calculations, with expression `27 // 4` evaluating to int value 6 (the mathematical floor of the quotient), and expression `27 % 4` evaluating to int value 3, the remainder of the integer division. We note that languages such as C, C++, and Java do not support the `//` operator; instead, the `/` operator returns the truncated quotient when both operands have integral type, and the
result of true division when at least one operand has a floating-point type.

Python carefully extends the semantics of `//` and `%` to cases where one or both operands are negative. For the sake of notation, let us assume that variables `n` and `m` represent  respectively the ***dividend*** and ***divisor*** of a quotient `n / m`, and that `q = n // m` and `r = n % m`. Python guarantees that `q * m + r` will equal `n`. We already saw an example of this identity with positive operands, as `6 * 4+ 3 = 27`. When the divisor `m` is positive, Python further guarantees that `m > r >= 0`. As a consequence, we find that `−27 // 4` evaluates to −7 and `−27 % 4` evaluates to 1, as `(−7) * 4+ 1 = −27`. When the divisor is negative, Python guarantees that `m < r <= 0`. As an example, `27 // −4` is −7 and `27 % −4` is −1, satisfying the
identity `27 = (−7) * (−4) + (−1)`.

The conventions for the `//` and `%` operators are even extended to floating-point operands, with the expression `q = n // m` being the integral floor of the quotient, and `r = n % m` being the "remainder" to ensure that `q * m + r` equals `n`. For example, `8.2 // 3.14` evaluates to 2.0 and `8.2 % 3.14` evaluates to 1.92, as `2.0 * 3.14 + 1.92 = 8.2`.

### Bitwise Operators

Python provides the following bitwise operators for integers

- `~`: bitwise complement (prefix unary operator)
- `&`: bitwise and
- `|`: bitwise or
- `^`: bitwise exclusive-or
- `<<`: shift bits left, filling in with zeros
- `>>`: shift bits right, filling in with sign bit

### Sequence Operators

Each of Python’s built-in sequence types (`str`, `tuple`, and `list`) support the following
operator syntaxes

- `s[j]`: element at index `j`
- `s[start:stop]`: slice including indices `[start,stop)`
- `s[start:stop:step]`: slice including indices `start, start + step, start + 2 step,...`, up to but not equalling or `stop`
- `s + t`: concatenation of sequences
- `k * s`: shorthand for `s + s + s + ... (k times)`
- `val in s`: containment check
- `val not in s`: non-containment check

Python relies on zero-indexing of sequences, thus a sequence of length `n` has elements indexed from `0` to `n − 1` inclusive. Python also supports the use of negative indices, which denote a distance from the end of the sequence; `index − 1` denotes the last element, index −2 the second to last, and so on. Python uses a ***slicing*** notation to describe subsequences of a sequence. Slices are described as half-open intervals, with a start index that is included, and a stop index that is excluded. For example, the syntax `data[3:8]` denotes a subsequence including the five indices: 3,4,5,6,7. An optional `step` value, possibly negative, can be indicated as a third
parameter of the slice. If a start index or stop index is omitted in the slicing notation, it is presumed to designate the respective extreme of the original sequence.

Because lists are mutable, the syntax `s[j] = val` can be used to replace an element at a given index. Lists also support a syntax, del `s[j]`, that removes the designated element from the list. Slice notation can also be used to replace or delete a sub-list.

The notation `val in s` can be used for any of the sequences to see if there is an element equivalent to `val` in the sequence. For strings, this syntax can be used to check for a single character or for a larger substring, as with `amp in 'example'`.

All sequences define comparison operations based on lexicographic order, performing an element by element comparison until the first difference is found. For example, `[5, 6, 9] < [5, 7]` because of the entries at index 1. Therefore, the following operations are supported by sequence types

- `s == t`: equivalent (element by element)
- `s != t`: not equivalent
- `s < t`: lexicographically less than
- `s <= t`: lexicographically less than or equal to
- `s > t`: lexicographically grater than
- `s >= t`: lexicographically grater than or equal to

### Operators for Sets and Dictionaries

Sets and frozensets support the following operators

- `key in s`: containment check
- `key not in s`: non-containment check
- `s1 == s2`: `s1` equivalent to `s2`
- `s1 != s2`: `s1` not equivalent to `s2`
- `s1 <= s2`: `s1` is subset of `s2`
- `s1 < s2`: `s1` is proper subset of `s2`
- `s1 >= s2`: `s1` is superset of `s2`
- `s1 > s2`: `s1` is proper superset of `s2`
- `s1 | s2`: the *union* of `s1` and `s2`
- `s1 & s2`: the intersection of `s1` and `s2`
- `s1 - s2`: the set of elements in `s1` but not `s2`
- `s1 ^ s2`: the set of elements precisely one of `s1` or `s2`

Note well that sets do not guarantee a particular order of their elements, so the comparison operators, such as `<`, are not lexicographic; rather, they are based on the mathematical notion of a subset. As a result, the comparison operators define a partial order, but not a total order, as disjoint sets are neither "less than", "equal to" or "greater than" each other. Sets also support many fundamental behaviors through named methods (e.g., `add`, `remove`)

Dictionaries, like sets, do not maintain a well-defined order on their elements. Furthermore, the concept of a subset is not typically meaningful for dictionaries, so the dict class does not support operators such as `<`. Dictionaries support the notion of equivalence, with `d1 == d2` if the two dictionaries contain the same set of key-value pairs. The most widely used behavior of dictionaries is accessing a value associated with a particular key `k` with the indexing syntax, `d[k]`. The supported operators are as follows

- `d[key]`: value associated with given key
- `d[key] = value`: set (or reset) the value associated with given `key`
- `del d[key]`: remove `key` and its associated `value` from dictionary
- `key in d`: containment check
- `key not in d`: non-containment check
- `d1 == d2`: `d1` is equivalent to `d2`
- `d1 != d2`: `d1` is not equivalent to `d2`

Dictionaries also support many useful behaviors through named methods.

### Extended Operators

Python supports an extended assignment operator for most binary operators, for example, allowing a syntax such as `count += 5`. By default, this is a shorthand for the more verbose `count = count + 5`. For an immutable type, such as a number or a string, one should not presume that this syntax changes the value of the existing object, but instead that it will reassign the identifier to a newly constructed value. However, it is possible for a type to redefine such semantics to mutate the object, as the list class does for the `+=` operator.

```python
alpha = [1, 2, 3]
beta = alpha            # an alias for alpha
beta += [4, 5]          # extends the original list with two more elements
beta = beta + [6, 7]    # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha)            # will be [1, 2, 3, 4, 5]
```

This example demonstrates the subtle difference between the list semantics for the syntax `beta += foo` versus `beta = beta + foo`.

### Compound Expressions and Operator Precedence

Programming languages must have clear rules for the order in which compound expressions, such as `5 + 2 * 3`, are evaluated. The formal order of precedence for operators in Python is given in ***Table*** below. Operators in a category with higher precedence will be evaluated before those with lower precedence, unless the expression is otherwise parenthesized. Therefore, we see that Python gives precedence to multiplication over addition, and therefore evaluates the expression `5 + 2 * 3` as `5 + (2 * 3)`, with value 11, but the parenthesized expression `(5 + 2) * 3` evaluates to value 21. Operators within a category are typically evaluated from left to right, thus `5 − 2 + 3` has value 6. Exceptions to this rule include that unary operators and exponentiation are evaluated from right to left.

Python allows a chained assignment, such as `x = y = 0`, to assign multiple identifiers to the rightmost value. Python also allows the chaining of comparison operators. For example, the expression `1 <= x + y <= 10` is evaluated as the compound `(1 <= x + y) and (x + y <= 10)`, but without computing the intermediate value `x + y` twice.

*Table*: Operator precedence in Python, with categories ordered from highest precedence to lowest precedence. When stated, we use `expr` to denote a literal, identifier, or result of a previously evaluated expression. All operators without explicit mention of expr are binary operators, with syntax `expr1` operator `expr2`.

| **Operator Precedence** | **Type** | **Symbol** |
| --- | --- | --- |
| 1 | member access | `expr.member` |
| 2 | function/method calls | `expr()` |
| 2 | container subscripts/slices | `expr[]` |
| 3 | exponentiation | `**` |
| 4 | unary operators | `+expr`, `−expr`, `~expr` |
| 5 | multiplication, division | `*`, `/`, `//`, `%` |
| 6 | addition, subtraction | `+`, `−` |
| 7 | bitwise shifting | `<<`, `>>` |
| 8 | bitwise-and | `&` |
| 9 | bitwise-xor | `^` |
| 10 | bitwise-or | `|` |
| 11 | comparisons | `is`, `is not`, `==`, `!=`, `<`, `<=`, `>`, `>=` |
| 11 | containment | `in`, `not in` |
| 12 | logical-not | `not expr` |
| 13 | logical-and | `and` |
| 14 | logical-or | `or` |
| 15 | conditional | `val1 if condition else val2` |
| 16 | assignments | `=`, `+=`, `−=`, `=`, etc. |

## Control Flows

In this section, we review Python’s most fundamental control structures: conditional statements and loops. Common to all control structures is the syntax used in Python for defining blocks of code. The colon character is used to delimit the beginning of a block of code that acts as a body for a control structure. If the body can be stated as a single executable statement, it can technically placed on the same line, to the right of the colon. However, a body is more typically typeset as an ***indented block*** starting on the line following the colon. Python relies on the indentation level to designate the extent of that block of code, or any nested blocks of
code within.

### Conditionals

Conditional constructs (also known as `if` statements) provide a way to execute a chosen block of code based on the run-time evaluation of one or more Boolean expressions. In Python, the most general form of a conditional is written as follows

```python
if first_condition:
    first_body
elif second_condition:
    second_body
elif third_condition:
    third_body
else:
    fourth_body
```

Each condition is a Boolean expression, and each body contains one or more commands that are to be executed conditionally. If the first condition succeeds, the first body will be executed; no other conditions or bodies are evaluated in that case. If the first condition fails, then the process continues in similar manner with the evaluation of the second condition. The execution of this overall construct will cause precisely one of the bodies to be executed. There may be any number of `elif` clauses (including zero), and the final `else` clause is optional. As described on page 7, non-boolean types may be evaluated as Booleans with intuitive meanings.

### Loops

Python offers two distinct looping constructs. A `while` loop allows general repetition based upon the repeated testing of a Boolean condition. A `for` loop provides convenient iteration of values from a defined series (such as characters of a string, elements of a list, or numbers within a given range). We discuss both forms in this section.

#### While Loop

The syntax for a `while` loop in Python is as follows

```python
while condition:
    body
```

As with an `if` statement, *condition* can be an arbitrary Boolean expression, and *body* can be an arbitrary block of code (including nested control structures). The execution of a while loop begins with a test of the Boolean condition. If that condition evaluates to `True`, the body of the loop is performed. After each execution of the body, the loop condition is retested, and if it evaluates to `True`, another iteration of the body is performed. When the conditional test evaluates to False (assuming it ever does), the loop is exited and the flow of control continues just beyond the body of the loop.

As an example, here is a loop that advances an index through a sequence of characters until finding an entry with value `'X'` or reaching the end of the sequence.

```python
j = 0
while j < len(data) and data[j] != 'X':
    j += 1
```

The `len` function, returns the length of a sequence such as a `list` or `string`. The correctness of this loop relies on the short-circuiting behavior of the `and` operator, as described on Section [Logical-operators](#logical-operators). We intentionally test `j < len(data)` to ensure that `j` is a valid index, prior to accessing element `data[j]`. Had we written that compound condition with the opposite order, the evaluation of `data[j]` would eventually raise an `IndexError` when `'X'` is not found. (See Section [Exception](#exceptions-handling) for discussion of exceptions).

As written, when this loop terminates, variable `j`’s value will be the index of the leftmost occurrence of `'X'` , if found, or otherwise the length of the sequence (which is recognizable as an invalid index to indicate failure of the search). It is worth noting that this code behaves correctly, even in the special case when the list is empty, as the condition `j < len(data)` will initially fail and the body of the loop will never be executed.

#### For Loop

Python’s `for-loop` syntax is a more convenient alternative to a while loop when iterating through a series of elements. The `for-loop` syntax can be used on any type of ***iterable*** structure, such as a `list`, `tuple`, `str`, `set`, `dict`, or `file` (we will discuss
iterators more formally in Section [Iteration](#iterators-and-generators)). Its general syntax appears as follows.

```python
for element in iterable:
    body        # body may refer to element as an identifier
```

For readers familiar with Java, the semantics of Python’s for loop is similar to the
"for each" loop style introduced in Java 1.5.

As an instructive example of such a loop, we consider the task of computing the sum of a list of numbers. (Admittedly, Python has a built-in function, sum, for this purpose.) We perform the calculation with a for loop as follows, assuming that data identifies the list

```python
total = 0
for val in data:
    total += val        # note use of the loop variable, val
```

The loop body executes once for each element of the data sequence, with the identifier, val, from the for-loop syntax assigned at the beginning of each pass to a respective element. It is worth noting that `val` is treated as a standard identifier. If the element of the original data happens to be mutable, the `val` identifier can be used to invoke its methods. But a reassignment of identifier `val` to a new value has no affect on the original `data`, nor on the next iteration of the loop.

As a second classic example, we consider the task of finding the maximum value in a list of elements (again, admitting that Python’s built-in `max` function already provides this support). If we can assume that the list, data, has at least one element, we could implement this task as follows

```python
biggest = data[0]       # as we assume nonempty list
for val in data:
    if val > biggest:
        biggest = val
```

Although we could accomplish both of the above tasks with a while loop, the for-loop syntax had an advantage of simplicity, as there is no need to manage an explicit index into the list nor to author a Boolean loop condition. Furthermore, we can use a for loop in cases for which a while loop does not apply, such as when iterating through a collection, such as a set, that does not support any direct form of indexing.

##### Index-Based For Loops

The simplicity of a standard for loop over the elements of a list is wonderful; however, one limitation of that form is that we do not know where an element resides within the sequence. In some applications, we need knowledge of the index of an element within the sequence. For example, suppose that we want to know *where* the maximum element in a list resides.

Rather than directly looping over the elements of the list in that case, we prefer to loop over all possible indices of the list. For this purpose, Python provides a built-in class named `range` that generates integer sequences. (We will discuss generators in Section [Generators and Iterators](#iterators-and-generators).) In simplest form, the syntax `range(n)` generates the series of `n` values from `0` to `n − 1`. Conveniently, these are precisely the series of
valid indices into a sequence of length `n`. Therefore, a standard Python idiom for looping through the series of indices of a data sequence uses a syntax

```python
for j in range(len(data)):
```

In this case, identifier `j` is not an element of the `data`—it is an integer. But the expression `data[j]` can be used to retrieve the respective element. For example, we can find the index of the maximum element of a list as follows

```python
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j
```

##### Break and Continue Statements

Python supports a `break` statement that immediately terminate a while or for loop when executed within its body. More formally, if applied within nested control structures, it causes the termination of the most immediately enclosing loop. As a typical example, here is code that determines whether a target value occurs in a data set

```python
found = False
for item in data:
    if item == target:
        found = True
        break
```

Python also supports a continue statement that causes the current *iteration* of a loop body to stop, but with subsequent passes of the loop proceeding as expected.

We recommend that the break and continue statements be used sparingly. Yet, there are situations in which these commands can be effectively used to avoid introducing overly complex logical conditions.

## Functions

In this section, we explore the creation of and use of functions in Python. As we
did in Section [Creating and Using Objects](#creating-and-using-objects), we draw a distinction between ***functions*** and ***methods***. We use the general term *function* to describe a traditional, stateless function that is invoked without the context of a particular class or an instance of that class, such as `sorted(data)`. We use the more specific term *method* to describe a member function that is invoked upon a specific object using an object-oriented message passing syntax, such as `data.sort()`. In this section, we only consider pure functions; methods will be explored with more general object-oriented principles in [Object Oriented Programming](#object-oriented-programming).

We begin with an example to demonstrate the syntax for defining functions in Python. The following function counts the number of occurrences of a given target value within any form of iterable data set.

```python
def count(data, target):
    n = 0
    for item in data:
        if item == target:      # found a match
            n += 1
    return n
```

The first line, beginning with the keyword `def`, serves as the function’s ***signature***.
This establishes a new identifier as the name of the function (`count`, in this example), and it establishes the number of parameters that it expects, as well as names
identifying those parameters (`data` and `target`, in this example). Unlike Java and C++, Python is a dynamically typed language, and therefore a Python signature does not designate the types of those parameters, nor the type (if any) of a return value. Those expectations should be stated in the function’s ***documentation*** and can be enforced within the body of the function, but misuse of a function will only be detected at run-time.

The remainder of the function definition is known as the ***body*** of the function. As is the case with control structures in Python, the body of a function is typically expressed as an indented block of code. Each time a function is called, Python creates a dedicated ***activation record*** that stores information relevant to the current call. This activation record includes what is known as a ***namespace*** (see Section [Scopes and Namespaces](#scope-and-namespaces)) to manage all identifiers that have ***local scope*** within the current call. The namespace includes the function’s parameters and any other identifiers that are defined locally within the body of the function. An identifier in the local scope of the function caller has no relation to any identifier with the same name in the caller’s scope (although identifiers in different scopes may be aliases to the same object). In our first example, the identifier n has scope that is local to the function call, as does the identifier item, which is established as the loop variable.

### Return Statement

A `return` statement is used within the body of a function to indicate that the function should immediately cease execution, and that an expressed value should be returned to the caller. If a return statement is executed without an explicit argument, the None value is automatically returned. Likewise, None will be returned if the flow of control ever reaches the end of a function body without having executed a return statement. Often, a return statement will be the final command within the body of the function, as was the case in our earlier example of a count function. However, there can be multiple return statements in the same function, with conditional logic controlling which such command is executed, if any. As a further
example, consider the following function that tests if a value exists in a sequence.

```python
def contains(data, target):
    for item in target:
        if item == target:      # found a match
            return True
    return False
```

If the conditional within the loop body is ever satisfied, the return `True` statement is executed and the function immediately ends, with `True` designating that the target value was found. Conversely, if the for loop reaches its conclusion without ever finding the match, the final return `False` statement will be executed.

### Information Passing

To be a successful programmer, one must have clear understanding of the mechanism in which a programming language passes information to and from a function. In the context of a function signature, the identifiers used to describe the expected parameters are known as ***formal parameters***, and the objects sent by the caller when invoking the function are the ***actual parameters***. Parameter passing in Python follows the semantics of the standard ***assignment statement***. When a function is invoked, each identifier that serves as a formal parameter is assigned, in the function’s local scope, to the respective actual parameter that is provided by the caller of the function.

For example, consider the following call to our `count` function

```python
prizes = count(grades, `'A')
```

Just before the function body is executed, the actual parameters, `grades` and `'A'`, are implicitly assigned to the formal parameters, `data` and `target`, as follows

```python
data = grades
target = 'A'
```

These assignment statements establish identifier `data` as an ***alias*** for `grades` and
`target` as a name for the string literal `'A'`.

The communication of a return value from the function back to the caller is similarly implemented as an assignment. Therefore, with our sample invocation of `prizes = count(grades, 'A')`, the identifier prizes in the caller’s scope is assigned to the object that is identified as `n` in the return statement within our function body.

An advantage to Python’s mechanism for passing information to and from a function is that objects are not copied. This ensures that the invocation of a function is efficient, even in a case where a parameter or return value is a complex object.

#### Mutable Parameters

Python’s parameter passing model has additional implications when a parameter is a mutable object. Because the formal parameter is an alias for the actual parameter, the body of the function may interact with the object in ways that change its state. Considering again our sample invocation of the count function, if the body of the function executes the command `data.append('F')`, the new entry is added to the end of the list identified as data within the function, which is one and the same as the list known to the caller as `grades`. As an aside, we note that reassigning a new value to a formal parameter with a function body, such as by setting `data = []`, does not alter the actual parameter; such a reassignment simply breaks the alias.

Our hypothetical example of a `count` method that appends a new element to a list lacks common sense. There is no reason to expect such a behavior, and it would be quite a poor design to have such an unexpected effect on the parameter. There are, however, many legitimate cases in which a function may be designed (and clearly documented) to modify the state of a parameter. As a concrete example, we present the following implementation of a method named scale that’s primary
purpose is to multiply all entries of a numeric data set by a given factor.

```python
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
```

#### Default Parameter Values

Python provides means for functions to support more than one possible calling signature. Such a function is said to be ***polymorphic*** (which is Greek for "many forms"). Most notably, functions can declare one or more default values for parameters, thereby allowing the caller to invoke a function with varying numbers of actual parameters. As an artificial example, if a function is declared with signature

```python
def foo(a, b=15, c=27):
```

there are three parameters, the last two of which offer default values. A caller is welcome to send three actual parameters, as in `foo(4, 12, 8)`, in which case the default values are not used. If, on the other hand, the caller only sends one parameter, `foo(4)`, the function will execute with parameters values `a=4, b=15, c=27`. If a caller sends two parameters, they are assumed to be the first two, with the third being the default. Thus, `foo(8, 20)` executes with `a=8, b=20, c=27`. However, it is illegal to define a function with a signature such as `bar(a, b=15, c)` with `b` having a default value, yet not the subsequent `c`; if a default parameter value is present for one parameter, it must be present for all further parameters.

As an additional example of an interesting polymorphic function, we consider Python’s support for `range`. (Technically, this is a constructor for the `range` class, but for the sake of this discussion, we can treat it as a pure function.) Three calling syntaxes are supported. The one-parameter form, `range(n)`, generates a sequence of integers from `0` up to but not including `n`. A two-parameter form, `range(start,stop)` generates integers from `start` up to, but not including, `stop`. A three-parameter form, `range(start, stop, step)`, generates a similar range as `range(start, stop)`, but with increments of size `step` rather than 1.

This combination of forms seems to violate the rules for default parameters. In particular, when a single parameter is sent, as in `range(n)`, it serves as the stop value (which is the second parameter); the value of start is effectively 0 in that case. However, this effect can be achieved with some sleight of hand, as follows

```python
def range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    ...
```

From a technical perspective, when `range(n)` is invoked, the actual parameter `n` will be assigned to formal parameter start. Within the body, if only one parameter is received, the `start` and `stop` values are reassigned to provide the desired semantics.

#### Keyword Parameters

The traditional mechanism for matching the actual parameters sent by a caller, to the formal parameters declared by the function signature is based on the concept of ***positional arguments***. For example, with signature `foo(a=10, b=20, c=30)`, parameters sent by the caller are matched, in the given order, to the formal parameters. An invocation of `foo(5)` indicates that `a=5`, while `b` and `c` are assigned their default values.

Python supports an alternate mechanism for sending a parameter to a function known as a ***keyword argument***. A keyword argument is specified by explicitly assigning an actual parameter to a formal parameter by name. For example, with the above definition of function foo, a call `foo(c=5)` will invoke the function with parameters `a=10, b=20, c=5`.

A function’s author can require that certain parameters be sent only through the keyword-argument syntax. We never place such a restriction in our own function definitions, but we will see several important uses of keyword-only parameters in Python’s standard libraries. As an example, the built-in `max` function accepts a keyword parameter, coincidentally named `key`, that can be used to vary the notion of "maximum" that is used.

By default, max operates based upon the natural order of elements according to the `<` operator for that type. But the maximum can be computed by comparing some other aspect of the elements. This is done by providing an auxiliary *function* that converts a natural element to some other value for the sake of comparison. For example, if we are interested in finding a numeric value with *magnitude* that is maximal (i.e., considering `−35` to be larger than `+20`), we can use the calling syntax `max(a, b, key=abs)`. In this case, the built-in `abs` function is itself sent as the value associated with the keyword parameter `key`. (Functions are first-class objects
in Python). When `max` is called in this way, it will compare `abs(a)` to `abs(b)`, rather than `a` to `b`. The motivation for the keyword syntax as an alternate to positional arguments is important in the case of max. This function is polymorphic in the number of arguments, allowing a call such as `max(a,b,c,d)`; therefore, it is not possible to designate a `key` function as a traditional positional element. Sorting functions in Python also support a similar `key` parameter for indicating a nonstandard order.

### Python Built-in Functions

***Table*** below provides an overview of common functions that are automatically available in Python, including the previously discussed `abs`, `max`, and `range`. When choosing names for the parameters, we use identifiers `x`, `y`, `z` for arbitrary numeric types, `k` for an integer, and `a`, `b`, and `c` for arbitrary comparable types. We use the identifier, iterable, to represent an instance of any iterable type (e.g., `str`, `list`, `tuple`, `set`, `dict`); we will discuss iterators and iterable data types in Section [Iterators and Generator](#iterators-and-generators). A sequence represents a more narrow category of indexable classes, including `str`, `list`, and `tuple`, but neither `set` nor `dict`. Most of the entries in ***Table*** can be categorized according to their functionality as follows

- **Input/Output**: `print`, `input`, and `open`
- **Character Encoding**: `ord` and `chr` relate characters and their integer code points. For example, `ord('A')` is 65 and `chr(65)` is `'A'`.
- **Mathematics**: `abs`, `divmod`, `pow`, `round`, and `sum` provide common mathematical functionality; an additional `math` module
- **Ordering**: `max` and `min` apply to any data type that supports a notion of comparison, or to any `collection` of such values. Likewise, `sorted` can be used to produce an ordered list of elements drawn from any existing `collection`.
- **Collections/Iterations**: `range` generates a new sequence of numbers; `len` reports the length of any existing collection; functions `reversed`, `all`, `any`, and `map` operate on arbitrary iterations as well; `iter` and `next` provide a general framework for iteration through elements of a collection.

***Table***: Commonly used built-in function in Python

| **Calling Syntax** | **Description** |
| --- | --- |
| `abs(x)` | Return the absolute value of a number |
| `all(iterable)` | Return `True` if `bool(e)` is `True` for each element `e` |
| `any(iterable)` | Return `True` if `bool(e)` is `True` for at least one element `e` |
| `chr(integer)` | Return a one-character string with the given Unicode code point |
| `divmod(x, y)` | Return `(x // y, x % y)` as tuple, if `x` and `y` are integers |
| `hash(obj)` | Return an integer hash value for the object |
| `id(obj)` | Return the unique integer serving as an "identity" for the object |
| `input(prompt)` | Return a string from standard input; the prompt is optional |
| `isinstance(obj, cls)` | Determine if obj is an instance of the class (or a subclass) |
| `iter(iterable)` | Return a new iterator object for the parameter |
| `len(iterable)` | Return the number of elements in the given iteration |
| `map(f, iter1, iter2, ...)` | Return an iterator yielding the result of function calls `f(e1, e2, ...)` for respective elements `e1 ∈ iter1,e2 ∈ iter2,...` |
| `max(iterable)` | Return the largest element of the given iteration |
| `max(a, b, c, ...)` | Return the largest of the arguments |
| `min(iterable)` | Return the smallest element of the given iteration |
| `min(a, b, c, ...)` | Return the smallest of the arguments |
| `next(iterator)` | Return the next element reported by the iterator |
| `open(filename, mode)` | Open a file with the given name and access mode |
| `ord(char)` | Return the Unicode code point of the given character |
| `pow(x, y)` | Return the value `x^y` (as an integer if `x` and `y` are integers); equivalent to `x ** y` |
| `pow(x, y, z)` | Return the value (`x^y mod z`) as an integer |
| `print(obj1, obj2, ...)` | Print the arguments, with separating spaces and trailing newline |
| `range(stop)` | Construct an iteration of values `0, 1, ..., stop − 1` |
| `range(start, stop)` | Construct an iteration of values `start, start+1, ..., stop − 1` |
| `range(start, stop, step)` | Construct an iteration of values `start, start+step, start+2 * step, ...` |
| `reversed(sequence)` | Return an iteration of the sequence in reverse |
| `round(x)` | Return the nearest int value (a tie is broken toward the even value) |
| `round(x, k)` | Return the value rounded to the nearest `10^(-k)` (return-type matches `x`) |
| `sorted(iterable)` | Return a list containing elements of the iterable in sorted order |
| `sum(iterable)` | Return the sum of the elements in the iterable (must be numeric) |
| `type(obj)` | Return the class to which the instance obj belongs |

## Simple Input and Output

### Console Input and Output

### Files

## Exceptions Handling

### Raising an Exception

### Catching an Exception

## Iterators and Generators

## Additional Python Conveniences

## Scope and Namespaces

## Modules and the `Import` Statement

### Existing Modules

## Object-Oriented Programming

## Algorithm Analysis

## Data Structures and Algorithms

### Data Structures

### Algorithms
