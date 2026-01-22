## 1. WHAT
A database is an organized collection of data used to store, manage, and retrieve information efficiently.  
In PostgreSQL, the database stores data in structured tables with defined relationships.

## 2. WHY
A database solves the problem of handling large, persistent data safely and consistently.  
Without a database, data storage using files becomes hard to search, update, secure, and scale.

## 3. WHERE
The database sits at the data layer of the system architecture.  
During a request–response cycle, the backend communicates with PostgreSQL to read or write data.

## 4. HOW
Data is stored in tables with rows and columns inside PostgreSQL.  
Applications send queries, PostgreSQL processes them, and returns the requested results.

## 5. WHEN
Use a database when applications need persistent, structured, and reliable data storage.  
Do not use a database for temporary or in-memory-only data that does not need persistence.

## 6. EXAMPLE
In a learning management system, PostgreSQL stores users, courses, and enrollments.  
The backend queries the database to fetch courses for a logged-in user.

## 7. PROS & CONS
Databases provide data consistency, fast querying, and support concurrent access.  
However, they require schema design and can add operational and performance overhead.

## 8. COMMON MISTAKES
Poor schema design leads to redundant data and slow queries.  
Another common mistake is not using indexes for frequently queried columns.
