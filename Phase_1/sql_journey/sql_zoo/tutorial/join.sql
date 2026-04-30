
-- The Join Operation

-- Modify it to show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'
SELECT matchid, player FROM goal WHERE teamid = 'GER'

-- Show id, stadium, team1, team2 for just game 1012
SELECT id,stadium,team1,team2 FROM game WHERE id = 1012

-- show the player, teamid, stadium and mdate for every German goal.
SELECT player,teamid, stadium, mdate 
  FROM game JOIN goal ON (id=matchid)
WHERE teamid = "GER"

-- Show the team1, team2 and player for every goal scored by a player called Mario
SELECT team1, team2, player 
 FROM game JOIN goal ON (id = matchid)
WHERE player LIKE 'Mario%'

-- Show player, teamid, coach, gtime for all goals scored in the first 10 minutes gtime<=10
SELECT player, teamid, coach, gtime
FROM goal JOIN eteam ON (teamid = id)
WHERE gtime <= 10

-- List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.
SELECT mdate, teamname 
FROM game JOIN eteam ON (team1 = eteam.id)
WHERE coach = "Fernando Santos" 

--List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'
SELECT player
FROM goal JOIN game ON (matchid = id)
WHERE stadium = "National Stadium, Warsaw"

-- MORE DIFFICULT QUESTIONS

-- Instead show the name of all players who scored a goal against Germany.
SELECT DISTINCT player
  FROM game JOIN goal ON matchid = id 
WHERE (team1 = "GER" OR team2 = "GER") AND teamid != "GER"

-- Show teamname and the total number of goals scored.
SELECT teamname, COUNT(player)
  FROM eteam JOIN goal ON id=teamid
GROUP BY teamname
ORDER BY teamname

-- Show the stadium and the number of goals scored in each stadium.
SELECT stadium, COUNT(player)
FROM goal
GROUP BY stadium

-- Show the stadium and the number of goals scored in each stadium.
SELECT stadium, COUNT(player)
FROM goal JOIN game ON (matchid = id)
GROUP BY stadium

-- For every match involving 'POL', show the matchid, date and the number of goals scored.
SELECT matchid, mdate, COUNT(matchid)
  FROM game JOIN goal ON matchid = id 
 WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY matchid, mdate

-- For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'
SELECT matchid, mdate, COUNT(matchid)
  FROM game JOIN goal ON matchid = id 
 WHERE (team1 = 'GER' OR team2 = 'GER') AND teamid = "GER"
GROUP BY matchid, mdate

-- List every match with the goals scored by each team for all ENG games as shown
SELECT mdate,team1,
SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) AS score1,
team2,
SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) AS score2
FROM game LEFT JOIN goal ON matchid = id
WHERE team1="ENG" OR team2="ENG"
GROUP BY mdate, team1, team2, matchid
ORDER BY mdate, matchid, team1, team2;


----- MORE JOIN OPERATIONS


-- List the films where the yr is 1962 and the budget is over 2000000 [Show id, title]
SELECT id, title
 FROM movie
 WHERE yr=1962 AND budget > 2000000

-- Give year of 'Citizen Kane'.
SELECT yr FROM movie
WHERE title = "Citizen Kane"

-- List all of the Star Trek movies, include the id, title and yr (all of these movies start with the words Star Trek in the title). Order results by year.
SELECT id, title, yr FROM movie 
WHERE title LIKE "Star Trek%"
ORDER BY yr

-- What id number does the actor 'Glenn Close' have?
SELECT id FROM actor 
WHERE name = 'Glenn Close'

-- What is the id of the 1942 film 'Casablanca'
SELECT id FROM movie 
WHERE title = 'Casablanca' AND yr = 1942

-- Obtain the cast list for the film 'Alien'
SELECT name
FROM actor
JOIN casting ON actorid = actor.id
JOIN movie ON movieid = movie.id
WHERE title = "Alien"

-- List the films in which 'Harrison Ford' has appeared
SELECT title
FROM actor
JOIN casting ON actorid = actor.id
JOIN movie ON movieid = movie.id
WHERE name = "Harrison Ford"

-- List the films where 'Harrison Ford' has appeared - but not in the starring role. [Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]
SELECT title
FROM actor
JOIN casting ON actorid = actor.id
JOIN movie ON movieid = movie.id
WHERE name = "Harrison Ford" AND ORD != 1

-- List the films together with the leading star for all 1962 films.
SELECT title, name
FROM actor
JOIN casting ON actorid = actor.id
JOIN movie ON movieid = movie.id
WHERE ORD = 1 AND yr = 1962