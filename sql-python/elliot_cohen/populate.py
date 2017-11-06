import os,sys
import psycopg2
import getpass

### connect to the database
upass = getpass.getpass()
conn = psycopg2.connect(database="golf", user="ender", password=upass, host="localhost", port="5432")
print("connected")

cur = conn.cursor()

## check to see if we created the table and if it exists drop it
cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('golf',))

if cur.fetchone()[0]:
    cur.execute("drop table %s;"%('golf'))
conn.commit()

### create a table to put the golf data in
cur = conn.cursor()
query = '''
        CREATE TABLE golf (
            Date date, 
            Outlook varchar, 
            Temperature integer,
            Humidity integer,
            Windy bool,
            Result varchar
        );
        '''
cur.execute(query)
conn.commit()


### populate that table
cur = conn.cursor()
copy_sql = """
           COPY golf FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """

with open('playgolf.csv', 'r') as f:
    cur.copy_expert(sql=copy_sql, file=f)
    conn.commit()
    cur.close()
conn.commit()


### query the table
cur = conn.cursor()
query = '''
        SELECT *
        FROM golf
        LIMIT 30;
        '''

cur.execute(query)

for r in cur.fetchall():
    print(r)

