# Postgresql on Docker

First, identify the directory on your machine that contains data that you want to import into a database. Let's call this directory `/PATH/TO/DATA`.

Next, run a containerized version of `postgresql`:

    $ docker run -d --name postgres -v /PATH/TO/DATA:/home/data -p 5432:5432 postgres

* `d` runs the container in the background.
* `--name postgres` gives the container a name
* `-v /PATH/TO/DATA:/home/data` makes `/PATH/TO/DATA` accessible as `/home/data` in the container.
* `-p 5432:5432` ensures that the container's postgres server port is accessible outside the container.

At this point you may be interested in loading data into the postgresql server. Open up a shell on the instance:

    $ docker exec -it postgres bash

This should give you a bash prompt for the container. Like:

    root@a4831cfc1629:/#

If you `cd /home/data` you'll see all the files in your machine's `/PATH/TO/DATA`.

You could open a `psql` client:

    root@a4831cfc1629:/# psql -U postgres

Which will stick you in a SQL prompt.

    postgres=# 

At this point you could use postgreSQL commands, like create table:

    postgres=# CREATE TABLE foo (bar text);
    CREATE TABLE
    postgres=# INSERT INTO foo (bar) VALUES ('baz');
    INSERT 0 1
    postgres=# SELECT * FROM foo;
    postgres=# SELECT * FROM foo;
     bar 
    -----
     baz
    (1 row)

Or load a file from CSV:

    postgres=# COPY your_table FROM '/home/data/your_table.csv' DELIMITER ',';

Note at this point we're in a client, inside a container, inside your computer.

To exit and delete the container:

    =# \q
    /# exit
    $ docker rm --force postgres

This will _not_ delete `/PATH/TO/DATA` or its contents.