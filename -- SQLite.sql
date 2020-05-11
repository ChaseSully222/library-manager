-- SQLite
INSERT INTO libraryapp_library
(title, address)
VALUES
('Bellview Library', '500 Main Street');

INSERT INTO libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
VALUES
('Lamb', '59359409490', 2004, 1, 'Christopher Moore', 1);

INSERT INTO libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
VALUES
('Taiko', '04275747474873', 2001, 1, 'Eiji Yoshikawa', 1);
