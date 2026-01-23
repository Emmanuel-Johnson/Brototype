# Primary Key

## What is a Primary Key?

A Primary Key is a constraint used to uniquely identify each row in a database table. It ensures that every record can be referenced without ambiguity and maintains entity integrity.

## Key Characteristics

* Must contain unique values
* Cannot be NULL
* Only one Primary Key per table
* Can be single-column or composite (multiple columns)

## Example (PostgreSQL)

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255),
  name TEXT
);
```

## Key Interview Point

A Primary Key automatically creates a unique index on the column(s), which improves lookup performance and enforces data integrity.
