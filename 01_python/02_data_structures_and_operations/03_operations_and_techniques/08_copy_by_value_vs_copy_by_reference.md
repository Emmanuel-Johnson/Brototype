In Python, variables store references to objects in memory. Whether something behaves like “copy by value” or “copy by reference” depends on object mutability.

## 1️⃣ Copy by Value (Immutable Objects)

Immutable types (examples): `int`, `float`, `str`, `tuple`, `frozenset`.

When you assign one variable to another both refer to the same object initially, but modifications create new objects.

```python
a = 10
b = a
b = 20

# a == 10
# b == 20
```

> Interview line: “Immutable objects behave like copy by value because changes create new objects.”

## 2️⃣ Copy by Reference (Mutable Objects)

Mutable types (examples): `list`, `dict`, `set`, custom class instances.

Assigning one variable to another makes both point to the same object; mutating via one reference is visible through the other.

```python
a = [1, 2, 3]
b = a
b.append(4)

# a -> [1, 2, 3, 4]
# b -> [1, 2, 3, 4]
```

> Interview line: “Mutable objects behave like copy by reference because the same object is modified.”

## 3️⃣ How to Actually Create a Copy

### Shallow copy
Creates a new outer object; nested/inner objects are still shared.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

# a is b           -> False
# a[0] is b[0]     -> True
```

### Deep copy
Creates a fully independent copy including nested objects.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

# a is b           -> False
# a[0] is b[0]     -> False
```

> Interview line: “Deep copy duplicates the entire object graph.”

## 4️⃣ Function Call Trap (Call by Object Reference)

Python passes object references. Mutability decides whether changes persist.

Mutable example:
```python
def modify(x):
    x.append(4)

lst = [1, 2, 3]
modify(lst)
# lst -> [1, 2, 3, 4]
```

Immutable example:
```python
def modify(x):
    x = x + 1

n = 10
modify(n)
# n -> 10
```

> Interview line: “Python passes object references; mutability determines whether changes persist.”

## 5️⃣ One-line Interview Summary

“Python doesn’t have true copy by value or copy by reference — it passes object references, and mutability determines behavior.”
