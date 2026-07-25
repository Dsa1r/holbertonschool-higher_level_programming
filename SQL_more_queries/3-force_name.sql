-- Creates the table force_name with a non-null name column

-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
