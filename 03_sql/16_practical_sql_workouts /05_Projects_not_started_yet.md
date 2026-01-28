## Projects That Haven’t Started Yet

If **“haven’t started yet” = start date is in the future**, this is the clean PostgreSQL query:

```sql
SELECT *
FROM projects
WHERE start_date > CURRENT_DATE;
```

### Why this works

* **CURRENT_DATE** → today’s date (no time part)
* **start_date > CURRENT_DATE** → projects that will start after today

---

## If `start_date` can be `NULL` (not scheduled yet)

Interviewers often love this edge case 👀

```sql
SELECT *
FROM projects
WHERE start_date IS NULL
   OR start_date > CURRENT_DATE;
```

---

## If `start_date` is a `TIMESTAMP`

Use `CURRENT_TIMESTAMP` instead:

```sql
SELECT *
FROM projects
WHERE start_date > CURRENT_TIMESTAMP;
```
