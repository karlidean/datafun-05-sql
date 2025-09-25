-- Get the total books and average publishing year per author
SELECT author_id, COUNT(*) AS total_books, AVG(year_published) AS avg_year
FROM books
GROUP BY author_id;