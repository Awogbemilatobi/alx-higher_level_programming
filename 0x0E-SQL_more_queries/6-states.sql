-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database and create a table
CREATE TABLE If NOT EXISTS hbtn_0d_usa.state(
id INT UNIQUE AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL, PRIMARY KEY(id));


