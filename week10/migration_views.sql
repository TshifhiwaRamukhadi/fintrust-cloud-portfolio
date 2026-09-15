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


/* =========================================
   FinTrust Migration Status Views
   Week 10 Day 3 view 1
   ========================================= */

    CREATE OR REPLACE VIEW v_daily_transfer_volume AS
SELECT
    DATE(started_at) AS transfer_date,
    source_volume,
    COUNT(*) AS execution_count,
    SUM(files_transferred) AS total_files,
    ROUND(
        SUM(bytes_transferred)
        / 1073741824.0,
        2
    ) AS total_gb,
    SUM(
        CASE
            WHEN status='SUCCESS'
            THEN 1
            ELSE 0
        END
    ) AS successful_runs,
    SUM(
        CASE
            WHEN status='ERROR'
            THEN 1
            ELSE 0
        END
    ) AS failed_runs
FROM datasync_executions
GROUP BY
    DATE(started_at),
    source_volume
ORDER BY transfer_date DESC;

/* =========================================
   FinTrust Migration Status Views
   Week 10 Day 3 view 2
   ========================================= */
   CREATE OR REPLACE VIEW
v_volume_migration_progress AS

SELECT

    v.volume_name,

    v.source_system,

    v.total_size_gb,

    COALESCE(
        SUM(
            e.bytes_transferred
        ) / 1073741824.0,
        0
    ) AS transferred_gb,

    ROUND(
        100.0 *
        COALESCE(
            SUM(
                e.bytes_transferred
            )
            / 1073741824.0,
            0
        )
        /
        NULLIF(
            v.total_size_gb,
            0
        ),
        1
    ) AS pct_complete,

    MAX(
        e.completed_at
    ) AS last_transfer

FROM transfer_volumes v

LEFT JOIN datasync_executions e

ON v.volume_id = e.task_id

AND e.status = 'SUCCESS'

GROUP BY
    v.volume_id,
    v.volume_name,
    v.source_system,
    v.total_size_gb

ORDER BY pct_complete DESC;


/* =========================================
   FinTrust Migration Status Views
   Week 10 Day 3 view 3(Extension Task)
   ========================================= */
   CREATE OR REPLACE VIEW
v_transfer_audit AS

SELECT

    tv.volume_name,

    cr.regulation,

    cr.encryption_required,

    de.status,

    de.bytes_transferred,

    de.completed_at,

    cr.retention_years

FROM datasync_executions de

JOIN transfer_volumes tv
ON de.task_id = tv.volume_id

JOIN compliance_requirements cr
ON tv.volume_id = cr.volume_id;