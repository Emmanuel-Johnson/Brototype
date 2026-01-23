# Composite Key

## What is a Composite Key?

A Composite Key is a key made up of two or more columns that together uniquely identify a row in a table. No single column alone is sufficient to guarantee uniqueness.

## Why it’s Needed

Composite Keys are used when uniqueness depends on a combination of values, such as `(user_id, course_id)` in an enrollment table where a user can enroll in many courses but only once per course.

## Example (PostgreSQL)

```sql
CREATE TABLE enrollments (
  user_id INT,
  course_id INT,
  enrolled_at TIMESTAMP,
  PRIMARY KEY (user_id, course_id)
);
```

## Key Characteristics

* Consists of multiple columns
* Each column individually may contain duplicate values
* The combination of column values must be unique
* Commonly used in junction or mapping tables for many-to-many relationships

## Key Interview Point

A Composite Key can be defined as a Primary Key or a Unique Key. If it is defined as a Primary Key, none of the columns can contain NULL values.
