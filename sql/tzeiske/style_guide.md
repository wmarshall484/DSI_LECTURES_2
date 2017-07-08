## SQL Style Guide

There isn't total concensus about how to do style in SQL, but here's some general guidelines.

1. Use all caps for SQL words.

    ```sql
    SELECT mycolumn FROM mytable WHERE anothercol IS NULL;
    ```

1. Like with all programming languages, keep lines under 80 characters.

1. If a query is really short, you can put it on one line:

    ```sql
    SELECT * FROM mytable;
    ```

1. If your query is running long, or is just a little unreadable, here are ways of break it down:

    * Break your query so that each of `SELECT`, `FROM`, `JOIN`, `ON`, `WHERE`, `GROUP BY`, `ORDER BY` are each on their own line.
    
        ```sql
        SELECT name
        FROM mytable
        WHERE price > 100
        ORDER BY name;
        ```

    * Put each column for the `SELECT` clause on its own line, *indented*:
        
        ```sql
        SELECT
            name,
            SUM(price) as total_price,
            COUNT(1)
        FROM mytable
        GROUP BY name;
        ```

    * Put each clause of the `ON` or `WHERE` clause on its own line, *indented*:
    
        ```sql
        SELECT
            a.name,
            a.price
        FROM mytable a
        JOIN anothertable b
        ON
            a.item_id=b.item_id AND
            a.price > 100 AND
            b.dept='shoes';
        ```

1. Nested queries can get tricky. The main idea is to keep everything in the nested query at the same indentation level. Here's an example:

    * Although you might be able to do the nested select all on one line.
    
        ```sql
        SELECT *
        FROM products
        WHERE price=(SELECT MAX(price) FROM products WHERE dept='shoes' AND date>'2014-10-01')
        ORDER BY name;
        ```

    * Here's what it looks like if you use multiple lines.
    
        ```sql
        SELECT *
        FROM products
        WHERE price=(SELECT MAX(price)
                     FROM products
                     WHERE
                         dept='shoes' AND
                         date>'2014-10-01')
        ORDER BY name;
        ```
        Much easier to follow with respect to how price is calculated for the main select clause.
        
        <br>
        The main rule of thumb for nested selects is to keep everything lined up with the `SELECT` keyword. This makes it clear what is part of the nested select and when it ends.0

