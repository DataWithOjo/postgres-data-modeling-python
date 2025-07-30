-- accounts table
CREATE TABLE accounts (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address_1 TEXT,
    address_2 TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    join_date DATE
);

CREATE INDEX idx_accounts_state ON accounts(state);

-- products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_code VARCHAR(10),
    product_description TEXT
);

CREATE INDEX idx_products_code ON products(product_code);

-- transactions table
CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    transaction_date DATE,
    product_id INT,
    product_code VARCHAR(10),
    product_description TEXT,
    quantity INT,
    account_id INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (account_id) REFERENCES accounts(customer_id)
);

CREATE INDEX idx_transactions_product_id ON transactions(product_id);
CREATE INDEX idx_transactions_account_id ON transactions(account_id);
