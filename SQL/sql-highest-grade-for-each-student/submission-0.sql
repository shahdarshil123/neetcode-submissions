-- Write your query below
WITH row_num_table AS
(SELECT student_id, exam_id, score, ROW_NUMBER()OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) AS row_num
FROM exam_results)

SELECT student_id, exam_id, score
FROM row_num_table
WHERE row_num = 1;

