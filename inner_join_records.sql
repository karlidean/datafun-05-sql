-- Joining the authors and books tables by the dependent key (author_id)
SELECT authors.first, authors.last, books.title, books.year_published, books.book_id, authors.author_id
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;