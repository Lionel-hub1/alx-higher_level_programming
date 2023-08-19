-- This script creates the table never_empty on your MySQL server (in localhost).
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1, 
    name VARCHAR(256)
);