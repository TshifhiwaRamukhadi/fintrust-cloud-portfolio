# Week 6 Day 2 - SQL Window Functions

## Objective

Learn how SQL Window Functions perform calculations across related rows while preserving individual row detail.

Unlike GROUP BY, window functions do not collapse rows.

---

## Window Function Components

### PARTITION BY

Groups rows into logical partitions without collapsing results.

Example:

```sql
SUM(amount) OVER (
    PARTITION BY customer_id
)
```

---

### ORDER BY

Defines the sequence of rows within a partition.

Example:

```sql
SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_date
)
```

---

### OVER()

Defines the window where the calculation occurs.

Example:

```sql
AVG(amount) OVER ()
```

---

## Ranking Functions

### ROW_NUMBER()

Assigns a unique number to every row.

Example:

```sql
ROW_NUMBER() OVER (
    ORDER BY amount DESC
)
```

---

### RANK()

Assigns the same rank to ties and creates gaps.

Example:

```text
50000 → 1
45000 → 2
45000 → 2
30000 → 4
```

---

### DENSE_RANK()

Assigns the same rank to ties but does not create gaps.

Example:

```text
50000 → 1
45000 → 2
45000 → 2
30000 → 3
```

---

## Running Totals

Window functions can calculate cumulative values.

Example:

```sql
SUM(amount) OVER (
    PARTITION BY branch_code
    ORDER BY transaction_date
)
```

This creates a running total per branch.

---

## LAG Function

LAG retrieves data from a previous row.

Example:

```sql
LAG(total_amount) OVER (
    PARTITION BY branch_code
    ORDER BY month_start
)
```

Use Cases:

- Month-over-month comparisons
- Fraud detection
- Customer spending trends

---

## LEAD Function

LEAD retrieves data from a future row.

Example:

```sql
LEAD(total_amount) OVER (
    PARTITION BY branch_code
    ORDER BY month_start
)
```

Use Cases:

- Forecasting
- Trend analysis

---

## Challenge 1 - Customer Spend Ranking

Use DENSE_RANK() to rank customers within spending tiers.

Requirements:

- Premium
- Standard
- Basic

Customers should be ranked within their tier, not globally.

---

## Challenge 2 - Running Fraud Exposure

Calculate cumulative suspicious transaction amounts by branch.

Use:

- PARTITION BY branch_code
- ORDER BY transaction_date
- SUM() OVER()

---

## Challenge 3 - Spending Spikes

Detect customers whose monthly spend exceeds three times the previous month.

Use:

- CTE
- LAG()
- PARTITION BY customer_id

---

## Why Not Use Window Functions In WHERE?

Window functions are calculated after the WHERE clause.

Correct pattern:

1. Create a CTE
2. Calculate window function
3. Filter in the outer query

---

## Reflection

Window functions are preferred when individual row details must be preserved while calculating rankings, running totals, averages, or comparisons across related rows without using self-joins.

---

## Key Takeaways

- PARTITION BY groups rows without collapsing them.
- OVER() defines the window.
- ROW_NUMBER() gives unique rankings.
- RANK() allows ties and gaps.
- DENSE_RANK() allows ties without gaps.
- LAG() retrieves previous-row values.
- LEAD() retrieves next-row values.
- SUM() OVER() is commonly used for running totals.