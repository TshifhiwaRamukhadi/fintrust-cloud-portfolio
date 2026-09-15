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