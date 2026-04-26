-- ############################################
-- TOPIC: SELECT FROM WORLD TABLE OF COUNTRIES
-- ############################################

-- Q1: Show the population of Germany
SELECT population FROM world WHERE name = 'Germany';

-- Q2: Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
SELECT name, population FROM world WHERE name in ("Sweden", "Norway", "Denmark");

-- Q3: Show the country and the area for countries with an area between 200,000 and 250,000.
SELECT name, area FROM world WHERE area BETWEEN 200000 and 250000


-- ###########################
-- PATTERN MATCHING WITH LIKE
-- ###########################

-- Q1: Find the country that start with Y
SELECT name FROM world WHERE name LIKE 'Y%'

-- Q2: Find the country that end with Y
SELECT name FROM world WHERE name LIKE '%Y'

-- Q3: Find the countries that contain the letter x
SELECT name FROM world WHERE name LIKE '%x%'

--Q4: Find the countries that end with land
SELECT name FROM world WHERE name LIKE '%land'

--Q5: Find the countries that end with land
SELECT name FROM world WHERE name LIKE 'C%ia'

--Q6: Find the country that has oo in the name
SELECT name FROM world WHERE name LIKE '%oo%'

--Q7: Find the countries that have three or more a in the name
SELECT name FROM world WHERE name LIKE '%a%a%a%'