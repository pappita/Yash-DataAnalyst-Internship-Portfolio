-- Check Missing Values
SELECT COUNT(*) FROM sales_data WHERE amount IS NULL;

-- Remove Duplicates
DELETE FROM sales_data
WHERE customer_id NOT IN (
    SELECT MIN(customer_id)
    FROM sales_data
    GROUP BY email, purchase_date
);

-- Remove Outliers
DELETE FROM sales_data
WHERE amount > 100000;

-- Add Age Column
ALTER TABLE sales_data ADD age INT;

UPDATE sales_data
SET age = YEAR(CURDATE()) - YEAR(date_of_birth);
