-- Selecting books released after a certain year
-- SELECT * FROM books WHERE year_published > 1950;

-- You can also filter based on anything in the table you pull from
-- The table you pull from determines what you can pull

-- To avoid duplicates, use the DISTINCT function
-- SELECT DISTINCT title FROM books WHERE year_published = 1997;