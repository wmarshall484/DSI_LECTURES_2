CREATE TABLE CUSTOMERS (
    id INTEGER PRIMARY KEY
,   name VARCHAR(50)
,   age INTEGER
,   city VARCHAR(255)
,   state VARCHAR(2)
    );

INSERT INTO CUSTOMERS(id, name, age, city, state) VALUES
    (1, 'john', 25, 'San Francisco', 'CA')
,   (2, 'becky', 30, 'NYC', 'NY')
,   (3, 'sarah', 20, 'Denver', 'CO') ;


CREATE TABLE PRODUCTS (
	id INTEGER PRIMARY KEY
,	name VARCHAR(50)
,	price FLOAT
	);

INSERT INTO PRODUCTS (id, name, price) VALUES
	(1, 'soccer ball', 20.5)
,	(2, 'iPod', 200)
,	(3, 'headphones', 50) ;

CREATE TABLE purchases_no_key (
    customer_id INTEGER
,    product_id INTEGER
,    date TIMESTAMP
,    quantity INTEGER);

INSERT INTO purchases_no_key ( customer_id, product_id, date, quantity) VALUES
	(1, 2, '2015-07-30', 2)
,	(2, 4, '2015-06-20', 3)
,	(1, 3, '2015-04-09', 1);

CREATE TABLE purchases (
    customer_id INTEGER REFERENCES customers(id)
,    product_id INTEGER REFERENCES products(id)
,    date TIMESTAMP
,    quantity INTEGER );

--breaks because of FK constraint on product_id
INSERT INTO purchases ( customer_id, product_id, date, quantity) VALUES
	(1, 2, '2015-07-30', 2)
,	(2, 4, '2015-06-20', 3)
,	(1, 3, '2015-04-09', 1);

--clean
INSERT INTO purchases ( customer_id, product_id, date, quantity) VALUES
	(1, 2, '2015-07-30', 2)
,	(2, 3, '2015-06-20', 3)
,	(1, 3, '2015-04-09', 1);

CREATE TABLE VISITS (
  id INTEGER PRIMARY KEY
,  created_at TIMESTAMP
,  customer_id INTEGER REFERENCES customers(id) );

INSERT INTO VISITS (id, created_at, customer_id) VALUES
	(1, '2015-06-20', 1)
,	(2, '2015-07-30', 1)
,	(3, '2015-06-20', 3)
,	(4, '2015-04-09', 1)
,	(5, '2015-03-09', 2);

CREATE TABLE LICENSES (
	id INTEGER PRIMARY KEY
,	state VARCHAR(2)
,	number VARCHAR(20)
,	uploaded_at TIMESTAMP
,	customer_id INTEGER REFERENCES customers(id)
,	UNIQUE(state, number))

INSERT INTO LICENSES (id, state, number, uploaded_at, customer_id) VALUES
	(1, 'CO', 'DL19480284', '2013-04-18', 3)
,	(2, 'CA', 'DL19852984', '2014-05-12', 1)


SELECT c.id, l.number
FROM customers c
LEFT JOIN licenses l
	ON l.customer_id = c.id