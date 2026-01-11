In Python, the `with` statement is used to work with files in a **safe and clean way**.
It automatically handles **resource management**, meaning the file is properly closed after use, even if an error occurs.

---

## Why We Use `with`

When we open files using `open()`, we must manually close them using `close()`.
If we forget to close a file, it can lead to:

- Memory leaks  
- File corruption  
- Locked system resources  

The `with` statement solves this problem by ensuring the file is **always closed automatically**.

---

## Basic Syntax

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

Here:
- `open()` returns a file object  
- The file object is assigned to `file`  
- Once the `with` block finishes, Python **automatically closes the file**  

---

## Reading a File Using `with`

To read a file safely, we open it in read mode.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

Even if an exception occurs while reading, the file is still closed.

---

## Writing to a File Using `with`

To write data, we open the file in write mode.

```python
with open("data.txt", "w") as file:
    file.write("Hello, Python")
```

- If the file exists, its contents are overwritten  
- If it doesn’t exist, Python creates a new file  

---

## Appending to a File Using `with`

Append mode allows us to add new data without removing existing content.

```python
with open("data.txt", "a") as file:
    file.write("\nNew line added")
```

This is commonly used in **logging systems**.

---

## Handling Errors Gracefully

The `with` statement internally uses **context management**.
It guarantees that cleanup code runs no matter what.

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
```

---

## Interview Insight (Important Point)

The `with` statement works because file objects implement special methods that handle setup and cleanup automatically.

This makes code:
- More readable  
- Safer  
- Less error-prone  

---

## Strong Interview Closing

> In summary, working with files using `with` is the recommended approach in Python.  
> It ensures files are properly closed, improves readability, and prevents resource leaks.  
> That’s why `with` is considered a best practice for file handling in real-world Python applications.