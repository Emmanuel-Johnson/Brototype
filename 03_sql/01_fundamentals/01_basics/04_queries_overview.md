## 1. What is an SQL Query?

An SQL query is a command used to retrieve, insert, update, or delete data in a relational database.
It tells the database what data you want and how it should be processed.

## 2. Main Types of SQL Queries

SQL queries are broadly divided into data retrieval, data modification, and schema control queries.
In interviews, most focus is on SELECT-based queries and how data is filtered, joined, and aggregated.

## 3. SELECT Queries (Most Important)

SELECT queries are used to fetch data from one or more tables.
They commonly combine clauses like WHERE, ORDER BY, LIMIT, and DISTINCT to control results.

**Example idea:**
Get all active users ordered by created date.

## 4. Filtering with WHERE

The WHERE clause filters rows based on conditions such as comparisons, ranges, or patterns.
Without WHERE, queries return full tables, which is inefficient and often incorrect.

**Common operators:**
=, >, <, IN, BETWEEN, LIKE, IS NULL

## 5. JOIN Queries

JOINs are used to combine data from multiple tables using related columns.
They solve the problem of normalized data spread across tables.

**Key types you should know:**

* INNER JOIN
* LEFT JOIN
* RIGHT JOIN

## 6. Aggregation & GROUP BY

Aggregate functions like COUNT, SUM, AVG, MIN, and MAX summarize data.
GROUP BY groups rows, while HAVING filters grouped results (not individual rows).

**Interview favorite:**
Find users with more than 5 orders.

## 7. Subqueries

A subquery is a query inside another query.
It’s used when the result of one query is needed to filter or compute another.

**Example use cases:**

* Filtering with IN
* Comparing against aggregated results

## 8. INSERT, UPDATE, DELETE

These queries modify data in tables.

* INSERT → add new rows
* UPDATE → modify existing rows
* DELETE → remove rows

In production systems, these are usually wrapped in transactions.

## 9. Transactions (Bonus Point)

Transactions ensure data consistency using ACID properties.
They group multiple queries so either all succeed or all fail.

**Keywords:**
BEGIN, COMMIT, ROLLBACK

## 10. Interview Tip (Important)

Interviewers don’t just test syntax — they test:

* Correct JOIN choice
* Efficient filtering
* Proper use of GROUP BY vs HAVING
* Ability to explain why a query works
