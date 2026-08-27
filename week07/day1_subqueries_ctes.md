# Week 6 Day 1 PM: SQL Subqueries and CTEs

## Objective

Learn how to use subqueries and Common Table Expressions (CTEs) to solve multi-step business problems.

---

## What is a Subquery?

A subquery is a query nested inside another query.

Common locations:

- WHERE clause
- FROM clause
- SELECT clause

### Example

```sql
SELECT *
FROM transactions
WHERE amount > (
    SELECT AVG(amount)
    FROM transactions
);
```

---

## What is a CTE?

A Common Table Expression (CTE) is a temporary named result set created using the WITH clause.

### Example

```sql
WITH customer_totals AS (
    SELECT
        customer_id,
        SUM(amount) AS total_spend
    FROM transactions
    GROUP BY customer_id
)
SELECT *
FROM customer_totals;
```

---

## Why Use CTEs?

- Easier to read
- Easier to debug
- Reusable logic
- Better structure for complex queries

---

## Lab Activities

### Query 1

Top 10 Customers by Suspicious Transaction Ratio.

### Query 2

Branch Month-on-Month Suspicious Amount Change.

---

## Reflection

### What makes a CTE more readable than a subquery?

CTEs break a complex query into smaller named steps, making the logic easier to follow. In the suspicious transaction ratio query, separate CTEs for total transactions and flagged transactions make the calculation clearer than a nested subquery.

### When would you use a WHERE subquery?

I would use a WHERE subquery when a filter depends on a calculated value, such as comparing a transaction amount to an average amount.

### Where would you add a Western Cape filter?

I would add the region filter in the final query when joining to the branches table because the region information belongs to the branch data and keeps the CTEs focused on transaction calculations.