# NoSQL Basics

## 1️⃣ What is NoSQL?

**NoSQL** stands for **Not Only SQL**.  
It refers to databases designed to handle:

- Huge volumes of data
- High-speed read/write operations
- Flexible or unstructured data

**Key differences from SQL databases:**

- No fixed tables
- No predefined schema

**Exam-friendly definition:**  
NoSQL is a type of database that stores data in non-relational formats and supports scalable, flexible data models.

---

## 2️⃣ Types of NoSQL Databases

### 🔑 1. Key-Value Store

- Data stored as key → value pairs

**Example:**
```
"user_id_101" → "Emmanuel"
```

- ✅ Very fast
- ❌ No complex queries

**Use cases:**  
Caching, session storage, user preferences

**Examples:**  
Redis, DynamoDB

---

### 📄 2. Document Store

- Data stored as documents (JSON, BSON, XML)

**Example:**
```json
{
    "id": 1,
    "name": "Alex",
    "skills": ["Python", "Django"]
}
```

- ✅ Flexible schema
- ✅ Supports nested data

**Use cases:**  
Content management, user profiles, APIs

**Examples:**  
MongoDB, CouchDB

---

### 🧱 3. Column-Based (Wide-Column Store)

- Data stored in columns instead of rows

**Example:**
```
RowKey | name | email | age
```
(Internally stored column-wise)

- ✅ High performance for analytics
- ✅ Handles massive data

**Use cases:**  
Data warehousing, analytics, logging systems

**Examples:**  
Cassandra, HBase

---

### 🕸️ 4. Graph Database

- Data stored as nodes (entities) and edges (relationships)

**Example:**
```
User ──FRIEND──> User
```

- ✅ Best for relationship-heavy data

**Use cases:**  
Social networks, recommendation systems, fraud detection

**Examples:**  
Neo4j, Amazon Neptune

---

## 3️⃣ SQL vs NoSQL

| Feature      | SQL                        | NoSQL                                 |
|--------------|---------------------------|---------------------------------------|
| Data model   | Tables (rows/columns)     | Key-Value, Document, Graph, Column    |
| Schema       | Fixed                     | Flexible / Schema-less                |
| Scalability  | Vertical                  | Horizontal                            |
| Transactions | ACID                      | BASE                                  |
| Joins        | Supported                 | Limited / Not supported               |
| Best for     | Structured data           | Big & unstructured data               |

**Shortcut memory tip:**  
- SQL = Structure + Consistency  
- NoSQL = Scale + Speed

---

## 4️⃣ ACID vs BASE

### 🧪 ACID (SQL Databases)

ACID ensures strong consistency:

- **A – Atomicity:** All or nothing
- **C – Consistency:** Valid state before & after transaction
- **I – Isolation:** Transactions don’t interfere
- **D – Durability:** Data persists after commit

**Example:**  
Bank transfer — money should not disappear or duplicate.

---

### ⚡ BASE (NoSQL Databases)

BASE focuses on availability & scalability:

- **B – Basically Available:** System always responds
- **A – Soft state:** Data may change over time
- **S – Eventual consistency:** Data becomes consistent later

**Example:**  
Social media likes — count may update slightly later.

---

### 🔁 ACID vs BASE (Quick Compare)

| ACID                | BASE                   |
|---------------------|-----------------------|
| Strong consistency  | Eventual consistency  |
| Less scalable       | Highly scalable       |
| Slower              | Faster                |
| SQL systems         | NoSQL systems         |

---

## 🧾 One-Page Exam Summary

- **NoSQL:** Non-relational, scalable, flexible DB
- **Types:** Key-Value, Document, Column, Graph
- **SQL vs NoSQL:** Structure vs Scale
- **ACID:** Consistency & reliability
- **BASE:** Availability & performance
