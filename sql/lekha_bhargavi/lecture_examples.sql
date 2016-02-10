Miniquiz:
https://github.com/zipfian/miniquizzes/blob/master/classes.md

Lecture and examples: https://github.com/zipfian/DSI_Lectures/tree/master/sql/lekha_bhargavi



CREATE DATABASE class;

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
,	(2, 'becky', 30, 'F', 'NYC', 'NY')
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
--- Check the tables in the database ---


--- Select all the rows in customers ---


-- Select only the top 3 rows in customers ---


--- Select all customers from CA ---



--- Max and min age of the customers ---



--- Count number of visits by customer ---



-- Select the number of distinct states in the customers table ---


--- Count visits by customer and sort in descending order ---



--- Return the customer_ids of all customers who visited in June ---

SELECT c.id, v.created_at
FROM customers as c
JOIN visits as v
ON c.id = v.customer_id
WHERE date_part('month', v.created_at) = 6;


--- Example of CASE: how many customers ?
SELECT
   CASE WHEN gender = 'F' THEN 'female' ELSE 'male' END AS gender_r
FROM customers


---JOINS----

---List the names of customers who visited the Licensing office in 2014---



--- All customers including the visits for 2014---










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
,	(3, 1, 3, '2015-04-09', 1)


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



---- POll SQL ---

PollEv.com/gschool702

SELECT customer_id, count(*) as cust_cnt
FROM visits
GROUP BY customer_id
HAVING cust_cnt > 1

SELECT customer_id, count(*) as cust_cnt
FROM visits
HAVING cust_cnt > 1
GROUP BY customer_id;

SELECT customer_id, count(*) as cust_cnt
FROM visits
GROUP BY customer_id
HAVING cust_cnt > 1;
