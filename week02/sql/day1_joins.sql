-- ==========================================================
-- FinTrust Bank
-- Week 2 Day 1
-- SQL JOIN Challenges
-- Author: Tshifhiwa Ramukhadi
-- ==========================================================

-- ==========================================================
-- Challenge 1
-- Find customers who have a CHEQUE account with a
-- balance below R1,000.
-- Uses INNER JOIN because we only want customers
-- who have matching account records.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    c.province,
    a.balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE a.account_type = 'CHEQUE'
  AND a.balance < 1000
ORDER BY a.balance ASC;


-- ==========================================================
-- Challenge 2
-- List all transactions made by customers from
-- Western Cape.
-- Uses a 3-table INNER JOIN.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    t.amount,
    t.transaction_type,
    t.transaction_date
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE c.province = 'Western Cape'
ORDER BY t.transaction_date DESC;


-- ==========================================================
-- Challenge 3
-- Find all accounts with NO transactions recorded.
-- Uses LEFT JOIN to keep all accounts and identify
-- accounts without matching transactions.
-- ==========================================================

SELECT
    a.account_id,
    a.account_type,
    a.balance,
    c.first_name,
    c.last_name
FROM accounts a
INNER JOIN customers c
    ON a.customer_id = c.customer_id
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;