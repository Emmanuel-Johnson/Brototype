# Unique Key

## What is a Unique Key?

A Unique Key is a constraint used to ensure that all values in a column or a group of columns are distinct. It prevents duplicate data while still allowing controlled flexibility in table design.

## Why it’s Needed

Unique Keys enforce data uniqueness for attributes such as email, username, or phone number where duplicates are not allowed but NULL values may still be acceptable.

## Example (PostgreSQL)

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  phone VARCHAR(15)
);
```

## Key Characteristics

* Does not allow duplicate values
* Allows NULL values (PostgreSQL allows multiple NULLs)
* A table can have multiple Unique Keys
* Automatically creates a unique index

## Key Interview Point

Primary Key = UNIQUE + NOT NULL
Unique Key = UNIQUE only
