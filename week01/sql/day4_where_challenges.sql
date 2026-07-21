-- ==========================================================
-- FinTrust Bank
-- Week 1 Day 4
-- WHERE Clause Challenge Solutions
-- Author: Tshifhiwa Ramukhadi
-- ==========================================================

-- ==========================================================
-- Challenge 1
-- Business Question:
-- Find customers outside Gauteng and Western Cape
-- for regional customer analysis.
-- ==========================================================

SELECT *
FROM customers
WHERE province NOT IN ('Gauteng', 'Western Cape');



-- ==========================================================
-- Challenge 2
-- Business Question:
-- Find CHEQUE and SAVINGS accounts with balances
-- between R1,000 and R20,000.
-- ==========================================================

SELECT *
FROM accounts
WHERE balance BETWEEN 1000 AND 20000
  AND account_type IN ('CHEQUE', 'SAVINGS');



-- ==========================================================
-- Challenge 3
-- Business Question:
-- Find high-value grocery or food transactions
-- over R200.
-- ==========================================================

SELECT *
FROM transactions
WHERE (
        merchant_category LIKE '%Food%'
        OR merchant_category LIKE '%Groceries%'
      )
  AND amount > 200;



-- ==========================================================
-- Challenge 4
-- Business Question:
-- Find DEBIT transactions with missing merchant
-- information and amounts greater than R100.
-- ==========================================================

SELECT *
FROM transactions
WHERE transaction_type = 'DEBIT'
  AND merchant_category IS NULL
  AND amount > 100;



-- ==========================================================
-- Challenge 5
-- Business Question:
-- Find customers with email addresses ending in
-- .co.za or .com who have a province recorded.
-- ==========================================================

SELECT *
FROM customers
WHERE (
        email LIKE '%.co.za'
        OR email LIKE '%.com'
      )
  AND province IS NOT NULL
ORDER BY last_name ASC;