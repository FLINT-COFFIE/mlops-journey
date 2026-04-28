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

--Q6 Show the countries which have a name that includes the word 'United'
SELECT name from world WHERE name LIKE "%United%"

--Q7 Show the countries that are big by area or big by population. Show name, population and area.
SELECT name, population, area FROM world WHERE area > 3000000   OR population > 250000000

--Q8 Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.
SELECT name, population, area FROM world WHERE area > 3000000   XOR population > 250000000

--Q9 Show the name and population in millions and the GDP in billions for the countries of the continent 'South America'.
SELECT name, ROUND(population/1000000, 2), ROUND(GDP/1000000000, 2) FROM world WHERE continent LIKE "South America"

--Q10 Show the name and per-capita GDP for those countries with a GDP of at least one trillion (1000000000000; that is 12 zeros). Round this value to the nearest 1000.
SELECT name, ROUND(GDP/population, -3) FROM world where GDP > 1E12

--Q11 Show the name and capital where the name and the capital have the same number of characters.
SELECT name, capital FROM world WHERE LENGTH(name) = LENGTH(capital) 

--Q12 Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.
SELECT name, capital FROM world WHERE LEFT(name,1) = LEFT(capital,1) AND name <> capital

--Q13 Find the country that has all the vowels and no spaces in its name.
SELECT name FROM world WHERE 
name LIKE "%a%" AND
name LIKE "%e%" AND
name LIKE "%i%" AND
name LIKE "%o%" AND
name LIKE "%u%" AND
name NOT LIKE "% %"

-- ###########################
-- SELECTING FROM NOBEL
-- ###########################

--Q1 Nobel prizes for 1950.
SELECT yr, subject, winner FROM nobel WHERE yr = 1950

--Q2 Show who won the 1962 prize for literature.
SELECT winner FROM nobel WHERE yr = 1962 AND subject = 'LITERATURE'

--Q3 Show the year and subject that won 'Albert Einstein' his prize.
SELECT yr, subject FROM nobel WHERE winner = "Albert Einstein"

--Q4 Give the name of the 'Peace' winners since the year 2000, including 2000.
SELECT winner FROM nobel WHERE subject LIKE "%PEACE%" AND yr >= 2000

--Q5 Show all details (yr, subject, winner) of the literature prize winners for 1980 to 1989 inclusive.
SELECT yr,subject,winner FROM nobel WHERE subject = "literature" and yr BETWEEN 1980 AND 1989

--Q6 Show all details of the presidential winners: Theodore Roosevelt Thomas Woodrow Wilson Jimmy Carter Barack Obama
SELECT * FROM nobel
WHERE winner IN ("Theodore Roosevelt", "Thomas Woodrow Wilson","Jimmy Carter","Barack Obama")

--Q7 Show the winners with first name John
SELECT winner FROM nobel WHERE winner LIKE "John%"

--Q8 Show the year, subject, and name of physics winners for 1980 together with the chemistry winners for 1984.
SELECT yr, subject, winner FROM nobel WHERE (subject = "physics" AND yr = 1980) OR (subject = "chemistry" AND yr = 1984)

--Q9 Show the year, subject, and name of winners for 1980 excluding chemistry and medicine
SELECT yr, subject, winner FROM nobel WHERE yr = 1980 AND subject NOT IN ("chemistry", "medicine")