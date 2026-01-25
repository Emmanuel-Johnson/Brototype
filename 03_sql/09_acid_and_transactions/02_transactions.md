# Transactions & Isolation Levels in PostgreSQL 🔐

## 1️⃣ What is a Transaction?

A **transaction** is a group of SQL statements that are executed as
**one logical unit of work**.

✔ Either all statements succeed\
❌ Or all are rolled back

### Example

``` sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
```

If any query fails → `ROLLBACK`.

### Transaction Commands

-   `BEGIN` / `START TRANSACTION`
-   `COMMIT`
-   `ROLLBACK`
-   `SAVEPOINT`

------------------------------------------------------------------------

## 2️⃣ Transaction Isolation Levels

Isolation level decides **how visible data changes are between
concurrent transactions**.

PostgreSQL supports **4 isolation levels** ⬇️

  Level                      Dirty Read                       Non-repeatable Read   Phantom Read
  -------------------------- -------------------------------- --------------------- --------------
  READ UNCOMMITTED           ❌ (treated as READ COMMITTED)   ✅                    ✅
  READ COMMITTED (default)   ❌                               ✅                    ✅
  REPEATABLE READ            ❌                               ❌                    ✅
  SERIALIZABLE               ❌                               ❌                    ❌

------------------------------------------------------------------------

### 1️⃣ READ COMMITTED (default)

-   Sees only **committed data**
-   Each query sees a **fresh snapshot**

``` sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

⚠️ Same query may return different results inside one transaction.

------------------------------------------------------------------------

### 2️⃣ REPEATABLE READ

-   Snapshot is **fixed for the whole transaction**
-   Same query → **same result**

``` sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

✔ Prevents non-repeatable reads\
⚠️ Phantom rows may still appear

------------------------------------------------------------------------

### 3️⃣ SERIALIZABLE (strongest)

-   Transactions behave as if run **one by one**
-   Fully isolated

``` sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

✔ Safest\
⚠️ Can cause transaction failures → retry needed

------------------------------------------------------------------------

## 3️⃣ Transaction Workouts (Hands-on Practice 💪)

### 🏋️ Workout 1: Basic Commit & Rollback

``` sql
BEGIN;
UPDATE employees SET salary = salary + 5000 WHERE id = 1;
ROLLBACK;   -- salary unchanged
```

``` sql
BEGIN;
UPDATE employees SET salary = salary + 5000 WHERE id = 1;
COMMIT;     -- salary saved
```

------------------------------------------------------------------------

### 🏋️ Workout 2: Savepoint

``` sql
BEGIN;

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
SAVEPOINT sp1;

UPDATE accounts SET balance = balance - 100 WHERE id = 2;
ROLLBACK TO sp1;

COMMIT;
```

✔ First update stays\
❌ Second update undone

------------------------------------------------------------------------

### 🏋️ Workout 3: Isolation Behavior

**Session 1**

``` sql
BEGIN;
UPDATE products SET price = 500 WHERE id = 1;
```

**Session 2**

``` sql
SELECT price FROM products WHERE id = 1;
```

👉 Session 2 won't see the change until Session 1 commits.

------------------------------------------------------------------------

### 🏋️ Workout 4: Serializable Conflict

``` sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

-   Two transactions update the same row →\
    ❌ One may fail with serialization error\
    ✔ Retry transaction

------------------------------------------------------------------------

## 🧠 Interview One-Liners

-   **Transaction**: Logical unit of work\
-   **Isolation**: Controls visibility between transactions\
-   **Default level in PostgreSQL**: READ COMMITTED\
-   **Strongest isolation**: SERIALIZABLE