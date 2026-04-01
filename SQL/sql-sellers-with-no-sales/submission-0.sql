-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN
(SELECT o.seller_id
FROM orders o
WHERE TO_CHAR(o.sale_date, 'YYYY') = '2020')
ORDER BY s.seller_name;
