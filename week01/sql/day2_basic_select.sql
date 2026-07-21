-- Exercise 1
SELECT first_name, last_name, province
FROM customers
ORDER BY province;

-- Exercise 2
SELECT account_number, account_type, balance
FROM accounts
WHERE account_type = 'SAVINGS'
LIMIT 20;

-- Exercise 3
SELECT DISTINCT province
FROM customers;

-- Exercise 4
SELECT
    account_number,
    balance,
    balance * 1.10 AS projected_balance
FROM accounts;

-- Exercise 5
SELECT COUNT(*) AS total_accounts
FROM accounts;