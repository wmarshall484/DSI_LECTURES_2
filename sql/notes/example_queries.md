## Part 1

1. Basic use of aggregates to get the maximum and minimum

    ```sql
    SELECT MIN(dt), MAX(dt) FROM visits;
    ```

2. Getting the count of visits on each date. Don't forget to group by the date!

    ```sql
    SELECT dt, COUNT(1) FROM visits GROUP BY dt;
    ```

    If you forget the group by, postgres will tell you:

    ```
    readychef=# SELECT dt, COUNT(1) FROM visits;
    ERROR:  column "visits.dt" must appear in the GROUP BY clause
            or be used in an aggregate function
    LINE 1: SELECT dt, COUNT(1) FROM visits;
                   ^
    ```

3. Recall that `HAVING` is used when you want to use `WHERE` for an aggregate.

    ```sql
    SELECT dt, COUNT(1) AS cnt
    FROM visits
    GROUP BY dt
    HAVING COUNT(1) > 1000;
    ```

    ***Incorrect Versions:***

    * Using where instead of having. This doesn't work because the `WHERE` clause is executed *before* aggregate functions.
        
        ```
        readychef=# SELECT dt, COUNT(1) FROM visits
                    WHERE COUNT(1) > 1000 GROUP BY visits;
        ERROR:  aggregate functions are not allowed in WHERE
        LINE 1: ...FROM visits WHERE COUNT(1) > 1000 GROUP ...
                                     ^
        ```

    * Using an alias for the count in the having clause
    
        ```
        readychef=# SELECT dt, COUNT(1) AS cnt FROM visits
                    GROUP BY dt HAVING cnt > 1000;
        ERROR:  column "cnt" does not exist
        LINE 1: ...GROUP BY dt HAVING cnt > 1000...
                                      ^
        ```
    
4. How to create a table. This can be used for testing your queries on smaller tables. It's also useful if you want to save results, or if you have a complicated query and want to make a temporary intermediary table.

    ```sql
    CREATE TABLE mini_visits AS
        SELECT * FROM VISITS LIMIT 10;
    ```

5. A more complicated query. This counts the number of times each Californian user has visited the site.

    *Note:* This isn't for the readychef data. Just pretend we also have name and state in our users table.

    ```sql
    SELECT
        users.userid,
        name,
        COUNT(1) AS cnt
    FROM users
    JOIN visits
    ON
        users.userid=visits.userid AND
        users.state='CA'
    GROUP BY users.userid, users.name;
    ```

    Note that we need `users.name` in the group by even though there aren't two users with the same userid and different names. We always need every column from the select in the group by. This is not the case in sqlite, but is the case in most sql languages, including postgres.

    You could get the same results by using the `WHERE` clause, but this would be less efficient since it would create the join of the two tables and then filter out the california rows. Here's what this would look like:

    ```sql
    SELECT
        users.userid,
        name,
        COUNT(1) AS cnt
    FROM users
    JOIN visits
    ON users.userid=visits.userid
    WHERE users.state='CA'
    GROUP BY users.userid, users.name;
    ```

## Part 2: Subqueries

1. I want to get all the users who registered on the first day.

    * We can hardcode in the first day if we know it:
    
        ```sql
        SELECT * FROM users WHERE dt='2013-01-01';
        ```

    * We might want to do it like this, but it's wrong!
    
        ```sql
        SELECT * FROM users HAVING dt=MIN(dt);
        ```

        Here you're using the same column twice. You're trying to do an aggregate over it and select all of the columns. This confuses poor sql.

    * You need to use a subquery:
    
        ```sql
        SELECT * FROM users
        WHERE dt=(SELECT MIN(dt) FROM users);
        ```

        Note that sql is clever and when the result of your subquery is a single value it can use it in comparisons. This would break if the result of the subquery was not a single value.

2. Get the ratio of the number of visits to the number of buys on the site.

    * First, here's how we get the number of visits:
    
        ```sql
        SELECT COUNT(1) FROM visits;
        ```

    * Here's how we get the number of buys:
    
        ```sql
        SELECT COUNT(1) FROM events WHERE event='bought';
        ```

    * We can combine them like this:
    
        ```sql
        SELECT
            COUNT(1) / (SELECT COUNT(1) FROM events WHERE event='bought')
        FROM visits;
        ```

    * The above gives the value as an integer. If we want all the decimals, just like in python, we need to cast one of the two to a real number (this is like a python float).
    
        ```sql
        SELECT
            CAST (COUNT(1) AS REAL) /
            (SELECT COUNT(1) FROM events WHERE event='bought')
        FROM visits;
        ```

3. Let's say we want to find all the users who registered on days where we got a lot of registrations. We define a lot of registrations as at least 20.

    * First, this query will get all the dates where we had at least 20 registrations.

        ```sql
        SELECT dt
        FROM users
        GROUP BY dt
        HAVING COUNT(1) > 20;
        ```

    * We can use this as a subquery to get our desired result.

        ```sql
        SELECT userid FROM users
        WHERE dt IN (SELECT dt FROM users
                     GROUP BY dt
                     HAVING COUNT(1) > 20);
        ```

    * We can also do this with a join.

        ```sql
        SELECT userid
        FROM users u
        JOIN (SELECT dt FROM users
              GROUP BY dt
              HAVING COUNT(1) > 20) t
        ON u.dt=t.dt;
        ```

        Note that it's required to alias the subquery. This means giving it a name (here `t`).

        I also aliased the `users` table to make it easier to reference it.

        There is an optional `AS` (I could've written `AS u`).

    * If you are finding your subqueries too cumbersome, you could create a table with the result of the subquery.
    
        ```sql
        CREATE TABLE dates AS
        SELECT dt FROM users
              GROUP BY dt
              HAVING COUNT(1) > 20;

        SELECT userid FROM users AS u
        JOIN dates AS t
        ON u.dt=t.dt;
        ```

    * Postgres also has what's called a *with clause*. This is used to create a temporary table that will only be used in this query.

        ```sql
        WITH t AS
            (SELECT dt FROM users
             GROUP BY dt
             HAVING COUNT(1) > 20),
            anothertable AS
            (SELECT ...)
        SELECT userid FROM users AS u
        JOIN t
        ON u.dt=t.dt;
        ```
