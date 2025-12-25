Truthiness and falsiness in Python basically refer to how values behave when evaluated in a Boolean context — like inside an if statement or a loop condition. Python doesn’t restrict conditions only to True or False; instead, any object can act as either truthy or falsy based on its value.

Let’s start with falsy values. These are values that Python automatically considers as False when checked in a Boolean expression. The common falsy values include:

The number zero: 0, 0.0, 0j

Empty data structures: empty string "", empty list [], empty tuple (), empty dictionary {}, empty set set(), empty range range(0)

The special objects: None and False itself

If any of these are used inside an if condition, the block will not execute because Python treats them as false.

For example:

if []:
    print("Yes")


This won’t print anything because an empty list is falsy.

Now, truthy values are simply everything else — any value that is not falsy. For example:

Non-zero numbers like 5, -3, 3.14

Non-empty sequences like "hello", [1,2,3], (10,), {'a':1}

Custom objects or instances unless they explicitly define boolean behavior

So:

if "hello":
    print("Runs!")


This will run because non-empty strings are truthy.

Why does Python do this?
It allows for clean, readable code. Instead of writing:

if len(my_list) > 0:


We can simply write:

if my_list:


This is especially useful in data-driven or loop-based code where emptiness or zero naturally implies "nothing to process".

Under the hood, Python determines this by using the special __bool__() or __len__() method on objects.

An object’s truthiness is determined first by its __bool__() method, and only if that method is not defined does Python fall back to using __len__(), where a length of zero makes the object falsy and a non-zero length makes it truthy. If both are defined, __bool__() takes priority, meaning if __bool__() returns False, the object is considered falsy even if __len__() returns a positive value; and if __bool__() returns True, the object is truthy even if __len__() returns zero. If neither method exists, the object is considered truthy by default.

Quick summary:

Truthy and falsy are about how Python treats values in boolean contexts. Empty, zero, or none-type values are falsy; everything else is truthy. This feature keeps Python code concise and expressive — and understanding it is essential for writing idiomatic Python.