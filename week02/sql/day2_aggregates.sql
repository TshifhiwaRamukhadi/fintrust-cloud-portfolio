-- ==========================================================
-- FinTrust Bank
-- Week 2 Day 2
-- Advanced JOINs & Aggregates
-- Author: Tshifhiwa Ramukhadi
-- ==========================================================

-- ==========================================================
-- Exercise 1
-- Business Purpose:
-- Show each customer's transaction activity and
-- total transaction value.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    c.province,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.province
ORDER BY total_amount DESC;


-- ==========================================================
-- Exercise 2
-- Business Purpose:
-- Analyse average balance by account type.
-- ==========================================================

SELECT
    account_type,
    COUNT(account_id) AS account_count,
    AVG(balance) AS avg_balance
FROM accounts
GROUP BY account_type
ORDER BY avg_balance DESC;


-- ==========================================================
-- Exercise 3
-- Business Purpose:
-- Find provinces where credit transactions
-- exceed R100,000.
-- ==========================================================

SELECT
    c.province,
    SUM(t.amount) AS total_deposit_amount,
    COUNT(t.transaction_id) AS credit_transaction_count
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'CREDIT'
GROUP BY c.province
HAVING SUM(t.amount) > 100000
ORDER BY total_deposit_amount DESC;


-- ==========================================================
-- Exercise 4
-- Business Purpose:
-- Monthly transaction summary.
-- ==========================================================

SELECT
    YEAR(transaction_date) AS year,
    MONTH(transaction_date) AS month,
    COUNT(transaction_id) AS transaction_count,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY year, month;


-- ==========================================================
-- Exercise 5
-- Business Purpose:
-- Fraud detection pattern:
-- Customers with more than 3 debit transactions
-- in a single day.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    DATE(t.transaction_date) AS transaction_day,
    COUNT(t.transaction_id) AS debit_count
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'DEBIT'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    DATE(t.transaction_date)
HAVING COUNT(t.transaction_id) > 3
ORDER BY debit_count DESC;