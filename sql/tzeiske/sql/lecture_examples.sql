---To create the database, see lecture_create.sql
\connect dsilecture

--- Querying the data
--- Select all the rows in customers ---
SELECT * FROM customers;

--- Check the table count ---
SELECT count(*) FROM customers;


-- Select only 3 rows in customers ---
SELECT * FROM customers LIMIT 3;


--- Select all customers from CA ---
SELECT name
FROM customers
WHERE state = 'CA';


--- Max and min age of the customers ---
SELECT
    MAX(age) as max_age
,   MIN(age) as min_age
FROM customers;


--- Select average age by state---
SELECT
    state
,    AVG(age) as avg_age
FROM customers
GROUP BY state;


--- Count number of visits by customer ---
SELECT
   customer_id
,  COUNT(*)
FROM visits
GROUP BY customer_id;


-- Select the number of distinct states in the customers table ---
SELECT DISTINCT state
FROM customers;


--- Count visits by customer and sort in descending order ---
SELECT
   customer_id
,  COUNT(*) as cnt
FROM visits
GROUP BY customer_id
ORDER BY cnt DESC;
-- try ASC instead of DESC!


---BACK TO SLIDES THEN DO THE FOLLOWING---


--- Return the customer_ids of all customers who visited in June ---
SELECT
  c.id
, v.created_at
FROM customers as c
JOIN visits as v
ON c.id = v.customer_id
WHERE date_part('month', v.created_at) = 6;


--- LEFT JOIN: return all customers from the customers table regardless of presence in visits
SELECT
  c.id
, v.created_at
FROM customers as c
LEFT JOIN visits as v
ON c.id = v.customer_id
WHERE date_part('month', v.created_at) = 6;
--DO BOTH WITHOUT THE WHERE CLAUSE TO SEE THE DIFFERENCE!--


--- Alternate way of doing an INNER JOIN ----
SELECT
  c.id
, v.created_at
FROM customers as c, visits as v
WHERE c.id = v.customer_id
and date_part('month', v.created_at) = 6;


--- Example of CASE: (same as if/else)
SELECT id, name,
   CASE WHEN gender = 'F' THEN 'female' ELSE 'male' END AS gender_r
FROM customers;
