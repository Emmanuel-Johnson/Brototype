# Super Key

## What is a Super Key?

A Super Key is a set of one or more columns that can uniquely identify a row in a table. It may include extra (redundant) columns beyond what is strictly required for uniqueness.

## Why it Exists

Super Keys represent all possible combinations of attributes that can uniquely identify a record during the database design phase. They help designers reason about uniqueness before minimizing keys.

## Example

Consider a `users` table with unique columns `id`, `email`, and `phone`:

The following are all Super Keys:

* (id)
* (email)
* (id, email)
* (id, phone)
* (email, phone)
* (id, email, phone)

Each combination uniquely identifies a row, even if some attributes are redundant.

## Key Characteristics

* Must uniquely identify a row
* May contain unnecessary or redundant columns
* Can be single-column or multi-column
* Used mainly in conceptual and logical database design

## Key Interview Point

A Candidate Key is a minimal Super Key, meaning it has no extra attributes beyond what is required for uniqueness.

## Full Key Hierarchy (Memory Trick)

Super Key → Candidate Key → Primary Key
