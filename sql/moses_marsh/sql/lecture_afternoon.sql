-- SQL, afternoon

\connect readychef

-- number of meals above the average price

-- (can do a subquery as part of a comparison)

SELECT COUNT(*)
	FROM meals
		WHERE price > (SELECT AVG(price) FROM meals);

-- meals above their types (e.g., french, italian, ...) average price

SELECT meal_id, meals.type, price, average.avg_price
	FROM meals 
	JOIN (
		SELECT type, AVG(price) AS avg_price
			FROM meals
			GROUP BY type
		) AS average ON average.type = meals.type
	WHERE price > avg_price
	LIMIT 10;

-- same as above but with a WITH clause

WITH average AS (
	SELECT type, AVG(price) AS avg_price
		FROM meals
		GROUP BY type
)

SELECT meal_id, meals.type, price, average.avg_price
	FROM meals
	INNER JOIN average ON average.type = meals.type
	WHERE price > avg_price
	LIMIT 10;

-- number of meals by type above the overall average price

SELECT COUNT(*), type
	FROM meals 
	WHERE price > (SELECT AVG(price) FROM meals)
	GROUP BY type;

-- number of meals by type above the overall average price ordered by decreasing number of meals

SELECT COUNT(*) as count, type
	FROM meals 
	WHERE price > (SELECT AVG(price) FROM meals)
	GROUP BY type
	ORDER BY count DESC;

-- type of meals whose average price is above the overall average price

SELECT type, AVG(price) AS avg_price
	FROM meals
	GROUP BY type
	HAVING AVG(price) > (SELECT AVG(price) FROM meals);

-- note: AVG(price) in HAVING is optional in SELECT
-- note: cannot have 'HAVING avg_price > ...'

-- same without HAVING

WITH average_by_type AS (
            SELECT type, AVG(price) AS avg_price 
            FROM meals 
            GROUP BY type
                        ),
     overall_average AS (
            SELECT AVG(price) AS avg_price 
            FROM meals
                        )

SELECT average_by_type.type, average_by_type.avg_price
	FROM average_by_type, overall_average
	WHERE average_by_type.avg_price > overall_average.avg_price;

-- find all the meals from that are above the average price of the previous 7 days.

SELECT a.meal_id
    FROM meals a
    JOIN meals b
        ON b.dt <= a.dt AND b.dt > (a.dt - 7)
    GROUP BY a.meal_id, a.price
    HAVING a.price > AVG(b.price);


SELECT *
    FROM meals a
    JOIN meals b
        ON b.dt <= a.dt AND b.dt > (a.dt - 7);



-- create table from query

CREATE TABLE average AS (
     SELECT type, AVG(price) AS avg_price
     FROM meals
     GROUP BY type
);

-- DELETE FROM TABLE

DELETE FROM average WHERE type = 'vietnamese';

-- DELETE FROM TABLE

DELETE FROM average WHERE avg_price > 10;

-- save to CSV

COPY average TO '/tmp/average.csv' DELIMITER ',';

-- DROP TABLE

DROP TABLE average;
