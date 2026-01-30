# Character Encoding

## What is Character Encoding?

**Character encoding** is a way to convert characters (`A`, `1`, `@`, `😊`) into numbers so computers can store and process them.

👉 Computers understand only **binary (0s and 1s)**
👉 Therefore, every character must be represented by a **numeric code**

---

## Simple Example

| Character | Number | Binary   |
| --------- | ------ | -------- |
| 'A'       | 65     | 01000001 |
| 'B'       | 66     | 01000010 |

So when you type **A**, the computer actually stores **65**.

---

## Why Character Encoding is Needed

* Computers store only numbers
* Text contains letters, symbols, and emojis
* Encoding creates a **mapping between characters and numbers**

---

## Common Character Encodings

### 1️⃣ ASCII

**Full form:** American Standard Code for Information Interchange

* Uses **7 bits**
* Supports **128 characters**
* Includes:

  * English letters (`A–Z`, `a–z`)
  * Digits (`0–9`)
  * Basic symbols

**Examples:**

* `'A'` = 65
* `'a'` = 97
* `'0'` = 48

❌ Does **not** support emojis or non-English languages

---

### 2️⃣ Unicode

**Unicode** is a global standard that supports **all languages and emojis** 🌍

Supports:

* English
* Indian languages
* Arabic, Chinese, etc.
* Emojis 😄🔥

**Examples:**

* `'A'` → `U+0041`
* `'😊'` → `U+1F60A`

👉 Unicode is a **character set**, not a storage format

---

### 3️⃣ UTF (Unicode Transformation Format)

UTF defines **how Unicode characters are stored in bytes**.

#### UTF-8 (Most Important ⭐)

* Uses **1 to 4 bytes**
* Backward compatible with ASCII
* Most widely used encoding on the web

**Examples:**

* `'A'` → 1 byte
* `'ह'` → 3 bytes
* `'😊'` → 4 bytes

✅ Efficient
✅ Supports all characters

---

## ASCII vs Unicode vs UTF-8

| Feature                | ASCII | Unicode      | UTF-8 |
| ---------------------- | ----- | ------------ | ----- |
| Supports English       | ✅     | ✅            | ✅     |
| Supports all languages | ❌     | ✅            | ✅     |
| Supports emojis        | ❌     | ✅            | ✅     |
| Bytes used             | 1     | Fixed number | 1–4   |
| Used today             | ❌     | Concept      | ✅     |

---

## Real-Life Example 💡

```
Hello → H�llo
```

This happens when:

* File is saved in **UTF-8**
* File is read as **ASCII**

👉 This is called an **encoding mismatch**

---

## One-Line Definition (Exam Ready 🎯)

> **Character encoding is the method of mapping characters to numeric values so computers can store and process text.**
