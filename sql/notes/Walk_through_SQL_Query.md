## Conceptual Order of Evaluation of a SQL SELECT Statement

1. `FROM` + `JOIN`: First the product of all tables in the from and join clauses is formed.
1. `WHERE`: The where clause is then evaluated to eliminate rows that do not satisfy the
search condition.
1. `GROUP BY` +  (`COUNT`, `SUM`, etc.): Next, the rows are grouped using the
   columns in the group by clause and the aggregation functions are applied on
   the grouping.
1. `HAVING`: Then, groups that do not satisfy the search condition in the having clause are
eliminated.
1. `SELECT`: Next, the expressions in the select clause target list are evaluated.
1. `DISTINCT`: If the distinct keyword in present in the select clause, duplicate rows are now
eliminated.
1. `ORDER BY`: Finally, the resulting rows are sorted according to the columns specified in the
order by clause.

*Source: http://tinman.cs.gsu.edu/~raj/sql/node22.html*

### Walking through a SQL Query

**What is this SQL query describing?** The name, age, and visit count for every
user in California that visited the site at least 5 times with the most frequent
visitors first.

```sql
SELECT u.name, u.age, COUNT(v.id) AS visit_count
FROM users AS u
INNER JOIN visits AS v
  ON v.user_id = u.id
WHERE u.state = 'CA'
GROUP BY u.id
HAVING COUNT(v.id) > 5
ORDER BY visit_count DESC
```

**What does the schema look like?**

```sql
--- users table
id INTEGER PRIMARY KEY
name VARCHAR(255)
age INTEGER
city VARCHAR(255)
state VARCHAR(2)

--- visits table
id INTEGER PRIMARY KEY
created_at TIMESTAMP
user_id INTEGER REFERENCES users(id)
```

**How is the query being executed?**

#### 1. FROM + JOIN: First the product of all tables in the from and join clauses is formed.
 

```
    FROM users AS u

 id | name | age | city | state 
--------------------------------
 5  | Amy  | 33  | Los..| CA    
 9  | Zed  | 88  | Mia..| FL    
 4  | Ned  | 89  | Mia..| FL    
 3  | John | 46  | San..| CA    
... | 


    INNER JOIN visits AS v
      ON v.user_id = u.id

#   user data on the left side  | visits data on the right side

 name | age | city | state | id | user_id | id | created_at 
------------------------------------------------------------
 Amy  | 33  | Los..| CA    | 5  | 5       | 97 | 2014-02-.. 
 Amy  | 33  | Los..| CA    | 5  | 5       | 79 | 2014-01-.. 
 Zed  | 88  | Mia..| FL    | 9  | 9       | 82 | 2014-01-.. 
 Ned  | 89  | Mia..| FL    | 4  | 4       | 81 | 2014-01-.. 
 John | 46  | San..| CA    | 3  | 3       | 98 | 2014-02-.. 
 John | 46  | San..| CA    | 3  | 3       | 87 | 2014-02-.. 
 John | 46  | San..| CA    | 3  | 3       | 77 | 2014-01-.. 
 John | 46  | San..| CA    | 3  | 3       | 68 | 2013-12-.. 
 John | 46  | San..| CA    | 3  | 3       | 55 | 2013-12-.. 
  ... | 
```

Note how each row contains data from both the users table and the visits table.

This `JOIN` is an `INNER JOIN`, so users who do not appear in the visits table
are not included in the set.  For each pair of user and visit where there is
a match `ON users.id = visits.id`, a row is inserted with the data of both
entries. 

If we had additional `JOIN` clauses, we'd have additional duplication of
information across rows (i.e. every match would get its own row) 
- a veritable bounty of rows. This is the power of relational databases and SQL.
Think in terms of rows.

Note that `users.id` and `visits.user_id` are the same on each row. That's the
effect of the `ON` clause within the `JOIN` clause. 


#### 2. WHERE: The where clause is then evaluated to eliminate rows that do not satisfy the search condition.

```
    WHERE u.state = 'CA'

 name | age | city | state | id | user_id | id | created_at 
------------------------------------------------------------
 Amy  | 33  | Los..| CA    | 5  | 5       | 97 | 2014-02-.. 
 Amy  | 33  | Los..| CA    | 5  | 5       | 79 | 2014-01-.. 
 John | 46  | San..| CA    | 3  | 3       | 98 | 2014-02-.. 
 John | 46  | San..| CA    | 3  | 3       | 87 | 2014-02-.. 
 John | 46  | San..| CA    | 3  | 3       | 77 | 2014-01-.. 
 John | 46  | San..| CA    | 3  | 3       | 68 | 2013-12-.. 
 John | 46  | San..| CA    | 3  | 3       | 55 | 2013-12-.. 
  ... | 
```

Note that Zed and Ned have dropped out of the set because they were in FL, not CA.


#### 3. GROUP BY & Aggregation Functions: Next, the rows are grouped using the columns in the group by clause and the aggregation functions are applied to the groups.

```
    GROUP BY u.id

 name | age | city | state | id | user_id | id | created_at | COUNT(visits.id)
------------------------------------------------------------------------------
 Amy  | 33  | Los..| CA    | 5  | 5       | 97 | 2014-02-.. | 2
 John | 46  | San..| CA    | 3  | 3       | 98 | 2014-02-.. | 5
 Sally| 24  | Fre..| CA    | 7  | 7       | 10 | 2013-08-.. | 7
 Bill | 21  | Bak..| CA    | 9  | 9       | 18 | 2013-10-.. | 8
  ... | 
```

Now each user only has one entry in the set and the aggregation function `COUNT`
was applied and the count inserted into the table. 

Note that visits table data is still in the table but the data is now
nonsensical - consider it simply data for a random visit. Columns will not be
chopped away until the `SELECT` clause.


#### 4. HAVING: Then, groups that do not satisfy the search condition in the having clause are eliminated.

```
    HAVING COUNT(v.id) > 5

 name | age | city | state | id | user_id | id | created_at | COUNT(visits.id)
------------------------------------------------------------------------------
 Sally| 24  | Fre..| CA    | 7  | 7       | 10 | 2013-08-.. | 7
 Bill | 21  | Bak..| CA    | 9  | 9       | 18 | 2013-10-.. | 8
 Nick | 42  | Los..| CA    | 2  | 2       | 34 | 2013-09-.. | 9
  ... | 
```

Amy and John are no longer in the set because they had 2 and 5 visits total,
repsectively.

#### 5. SELECT: Next, the expressions in the select clause target list are evaluated.

```
    SELECT u.name, u.age, COUNT(v.id) AS visit_count

 name | age | visit_count
------------------------------
 Sally| 24  | 7
 Bill | 21  | 8
 Nick | 42  | 9
  ... | 
```

Here the columns are cut down to those specificed in the `SELECT` clause and the
aliasing of the `COUNT` column occurs.
  
#### 6. ORDER BY: Finally, the resulting rows are sorted according to the columns specified in the order by clause.

```
    ORDER BY visit_count DESC

 name | age | visit_count
------------------------------
 Nick | 42  | 9
 Bill | 21  | 8
 Sally| 24  | 7
  ... | 

```

And voila, our result set.

```
 name | age | visit_count
------------------------------
 Nick | 42  | 9
 Bill | 21  | 8
 Sally| 24  | 7
  ... | 

