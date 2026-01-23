# Foreign Key

## What is a Foreign Key?

A Foreign Key is a constraint used to create a relationship between two tables. It ensures that a value in one table must match an existing value in another table’s Primary Key or UNIQUE key.

## Why it’s Needed

Foreign Keys maintain referential integrity by preventing invalid or orphan records, such as an order that references a non-existent user.

## Example (PostgreSQL)

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT,
  CONSTRAINT fk_user
    FOREIGN KEY (user_id)
    REFERENCES users(id)
);
```

## Key Characteristics

* Can have duplicate values
* Can be NULL (unless restricted)
* A table can have multiple Foreign Keys
* Enforces relationships between tables

## Key Interview Point

Foreign Keys support actions such as ON DELETE CASCADE, SET NULL, and RESTRICT, which control what happens to child records when a parent row is deleted.
