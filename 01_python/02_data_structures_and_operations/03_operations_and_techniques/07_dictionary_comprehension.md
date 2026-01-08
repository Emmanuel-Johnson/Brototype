Dictionary comprehension is a concise, readable way to create or transform dictionaries from iterables (lists, tuples, strings, or other dictionaries).

## Basic syntax

```python
{key_expression: value_expression for item in iterable}
```

## Simple example

Create a dictionary of numbers and their squares:

```python
squares = {x: x * x for x in range(1, 6)}
# -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

- `x` becomes the key
- `x * x` becomes the value
- `range(1, 6)` is the iterable

## With a condition (filtering)

Filter items with `if`:

```python
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
# -> {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

## Transforming an existing dictionary

Modify values from another dictionary:

```python
prices = {"apple": 100, "banana": 40, "orange": 60}
updated_prices = {k: v + 10 for k, v in prices.items()}
# -> {'apple': 110, 'banana': 50, 'orange': 70}
```

- `.items()` yields key-value pairs
- `k, v` unpacks each pair

## Conditional values (if-else)

Use `if-else` inside the value expression to choose values:

```python
result = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
# -> {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
```

## Important interview point

- `if` at the end of the comprehension filters items.
- `if-else` inside the value expression changes the value.

## Practical example

Remove keys that start with vowels:

```python
data = {"apple": 1, "banana": 2, "orange": 3, "grape": 4}
filtered = {k: v for k, v in data.items() if k[0].lower() not in "aeiou"}
# -> {'banana': 2, 'grape': 4}
```

## Why dictionary comprehension matters

- Improves readability
- Reduces boilerplate
- Often faster than explicit loops
- Common in data processing and transformations

> One-line interview summary: Dictionary comprehension in Python creates or transforms dictionaries in a single, readable expression using key-value expressions and optional conditions.
