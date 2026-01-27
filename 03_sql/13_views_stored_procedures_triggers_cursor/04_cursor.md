# Cursors -- Complete Notes

## 1️⃣ What is a Cursor?

A **cursor** is a database object used to process query results **one
row at a time**.

📌 **Normally:** - SQL works on **sets of rows** (all at once)

📌 **Cursor:** - Lets you **iterate row-by-row**

**Exam-friendly definition:**

> A cursor is a pointer to the result set of a query that allows
> row-by-row processing.

📖 **Analogy:**

-   Normal SQL → Calculator (bulk processing)
-   Cursor → for-loop (one by one)

------------------------------------------------------------------------

## 2️⃣ Why Do We Need Cursors?

SQL is **set-based**, but sometimes you need:

-   Per-row logic
-   Conditional actions per record
-   Sequential processing

👉 That's where **cursors** come in.

------------------------------------------------------------------------

## 3️⃣ Cursor Use Cases 💡

### 🔹 1. Row-by-Row Processing

When logic depends on each individual row.

**Examples:** - Increase salary differently for each employee - Validate
rows one by one

------------------------------------------------------------------------

### 🔹 2. Complex Business Logic

When set-based SQL becomes messy or impossible.

**Examples:** - Nested conditions - Multiple dependent updates

------------------------------------------------------------------------

### 🔹 3. Data Migration / Cleanup

-   Move data row by row
-   Transform data before inserting

------------------------------------------------------------------------

### 🔹 4. Generating Reports Sequentially

-   Process ordered data
-   Accumulate running totals

------------------------------------------------------------------------

### 🔹 5. Calling Procedures Per Row

-   Loop through records
-   Call another stored procedure for each row

------------------------------------------------------------------------

## 4️⃣ Cursor vs Normal SQL (Very Important)

  Normal SQL   Cursor
  ------------ --------------------
  Set-based    Row-based
  Faster       Slower
  Less code    More control
  Preferred    Use only if needed

📌 **Golden rule:**

> Avoid cursors unless set-based SQL cannot solve the problem.

------------------------------------------------------------------------

## 5️⃣ Types of Cursors

-   **Implicit Cursor** -- Automatically created by the database
-   **Explicit Cursor** -- Defined and controlled by the programmer

------------------------------------------------------------------------

## 6️⃣ Key Exam Points 📝

-   Cursor processes **one row at a time**
-   Used inside **stored procedures / functions**
-   Slower than set-based queries
-   Should be used **carefully**