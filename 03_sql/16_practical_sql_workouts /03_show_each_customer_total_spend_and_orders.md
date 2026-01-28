# Show each customer’s total amount spent and total number of orders in a single row

```sql
-- Using INNER JOIN: Only customers with orders
SELECT
    c.first_name || ' ' || c.last_name AS full_name,
    SUM(o.amount) AS "total amount spent",
    COUNT(o.customer_id) AS "total number of orders"
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.first_name, c.last_name;
```

```sql
-- Using LEFT JOIN: Includes customers with zero orders
SELECT
    c.first_name || ' ' || c.last_name AS full_name,
    COALESCE(SUM(o.amount), 0) AS "total amount spent",
    COUNT(o.order_id) AS "total number of orders"
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name;
```
