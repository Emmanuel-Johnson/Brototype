# Alternate Key

## What is an Alternate Key?

An Alternate Key is a Candidate Key that is not selected as the Primary Key. It can still uniquely identify a record but plays a secondary role in table design.

## Why it’s Needed

When a table has multiple Candidate Keys, only one is chosen as the Primary Key. The remaining Candidate Keys become Alternate Keys and are used to enforce additional uniqueness rules.

## Example

Consider a `users` table:

* `id` → Primary Key
* `email` → Candidate Key → Alternate Key
* `phone` → Candidate Key → Alternate Key

Here, **email** and **phone** uniquely identify users but are not chosen as the Primary Key.

## Key Characteristics

* Must be UNIQUE and NOT NULL
* Derived from Candidate Keys
* Typically enforced using a UNIQUE constraint
* A table can have multiple Alternate Keys

## Key Interview Point

Alternate Keys help enforce business-level uniqueness without using those fields as the Primary Key.

## Final Key Flow (Interview Memory Map)

Super Key → Candidate Key → { Primary Key + Alternate Keys }
