“In Python, an iterator is an object that allows traversal through a sequence of elements one at a time.”

## 1. What is an iterator?
An iterator is any object that implements two special methods:

- `__iter__()` — returns the iterator object itself  
- `__next__()` — returns the next value from the sequence and raises `StopIteration` when exhausted

In short:
- Iterable → something you can loop over  
- Iterator → the object that remembers state and yields values one by one

Examples of iterable objects: lists, tuples, strings, files, generators. Note: generators and file objects are iterators (they implement `__next__()`), while lists/tuples/strings are iterable (they produce iterators via `iter()`).

## 2. Iterable vs Iterator (quick)
An iterable is an object that can return an iterator using `iter()`; an iterator is the object that produces values using `next()`.

Example:
```python
nums = [1, 2, 3]      # iterable
it = iter(nums)      # iterator

print(next(it))  # 1
print(next(it))  # 2
```

## 3. How `for` loop uses iterators
When you write:
```python
for x in data:
    print(x)
```
Python internally:
- Calls `iter(data)` to get an iterator
- Repeatedly calls `next()` on that iterator
- Stops automatically when `StopIteration` is raised

## 4. Custom iterator implementation
Create a custom iterator by implementing `__iter__` and `__next__`.

Example — count numbers from 1 to `n`:
```python
class CountUpTo:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
```

Usage:
```python
counter = CountUpTo(5)

for num in counter:
    print(num)
```
Output:
```
1
2
3
4
5
```

## 5. Key points
- `__iter__()` often returns `self`, making the object its own iterator  
- `__next__()` maintains iteration state (e.g., `self.current`)  
- `StopIteration` signals the end of iteration  
- Works seamlessly with `for` loops and `next()`

## 6. Why iterators matter
- Memory efficient (generate values on demand)  
- Ideal for large datasets and streaming data  
- Avoid loading everything into memory at once

## 7. Iterator vs Generator (one-line)
- Iterator → class implementing `__iter__` and `__next__`  
- Generator → function using `yield` (creates an iterator)

> Final summary: An iterator in Python follows the iterator protocol by implementing `__iter__()` and `__next__()`. It provides sequential access to elements, raises `StopIteration` when exhausted, and enables memory-efficient, on-demand value generation.
