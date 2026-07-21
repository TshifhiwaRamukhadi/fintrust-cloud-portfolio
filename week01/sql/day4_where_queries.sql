-- ==========================================================
-- FinTrust Bank
-- Week 1 Day 4
-- WHERE Clause Filtering
-- Author: Tshifhiwa Ramukhadi
-- ==========================================================

-- ==========================================================
-- Exercise 1
-- Find all customers from Gauteng.
-- ==========================================================

SELECT *
FROM customers
WHERE province = 'Gauteng';


-- ==========================================================
-- Exercise 2
-- Find all accounts with a balance greater than R5,000.
-- ==========================================================

SELECT *
FROM accounts
WHERE balance > 5000;


-- ==========================================================
-- Exercise 3
-- Find customers whose email ends with .co.za
-- ==========================================================

SELECT *
FROM customers
WHERE email LIKE '%.co.za';


-- ==========================================================
-- Exercise 4
-- Find all DEBIT or PAYMENT transactions.
-- ==========================================================

SELECT *
FROM transactions
WHERE transaction_type IN ('DEBIT', 'PAYMENT');


-- ==========================================================
-- Exercise 5
-- Find SAVINGS accounts with balances between
-- R1,000 and R50,000.
-- ==========================================================

SELECT *
FROM accounts
WHERE account_type = 'SAVINGS'
  AND balance BETWEEN 1000 AND 50000;


-- ==========================================================
-- Exercise 6
-- Find transactions that have a merchant category.
-- ==========================================================

SELECT *
FROM transactions
WHERE merchant_category IS NOT NULL;


-- ==========================================================
-- Lab Query 1
-- Gauteng customers for regional campaign.
-- ==========================================================

SELECT customer_id, first_name, last_name, email
FROM customers
WHERE province = 'Gauteng'
ORDER BY last_name;


-- ==========================================================
-- Lab Query 2
-- Accounts with balances above R10,000.
-- ==========================================================

SELECT account_id, account_number, account_type, balance
FROM accounts
WHERE balance > 10000
ORDER BY balance DESC;


-- ==========================================================
-- Lab Query 3
-- All SAVINGS accounts.
-- ==========================================================

SELECT account_id, customer_id, account_number, balance
FROM accounts
WHERE account_type = 'SAVINGS'
ORDER BY balance DESC;


-- ==========================================================
-- Lab Query 4
-- Grocery transactions over R500.
-- ==========================================================

SELECT transaction_id,
       account_id,
       amount,
       transaction_type,
       transaction_date
FROM transactions
WHERE merchant_category = 'Groceries'
  AND amount > 500
ORDER BY amount DESC;


-- ==========================================================
-- Lab Query 5
-- Gmail customers.
-- ==========================================================

SELECT first_name, last_name, email
FROM customers
WHERE email LIKE '%gmail%'
ORDER BY last_name;


-- ==========================================================
-- Stretch Query
-- Active accounts with balances above R20,000.
-- ==========================================================

SELECT *
FROM accounts
WHERE balance > 20000;