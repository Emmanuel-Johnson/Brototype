# DDL (Data Definition Language)

## What is DDL?

DDL (Data Definition Language) is a category of SQL commands used to define, change, or remove the structure of database objects such as tables, schemas, and indexes. It focuses on the structure of data, not the data stored inside it.

## Main DDL Commands

### CREATE

Used to create new database objects.
Examples include creating a table, database, schema, or index.

### ALTER

Used to modify the structure of an existing database object.
Common uses include adding or removing columns and changing data types.

### DROP

Used to permanently remove a database object.
This deletes both the structure and all associated data.

### TRUNCATE

Used to quickly remove all rows from a table.
The table structure remains, but the data is deleted irreversibly.

## Key Interview Point

DDL commands usually auto-commit, meaning their changes cannot be rolled back in most databases.
