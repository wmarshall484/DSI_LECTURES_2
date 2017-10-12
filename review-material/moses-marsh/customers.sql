CREATE TABLE customers (
    cust_id integer,
    cust_name character varying,
    current_city character varying,
    hometown character varying);

COPY customers (cust_id, cust_name, current_city, hometown) FROM stdin;
1	Amanda	Atlanta	Raleigh
2	Brittany	Denver	New York
3	Charles	Paris	Raleigh
4	David	San Diego	Los Angeles
5	Elizabeth	Atlanta	London
6	Greg	Denver	Atlanta
7	Maria	Raleigh	New York
8	Sarah	New York	Raleigh
9	Thomas	Atlanta	Raleigh
\.
