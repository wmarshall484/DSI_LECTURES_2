-- List the tables in the database

-- Check details of musician table


-- Check out the first five rows from band
SELECT * FROM band
ORDER BY band_home DESC
LIMIT 5;


-- How many rows total?
SELECT COUNT(*) FROM band;


-- Get min and max born date from musician table
SELECT
    MIN(born) AS min_born_date,
    MAX(born) AS "max_born_date b"
FROM musician;


-- Getting the types of instruments with counts by type of music for the performers
SELECT
    instrument,
    perf_type,
    COUNT(*) AS num_records
FROM performer
GROUP BY instrument, perf_type
ORDER BY perf_type, num_records DESC;

-- Selecting the types of instruments with counts for only 'classical'
SELECT
    instrument,
    COUNT(distinct perf_is)
FROM performer
WHERE perf_type = 'classical'
GROUP BY instrument;

-- What about if you want to condition on the aggregate variable you created
SELECT
    instrument,
    perf_type,
    COUNT(*) AS num_records
FROM performer
WHERE perf_type = 'classical'
GROUP BY instrument, perf_type
HAVING COUNT(*) > 1
ORDER BY perf_type, num_records DESC;


-- How many total musicians are alive/dead?
SELECT
    CASE WHEN died IS NULL THEN 1 ELSE 0 END AS is_alive,
    COUNT(*)
FROM musician
GROUP BY is_alive;



-- What fraction of musicians are alive?
SELECT
    AVG(CASE WHEN died IS NULL THEN 1 ELSE 0 END) as fraction_alive
FROM musician;


#Part 2: Joins

-- Give the names of musicians that organized concerts in the Assembly Rooms after the first of Feb, 1997.
SELECT
    m.m_name,
    c.concert_venue,
    c.con_date
FROM musician m JOIN concert c
ON m.m_no = c.concert_orgniser
WHERE c.concert_venue = 'Assembly Rooms'
AND c.con_date > '1997-02-01';


-- Find all the performers who played guitar or violin, and were born in England
SELECT
    m.m_name,
    p.instrument,
    pl.place_country
FROM musician m
JOIN performer p ON m.m_no = p.perf_is
JOIN place pl ON m.born_in = pl.place_no
WHERE pl.place_country = 'England'
AND p.instrument IN ('guitar', 'violin');

SELECT
*
FROM musician m, performer p
WHERE m.m_no = p.perf_is;


-- Part 3: Complex queries with Subqueries

-- List the names, dates of birth and the instrument played of living musicians who play an instrument which Theo Mengel also plays

SELECT
m.m_name,
m.born,
p.instrument
FROM musician m JOIN performer p
ON m.m_no = p.perf_is
WHERE p.instrument IN (
    SELECT DISTINCT
        p.instrument
    FROM musician m JOIN performer p
    ON m.m_no = p.perf_is
    WHERE m.m_name = 'Theo Mengel'
)
AND m.died IS NULL;


--- Alternatively
WITH t AS(
    SELECT
        m.m_name,
        m.born,
        p.instrument,
        m.died
    FROM musician m JOIN performer p
    ON m.m_no = p.perf_is
)
SELECT
    m_name,
    born,
    instrument
FROM t
WHERE instrument IN (
    SELECT  DISTINCT instrument
    FROM t
    WHERE m_name = 'Theo Mengel'
)
AND died IS NULL;


-- Alternatively
DROP TABLE IF EXISTS t;
CREATE TABLE t AS
SELECT
    m.m_name,
    m.born,
    p.instrument
FROM musician m JOIN performer p
ON m.m_no = p.perf_is;


CREATE TEMP TABLE result AS
SELECT
    m_name,
    born,
    instrument
FROM t
WHERE instrument IN (
    SELECT  DISTINCT instrument
    FROM t
    WHERE m_name = 'Theo Mengel'
);

\copy (SELECT * FROM result) TO 'myresult.csv' WITH DELIMITER ',' CSV HEADER












-- List the name and town of birth of any performer born in the same city as James First.


-- Alternatively

-- Alternatively

-- Download mytab to my machine


-- List the name and the number of players for the band whose number of players is greater than the average number of players in each band.















lkjlkjlkj
