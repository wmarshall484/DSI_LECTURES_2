--Get all meals above the average price.

SELECT AVG(price)
FROM meals
;

--Subquery 
SELECT meal_id
FROM meals as transactions, (
     SELECT AVG(price) as avg_price
     FROM meals
) as average
WHERE transactions.price > average.avg_price
;

--Can do a subquery as part of a comparison
SELECT meal_id
FROM meals as transactions
WHERE transactions.price > (SELECT AVG(price) from meals)
;

--Get meals above average price for that type
SELECT meal_id
, transactions.price
, average.avg_price
, average.type
FROM meals as transactions
INNER JOIN (
     SELECT type
     	    , AVG(price) as avg_price
     FROM meals
     GROUP BY type
) as average
ON transactions.type = average.type
WHERE price > avg_price
LIMIT 10
;

--Same thing as above but more readably
WITH average as (
     SELECT type
     	    , AVG(price) as avg_price
     FROM meals
     GROUP BY type
)

SELECT meal_id
, transactions.price
, average.avg_price
, average.type
FROM meals as transactions
INNER JOIN average
ON transactions.type = average.type
WHERE price > avg_price
LIMIT 10
;

--Create table based on query.
CREATE TABLE average as (
     SELECT type
     	    , AVG(price) as avg_price
     FROM meals
     GROUP BY type
);

--Drop table.
DROP TABLE average;

--DELETE FROM TABLE
DELETE FROM average
WHERE type='vietnamese';

--DELETE FROM TABLE
DELETE FROM average
WHERE avg_price > 10;

--Create CSV

 COPY customers TO '/tmp/customer.csv' DELIMITER ',';
