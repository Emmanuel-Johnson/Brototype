# 🔹 LIKE and ILIKE in PostgreSQL

## What are LIKE and ILIKE?

They are used for **pattern matching on text**.

| Operator | Case‑sensitive?        |
| -------- | ---------------------- |
| LIKE     | ✅ Yes                  |
| ILIKE    | ❌ No (PostgreSQL‑only) |

---

## 🧩 Wildcards (Very Important)

| Symbol | Meaning                  | Example |
| ------ | ------------------------ | ------- |
| %      | any number of characters | `'A%'`  |
| _      | exactly one character    | `'A_'`  |

---

## 1️⃣ LIKE (Case‑Sensitive)

```sql
SELECT *
FROM users
WHERE name LIKE 'A%';
```

✔ Matches: `Alex`, `Adam`
❌ Does NOT match: `alex`

### Ends with

```sql
WHERE email LIKE '%@gmail.com';
```

### Contains

```sql
WHERE name LIKE '%son%';
```

### Single character `_`

```sql
WHERE code LIKE 'A_1';
```

Matches:

* `A21`
* `A31`

---

## 2️⃣ ILIKE (Case‑Insensitive)

```sql
SELECT *
FROM users
WHERE name ILIKE 'a%';
```

✔ Matches: `Alex`, `alex`, `ALAN`

📌 PostgreSQL feature (not standard SQL)

---

## 3️⃣ NOT LIKE / NOT ILIKE

```sql
WHERE name NOT LIKE 'A%';
```

```sql
WHERE email NOT ILIKE '%spam%';
```

⚠️ Rows with `NULL` values are excluded

---

## ⚠️ LIKE + NULL Behavior

```sql
WHERE name LIKE 'A%';
```

If `name` is `NULL` → row is excluded

Because:

```
NULL LIKE 'A%' → UNKNOWN
```

---

## 4️⃣ LIKE with Numbers (Implicit Cast)

```sql
WHERE phone LIKE '98%';
```

✔ Works **only if column is text**
❌ Avoid on numeric columns (bad for indexes)

---

## 5️⃣ Performance Tips (Interview Gold 🥇)

### Index works ✅

```sql
WHERE name LIKE 'A%';
```

### Index NOT used ❌

```sql
WHERE name LIKE '%son';
WHERE name LIKE '%son%';
```

Because the pattern starts with `%`.

---

### 🔥 Faster Case‑Insensitive Search

Instead of:

```sql
WHERE name ILIKE 'a%';
```

Use:

```sql
WHERE LOWER(name) LIKE 'a%';
```

And create index:

```sql
CREATE INDEX idx_users_name_lower
ON users (LOWER(name));
```

---

## 6️⃣ LIKE vs SIMILAR TO vs Regex

| Feature         | Operator     |
| --------------- | ------------ |
| Simple patterns | LIKE / ILIKE |
| SQL regex       | SIMILAR TO   |
| Full regex      | `~`, `~*`    |

### Regex Example

```sql
WHERE name ~* '^a.*';
```

---

## 🧠 Interview Rules to Remember

* `LIKE` → case‑sensitive
* `ILIKE` → case‑insensitive (PostgreSQL)
* `%` = many characters, `_` = one character
* Leading `%` kills index usage
* `NULL` never matches
* Prefer `LIKE` over regex for simple cases

---

## ✅ One‑Line Summary

Use `LIKE` for simple text patterns, `ILIKE` when case doesn’t matter — but **avoid leading `%` if performance matters**.
