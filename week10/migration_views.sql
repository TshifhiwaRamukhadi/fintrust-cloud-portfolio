/* =========================================
   FinTrust Migration Status Views
   Week 10 Day 1
   ========================================= */

CREATE OR REPLACE VIEW v_wave_progress AS
SELECT
    migration_wave,
    COUNT(*) AS total_assets,

    SUM(
        CASE
            WHEN status = 'C'
            THEN 1
            ELSE 0
        END
    ) AS complete,

    SUM(
        CASE
            WHEN status = 'I'
            THEN 1
            ELSE 0
        END
    ) AS in_progress,

    SUM(
        CASE
            WHEN status = 'F'
            THEN 1
            ELSE 0
        END
    ) AS failed,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN status = 'C'
                THEN 1
                ELSE 0
            END
        )
        /
        COUNT(*),
        1
    ) AS completion_pct

FROM migration_plan

GROUP BY migration_wave

ORDER BY migration_wave;


/* =========================================
   Portfolio Completion Summary
   ========================================= */

CREATE OR REPLACE VIEW v_portfolio_completion AS
SELECT
    COUNT(*) AS total_assets,

    SUM(
        CASE
            WHEN status = 'C'
            THEN 1
            ELSE 0
        END
    ) AS total_complete,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN status = 'C'
                THEN 1
                ELSE 0
            END
        )
        /
        COUNT(*),
        1
    ) AS overall_completion_pct

FROM migration_plan;

/* =========================================
   FinTrust Migration Status Views
   Week 10 Day 2
   ========================================= */

CREATE OR REPLACE VIEW v_customer_accounts AS
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name
        AS full_name,
    c.segment,
    c.region,
    COUNT(a.account_id)
        AS account_count,
    SUM(a.balance)
        AS total_balance,
    SUM(
        CASE
            WHEN a.currency='ZAR'
            THEN a.balance
            ELSE 0
        END
    ) AS zar_balance,
    MIN(c.onboarded_date)
        AS onboarded_date
FROM customers c
LEFT JOIN accounts a
ON c.customer_id = a.customer_id
AND a.status = 'active'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.segment,
    c.region;


CREATE OR REPLACE VIEW v_monthly_txn_summary AS
SELECT
    DATE_TRUNC(
        'month',
        t.txn_date
    ) AS txn_month,

    c.segment,

    t.channel,

    t.txn_type,

    COUNT(*) AS txn_count,

    SUM(t.amount)
        AS total_amount,

    AVG(t.amount)
        AS avg_amount,

    MAX(t.amount)
        AS max_amount

FROM transactions t

JOIN accounts a
ON t.account_id =
   a.account_id

JOIN customers c
ON a.customer_id =
   c.customer_id

GROUP BY
    DATE_TRUNC(
        'month',
        t.txn_date
    ),
    c.segment,
    t.channel,
    t.txn_type

ORDER BY
    txn_month DESC,
    total_amount DESC;