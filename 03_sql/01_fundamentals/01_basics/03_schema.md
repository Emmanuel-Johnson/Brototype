## 1. WHAT
Schema is a logical container used to organize database objects like tables, views, and functions.  
In PostgreSQL, a schema is used to group related objects and avoid name conflicts.

## 2. WHY
Schema solves the problem of managing large databases with many tables and teams.  
Without schemas, object names collide, access control becomes messy, and organization is hard to maintain.

## 3. WHERE
Schema exists inside a PostgreSQL database, between the database and tables layer.  
During query execution, PostgreSQL resolves objects using the schema search path.

## 4. HOW
Schemas are created inside a database to group related objects.  
Tables and other objects are created within a schema, and queries reference them using `schema_name.object_name`.

## 5. WHEN
Use schemas when separating modules, environments, or teams within the same database.  
Do not use schemas as a replacement for separate databases when strong isolation is required.

## 6. EXAMPLE
In an LMS project, `auth` schema stores users and roles, while `courses` schema stores course data.  
This keeps authentication and course logic cleanly separated.

## 7. PROS & CONS
Schemas improve organization, avoid naming conflicts, and enable fine-grained access control.  
However, overusing schemas can complicate queries and increase maintenance effort.

## 8. COMMON MISTAKES
Relying only on the default `public` schema for all tables.  
Another mistake is forgetting to set the correct schema search path in applications.
