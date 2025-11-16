### 1. LIST 

A List in Python is an ordered, mutable collection that allows duplicate values. Since lists are mutable, you can freely add, update, or remove elements at any time. Lists preserve the insertion order, meaning elements appear in the same sequence you added them. They also support indexing, slicing, and can store multiple data types in the same list (e.g., integers, strings, floats, even other lists). Lists are dynamic — their size grows or shrinks automatically based on the operations you perform. Internally, Python lists are implemented as dynamic arrays, which makes access by index very fast (O(1)), but inserting or deleting in the middle slower (O(n)).

Because of these characteristics, lists are ideal when you want to maintain order and frequently modify values. They behave like a shopping list — you can add new items, remove wrong ones, reorder items, or update them easily.

| Method            | Description                       |
|-------------------|-----------------------------------|
| `append(x)`       | Add item at end                   |
| `insert(i, x)`    | Insert at index `i`               |
| `extend(iterable)`| Add multiple items                |
| `pop()`       | Remove and return element         |
| `remove(x)`       | Remove first matching value       |
| `sort()`          | Sort list in-place                |
| `reverse()`       | Reverse list                      |
| `index(x)`        | Return index of element           |
| `count(x)`        | Count occurrences                 |
| `clear()`         | Remove all items                  |
| `copy()`          | Shallow copy                      |

### 2. TUPLE 

A Tuple in Python is an ordered, immutable collection that allows duplicate values. Because tuples are immutable, their contents cannot be changed after creation — no adding, deleting, or modifying elements. This immutability makes tuples ideal for representing fixed or permanent data, such as coordinates, dates, configuration settings, or any values that must not be altered accidentally.

Tuples preserve insertion order and support indexing, slicing, and nesting, just like lists. Another key characteristic is that tuples can contain multiple data types, including lists or even other tuples. Since tuples are hashable (as long as all items inside are hashable), they can be used as dictionary keys or stored inside a set, which lists cannot do. Performance-wise, tuples are faster and more memory-efficient than lists because Python can optimize their storage internally due to their immutability.

| Method    | Description            |
|-----------|------------------------|
| `count(x)` | Count occurrences      |
| `index(x)` | Find index of element  |

### 3. SET 

A Set in Python is an unordered, mutable collection of unique elements, meaning it automatically removes duplicates and stores only one instance of each value. Since sets are unordered, they do not maintain insertion order (although elements may appear in a stable hashed order). Sets are implemented using a hash table, which allows extremely fast membership checking—operations like x in set typically run in O(1) time. Sets can store only hashable (immutable) objects as elements, such as integers, strings, and tuples, but cannot store lists or dictionaries.

Sets are highly optimized for mathematical operations, including union, intersection, difference, and symmetric difference, making them ideal for comparing datasets or extracting distinct items. They are often used for tasks like removing duplicates from a list, checking common elements between groups, filtering data, and performing fast lookups. 

| Method                   | Description                                      |
|--------------------------|--------------------------------------------------|
| `add(x)`                 | Add an element                                   |
| `remove(x)`              | Remove element (raises KeyError if missing)      |
| `discard(x)`             | Remove element (no error if missing)             |
| `pop()`                  | Remove and return an arbitrary element           |
| `clear()`                | Remove all elements                              |
| `union(s2)`              | Return a new set with elements from both sets    |
| `intersection(s2)`       | Return common elements                           |
| `difference(s2)`         | Return elements only in the first set            |
| `symmetric_difference(s2)` | Return elements in either set but not both     |
| `issubset(s2)`           | Check if all elements are in `s2`                |
| `issuperset(s2)`         | Check if set contains all elements of `s2`       |
| `isdisjoint(s2)`         | Check if no elements in common                   |
| `update(s2)`             | Add all elements from `s2` into the set          |

# 4. FROZENSET

A frozenset in Python is an immutable, unordered collection of unique, hashable elements, functioning as the read-only version of a regular set. Since a frozenset cannot be modified after creation, it does not support methods like add(), remove(), or update(). This immutability makes frozensets hashable, allowing them to be used as dictionary keys or stored inside other sets, which is impossible with regular sets. Like normal sets, frozensets provide fast membership testing and support all non-mutating set operations such as union, intersection, difference, and symmetric_difference, each returning a new set or frozenset without altering the original.

Frozensets are particularly useful when you need the benefits of a set—such as uniqueness, mathematical operations, and O(1) average lookup time—but also require the data to remain fixed, safe, and protected from accidental modification. They are ideal for representing constant groups of values, configuration flags, permission sets, or any data that must remain unchanged throughout the program.

| Method                     | Description                                    |
|----------------------------|------------------------------------------------|
| `copy()`                  | Returns a shallow copy (same object since immutable) |
| `union(s2)`               | Returns a new set that is the union            |
| `intersection(s2)`        | Common elements                                |
| `difference(s2)`          | Elements in first but not second               |
| `symmetric_difference(s2)`| Elements in either set, not both               |
| `issubset(s2)`            | Check if subset                                |
| `issuperset(s2)`          | Check if superset                              |
| `isdisjoint(s2)`          | Check if no common elements                    |

### 5. STRING 

A String in Python is an immutable, ordered collection of characters. Because strings are immutable, they cannot be modified after creation—any operation that appears to change a string actually creates a new string object in memory. Strings support indexing, slicing, and iteration, making it easy to access individual characters or extract substrings. They can contain letters, digits, symbols, and spaces, and are stored as sequences of Unicode characters, giving them excellent international language support.

Python strings come with a wide range of built-in methods for tasks like searching (find, index), text transformation (upper, lower, capitalize), splitting and joining (split, join), formatting (format, replace), and validation (isalpha, isdigit, isalnum). Since strings are hashable, they can be used as dictionary keys or stored inside sets.

Strings are one of the most commonly used data types in Python and are essential for handling user input, file content, API responses, messages, identifiers, and any kind of textual information. Their immutability ensures safety, consistency, and optimized performance in repeated operations.

| Method          | Description                     |
|-----------------|---------------------------------|
| `upper()`       | Convert to uppercase            |
| `lower()`       | Convert to lowercase            |
| `capitalize()`  | Capitalize first letter         |
| `title()`       | Capitalize each word            |
| `strip()`       | Remove leading/trailing spaces  |
| `split()`       | Split into list                 |
| `join(iterable)`| Join list into string           |
| `replace(a, b)` | Replace substring               |
| `find()`        | Return index of substring       |
| `count()`       | Count occurrences               |
| `startswith()`  | Check prefix                    |
| `endswith()`    | Check suffix                    |
| `isdigit()`     | All digits?                     |
| `isalpha()`     | All letters?                    |
| `isalnum()`     | Letters + digits?               |

### 6. DICTIONARY 

A Dictionary in Python is a collection of key–value pairs that allows extremely fast lookups because it is implemented using a hash table internally. Dictionaries are mutable, so you can add, update, or delete key–value pairs at any time. Keys must be unique, immutable, and hashable (e.g., strings, numbers, tuples), while values can be of any data type, including lists or even other dictionaries. Dictionary items are stored in insertion order (from Python 3.7+), and you can access values in O(1) average time if you know the key.

Dictionaries support indexing by key, not by position, and allow nested structures, making them very flexible. They are ideal when you need to quickly access data using a unique identifier, such as storing user details, caching results, or mapping IDs to objects. A dictionary works exactly like a phonebook: the name is the key, and the phone number is the value.

| Method                        | Description                           |
|-------------------------------|---------------------------------------|
| `get(key, default)`           | Safely get value                      |
| `keys()`                      | Return all keys                       |
| `values()`                    | Return all values                     |
| `items()`                     | Return key–value pairs                |
| `pop(key)`                    | Remove a key and return value         |
| `popitem()`                   | Remove last added pair                |
| `update(dict2)`               | Merge another dictionary              |
| `setdefault(key, default)`    | Insert with default if missing        |
| `clear()`                     | Remove all items                      |
| `copy()`                      | Shallow copy                          |
