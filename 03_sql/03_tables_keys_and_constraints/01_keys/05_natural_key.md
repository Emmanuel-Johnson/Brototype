# Natural Key

## What is a Natural Key?

A Natural Key is a real-world, meaningful attribute used to uniquely identify a record in a table. Its value comes from business data rather than from an artificially generated identifier.

## Why it’s Used

Natural Keys represent data that is already unique by nature, such as an email address, passport number, or Aadhaar number. They can directly reflect business rules without requiring an additional ID column.

## Example (PostgreSQL)

```sql
CREATE TABLE users (
  email VARCHAR(255) PRIMARY KEY,
  name TEXT
);
```

## Key Characteristics

* Based on real-world business logic
* Human-readable and meaningful
* Can change over time (email updates, document reissue)
* Changes can break foreign key relationships

## Key Interview Point

Natural Keys reduce the need for extra columns, but they are less stable over time. Because of this, many systems prefer Surrogate Keys as Primary Keys for long-term reliability.
