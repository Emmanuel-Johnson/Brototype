# Built-in Functions & Methods (Python)

## Common built-in functions (work on most data types)
These work on `list`, `tuple`, `set`, `dict`, `str`, etc.

- `len()` — number of elements  
- `type()` — data type  
- `sorted()` — returns a sorted list (does **not** modify original)  
- `min()` / `max()` — smallest / largest element  
- `sum()` — sum of numeric elements  
- `any()` — `True` if at least one element is truthy  
- `all()` — `True` if all elements are truthy  
- `enumerate()` — index + value pairs  
- `zip()` — combine multiple iterables  
- `reversed()` — reverse iterator

---

## List methods
Lists are mutable.

- `append(x)` — add element at end  
- `extend(iterable)` — add multiple elements  
- `insert(i, x)` — insert at index `i`  
- `remove(x)` — remove first occurrence of `x`  
- `pop(i)` — remove & return element at index `i` (default last)  
- `clear()` — remove all elements  
- `index(x)` — index of first occurrence  
- `count(x)` — frequency of `x`  
- `sort()` — in-place sort  
- `reverse()` — in-place reverse  
- `copy()` — shallow copy

> **Interview tip:** `sort()` modifies the list in-place; `sorted()` returns a new, sorted list.

---

## Tuple methods
Tuples are immutable, so fewer methods.

- `count(x)` — frequency of `x`  
- `index(x)` — index of first occurrence

> Immutability = fewer operations.

---

## Set methods
Sets store unique elements and are unordered.

Modification:
- `add(x)`  
- `update(iterable)`  
- `remove(x)` — raises `KeyError` if not found  
- `discard(x)` — no error if missing  
- `pop()` — removes and returns an arbitrary element  
- `clear()`

Mathematical operations:
- `union()`  
- `intersection()`  
- `difference()`  
- `symmetric_difference()`

Checks:
- `issubset()`  
- `issuperset()`  
- `isdisjoint()`

---

## Dictionary methods
Dictionaries store key → value pairs.

Access:
- `keys()`  
- `values()`  
- `items()`  
- `get(key, default)` — safe access with default

Modification:
- `update()`  
- `pop(key)`  
- `popitem()`  
- `setdefault()`  
- `clear()`  
- `copy()`

> **Interview trap:** `dict['key']` raises `KeyError` if missing; `dict.get('key')` returns `None` (or the provided default).

---

## String methods
Strings are immutable.

Case & checks:
- `upper()` / `lower()`  
- `capitalize()`  
- `title()`  
- `swapcase()`  
- `isalpha()` / `isdigit()` / `isalnum()`  
- `isspace()`

Search & replace:
- `find()`  
- `index()`  
- `replace()`  
- `count()`

Split & join:
- `split()` / `rsplit()`  
- `join(iterable)`

Trim:
- `strip()` / `lstrip()` / `rstrip()`

---

## Numeric types (`int`, `float`)
- `abs()` — absolute value  
- `round()` — rounding  
- `pow(a, b)` — power  
- `divmod(a, b)` — returns `(quotient, remainder)`

---

## Bonus: Type conversion functions
- `int()`  
- `float()`  
- `str()`  
- `list()`  
- `tuple()`  
- `set()`  
- `dict()`
