/* =========================================
   Challenge 1 - Customer Spend Ranking
   ========================================= */

WITH customer_spend AS (
    SELECT
        customer_id,
        spend_tier,
        SUM(amount) AS total_spend
    FROM transactions
    WHERE transaction_date >= '2024-06-01'
      AND transaction_date < '2024-07-01'
    GROUP BY customer_id, spend_tier
)
SELECT
    customer_id,
    spend_tier,
    total_spend,
    DENSE_RANK() OVER (
        PARTITION BY spend_tier
        ORDER BY total_spend DESC
    ) AS tier_rank
FROM customer_spend
ORDER BY spend_tier, tier_rank;


/* =========================================
   Challenge 2 - Running Fraud Exposure
   ========================================= */

SELECT
    branch_code,
    transaction_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY branch_code
        ORDER BY transaction_date
    ) AS running_total
FROM transactions
WHERE suspicious_flag = 'Y'
ORDER BY branch_code, transaction_date;


/* =========================================
   Challenge 3 - Spending Spikes
   ========================================= */

WITH monthly_spend AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', transaction_date) AS month_start,
        SUM(amount) AS monthly_amount
    FROM transactions
    WHERE transaction_date >= '2024-01-01'
      AND transaction_date < '2024-07-01'
    GROUP BY customer_id,
             DATE_TRUNC('month', transaction_date)
),
spend_comparison AS (
    SELECT
        customer_id,
        month_start,
        monthly_amount,
        LAG(monthly_amount) OVER (
            PARTITION BY customer_id
            ORDER BY month_start
        ) AS previous_month_amount
    FROM monthly_spend
)
SELECT
    customer_id,
    month_start,
    monthly_amount,
    previous_month_amount
FROM spend_comparison
WHERE previous_month_amount IS NOT NULL
  AND monthly_amount > (previous_month_amount * 3)
ORDER BY customer_id, month_start;