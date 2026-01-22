## 1. WHAT
SQL is a query language used to define, read, update, and delete data in relational databases.  
In PostgreSQL, SQL is used to interact with tables, relationships, and stored data reliably.

## 2. WHY
SQL solves the problem of structured data storage and retrieval at scale.  
Without SQL, managing filtering, joins, updates, and data consistency becomes repetitive, error-prone, and slow.

## 3. WHERE
SQL sits between the application and the PostgreSQL database in the system architecture.  
In a request–response flow, the backend sends SQL queries to PostgreSQL and receives structured results.

## 4. HOW
The application sends an SQL query to PostgreSQL.  
PostgreSQL parses and executes the query on tables and indexes, then returns the result set to the application.

## 5. WHEN
Use SQL when working with structured, relational data that requires consistency and complex queries.  
Do not use SQL alone for unstructured or highly flexible schema data like logs or documents.

## 6. EXAMPLE
In an e-commerce app, SQL is used to fetch orders by user, join them with payments, and calculate totals.  
PostgreSQL executes a SELECT with JOIN and WHERE clauses to return accurate order data.

## 7. PROS & CONS
SQL provides powerful querying, strong data integrity, and works well with large relational datasets.  
However, complex queries can be hard to maintain, and schema changes require careful planning.

## 8. COMMON MISTAKES
Writing inefficient queries without indexes leads to performance issues.  
Another mistake is mixing business logic into SQL instead of keeping it in the application layer.
