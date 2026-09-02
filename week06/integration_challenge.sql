/* =========================================
   Week 6 Day 5 Integration Challenge
   Top 20 Fraud Risk Customers
   ========================================= */

WITH suspicious_ratios AS (

    SELECT
        customer_id,
        COUNT(
            CASE
                WHEN suspicious_flag = 'Y'
                THEN 1
            END
        )::FLOAT
        /
        COUNT(*) AS ratio

    FROM transactions

    GROUP BY customer_id

),

monthly_spend AS (

    SELECT
        customer_id,
        DATE_TRUNC(
            'month',
            transaction_date
        ) AS month_start,
        SUM(amount) AS monthly_amount

    FROM transactions

    WHERE transaction_date >= '2024-01-01'
      AND transaction_date < '2025-01-01'

    GROUP BY
        customer_id,
        DATE_TRUNC(
            'month',
            transaction_date
        )
),

spending_spikes AS (

    SELECT DISTINCT
        customer_id

    FROM (

        SELECT
            customer_id,
            monthly_amount,

            LAG(
                monthly_amount
            ) OVER (

                PARTITION BY customer_id
                ORDER BY month_start

            ) AS previous_month_amount

        FROM monthly_spend

    ) s

    WHERE previous_month_amount IS NOT NULL
      AND monthly_amount >
          previous_month_amount * 3

),

combined AS (

    SELECT

        sr.customer_id,

        sr.ratio AS suspicious_ratio,

        CASE
            WHEN ss.customer_id
            IS NOT NULL
            THEN 1
            ELSE 0
        END AS spike_flag,

        (
            sr.ratio * 0.6
        )
        +
        (
            CASE
                WHEN ss.customer_id
                IS NOT NULL
                THEN 0.4
                ELSE 0
            END
        ) AS risk_score

    FROM suspicious_ratios sr

    LEFT JOIN spending_spikes ss
        ON ss.customer_id = sr.customer_id

)

SELECT
    customer_id,
    suspicious_ratio,
    spike_flag,
    risk_score

FROM combined

ORDER BY risk_score DESC

LIMIT 20;