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

--Q8: Find the countries that have "t" as the second character.
SELECT name FROM world WHERE name LIKE '_t%'

--Q9: Find the countries that have two "o" characters separated by two others.
SELECT name FROM world WHERE name LIKE '%o__o%'

--Q10: Find the countries that have exactly four characters.
SELECT name FROM world WHERE name LIKE '____'

-- OPTIONAL HARDER QUESTIONS

--Q1 Find the country where the name is the capital city.
SELECT name FROM world WHERE name in country

--Q2 Find the country where the name is the capital city.
SELECT name FROM world WHERE concat(name, ' City') LIKE capital

--Q3 Find the capital and the name where the capital includes the name of the country.
SELECT capital, name from world WHERE capital like concat('%', name, '%') 