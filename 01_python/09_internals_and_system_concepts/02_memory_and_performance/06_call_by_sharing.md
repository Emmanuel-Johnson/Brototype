> **Python uses a parameter-passing mechanism called _call by sharing_.**

When a value is passed to a function in Python:
- The function does **not** receive a copy of the object  
- It is **not** true call by reference either  

Instead, Python passes a **reference to the object**, and this reference is **shared** between the caller and the function.

---

## 🔹 What Exactly Is Shared?

👉 The **reference to the object** is shared — **not the variable itself**.

That means:
- The function parameter and the original variable initially point to the **same object**
- Python **never copies objects automatically** when passing arguments

---

## 🔹 Effect on Mutable Objects

If the object is **mutable** (list, dict, set):

- The function can **modify the object in place**
- Changes are visible outside the function because both references point to the same object

### Example
```python
def add_item(lst):
    lst.append(10)

a = [1, 2, 3]
add_item(a)
print(a)
```

**Output**
```text
[1, 2, 3, 10]
```

📌 The list is modified, so the change is reflected outside the function.

---

## 🔹 Effect on Immutable Objects

If the object is **immutable** (int, str, float, tuple):

- The object **cannot be modified**
- Any “modification” creates a **new object**
- The function parameter is simply **rebound** to that new object

### Example
```python
def increment(x):
    x = x + 1

n = 5
increment(n)
print(n)
```

**Output**
```text
5
```

📌 The original value remains unchanged.

---

## 🔹 Reassignment vs Modification (Very Important ⚠️)

Even for mutable objects, **reassignment does NOT affect the caller**.

- **Modification** → affects the original object  
- **Reassignment** → changes only the local reference  

### Example
```python
def change_list(lst):
    lst = [9, 9, 9]

a = [1, 2, 3]
change_list(a)
print(a)
```

**Output**
```text
[1, 2, 3]
```

📌 The list was **reassigned**, not modified.

---

## 🔹 Key Takeaways

- Python uses **call by sharing**
- A **reference to the object** is passed
- **Modification** affects the original object
- **Reassignment** never affects the original reference
- **Immutability prevents modification**

---

## 🧠 One-Line Interview Summary 🏆

> **Python is neither call by value nor call by reference; it uses call by sharing, where references are passed and object mutability determines whether changes are visible outside the function.**