-- Delete movies by title
--DELETE FROM movies WHERE title IN ('Batman', 'Spiderman', 'Avatar');

-- Delete discontinued movies
--DELETE FROM movies WHERE discontinued = 1;

-- Delete books wrote before 1900
DELETE FROM books WHERE year_published < 1900;