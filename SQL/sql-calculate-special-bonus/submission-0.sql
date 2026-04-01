-- Write your query below
SELECT e.employee_id,
    CASE 
    WHEN e.employee_id % 2 = 1 AND SUBSTRING(e.name,1,1) != 'M' THEN e.salary
    ELSE 0
    END AS bonus
FROM employees e
ORDER BY e.employee_id
