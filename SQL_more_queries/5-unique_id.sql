-- Creates the table unique_id with a unique id column

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
