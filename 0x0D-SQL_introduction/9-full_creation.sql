-- Displays the number of records with id = 89 in the table first_table of the database
CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
);
INSERT INTO second_table (id, name, score) VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
