In Python, file creation and deletion are commonly handled using built-in functions and the `os` module.
These operations are essential for tasks like **logging, data processing, and automation**.

---

## 1. Creating a File in Python

Python allows us to create files using the built-in `open()` function.
If the file does not already exist, Python automatically creates it.

### Example

```python
file = open("example.txt", "w")
file.write("Hello, Python!")
file.close()
```

Explanation:
- The file is opened in **write mode (`'w'`)**
- If the file does not exist, it is created  
- If it already exists, its contents are **overwritten**

---

## Common File Modes

Some commonly used file modes are:

- `'w'` → create or overwrite a file  
- `'a'` → create or append to a file  
- `'x'` → create a file, but raise an error if it already exists  
- `'r'` → read an existing file  

### Safe Creation Using `'x'`

```python
open("data.txt", "x")
```

This is useful when you want to ensure the file is created **only once**.

---

## Using the `with` Statement (Best Practice)

In real-world applications, we usually use the `with` statement.
It automatically closes the file, even if an error occurs.

```python
with open("notes.txt", "w") as file:
    file.write("File created safely")
```

---

## 2. Removing a File in Python

To delete a file, Python provides the `remove()` function inside the `os` module.

```python
import os
os.remove("example.txt")
```

This permanently deletes the file from the system.

---

## Handling File Deletion Safely

If the file does not exist, `os.remove()` raises a `FileNotFoundError`.
So it’s important to handle this safely.

```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("File not found")
```

---

## Interview Tip (Important)

File operations interact directly with the operating system, so always:

- Check if the file exists  
- Use exception handling  
- Prefer the `with` statement for safety  

---

## Final One-Line Summary (Interview Gold)

> In Python, files are created using `open()` with modes like `'w'`, `'a'`, or `'x'`, and files are removed using `os.remove()`, usually with proper error handling to ensure safe file operations.