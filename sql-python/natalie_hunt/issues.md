If students are running Linux they might not be able to use psycopg2 because of default security settings.

Make sure they ran line
sudo ln -s /var/run/postgresql/.s.PGSQL.5432 /tmp/.s.PGSQL.5432

IF they are still having issues they can follow these steps:

We need to change pg_hba.conf file for psql.

1) type this command to find the file location : psql -t -P format=unaligned -c ‘show hba_file’;
2) change the mode of the file : su chmod 777 pg_hba.conf;
3) edit the file : change md5 to trust;


Stack overflow of the issue to reference:
https://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge
