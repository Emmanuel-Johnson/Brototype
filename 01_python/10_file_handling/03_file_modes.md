## What Are File Modes in Python?

In Python, file modes define **how a file is opened and what operations are allowed** on it.
They are passed as the second argument to the built-in `open()` function and control whether a file is read, written, appended, or created.

---

## Why File Modes Matter

Choosing the correct file mode is important because it affects:

- Whether data is preserved or overwritten  
- Whether the file must already exist  
- What operations — read or write — are permitted  

---

## 1. Read Mode – `'r'`

The `'r'` mode is used to **read an existing file**.

```python
file = open("data.txt", "r")
```

- If the file does not exist, Python raises a `FileNotFoundError`  
- This mode does **not** allow writing  

---

## 2. Write Mode – `'w'`

The `'w'` mode is used to **write data to a file**.

```python
file = open("data.txt", "w")
```

- If the file exists, its content is **overwritten**  
- If it does not exist, Python **creates a new file**  

---

## 3. Append Mode – `'a'`

Append mode adds data to the **end of a file** without removing existing content.

```python
file = open("data.txt", "a")
```

This mode is commonly used for **logging and audit files**.

---

## 4. Exclusive Creation Mode – `'x'`

The `'x'` mode is used to create a file **only if it does not already exist**.

```python
file = open("data.txt", "x")
```

- If the file exists, Python raises a `FileExistsError`  
- This helps prevent accidental overwrites  

---

## 5. Read and Write Modes – `'r+'`, `'w+'`, `'a+'`

Python also supports **combined modes** for both reading and writing:

- `'r+'` → read and write, file **must exist**  
- `'w+'` → write and read, **overwrites existing file**  
- `'a+'` → append and read, **creates file if needed**  

```python
file = open("data.txt", "r+")
```

---

## 6. Binary vs Text Modes

By default, files are opened in **text mode**.
Binary mode is used when working with images, audio, or video files.

- Text mode → `'r'`, `'w'`, `'a'`  
- Binary mode → `'rb'`, `'wb'`, `'ab'`  

```python
file = open("image.png", "rb")
```

---

## Best Practice Tip

In real-world applications, always use the `with` statement so the file is closed automatically.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

## Strong Interview Closing

> To summarize, file modes in Python define how a file is accessed.  
> `'r'` is for reading, `'w'` for writing, `'a'` for appending, `'x'` for exclusive creation, and combined modes like `'r+'` allow both reading and writing.  
> Choosing the correct mode ensures safe and efficient file handling.