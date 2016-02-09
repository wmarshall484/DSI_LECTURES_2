# Example using musicians database on SQLZOO: http://sqlzoo.net/wiki/Musicians
## Tables used in musicians database

```sql
\d

               List of relations
 Schema |     Name     | Type  |     Owner      
--------+--------------+-------+----------------
 public | band         | table | clayton.schupp
 public | composer     | table | clayton.schupp
 public | composition  | table | clayton.schupp
 public | concert      | table | clayton.schupp
 public | has_composed | table | clayton.schupp
 public | musician     | table | clayton.schupp
 public | performance  | table | clayton.schupp
 public | performer    | table | clayton.schupp
 public | place        | table | clayton.schupp
 public | plays_in     | table | clayton.schupp
```

```sql
SELECT *
FROM band
LIMIT 5;

 band_no |   band_name    | band_home | band_type |   b_date   | band_contact 
---------+----------------+-----------+-----------+------------+--------------
       1 | ROP            |         5 | classical | 2001-01-30 |           11
       2 | AASO           |         6 | classical |            |           10
       3 | The J Bs       |         8 | jazz      |            |           12
       4 | BBSO           |         9 | classical |            |           21
       5 | The left Overs |         2 | jazz      |            |            8
```

```sql
SELECT *
FROM composer
LIMIT 5;

 comp_no | comp_is | comp_type 
---------+---------+-----------
       1 |       1 | jazz
       2 |       3 | classical
       3 |       5 | jazz
       4 |       7 | classical
       5 |       9 | jazz
```

```sql
SELECT *
FROM composition
LIMIT 5;

 c_no | comp_date  |    c_title     | c_in 
------+------------+----------------+------
    1 | 1975-06-17 | Opus 1         |    1
    2 | 1976-07-21 | Here Goes      |    2
    3 | 1981-12-14 | Valiant Knight |    3
    4 | 1982-01-12 | Little Piece   |    4
    5 | 1985-03-13 | Simple Song    |    5
```

```sql
SELECT *
FROM concert
LIMIT 5;

 concert_no |  concert_venue   | concert_in |  con_date  | concert_orgniser 
------------+------------------+------------+------------+------------------
          1 | Bridgewater Hall |          1 | 1995-06-01 |               21
          2 | Bridgewater Hall |          1 | 1996-08-05 |                3
          3 | Usher Hall       |          2 | 1995-03-06 |                3
          4 | Assembly Rooms   |          2 | 1997-09-20 |               21
          5 | Festspiel Haus   |          3 | 1995-02-21 |                8
```

```sql
SELECT *
FROM has_composed
LIMIT 5;

 cmpr_no | cmpn_no 
---------+---------
       1 |       1
       1 |       8
       2 |      11
       3 |       2
       3 |      13
```

```sql
SELECT *
FROM musician
LIMIT 5;

 m_no |      m_name      |    born    |    died    | born_in | living_in 
------+------------------+------------+------------+---------+-----------
    1 | Fred Bloggs      | 2048-02-01 |            |       1 |         2
    2 | John Smith       | 2050-03-03 |            |       3 |         4
    3 | Helen Smyth      | 2048-08-08 |            |       4 |         5
    4 | Harriet Smithson | 2009-09-05 | 1980-09-20 |       5 |         6
    5 | James First      | 2065-10-06 |            |       7 |         7
```

```sql
SELECT *
FROM performance
LIMIT 5;

 pfrmnc_no | gave | performed | conducted_by | performed_in 
-----------+------+-----------+--------------+--------------
         1 |    1 |         1 |           21 |            1
         2 |    1 |         3 |           21 |            1
         3 |    1 |         5 |           21 |            1
         4 |    1 |         2 |            1 |            2
         5 |    2 |         4 |           21 |            2
```

```sql
SELECT *
FROM performer
LIMIT 5;

 perf_no | perf_is | instrument | perf_type 
---------+---------+------------+-----------
       1 |       2 | violin     | classical
       2 |       4 | viola      | classical
       3 |       6 | banjo      | jazz
       4 |       8 | violin     | classical
       5 |      12 | guitar     | jazz
```

```sql
SELECT *
FROM place
LIMIT 5;

 place_no | place_town | place_country 
----------+------------+---------------
        1 | Manchester | England
        2 | Edinburgh  | Scotland
        3 | Salzburg   | Austria
        4 | New York   | USA
        5 | Birmingham | England
```

```sql
SELECT *
FROM plays_in
LIMIT 5;

 player | band_id 
--------+---------
      1 |       1
      1 |       7
      3 |       1
      4 |       1
      4 |       7
```
## Part 1: Basic Queries

1. Basic use of aggregates to get the maximum and minimum date of birth

  ```sql
  SELECT MIN(born), MAX(born) 
  FROM musician;
  ```
  
2. Getting the types of instruments with counts by type of music for the performers

  ```sql
  SELECT perf_type, instrument, COUNT(*) AS cnt
  FROM performer
  GROUP BY perf_type, instrument
  ORDER BY perf_type, instrument;
  ```
  
3. Selecting the types of instruments with counts for only 'classical'

  ```sql
  SELECT instrument, COUNT(*) AS cnt
  FROM performer
  WHERE perf_type='classical'
  GROUP BY instrument;
  ```
  
4. What about if you want to condition on the aggregate variable you created

  ```sql
  SELECT perf_type, instrument, COUNT(*) AS cnt
  FROM performer
  GROUP BY perf_type, instrument
  HAVING COUNT(*) >= 2
  ORDER BY perf_type;
  ```

#Part 2: Joins

1. Give the organiser's name of the concert in the Assembly Rooms after the first of Feb, 1997.

  ```sql
  SELECT m.m_name
  FROM concert c
  JOIN musician m
  ON c.concert_orgniser=m.m_no
  WHERE concert_venue = 'Assembly Rooms' AND con_date > '02/01/97';
```

2. Find all the performers who played guitar or violin, were born in England, and are still alive.

  ```sql
  SELECT m_name
  FROM musician m
  JOIN place p
  ON m.born_in=p.place_no
  WHERE p.place_country='England' AND m.died IS NULL;
  ```

3. List the names of musicians who have conducted concerts in USA together with the towns and dates of these concerts.

  ```sql
  SELECT m.m_name, pl.place_town, c.con_date
  FROM musician m
  LEFT JOIN performance p
  ON m.m_no=p.conducted_by
  LEFT JOIN place pl 
  ON p.performed_in=pl.place_no
  LEFT JOIN concert c
  ON c.concert_in=pl.place_no
  WHERE pl.place_country='USA';
  ```

4. How many concerts have featured at least one composition by Andy Jones? List concert date, venue and the composition's title.

  ```sql
  SELECT *
  FROM musician m
  LEFT JOIN performance p
  ON m.m_no=p.conducted_by
  LEFT JOIN place pl 
  ON p.performed_in=pl.place_no
  LEFT JOIN concert c
  ON c.concert_in=pl.place_no
  WHERE pl.place_country='USA';
  ```

#Part 3: Complex queries with Subqueries

1. List the name and town of birth of any performer born in the same city as James First.

  ```sql
  SELECT m.m_name, p.place_town 
  FROM musician m
  JOIN place p
  ON m.born_in=p.place_no
  WHERE m.born_in=
                 (SELECT born_in
                  FROM musician
                  WHERE m_name='James First')
  ;
  ```

#Part 4: Miscellaneous

1. How to create a table. This can be used for testing your queries on smaller tables. It's also useful if you want to save results, or if you have a complicated query and want to make a temporary intermediary table.

  ```sql
  CREATE TABLE dead_brits AS
      SELECT *
      FROM musician m
      JOIN place p
      ON m.born_in=p.place_no
      WHERE p.place_country='England' AND m.died IS NOT NULL;
  
  SELECT * 
  FROM dead_brits;
  ```

2. Postgres has what's called a **with** clause that is used to create a temporary table that will only be used for the query.
  ```sql
  WITH t AS
     (SELECT *
      FROM musician m
      JOIN place p
      ON m.born_in=p.place_no
      WHERE p.place_country='England' AND m.died IS NOT NULL)
  SELECT * 
  FROM t;
  ```


