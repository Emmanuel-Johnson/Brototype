### 1. LIST 

A List in Python is an ordered, mutable collection that allows duplicate values. Because lists are mutable, you can add, update, or remove elements at any time. They are ideal when you want to maintain order and frequently modify values. Lists behave like a shopping list — you can keep adding items, deleting wrong ones, or rearranging them.

| Method            | Description                       |
|-------------------|-----------------------------------|
| `append(x)`       | Add item at end                   |
| `insert(i, x)`    | Insert at index `i`               |
| `extend(iterable)`| Add multiple items                |
| `pop(i=-1)`       | Remove and return element         |
| `remove(x)`       | Remove first matching value       |
| `sort()`          | Sort list in-place                |
| `reverse()`       | Reverse list                      |
| `index(x)`        | Return index of element           |
| `count(x)`        | Count occurrences                 |
| `clear()`         | Remove all items                  |
| `copy()`          | Shallow copy                      |

### 2. DICTIONARY 

A Dictionary is a collection of key–value pairs and provides extremely fast lookups because it uses a hash table internally. Dictionaries are mutable, keys must be unique, and values can be anything. They work like a phonebook where the name is the key and the phone number is the value. Dictionaries are perfect when you want to quickly access data using a unique identifier.

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

### 3. SET 

A Set is an unordered, mutable collection of unique elements. Because sets do not allow duplicates, they are used when uniqueness matters. They provide extremely fast membership checking, making them suitable for tasks like removing duplicates, checking common elements, or performing mathematical operations like union, intersection, and difference.

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

### 4. TUPLE 

A Tuple is an ordered, immutable collection that allows duplicate values. Because tuples cannot be changed after creation, they are ideal for storing permanent or fixed data such as coordinates, configuration values, or birthdates. Tuples are faster than lists and can be used as dictionary keys because they are hashable.

| Method    | Description            |
|-----------|------------------------|
| `count(x)` | Count occurrences      |
| `index(x)` | Find index of element  |

### 5. STRING 

A String is an immutable collection of characters. Since strings cannot be modified, every transformation creates a new string. Strings provide a variety of methods for searching, splitting, formatting, and validating text. They are widely used for handling user input, file data, and application messages.

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
