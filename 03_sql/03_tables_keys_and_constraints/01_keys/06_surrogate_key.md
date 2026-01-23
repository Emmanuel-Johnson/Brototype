# Surrogate Key

## What is a Surrogate Key?

A Surrogate Key is an artificial, system-generated identifier used to uniquely identify a row in a table. It has no business meaning and exists purely for database and technical purposes.

## Why it’s Used

Surrogate Keys provide a stable, simple, and efficient Primary Key, even when real-world business data changes over time. This makes them ideal for long-term system design.

## Example (PostgreSQL)

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE,
  name TEXT
);
```

## Key Characteristics

* Has no real-world or business meaning
* Usually an auto-increment integer or a UUID
* Never changes once assigned
* Ideal for use in foreign key relationships

## Key Interview Point

Most production systems use Surrogate Keys as Primary Keys and enforce business rules using UNIQUE constraints rather than relying on business data for identity.

## Natural Key vs Surrogate Key (Memory Trick)

Natural Key → meaningful but unstable
Surrogate Key → meaningless but stable
