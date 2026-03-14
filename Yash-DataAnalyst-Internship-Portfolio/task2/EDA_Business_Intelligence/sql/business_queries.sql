-- Top 5 products by revenue
SELECT product_name, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Category wise sales
SELECT category, SUM(revenue) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Average order value
SELECT AVG(revenue) AS avg_order_value
FROM sales;

-- Top customers by spending
SELECT customer_id, SUM(revenue) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;