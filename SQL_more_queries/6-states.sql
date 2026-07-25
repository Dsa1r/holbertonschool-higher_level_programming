-- Creates the database hbtn_0d_usa and the table states

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database
USE hbtn_0d_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
