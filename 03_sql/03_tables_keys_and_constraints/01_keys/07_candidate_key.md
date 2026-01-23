# Candidate Key

## What is a Candidate Key?

A Candidate Key is a column or a set of columns that can uniquely identify each row in a table without containing NULL values. It represents a potential choice for the Primary Key.

## Why it’s Needed

During database design, there may be multiple attributes that can uniquely identify a record. All such valid options are called Candidate Keys, from which one is chosen as the Primary Key.

## Example

Consider a `users` table with the following attributes:

* `id` → unique, NOT NULL
* `email` → unique, NOT NULL
* `phone` → unique, NOT NULL

Here, **id**, **email**, and **phone** are all Candidate Keys. Only one of them will be selected as the Primary Key.

## Key Characteristics

* Must be UNIQUE
* Must be NOT NULL
* A table can have multiple Candidate Keys
* One Candidate Key is chosen as the Primary Key

## Key Interview Point

Primary Key ⊂ Candidate Keys
