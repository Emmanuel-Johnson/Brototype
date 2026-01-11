## What is `match-case` in Python?

In Python **3.10 and above**, the `match-case` statement is a **structural pattern matching** feature.

It is similar to a `switch-case` in other languages, but **more powerful and expressive**.

We use `match-case` when we want to compare a single value against multiple patterns and execute different blocks of code based on which pattern matches.

---

## Basic Syntax

```python
match value:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

The underscore `_` acts as a **default case**, similar to `else`.

---

## Simple Example

```python
status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")
```

This is cleaner and more readable than using multiple `if-elif-else` statements.

---

## Matching Multiple Values

```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
```

Here, the pipe `|` works like a logical **OR**.

---

## Pattern Matching with Data Structures

One big advantage of `match-case` is that it can match **structures**, not just values.

```python
point = (0, 5)

match point:
    case (0, y):
        print(f"On Y axis at {y}")
    case (x, 0):
        print(f"On X axis at {x}")
    case (x, y):
        print(f"Point at {x}, {y}")
```

This kind of matching is **not possible** with traditional switch statements.

---

## Matching Dictionaries

```python
user = {"role": "admin", "active": True}

match user:
    case {"role": "admin", "active": True}:
        print("Active admin")
    case {"role": "user"}:
        print("Normal user")
    case _:
        print("Unknown")
```

This is extremely useful in **APIs, JSON handling, and backend logic**.

---

## Guards (Conditions)

We can also add conditions using `if`, called **guards**.

```python
age = 20

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")
```

---

## Why Use `match-case`? (Interview Answer)

- Improves readability  
- Reduces complex `if-elif` chains  
- Supports structural pattern matching  
- Very useful for APIs, state machines, and data parsing  

---

## Important Notes

- Available only from **Python 3.10+**  
- First matching case executes, others are skipped  
- No `break` needed (unlike `switch` in C/Java)  

---

## One-Line Summary (Interview Gold)

> Python’s `match-case` provides powerful structural pattern matching, making complex conditional logic cleaner, safer, and more readable than traditional `if-elif-else` statements.