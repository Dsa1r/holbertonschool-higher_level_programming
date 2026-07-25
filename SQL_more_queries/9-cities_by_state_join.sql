-- Lists all cities with their corresponding state

-- Select all cities and their state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
