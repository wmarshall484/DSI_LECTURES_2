# Databases and SQL

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

## The RDBMS Data Model

Relational databases have a **schema** that defines the structure of the data.
Each database is composed of a number of user-defined **tables**, each with
**columns** and **rows**. Each column is of a certain **data type** such as
integer, string, or date. Each row is an entry in the table with data for each
column of that table.

Here's an example of a database table creation specifying a `users` table with various
fields and their data types:

```sql
CREATE TABLE users {
  id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  age INTEGER,
  city VARCHAR(255),
  state VARCHAR(2)
}
```

The data types available to you vary from system to system. These above are from
PostgreSQL. `VARCHAR` is a string data type.

A **primary key** is a column in a table that uniquely identifies that entry. No
two rows in the same table can share a value for a column specified as primary
key. The primary key column is most often `id`.

Here's an example of what this users table looks like:

```
 id | name | age | city | state 
--------------------------------
 5  | Amy  | 33  | Los..| CA    
 9  | Zed  | 88  | Mia..| FL    
 4  | Ned  | 89  | Mia..| FL    
 3  | John | 46  | San..| CA    
... | 
```

## Modeling Relations in RDBMS

Part of the power of relational databases are their ability to model relations
in data. The way they do so is through the use of **foreign keys**.
A foreign key is a column that references some other entry in the database.
That foreign entry could be in the same table or in some other table. Foreign
keys are how relations are modeled in relational databases.

For example, let's say there is another table that contains data for each visit
to our website. Each time a user visits the site, a row is created and inserted
into the `visits` table. We'd like to maintain some data that indicates which
visit is associated with which user (so that we could later, for example, find
the users who visited our site the most). Each visit then will have a `user_id`
that can connect it to a user in the `users` table.

Here's the definition of the `visits` table:

```sql
CREATE TABLE visits {
  id INTEGER PRIMARY KEY,
  created_at TIMESTAMP,
  user_id INTEGER REFERENCES users(id)
}
```

Here we specify not only that the `visits` table has a column called `user_id`,
but that the column references the `id` column in the `users` table. PostgreSQL
will treat this as a constraint and ensure that new visits have a `user_id`
value that references an actual user in the database.

### Types of Relationships

#### One-to-one

For a one-to-one relationship, place the foreign key on either side of the
relationship. 

**Example: User and Subscription**

```
---subscriptions
user_id INTEGER
```

To find the user for a particular subscription:

```sql
SELECT *
FROM users
WHERE id=?
LIMIT 1 
```

To find the subscription for a user:

```sql
SELECT *
FROM subscriptions
WHERE user_id=?
LIMIT 1
```

#### One-to-many and many-to-one

For a one-to-many/many-to-one relationship (they are inverses of each other),
place the foreign key on the many side of the relationship.

**Example: User and Posts**

```
---posts
user_id INTEGER REFERENCES users(id)
```

To find the posts for a user:

```sql
SELECT *
FROM posts
WHERE user_id=?
```

To find the user for a post:

```sql
SELECT *
FROM users
WHERE id=?
LIMIT 1
```

#### Many-to-many

For a many-to-many relationship, create a table that contains two foreign keys,
one to each side of the relationship. This intermediate table is often referred
to as a **JOIN table**.

**Example 1: Posts and Tags**

```
---post_tags
post_id INTEGER REFERENCES posts(id)
tag_id INTEGER REFERENCES tags(id)
```

To find the tags for a post:

```sql
SELECT tags.*
FROM tags
JOIN post_tags
  ON post_tags.tag_id = tags.id
WHERE post_tags.post_id=?
```

To find the posts for a tag:

```sql
SELECT posts.*
FROM posts
JOIN post_tags
  ON post_tags.post_id = posts.id
WHERE post_tags.tag_id=?
```

**Example 2: Friendships**

Let's assume friendships are one-sided so that if Alice is Bob's friend, and Bob
is Alice's friend, then there are two entries in the friendships table for the
double-sided friendship.

```
---friendships
in_friend_id INTEGER REFERENCES users(id)
out_friend_id INTEGER REFERENCES users(id)
```

To find all of a user's friends:

```sql
SELECT users.*
FROM users
JOIN friendships
  ON friendships.out_friend_id=users.id
WHERE friendships.in_friend_id = ?
```

To find all the users who have friended a user:

```sql
SELECT users.*
FROM users
JOIN friendships
  ON friendships.in_friend_id = users.id
WHERE friendships.out_friend_id = ?
```

## Schema Normalization

When designing a database schema (the tables and columns the database will
contain), we aim to minimize redundancy. This most importantly comes into play
with relations between data. As you saw above, when you want to relate data to
each other, use a simple foreign key - that's the smallest piece of information
that you can keep about another entry.

As an example, each post has an author, which is an entry in the `users` table.
In a fully normalized schema, the post entry would have a `user_id` which would
relate the post to a user. A denormalized way of doing this would be to have a
column in the `posts` table called `author_name`, which would duplicate the
`name` column in the `users` table. 

Normalization is largely about reducing redundancy. The cost is that some
queries will take longer to run because you will have to look up additional
information in other tables. The benefit is simplicity and a system that is
easier to understand and use. Always start with a fully normalized schema and
then when performance becomes an issue, you can consider selectively
denormalizing.

You can learn more about database normalization from [Wikipedia][wiki-normal].

[wiki-normal]: http://en.wikipedia.org/wiki/Database_normalization

## SQL

Structed Query Language (SQL) is the language used to query relational
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
FROM users
```

This query returns the name and age for every user in the `users` table.

```sql
SELECT name, age
FROM users
WHERE state = 'CA'
```

This query returns the name and age for every user in the `users` table who
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
SELECT users.name, visits.created_at
FROM visits
INNER JOIN users
  ON users.id = visits.user_id
```

Each visit has a `user_id` that corresponds to the `id` column in the users
table. In SQL, you specify the correspondence in the `ON` segment of the `JOIN`
clause. 

**For each match between `users.id` and `visits.user_id` that is found, a row is
inserted into the result set.** That means that if a user has visited the site
multiple times, their information will be in the result set multiple times.

For example, the result may look like this:

```
users.name | visits.created_at
------------------------------
Bill       |  2012-10-11...
Bill       |  2012-10-03...
Bill       |  2012-09-07...
Amy        |  2012-10-01...
Amy        |  2012-10-02...
Sally      |  2012-01-22...
```

Note how each user shows up multiple times for in the result set. This make
sense given that each user visted the site multiple times. You'll see later in
this document a slightly more detailed look at how the RDBMS constructs a result
set, including how it processes `JOIN`s.

### `JOIN` types

The various `JOIN`s specify how to deal with different circumstances regarding
the primary and foreign key matchings. 

`INNER JOIN`s discard any entries that do not have a match between the keys
specified in the `ON` clause. For example, in the above query, any user who had
not visited the site will NOT be in the result set because a match would not
have been found between the user's `id` and a visit's `user_id`.

An `LEFT OUTER JOIN` keeps all the entries in the left table regardless of
whether a match is found in the right table. In that case, the columns
associated with the right table for that entry will simply be `NULL`. A `RIGHT
OUTER JOIN` is the same except it keeps all the entries in the right table
instead of the left one.

A `FULL OUTER JOIN` will keep the rows of both tables no matter what with `NULL`
values for ones that don't have matches.


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

## Addtional Resources

* [PostgreSQL Documentation](http://www.postgresql.org/docs/9.2/interactive/index.html)
* [SQL for Data Science](http://bensresearch.com/downloads/SQL.pdf)

**Database theory resources**

* [ACID](http://en.wikipedia.org/wiki/ACID)
* [CAP Theorem](http://en.wikipedia.org/wiki/CAP_theorem)
* [Relational Algebra](http://en.wikipedia.org/wiki/Relational_algebra)
* [Set Theory](http://en.wikipedia.org/wiki/Set_theory)

