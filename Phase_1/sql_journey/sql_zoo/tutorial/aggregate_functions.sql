-- Aggregates 
-- Aggregate functions like SUM and COUNT take many rows and summarise them into a single row.

-- Distinct
-- The result of a SELECT statement may contain identical rows. We can remove these duplicates using the DISTINCT key word.

-- Order by
-- ORDER BY allows us to see the result of a SELECT in a particular order. We may indicate ASC or DESC for ascending (smallest first, largest last) or descending order.
-- If you don't use ORDER BY the results given might be in any order.

-- Total Population
SELECT SUM(population) FROM world

-- List all the continents - just once each.
SELECT DISTINCT continent FROM world

-- Give the total GDP of Africa
SELECT SUM(gdp) FROM world WHERE continent = "Africa"

-- How many countries have an area of at least 1000000
SELECT COUNT(name) FROM world WHERE area >= 1000000

--What is the total population of ('Estonia', 'Latvia', 'Lithuania')
SELECT SUM(population) FROM world WHERE name IN ('Estonia', 'Latvia', 'Lithuania')


-- Using GROUP BY and HAVING

-- For each continent show the continent and number of countries.
SELECT continent, COUNT(name) FROM world GROUP BY continent

--