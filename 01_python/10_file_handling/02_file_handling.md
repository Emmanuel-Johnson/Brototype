File handling in Python allows us to **create, read, write, and modify files** stored on the system.
Python provides built-in functions that make file operations simple, safe, and efficient.

---

## 1. `open()` – Opening a File

The first step in file handling is opening a file.
Python uses the built-in `open()` function for this.

```python
file = open("data.txt", "r")
```

The `open()` function takes two main arguments:
- The file name  
- The mode in which the file is opened  

---

## Common File Modes

Some commonly used file modes are:

- `'r'` → read mode  
- `'w'` → write mode (creates or overwrites a file)  
- `'a'` → append mode (adds data without deleting existing content)  
- `'x'` → exclusive creation  
- `'r+'` → read and write  

---

## 2. `read()` – Reading from a File

Once a file is opened in read mode, we can use the `read()` method to read its contents.

```python
file = open("data.txt", "r")
content = file.read()
print(content)
```

- `read()` reads the entire file at once  
- Python also provides `readline()` and `readlines()` for line-by-line reading  

---

## 3. `write()` – Writing to a File

To write data into a file, we open it in write mode using `'w'`.

```python
file = open("data.txt", "w")
file.write("Hello, Python")
file.close()
```

- If the file already exists, its content is overwritten  
- If it doesn’t exist, Python automatically creates it  

---

## 4. `append()` – Appending to a File

Appending means adding new data without removing existing content.
This is done using append mode `'a'`.

```python
file = open("data.txt", "a")
file.write("\nNew line added")
file.close()
```

Append mode is commonly used in **logging and audit files**.

---

## 5. `close()` – Closing a File

After file operations, it’s important to close the file using `close()`.

```python
file.close()
```

Closing a file:
- Releases system resources  
- Ensures data is properly written  
- Prevents file corruption  

---

## Best Practice: Using the `with` Statement

In real-world applications, we prefer the `with` statement because it automatically closes the file.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

This makes the code **cleaner and safer**.

---

## Final Interview Summary (Strong Ending)

> In Python, file handling is done using the `open()` function with different modes.  
> We use `read()` to read data, `write()` to overwrite or create files, `append()` to add data, and `close()` to release resources.  
> For safe and clean code, the `with` statement is the recommended approach.