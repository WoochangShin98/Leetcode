# Write your MySQL query statement below
SELECT l.book_id, l.title, l.author, l.genre, l.publication_year, t.current_borrowers
FROM library_books l
JOIN (SELECT book_id, COUNT(*) AS current_borrowers 
FROM borrowing_records 
WHERE return_date IS NULL
GROUP BY book_id) t
ON l.book_id = t.book_id
WHERE l.total_copies = t.current_borrowers
ORDER BY t.current_borrowers DESC, l.title ASC;