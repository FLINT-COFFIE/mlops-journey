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

--Q4 Find the capital and the name where the capital is an extension of name of the country.
SELECT capital, name from world WHERE capital like concat(name,"_", "%")

--Q5 Show the name and the extension where the capital is a proper (non-empty) extension of name of the country.
SELECT name, from world WHERE capital like concat(name,"-", "%")

--Q6 Show the name and the extension where the capital is a proper (non-empty) extension of name of the country.
SELECT name, replace(capital , name, "" ) from world WHERE capital like concat(name,"_", "%")

-- NB: concat combines words
--     replace takes the first string and replaces the second instance of the string with the third.


-- ###########################
-- SELECTING FROM WORLD
-- ###########################

--Q1 selecting name continent and population
SELECT name, continent, population FROM world

--Q2 Large questions
SELECT name FROM world WHERE population >= 200000000

--Q3 Give the name and the per capita GDP for those countries with a population of at least 200 million.
SELECT name, GDP/population FROM world WHERE population >= 200000000

--Q4 Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.
SELECT name, population/1000000 FROM world WHERE continent = "South America"

--Q5 Show the name and population for France, Germany, Italy
SELECT name, population FROM world WHERE name in ("France", "Germany", "Italy")