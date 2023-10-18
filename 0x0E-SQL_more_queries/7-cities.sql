-- Creates the database hbtn_0d_usa and the table cities (in the database
-- hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	FOREIGN KEY (state_id INT NOT NULL) REFERENCES states(id),
	mame VARCHAR(256) NOT NULL
);
