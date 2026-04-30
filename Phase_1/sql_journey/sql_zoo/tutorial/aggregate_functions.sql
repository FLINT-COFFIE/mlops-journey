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

-- For each continent show the continent and number of countries with populations of at least 10 million.
SELECT continent, COUNT(name) FROM world WHERE population >= 10000000 GROUP BY continent

-- List the continents that have a total population of at least 100 million.
SELECT continent FROM world WHERE population >= 100000000 GROUP BY continent


-- The Join Operation

-- Modify it to show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'
SELECT matchid, player FROM goal WHERE teamid = 'GER'

-- Show id, stadium, team1, team2 for just game 1012
SELECT id,stadium,team1,team2 FROM game WHERE id = 1012

-- show the player, teamid, stadium and mdate for every German goal.
SELECT player,teamid, stadium, mdate 
  FROM game JOIN goal ON (id=matchid)
WHERE teamid = "GER"

