# Advanced SQL

To be a SQL wizard, it's important to become very comfortable with SQL joins, nested `SELECTS` and `GROUP BY`s.

Let's say for an online sales company you have the following tables:


### Inner Join

![inner_join](https://cloud.githubusercontent.com/assets/1425450/9778836/9f669cae-572a-11e5-9c96-98b59a930b7d.png)

If you want to get all the purchases but you want to include the customer name and the product name, you would use a stardard join (this is also called an *inner join*):

```sql
SELECT customers.name AS cust_name, products.name AS prod_name, date, quantity
FROM purchases purchases
JOIN products 
    ON products.id=purchases.product_id
JOIN customers 
    ON customers.id=purchases.customer_id;
```

### Outer Join

Let's say there's a mistake in our database and some products are in the purchase table but not in the products table. With the above inner join query, they would just end up being excluded. An inner join only includes entries which are in both tables.

_Table with mistakes_
```sql
CREATE TABLE purchases_no_key (
  	id INTEGER PRIMARY KEY
,   customer_id INTEGER
,   product_id INTEGER
,   date TIMESTAMP
,   quantity INTEGER);

INSERT INTO purchases_no_key ( id, customer_id, product_id, date, quantity) VALUES
    (1, 1, 2, '2015-07-30', 2)
,   (2, 2, 4, '2015-06-20', 3)
,   (3, 1, 3, '2015-04-09', 1);
```

We can ensure all records are included in our result by using an *outer join*.

```sql
SELECT customers.name AS cust_name, products.name AS prod_name, date, quantity
FROM purchases_no_key purchases
LEFT OUTER JOIN products 
    ON products.id=purchases.product_id
JOIN customers 
    ON customers.id=purchases.customer_id;
```

![left_join](https://cloud.githubusercontent.com/assets/1425450/9778839/9f69bbd2-572a-11e5-9b13-7b2c2d7a04fb.png)

The LEFT means that everything from the first table will be included even if there isn't a matching entry in the second table. This will include those missing products, but their names will be `NULL`.

We'll want to isolate those mistakes, we can use the same query as above, but only returns rows where
something in the left table isn't in the joined table.

```sql
SELECT purchases.*
FROM purchases_no_key purchases
LEFT OUTER JOIN products 
    ON products.id=purchases.product_id
JOIN customers 
    ON customers.id=purchases.customer_id
WHERE products.name IS NULL;
```

![left_join_null](https://cloud.githubusercontent.com/assets/1425450/9779111/1b8b0df4-572d-11e5-922d-55d7b2d36dd2.png)

Even better, we can create the Purchases table with a FOREIGN KEY constraint to ensure that all customer and product ids are in their respective tables.  If you try the below, you will receive an error:

```sql
INSERT INTO purchases ( id, customer_id, product_id, date, quantity) VALUES
   (4, 2, 4, '2015-06-20', 3);

ERROR:  insert or update on table "purchases" violates foreign key constraint "purchases_product_id_fkey"
DETAIL:  Key (product_id)=(4) is not present in table "products".
```

### Except


You can also use `EXCEPT` (MINUS in some versions of SQL):

```sql
SELECT purchases.product_id
FROM purchases_no_key purchases
EXCEPT
SELECT products.id
FROM products;
```

### Getting the maximum

For this we will assume that there's no missing data in our tables.

There is a MAX function which gives you the maximum value, but often you want the entry associated with it. Let's say you want to find the most expensive item. The way to do this is to find the maximum price and then find all the elements whose price is that value.

This requires you to do a nested SELECT statement.

```sql
SELECT *
FROM products
WHERE price=(
            SELECT MAX(price) 
            FROM products
            ); 
```

Or maybe you want the product which has generated the most profit. Sometimes it's helpful to, instead of having multiple nested selects, creating a temporary table as an intermediary step.

```sql
CREATE TEMPORARY TABLE profits AS
SELECT products.name, products.id, SUM(purchases.quantity * products.price) AS profit
FROM products
JOIN purchases
    ON products.id=purchases.product_id
GROUP BY products.name, products.id;

SELECT name, id
FROM profits
WHERE profit=(SELECT MAX(profit) FROM profits);
```

You can also do this using a WITH clause:

```sql
WITH p AS (
SELECT products.name, products.id, SUM(purchases.quantity * products.price) AS profit
FROM products
JOIN  purchases
    ON products.id=purchases.product_id
GROUP BY products.name, products.id)

SELECT name, id
FROM p
WHERE profit=(SELECT MAX(profit) FROM p);
```

### Windowing Functions

If all of this made sense so far and you are ready for more, checkout [windowing functions](http://www.postgresql.org/docs/9.1/static/tutorial-window.html)

We can get the same result as above using the RANK window function.

```sql
WITH p AS (
SELECT products.name, products.id, SUM(purchases.quantity * products.price) AS profit
FROM products
JOIN  purchases
    ON products.id=purchases.product_id
GROUP BY products.name, products.id)

SELECT name, id, profit
FROM (  SELECT name, id, profit, rank() OVER (ORDER BY profit DESC)
        FROM p) ranked_profit
    WHERE rank=1
```
