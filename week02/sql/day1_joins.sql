-- ==========================================================
-- FinTrust Bank
-- Week 2 Day 1
-- SQL JOIN Exercises
-- Author: Tshifhiwa Ramukhadi
-- ==========================================================

-- ==========================================================
-- Exercise 1
-- Show customer name, account type and balance.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    a.account_type,
    a.balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
ORDER BY a.balance DESC;


-- ==========================================================
-- Exercise 2
-- Gauteng customers with balance greater than R25,000.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    c.province,
    a.account_type,
    a.balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE c.province = 'Gauteng'
  AND a.balance > 25000
ORDER BY a.balance DESC;


-- ==========================================================
-- Exercise 3
-- Three-table JOIN showing customer transactions.
-- Only DEBIT transactions.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    a.account_type,
    t.amount,
    t.transaction_date
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'DEBIT'
ORDER BY t.transaction_date DESC;


-- ==========================================================
-- Exercise 4
-- Customers who have never made a transaction.
-- LEFT JOIN + IS NULL pattern.
-- ==========================================================

SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;


-- ==========================================================
-- Exercise 5
-- Transactions greater than R10,000 for customers
-- in Western Cape or KwaZulu-Natal.
-- ==========================================================

SELECT
    c.first_name,
    c.last_name,
    c.province,
    t.amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.amount > 10000
  AND c.province IN ('Western Cape', 'KwaZulu-Natal')
ORDER BY t.amount DESC;