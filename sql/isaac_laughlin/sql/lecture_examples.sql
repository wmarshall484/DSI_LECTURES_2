
---To create a database, run the following command at the psql prompt
CREATE DATABASE cohort17;
\connect cohort17


--- Licensing System ----
CREATE TABLE CUSTOMERS (
    id INTEGER PRIMARY KEY
,   name VARCHAR(50)
,   age INTEGER
,   gender VARCHAR(1)
,   city VARCHAR(255)
,   state VARCHAR(2));


INSERT INTO CUSTOMERS(id, name, age, gender, city, state) VALUES
	(1, 'john', 25, 'M', 'San Francisco', 'CA')
,	(2, 'becky', null, 'F', 'NYC', 'NY')
,	(3, 'sarah', 20, 'F', 'Denver', 'CO')
,   (4, 'max', 35, 'M', 'Austin', 'TX')
,   (5, 'sam', 40, 'M', 'Fremont', 'CA')
,   (6, 'riley', 22, 'F', 'Seattle', 'WA');



CREATE TABLE VISITS (
  id INTEGER PRIMARY KEY
,  created_at TIMESTAMP
,  customer_id INTEGER REFERENCES customers(id) );


INSERT INTO VISITS (id, created_at, customer_id) VALUES
	(1, '2014-06-20', 1)
,	(2, '2015-07-30', 1)
,	(3, '2015-06-20', 3)
,	(4, '2015-04-09', 1)
,	(5, '2015-03-09', 2);


CREATE TABLE LICENSES (
  id INTEGER PRIMARY KEY
, state VARCHAR(2)
, number VARCHAR(20)
, uploaded_at TIMESTAMP
, customer_id INTEGER REFERENCES customers(id)
, UNIQUE(state, number));


INSERT INTO LICENSES (id, state, number, uploaded_at, customer_id) VALUES
  (1, 'CO', 'DL19480284', '2013-04-18', 3)
, (2, 'CA', 'DL19852984', '2013-05-12', 1);

--- Querying the data
--- Check the table count ---
SELECT count(*) FROM customers;

--- Select all the rows in customers ---

SELECT * FROM customers;

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


----
SELECT
    id
,   name
,   state
,   avg(age) as avg_age
FROM customers
GROUP BY id, name, state
HAVING avg(age) > 30;

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


--- Alternate way of doing an INNER JOIN ----

SELECT
  c.id
, v.created_at
FROM customers as c, visits as v
WHERE c.id = v.customer_id
and date_part('month', v.created_at) = 6;


--- Example of CASE: how many customers ?
SELECT id, name,
   CASE WHEN gender = 'F' THEN 'female' ELSE 'male' END AS gender_r
FROM customers;


--- Products Table ----
CREATE TABLE PRODUCTS (
  id INTEGER PRIMARY KEY
, name VARCHAR(50)
, price FLOAT);


INSERT INTO PRODUCTS (id, name, price) VALUES
	(1, 'soccer ball', 20.5)
,	(2, 'iPod', 200)
,	(3, 'headphones', 50);


CREATE TABLE PURCHASES (
  	id INTEGER PRIMARY KEY
,   customer_id INTEGER REFERENCES customers(id)
,   product_id INTEGER REFERENCES products(id)
,   date TIMESTAMP
,   quantity INTEGER );


INSERT INTO PURCHASES (id, customer_id, product_id, date, quantity) VALUES
    (1, 1, 2, '2015-07-30', 2)
,	(2, 2, 3, '2015-06-20', 3)
,	(3, 1, 3, '2015-04-09', 1);


CREATE TABLE purchases_no_key (
  	id INTEGER PRIMARY KEY
,   customer_id INTEGER
,   product_id INTEGER
,   date TIMESTAMP
,   quantity INTEGER);


INSERT INTO purchases_no_key (id, customer_id, product_id, date, quantity) VALUES
    (1, 1, 2, '2015-07-30', 2)
,   (2, 2, 4, '2015-06-20', 3)
,   (3, 1, 3, '2015-04-09', 1);

INSERT INTO purchases ( id, customer_id, product_id, date, quantity) VALUES
   (4, 2, 4, '2015-06-20', 3);
