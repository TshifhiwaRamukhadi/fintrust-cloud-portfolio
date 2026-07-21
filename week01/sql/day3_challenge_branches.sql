CREATE TABLE branches (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL,
    province VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE accounts
ADD COLUMN branch_id INT,
ADD FOREIGN KEY (branch_id)
REFERENCES branches(branch_id);

INSERT INTO branches
(branch_name, province, city)
VALUES
('Sandton City Branch', 'Gauteng', 'Johannesburg'),
('Cape Town CBD Branch', 'Western Cape', 'Cape Town'),
('Gateway Branch', 'KwaZulu-Natal', 'Durban');

UPDATE accounts
SET branch_id = 1
WHERE account_id = 1;

UPDATE accounts
SET branch_id = 2
WHERE account_id = 2;