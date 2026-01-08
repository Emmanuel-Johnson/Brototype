List comprehension is a concise and readable way to create lists in Python using a single line of code instead of traditional loops. It lets you transform, filter, or generate lists efficiently.

## Basic syntax
```python
new_list = [expression for item in iterable]
```

Equivalent:
```python
new_list = []
for item in iterable:
    new_list.append(expression)
```

## Example 1 — Square of numbers
```python
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
print(squares)
```
Output:
```
[1, 4, 9, 16]
```

## Adding conditions (filtering)
```python
evens = [n for n in nums if n % 2 == 0]
print(evens)
```
Output:
```
[2, 4]
```
Meaning: take n from nums only if n is even.

## Example 2 — String processing
```python
names = ["anna", "Bob", "cAt"]
upper_names = [name.upper() for name in names]
print(upper_names)
```
Output:
```
['ANNA', 'BOB', 'CAT']
```

## If–else in list comprehension
Use if–else before the for to produce conditional values:
```python
result = ["even" if n % 2 == 0 else "odd" for n in nums]
print(result)
```
Output:
```
['odd', 'even', 'odd', 'even']
```

Note: filter (if) goes at the end; conditional value (if–else) goes before the for.

## Nested list comprehension
Used for flattening or working with matrices:
```python
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)
```
Output:
```
[1, 2, 3, 4]
```
Evaluation order is left-to-right, like nested loops.

## Performance & readability
- Often faster than equivalent for-loops.
- More memory-efficient for simple transformations.
- For complex logic, regular loops are usually more readable.

## Interview best practice
Use list comprehensions for simple, clear transformations — avoid heavy business logic inside them.

## When NOT to use list comprehension
- Too complex conditions
- Multiple side effects
- Deep nesting (hurts readability)

> One-line interview summary:  
> "List comprehension is a Pythonic way to create lists using expressions and conditions in a single line, making code shorter, faster, and more readable."
