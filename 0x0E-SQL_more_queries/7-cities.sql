-- This script creates a table cities with some constraints.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- selecting the correct database
USE hbtn_0d_usa;
-- Then create the table in there
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);