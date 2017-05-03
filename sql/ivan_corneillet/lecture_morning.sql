-- SQL, morning

-- "show databases"

\l or \list

DROP DATABASE IF EXISTS galvanize_dsi;

CREATE DATABASE galvanize_dsi;

\connect galvanize_dsi

-- "show tables"

\d

-- licensing system example database setup

CREATE TABLE customers (
	id INTEGER PRIMARY KEY,
	name VARCHAR(50),
	age INTEGER,
	gender VARCHAR(1),
	city VARCHAR(255),
	state VARCHAR(2)
);

INSERT INTO customers (id, name, age, gender, city, state) VALUES
	(1, 'john', 25, 'M', 'San Francisco', 'CA'),
	(2, 'becky', null, 'F', 'NYC', 'NY'),
	(3, 'sarah', 20, 'F', 'Denver', 'CO'),
	(4, 'max', 35, 'M', 'Austin', 'TX'),
	(5, 'sam', 40, 'M', 'Fremont', 'CA'),
	(6, 'riley', 22, 'F', 'Seattle', 'WA'),
	(7, 'eve', 43, 'F', 'NYC', 'NY');

CREATE TABLE visits (
	id INTEGER PRIMARY KEY,
	created_at TIMESTAMP,
	customer_id INTEGER REFERENCES customers(id)
);

INSERT INTO visits (id, created_at, customer_id) VALUES
	(1, '2014-06-20', 1),
	(2, '2015-07-30', 1),
	(3, '2015-06-20', 3),
	(4, '2015-04-09', 1),
	(5, '2015-03-09', 2);

CREATE TABLE licenses (
	id INTEGER PRIMARY KEY,
	state VARCHAR(2),
	number VARCHAR(20),
	uploaded_at TIMESTAMP,
	customer_id INTEGER REFERENCES customers(id),
	UNIQUE(state, number)
);

INSERT INTO LICENSES (id, state, number, uploaded_at, customer_id) VALUES
	(1, 'CO', 'DL19480284', '2013-04-18', 3),
	(2, 'CA', 'DL19852984', '2013-05-12', 1);

\d

-- number of customers

SELECT COUNT(*) FROM customers;

-- all rows in customers

SELECT * FROM customers;

-- only 3 rows in customers ---

SELECT * FROM customers LIMIT 3;

-- all customers from CA ---

SELECT name
	FROM customers
	WHERE state = 'CA';

-- customers' max and min age

SELECT MAX(age) AS max_age, MIN(age) AS min_age
	FROM customers;

-- average age by state

SELECT state, AVG(age) AS avg_age
	FROM customers
	GROUP BY state;

-- number of visits by customer

SELECT customer_id, COUNT(*)
	FROM visits
	GROUP BY customer_id;

-- states the customers are from

SELECT DISTINCT state
	FROM customers;

-- number of visits by customer, sorted in descending order of visits

SELECT customer_id, COUNT(*) AS cnt
	FROM visits
	GROUP BY customer_id
	ORDER BY cnt DESC;

-- 

SELECT state, AVG(age) AS avg_age
	FROM customers
	GROUP BY state
	HAVING avg(age) > 30;

-- which customers visited in June and when (INNER JOINs)

SELECT c.id, v.created_at AS on
	FROM customers AS c, visits AS v
	WHERE (c.id = v.customer_id) AND DATE_PART('month', v.created_at) = 6;

SELECT c.id, v.created_at AS on
	FROM customers AS c
	JOIN visits AS v ON v.customer_id = c.id
	WHERE DATE_PART('month', v.created_at) = 6;

-- all customers and their visits, if any (LEFT JOIN)

SELECT c.id, v.created_at
	FROM customers AS c
	LEFT JOIN visits AS v ON v.customer_id = c.id;

-- formatting gender (CASE)

SELECT id, name,
	CASE WHEN gender = 'F' THEN 'female' ELSE 'male' END AS gender
	FROM customers;

-- products

CREATE TABLE products (
	id INTEGER PRIMARY KEY,
	name VARCHAR(50),
	price FLOAT);

INSERT INTO products (id, name, price) VALUES
	(1, 'soccer ball', 20.5),
	(2, 'iPod', 200),
	(3, 'headphones', 50);

-- purchases

CREATE TABLE purchases (
  	id INTEGER PRIMARY KEY,
	customer_id INTEGER REFERENCES customers(id),
	product_id INTEGER REFERENCES products(id),
	date TIMESTAMP,
	quantity INTEGER);

CREATE TABLE purchases_no_references (
  	id INTEGER PRIMARY KEY,
	customer_id INTEGER,
	product_id INTEGER,
	date TIMESTAMP,
	quantity INTEGER);

INSERT INTO purchases (id, customer_id, product_id, date, quantity) VALUES
	(1, 1, 2, '2015-07-30', 2),
	(2, 2, 3, '2015-06-20', 3),
	(3, 1, 3, '2015-04-09', 1);

INSERT INTO purchases_no_references (id, customer_id, product_id, date, quantity) VALUES
	(1, 1, 2, '2015-07-30', 2),
	(2, 2, 3, '2015-06-20', 3),
	(3, 1, 3, '2015-04-09', 1);

INSERT INTO purchases_no_references (id, customer_id, product_id, date, quantity) VALUES
	(4, 1, 4, '2015-04-23', 5);

INSERT INTO purchases (id, customer_id, product_id, date, quantity) VALUES
	(4, 1, 4, '2015-04-23', 5);
