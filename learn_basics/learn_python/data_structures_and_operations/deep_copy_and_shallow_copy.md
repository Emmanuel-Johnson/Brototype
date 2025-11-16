# 1. Copy by value and copy by reference

Python does not strictly use “copy by value” or “copy by reference” like some other languages; instead, it uses a model called pass-by-object-reference (or pass-by-assignment). This means that variables in Python do not store the actual data — they store references (labels) to objects in memory. Whether changes affect other variables depends on whether the underlying object is immutable or mutable. Immutable types like integers, strings, tuples, and booleans cannot be modified—any operation on them creates a new object. So when two variables reference the same immutable object and one is reassigned, the other remains unchanged. This behavior often looks like copy-by-value, but it is simply reassignment to a new object. Mutable types like lists, dictionaries, and sets can be modified in place. So if two variables reference the same mutable object and you modify it — for example using .append(), .update(), or item assignment — the change is visible through both variables. This is why Python appears to behave like “copy by reference” for mutable types.

# 2. Shallow Copy (copy.copy)

In Python, a shallow copy creates a new top-level object but does not create independent copies of the nested objects inside it. This means only the outer container is duplicated, while all inner mutable objects—such as lists, dictionaries, or sets—are still shared references between the original and the copied object. So, modifying the outer structure (like adding or removing items) does not affect the original, but modifying nested objects (like changing an element inside a list of lists or a dictionary inside a dictionary) will affect both. Shallow copies can be created using copy.copy(), slicing (list[:]), constructors (list(), dict()), or some built-in methods. Because they are faster and use less memory, shallow copies are useful when your data contains only immutable objects or when shared references to nested objects are acceptable.

# 3. Deep Copy (copy.deepcopy)

A deep copy solves the shared-reference problem by recursively copying every level of the object—including all nested mutable objects—creating a completely independent clone of the original structure. With copy.deepcopy(), changes made to any part of the deep-copied object (outer or inner) never affect the original. Deep copy is essential when working with complex nested structures like lists of lists, dictionaries containing lists, or objects containing other objects. Although it is slower and uses more memory than shallow copy, it ensures full independence and prevents hard-to-debug shared reference issues.

# Importing 

from copy import copy, deepcopy