## Customers Spending More Than $12,000

The following SQL query retrieves the full names of customers whose total spending exceeds $12,000:

```sql
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    SUM(o.amount) AS total
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING SUM(o.amount) > 12000;
```
