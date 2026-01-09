A generator is a special function that produces values one at a time using `yield` instead of `return`. The key benefit is memory efficiency — values are generated lazily, only when needed.

## Generator Basics
- Use `yield` to pause and resume execution.
- Generators are ideal for large or infinite sequences and streaming data.

---

## Example: Count Up to n

Normal generator function:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Usage:

```python
for num in count_up_to(5):
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

Interview explanation: This generator yields numbers from 1 to `n` one by one. Each `yield` pauses execution and resumes from the same state on the next call.

---

## Infinite Fibonacci Generator

Generator function:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

Usage (important: limit it!):

```python
fib = fibonacci()
for _ in range(7):
    print(next(fib))
```

Output:
```
0
1
1
2
3
5
8
```

Interview explanation: This is an infinite generator; it never ends. Generators are ideal here because they don't store all Fibonacci values in memory.

---

## Generator vs Normal Function

| Normal Function | Generator        |
|-----------------|------------------|
| Uses `return`   | Uses `yield`     |
| Executes fully  | Pauses & resumes |
| Stores all data | Generates on demand |
| High memory     | Memory efficient |

---

## Generator Using a Class (Iterator Protocol)

In interviews, this is a bonus advanced answer. A class-based generator must implement `__iter__()` and `__next__()`.

Class-based Count Up to n:

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
for num in CountUpTo(5):
    print(num)
```

Class-based Fibonacci generator:

```python
class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value
```

Usage:

```python
fib = Fibonacci()
for _ in range(6):
    print(next(fib))
```

---

## When to Use Generators 
- Large datasets
- Infinite sequences
- Streaming data
- Performance & memory optimization

> One-line interview summary: Generators produce values lazily using `yield`, saving memory, and can be implemented using functions or classes via the iterator protocol.