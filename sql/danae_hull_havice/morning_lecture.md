# Databases and SQL

## Why learn RDBMS/SQL?

RDBMS = Relational Database Management System

SQL = Structured Query Language

SQL is everywhere. It will often be the tool between you and the data you want. The majority of businesses store their data in a RDBMS and use SQL or SQL-like tools to access it. The combination is exceptionally good at efficiently storing complicated data sets while allowing for efficient information retrieval.

Data is stored in an SQL server, usually connected to remotely. For the exercises and examples, we'll be locally hosting our database. This is somewhat atypical of what you'll experience in the field.

Example:
Web front end <----> SQL Server <----> Data Queries

## Data Persistence

The most common form of data persistence is the flat file. You open up a text
editor, enter some information, and save the file to disk. You've just persisted
some data and can transfer that file wherever you wish. For most data, that's
enough, but for many applications, there are additional constraints other than
persistence and portability.

For example,

  * Ease of sharing between programming languages
  * Reliability guarantees 
  * Data integrity guarantees (e.g. no duplication)
  * Ability to query data efficiently
  * Ability to model relations in data

The first constraint is easily met by data formats such as JSON, CSV, or XML.
All mainstream programming languages have libraries to convert these formats to
native data structures and back to the interchange format. For example, Python
has the `json` module that converts between JSON strings and Python dicts.

However, these widely used data formats cannot meet the other constraints
listed above (and this is by no means an exhaustive list of desirable
constraints on data persistence).

## Relational Database Management Systems (RDBMS)

Relational databases such as PosgreSQL, MySQL, and SQLite were built for just
those purposes. They provide the ability to model relations in data and query
the data and their relations efficiently. They also provide a bevy of guarantees
to maintain data consistency and integrity.

*Note: The sorts of guarantees that these databases provide is beyond
the scope of this document (and this class), but feel free to reference the
resources at the bottom of this document if you're interested in learning more
about the underlying theory of relational databases.*

*Second Note: there are non-relational databases (NoSQL/MongoDB, etc.) that store data with different constraints and mechanisms for relationships between data subsets. We'll touch on these later in the course.*

## The RDBMS Data Model

Relational databases have a **schema** that defines the structure of the data. It's set when the database is created and is difficult to change later.

Each database is composed of a number of user-defined **tables**, each with
**columns** and **rows**. Each column is of a certain **data type** such as
integer, string, or date. Each row is an entry in the table with data for each
column of that table.

Here's an example of a database table creation specifying a `customers` table with various
fields and their data types:

```sql
CREATE TABLE CUSTOMERS (
    id INTEGER PRIMARY KEY
,   name VARCHAR(50)
,   age INTEGER
,   city VARCHAR(255)
,   state VARCHAR(2));
```

The data types available to you vary from system to system. These above are from
PostgreSQL. `VARCHAR` is a string data type.

A **primary key** is a column in a table that uniquely identifies that entry. No
two rows in the same table can share a value for a column specified as primary
key. The primary key column is most often `id`.

Here's an example of what this customers table looks like:

```
 id | name  | age |     city      | state
----+-------+-----+---------------+-------
  1 | john  |  25 | San Francisco | CA
  2 | becky |  30 | NYC           | NY
  3 | sarah |  20 | Denver        | CO
... | 
```

## Modeling Relations in RDBMS

Part of the power of relational databases are their ability to model relations
in data. The way they do so is through the use of **foreign keys**.
A foreign key is a column that references some other entry in the database.
That foreign entry could be in the same table or in some other table. Foreign
keys are how relations are modeled in relational databases.

For example, let's say there is another table that contains data for each visit
to our website. Each time a customer visits the site, a row is created and inserted
into the `visits` table. We'd like to maintain some data that indicates which
visit is associated with which customer (so that we could later, for example, find
the customers who visited our site the most). Each visit then will have a `customer_id`
that can connect it to a customer in the `customers` table.

Here's the definition of the `visits` table:

```sql
CREATE TABLE VISITS (
  id INTEGER PRIMARY KEY
,  created_at TIMESTAMP
,  customer_id INTEGER REFERENCES customers(id) );
```

Here's an example of what this visits table looks like:

```
 id |     created_at      | customer_id
----+---------------------+-------------
  1 | 2015-06-20 00:00:00 |           1
  2 | 2015-07-30 00:00:00 |           1
  3 | 2015-06-20 00:00:00 |           3
  4 | 2015-04-09 00:00:00 |           1
  5 | 2015-03-09 00:00:00 |           2
... | 
```

Here we specify not only that the `visits` table has a column called `customer_id`,
but that the column references the `id` column in the `customers` table. PostgreSQL
will treat this as a constraint and ensure that new visits have a `customer_id`
value that references an actual customer in the database.

### Types of Relationships

#### One-to-one

For a one-to-one relationship, place the foreign key on either side of the
relationship.

**Example: Customers and Licenses**
Licenses is a table that holds the _most recent_ driver's license number for a customer,
because customers can only have 1 driver's license at time, it will be a one-to-one relationship.

```sql
CREATE TABLE LICENSES (
  id INTEGER PRIMARY KEY
, state VARCHAR(2)
, number VARCHAR(20)
, uploaded_at TIMESTAMP
, customer_id INTEGER REFERENCES customers(id)
, UNIQUE(state, number))
```
```
SELECT * FROM licenses;
 id | state |   number   |     uploaded_at     | customer_id
----+-------+------------+---------------------+-------------
  1 | CO    | DL19480284 | 2013-04-18 00:00:00 |           3
  2 | CA    | DL19852984 | 2014-05-12 00:00:00 |           1
```

To find the license for a customer:

```sql
SELECT *
FROM licenses
WHERE customer_id=?
LIMIT 1
```
**Notice** we also used a UNIQUE constraint as the last part of our CREATE TABLE statement.
This is part of the power of SQL.  Because State and Driver's Licenses numbers should be unique,
we can help limit data input errors by placing a UNIQUE constraint.

#### One-to-many and many-to-one

For a one-to-many/many-to-one relationship (they are inverses of each other),
place the foreign key on the many side of the relationship.

**Example: Customer and Visits**

To find the visits for a customer:

```sql
SELECT *
FROM visits
WHERE customer_id=?
```

To find details on the customer for that visit:

```sql
SELECT *
FROM customers
WHERE id=?
LIMIT 1
```

#### Many-to-many

For a many-to-many relationship, create a table that contains two foreign keys,
one to each side of the relationship. This intermediate table is often referred
to as a **JOIN table**.

**Example 1: Customers and Products**

Here is our products table.  It lists all the products in the inventory.

```sql
CREATE TABLE PRODUCTS (
  id INTEGER PRIMARY KEY
, name VARCHAR(50)
, price FLOAT
  );
```
```
id |    name     | price
----+-------------+-------
  1 | soccer ball |  20.5
  2 | iPod        |   200
  3 | headphones  |    50
```

How do we know which customer purchased which product?  Here is our **JOIN** table.

```sql
CREATE TABLE PURCHASES (
  	id INTEGER PRIMARY KEY
,   customer_id INTEGER REFERENCES customers(id)
,   product_id INTEGER REFERENCES products(id)
,   date TIMESTAMP
,   quantity INTEGER );
```
```
 id | customer_id | product_id |        date         | quantity
----+-------------+------------+---------------------+----------
  1 |           1 |          2 | 2015-07-30 00:00:00 |        2
  2 |           2 |          3 | 2015-06-20 00:00:00 |        3
  3 |           1 |          3 | 2015-04-09 00:00:00 |        1
```

**Notice**  In the customers and products tables, there are PRIMARY KEY constraints on the IDs.
This ensures there is only 1 record for each customer and product.  We then used those keys to 
place FOREIGN KEY constraints on the customer_id and product_id in purchases.  This ensures our
data will only contain purchases by customers already in the database for products already in the
database.  Any other scenario indicates our data is not correct.

To find the products purchased by a customer:

```sql
SELECT products.*
FROM products
JOIN purchases
  ON products.id = purchases.product_id
WHERE purchases.customer_id=?
```

To find the customers who purchased a product:

```sql
SELECT customers.*
FROM customers
JOIN purchases
  ON customers.id = purchases.customer_id
WHERE purchases.product_id=?
```

## Schema Normalization

When designing a database schema (the tables and columns the database will
contain), we aim to minimize redundancy. This most importantly comes into play
with relations between data. As you saw above, when you want to relate data to
each other, use a simple foreign key - that's the smallest piece of information
that you can keep about another entry.

As an example, each post has an author, which is an entry in the `customers` table.
In a fully normalized schema, the post entry would have a `customer_id` which would
relate the post to a customer. A denormalized way of doing this would be to have a
column in the `posts` table called `author_name`, which would duplicate the
`name` column in the `customers` table. 

Normalization is largely about reducing redundancy. The cost is that some
queries will take longer to run because you will have to look up additional
information in other tables. The benefit is simplicity and a system that is
easier to understand and use. Always start with a fully normalized schema and
then when performance becomes an issue, you can consider selectively
denormalizing.

You can learn more about database normalization from [Wikipedia][wiki-normal].

[wiki-normal]: http://en.wikipedia.org/wiki/Database_normalization

## SQL

Structured Query Language (SQL) is the language used to query relational
databases. All RDBMS use SQL and the syntax and keywords are for the most part
the same across systems, though each system does have some of its own
peculiarities.

SQL is used to interact with RDBMS. That is, it allows you to create tables,
alter tables, insert records, update records, delete records, and query for
records within and across tables.

**We will focus primarily on querying.**

SQL, unlike Python or many other general purpose programming languages, is a
declarative language, meaning the query describes the set of results. Here's an
example of a simple query:

```sql
SELECT name, age
FROM customers
```

This query returns the name and age for every customer in the `customers` table.

```sql
SELECT name, age
FROM customers
WHERE state = 'CA'
```

This query returns the name and age for every customer in the `customers` table who
lives in CA.

## SQL Queries

SQL queries are composed of **clauses**. Each clause begins with a **keyword**.
Every query begins with the `SELECT` clause followed by the `FROM` and
`JOIN` clauses. You then have the ability to apply filtering, aggregation, and
ordering clauses. 

While `SELECT` appears at the top of the query, it is actually very nearly the
last part of the query that is executed. `SELECT` specifies the columns that
should be returned. 

**The most important parts of any SQL query are the `FROM` and `JOIN` clauses.**
These are the first parts of the query to be evaluated, specifying the rows upon
which all the filtering, aggregation, and ordering functions are applied.

We'll briefly cover `JOIN` and variants and then move to a conceptual overview
of the order of execution of a SQL query followed by a detailed example.

### JOIN

The `JOIN` clause enables querying based on relations in the data. It does so by
making use of foreign keys. 

Every `JOIN` clause has two segments: first, specifying the table to join, and
second, specifying the columns to match up (usually a primary key from one side
matched up with a foreign key on another).

There are a few different kinds of `JOIN`s: `INNER JOIN`, `LEFT OUTER JOIN`,
`RIGHT OUTER JOIN`, `FULL OUTER JOIN`, `NATURAL JOIN`, and `CROSS JOIN` are some
of the types.  We'll discuss the differences in just a moment. For now, we'll
start with `INNER JOIN`.

Here's an example of a simple `INNER JOIN`:

```sql
SELECT customers.name, visits.created_at
FROM visits
INNER JOIN customers
  ON customers.id = visits.customer_id
```

![inner_join](https://cloud.githubusercontent.com/assets/1425450/9778836/9f669cae-572a-11e5-9c96-98b59a930b7d.png)

Each visit has a `customer_id` that corresponds to the `id` column in the customers
table. In SQL, you specify the correspondence in the `ON` segment of the `JOIN`
clause. 

**For each match between `customers.id` and `visits.customer_id` that is found, a row is
inserted into the result set.** That means that if a customer has visited the site
multiple times, their information will be in the result set multiple times.

For example, the result may look like this:

```
 name  |     created_at
-------+---------------------
 john  | 2015-06-20 00:00:00
 john  | 2015-07-30 00:00:00
 sarah | 2015-06-20 00:00:00
 john  | 2015-04-09 00:00:00
 becky | 2015-03-09 00:00:00
```

Note how some customers show up multiple times in the result set. This make
sense given that some customers visited the site multiple times. You'll see later in
this document a slightly more detailed look at how the RDBMS constructs a result
set, including how it processes `JOIN`s.

### Aggregations

SQL allows you to aggregate your data set based on common keys.  To see the number of visits
from each customer_id we would query:

```sql
SELECT customer_id, COUNT(*)
FROM visits
GROUP BY customer_id
```

```
 customer_id | count
-------------+-------
           1 |     3
           3 |     1
           2 |     1
```

**Notice** The GROUP BY clause tells SQL what common factor we'd like to use to aggregate the data.
The COUNT aggregate function tells SQL how we'd like to aggregate.

When we JOIN tables we are essentially creating a new table, so we can use aggregate functions when 
using JOINs.  To get the amount of revenue from each product:

```sql
SELECT products.name, products.id, SUM(purchases.quantity * products.price) AS revenue
FROM products
JOIN purchases 
  ON products.id=purchases.product_id
GROUP BY products.name, products.id
```
```
    name    | id | revenue
------------+----+--------
 iPod       |  2 |    400
 headphones |  3 |    200
 ```

### Sorting

To make the results more readable, we can sort them.  Maybe we want the customers in alphabetical order.

```sql
SELECT *
FROM customers
ORDER BY NAME
```
```
 id | name  | age |     city      | state
----+-------+-----+---------------+-------
  2 | becky |  30 | NYC           | NY
  1 | john  |  25 | San Francisco | CA
  3 | sarah |  20 | Denver        | CO
```
And if we wanted them in reverse alphabetical order, we'd add the DESC keyword.

```sql
SELECT *
FROM customers
ORDER BY NAME DESC
```
```
 id | name  | age |     city      | state
----+-------+-----+---------------+-------
  3 | sarah |  20 | Denver        | CO
  1 | john  |  25 | San Francisco | CA
  2 | becky |  30 | NYC           | NY
  ```

### SQL Order of Operations

SQL does not perform operations "top to bottom".  Rather it executes statements in the following order:

1. **FROM**, **JOIN**: first the product of all tables is formed
2. **WHERE**: the where clause is used to filter rows not satisfying search conditions
3. **GROUP BY** + (**COUNT**, **SUM**, etc): rows are grouped using the columns in the group by clause and the aggregation functions are applied
4. **HAVING**: like the **WHERE** clause, but can be applied after aggregation
5. **SELECT**: the targeted list of columns are evaluated and returned
6. **ORDER BY**: the resulting rows are sorted

### `JOIN` types

The various `JOIN`s specify how to deal with different circumstances regarding
the primary and foreign key matchings. 

`INNER JOIN`s discard any entries that do not have a match between the keys
specified in the `ON` clause. For example, in the above query, any customer who had
not visited the site will NOT be in the result set because a match would not
have been found between the customer's `id` and a visit's `customer_id`.

![inner_join](https://cloud.githubusercontent.com/assets/1425450/9778836/9f669cae-572a-11e5-9c96-98b59a930b7d.png)

An `LEFT OUTER JOIN` keeps all the entries in the left table regardless of
whether a match is found in the right table. In that case, the columns
associated with the right table for that entry will simply be `NULL`. A `RIGHT
OUTER JOIN` is the same except it keeps all the entries in the right table
instead of the left one.

![left_join](https://cloud.githubusercontent.com/assets/1425450/9778839/9f69bbd2-572a-11e5-9b13-7b2c2d7a04fb.png)

![right_join](https://cloud.githubusercontent.com/assets/1425450/9779109/19ace62e-572d-11e5-9868-17a9a7e3440f.png)

```sql

SELECT c.id, l.number
FROM customers c
LEFT JOIN licenses l
  ON l.customer_id = c.id
  ```

```
 id |   number
----+------------
  3 | DL19480284
  1 | DL19852984
  2 |
```

A `FULL OUTER JOIN` will keep the rows of both tables no matter what with `NULL`
values for ones that don't have matches.

![full_outer_join](https://cloud.githubusercontent.com/assets/1425450/9778837/9f66b90a-572a-11e5-9d29-2b6c817cc7ec.png)


```
## Keyword Cheatsheet

* Return values
  * SELECT
  * DISTINCT
* Tables and rows
  * FROM
  * JOIN
    * INNER
    * LEFT, RIGHT
    * FULL
* Filtering
  * WHERE
  * =, !=, >, <, >=, <=
  * AND, OR
  * IN, NOT IN
  * LIKE
  * IS NULL, IS NOT NULL
  * LIMIT
  * BETWEEN
* Aggregating
  * GROUP BY
  * COUNT
  * MAX, MIN
  * SUM
  * AVG
  * HAVING
* Ordering
  * ORDER BY
* Aliasing
  * AS

## Additional Resources

* [PostgreSQL Documentation](http://www.postgresql.org/docs/9.2/interactive/index.html)
* [SQL for Data Science](http://bensresearch.com/downloads/SQL.pdf)

**Database theory resources**

* [ACID](http://en.wikipedia.org/wiki/ACID)
* [CAP Theorem](http://en.wikipedia.org/wiki/CAP_theorem)
* [Relational Algebra](http://en.wikipedia.org/wiki/Relational_algebra)
* [Set Theory](http://en.wikipedia.org/wiki/Set_theory)

