# TCL (Transaction Control Language)

## What is TCL?

TCL (Transaction Control Language) is a category of SQL commands used to manage database transactions. It ensures data consistency and safety when multiple DML operations are executed together.

## Main TCL Commands

### COMMIT

Permanently saves all changes made in the current transaction.
After a COMMIT, the changes cannot be rolled back.

### ROLLBACK

Undoes changes made in the current transaction before a COMMIT.
It is used to recover from errors or unexpected failures.

### SAVEPOINT

Creates a checkpoint inside a transaction.
You can roll back to a SAVEPOINT instead of rolling back the entire transaction.

## Key Interview Point

TCL works only with DML commands, not DDL commands, because most DDL operations auto-commit.
