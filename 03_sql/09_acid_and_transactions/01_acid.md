# ACID in Databases 🔐

ACID is a set of rules that make sure database transactions are reliable
and safe --- especially when many users are accessing data at the same
time.

**ACID = Atomicity, Consistency, Isolation, Durability**

Think of ACID as the **trust contract of a database**.

------------------------------------------------------------------------

## 1️⃣ Atomicity (All or Nothing)

**Definition:**\
A transaction must either complete fully or not happen at all.

There is no partial success.

**Example:**\
Bank transfer ₹100 from A → B

**Steps:** - Deduct ₹100 from A\
- Add ₹100 to B

✔ Both succeed → transaction committed\
❌ If adding to B fails → deduction from A is rolled back

**Key idea:**\
If one step fails, everything is undone.

------------------------------------------------------------------------

## 2️⃣ Consistency (Rules Must Hold)

**Definition:**\
A transaction must take the database from one valid state to another
valid state.

All: - Constraints\
- Triggers\
- Rules

must be satisfied.

**Example:** - Balance cannot be negative\
- Foreign key must exist

❌ If a transaction violates a rule → it is rejected

**Key idea:**\
Database rules are never broken.

------------------------------------------------------------------------

## 3️⃣ Isolation (Transactions Don't Interfere)

**Definition:**\
Multiple transactions running at the same time should behave as if they
run one after another.

No transaction should see half-finished data from another.

**Example:** - Transaction A is updating salary\
- Transaction B reads salary

👉 B should see either old value or final value, not something in
between.

**PostgreSQL isolation levels:** - READ COMMITTED (default)\
- REPEATABLE READ\
- SERIALIZABLE

**Key idea:**\
Each transaction runs in its own bubble 🫧

------------------------------------------------------------------------

## 4️⃣ Durability (Once Saved, Always Saved)

**Definition:**\
Once a transaction is committed, it will never be lost --- even if: -
Power fails\
- System crashes\
- Server restarts

**Example:** - Order placed successfully\
- System crashes immediately

✔ Order still exists after restart

**Key idea:**\
Commit = permanent 💾

------------------------------------------------------------------------

## 🧠 One-line Interview Summary

**ACID ensures that database transactions are reliable, consistent,
isolated, and permanently stored.**