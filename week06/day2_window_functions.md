# Week 6 Day 2: SQL Window Functions

## Objective

Learn how to use SQL Window Functions to perform analytics while retaining individual row detail.

## Key Concepts

### PARTITION BY

Creates logical groups for calculations without collapsing rows.

Example:

```sql
SUM(amount) OVER (
    PARTITION BY customer_id
)
```

### ROW_NUMBER()

Assigns a unique sequential number to each row.

Example:

```sql
ROW_NUMBER() OVER (
    PARTITION BY branch_code
    ORDER BY amount DESC
)
```

### DENSE_RANK()

Assigns rankings without gaps when ties occur.

Example:

| Amount | Rank |
|---------|------|
| 50000 | 1 |
| 45000 | 2 |
| 45000 | 2 |
| 30000 | 3 |

### SUM() OVER()

Calculates running totals.

Example:

```sql
SUM(amount) OVER (
    PARTITION BY branch_code
    ORDER BY transaction_date
)
```

### LAG()

Retrieves values from previous rows.

Example:

```sql
LAG(monthly_amount) OVER (
    PARTITION BY customer_id
    ORDER BY month_start
)
```

## Lab Activities

### Challenge 1

Rank customers within spending tiers using DENSE_RANK.

### Challenge 2

Calculate running totals of suspicious transaction amounts.

### Challenge 3

Detect customer spending spikes using LAG.

## Reflection

I would use a window function when I need to keep detailed row-level information while also performing calculations such as rankings, running totals, or comparisons with previous rows. Unlike GROUP BY, window functions do not collapse rows into summaries.