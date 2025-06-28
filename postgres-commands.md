/ [Home](index.md)

# Postgres Commands

**Note:** tbw



How to connect localhost DB?
```
psql -U postgres -h localhost -p 5432 <db_name>
```


How to connect to remote DB from command?
```
psql -U postgres -h <remote_db_end_point> -p 5432 <remote_db_name>
```



Connect to DB
```
psql -U postgres
```


Show databases
```
\l
```



show size of the database
```
\l+
```



Show roles
```
\du
```



switch database
```
\c db_name
```



show schema table
```
\dt+
```



Get current database:
```
select current_database();

or 

\c

or

SELECT * FROM current_catalog;
```





List tables in the database
```
\dt
```



show table with size
```
\dt+
```



show specific schema tables
```
\dt schema_name.* 
```


specific tble
```
\d table_name
```


Get table details from specific schema:
```
select * from  pg_catalog.pg_tables where schemaname != 'flcity' and schemaname != 'pg_catalog';
```



quit database
```
\q
```


```
Docker:
docker run --name pg11 -e POSTGRES_PASSWORD=kaipulla -d -p 5432:5432 postgres
docker exec -it pg11 bash

psql -h 0.0.0.0 -p 5432 -U postgres

psql -h 127.0.0.1 -p 5432 -U postgres

psql -h 0.0.0.0 -p 5432 -U raja

psql -h 0.0.0.0 -p 5432 -U raja -d rjdbtest


docker exec -it kwikee_postgres_1 psql -U kwikee

psql -h 165.225.36.90 -p 5432 -U postgres
psql -h 120.0.0.1 -p 5432 -U postgres
psql -h localhost -p 5432 -U postgres

172.17.0.3
psql -h 172.17.0.3 -p 5432 -U postgres

psql postgresql://postgres:root@localhost:5432/postgres


# how to install postgres client?
brew install libpq  
	https://www.compose.com/articles/postgresql-tips-installing-the-postgresql-client/

#
show databases
\l

#
show size of the database
\l+

#
show roles / users
\du

#
Show current user
select current_user();
    https://www.dark-hamster.com/database/show-current-user-postgresql/


#
create new user
CREATE USER raja WITH PASSWORD 'kaipulla';

#
psql -U raja -d rjdbtest
    https://stackoverflow.com/questions/56146149/how-to-login-to-postgresql-with-different-username-than-postgres-and-how-to-en

#
grant permission
grant all privileges on database rjdbtest to raja;

grant all privileges on database rjdbtest to raja;

# to do
GRANT SELECT ON DATABASE postgres TO raja;



#
switch database
\c db_name

#
list tables in the database
\dt

#
show schema table
\dt+

#
show specific schema tables
\dt schema_name.* 


#
specific tble
\d table_name

#
select 
  * 
from 
  pg_catalog.pg_tables 
where 
  schemaname != 'my_schema_name' 
  and schemaname != 'pg_catalog';

#
Get current database
SELECT current_database();

or
\c

or

SELECT * FROM current_catalog;

#
Show all user defined functions
\df

#
quit database
\q

# clear screen
\! clear



#
Create DB
CREATE DATABASE rjdbtest;
GRANT CONNECT ON DATABASE rjdbtest TO raja;

CREATE DATABASE rj;
	https://www.digitalocean.com/docs/databases/postgresql/how-to/modify-user-privileges/

CREATE TABLE CITY (
   ID serial PRIMARY KEY,
   NAME VARCHAR (50) UNIQUE NOT NULL,
   STATE VARCHAR (50) NOT NULL,
   COUNTRY VARCHAR (100) NOT NULL,
   CREATED_AT TIMESTAMP NOT NULL
);

INSERT INTO CITY (NAME, STATE, COUNTRY, CREATED_AT) VALUES ('Toronto', 'Ontario', 'Canada', NOW());
INSERT INTO CITY (NAME, STATE, COUNTRY, CREATED_AT) VALUES ('Montreal', 'Quebec', 'Canada', NOW());

DELETE FROM CITY;
DROP TABLE CITY;

CREATE TABLE CITY (
   ID serial PRIMARY KEY,
   NAME VARCHAR (50) UNIQUE NOT NULL,
   STATE VARCHAR (50) NOT NULL,
   COUNTRY VARCHAR (100) NOT NULL
);

INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Toronto', 'Ontario', 'Canada');
INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Montreal', 'Quebec', 'Canada');
INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Chennai', 'Tamilnadu', 'India');
INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Madurai', 'Tamilnadu', 'India');
INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Quebec City', 'Quebec', 'Canada');

INSERT INTO CITY (ID, NAME, STATE, COUNTRY) VALUES (90, 'Chidambaram', 'Tamilnadau', 'India');
INSERT INTO CITY (ID, NAME, STATE, COUNTRY) VALUES (4, 'Cumbum', 'Tamilnadau', 'India');



CREATE TABLE CITY (
   CITYID serial PRIMARY KEY,
   CNAME VARCHAR (50) UNIQUE NOT NULL,
   STATE VARCHAR (50) NOT NULL
);

INSERT INTO CITY (CNAME, STATE) VALUES ('Toronto', 'Ontario');
INSERT INTO CITY (CNAME, STATE) VALUES ('Montreal', 'Quebec');
INSERT INTO CITY (CNAME, STATE) VALUES ('Chennai', 'Tamilnadu');
INSERT INTO CITY (CNAME, STATE) VALUES ('Madurai', 'Tamilnadu');
INSERT INTO CITY (CNAME, STATE) VALUES ('Waterloo', 'Ontario');

SELECT * FROM CITY;

DELETE FROM CITY;

DROP TABLE CITY;

SELECT * FROM CITY LIMIT 2;
SELECT * FROM CITY LIMIT 2 OFFSET 2;
    https://www.postgresqltutorial.com/postgresql-limit/

SELECT * FROM CITY 
ORDER BY CITYID DESC
LIMIT 2;

SELECT * FROM CITY WHERE CITYID = 3;

UPDATE CITY SET CNAME = 'Greater Chennai' WHERE CITYID = 3;

UPDATE CITY SET CNAME = 'Greater Chennai', STATE = 'Thamizhnadu' WHERE CITYID = 3;


SELECT * FROM CITY WHERE STATE LIKE '%du%';
SELECT * FROM CITY WHERE STATE LIKE '%n%';

SELECT * FROM CITY WHERE STATE LIKE '%na%';


SELECT * FROM CITY WHERE STATE NOT LIKE '%n%';

DELETE FROM CITY WHERE CITYID = 3;

SELECT count(*) FROM CITY;

SELECT count(CITYID) FROM CITY;

WITH rows AS (
    DELETE FROM CITY
    WHERE CITYID = 3
    RETURNING 1
)
SELECT count(*) FROM rows;

# Delete all contains the letter n and return how many items deleted
WITH rows AS (
    DELETE FROM CITY
    WHERE STATE LIKE '%n%'
    RETURNING 1
)
SELECT count(*) FROM rows;

CRUD: 
Create
    INSERT
Read
    SELET
Update
    UPDATE
Delete
    DELETE

More commands:
https://stackoverflow.com/questions/769683/show-tables-in-postgresql

if you face pycopg2 issue in alpine:
https://github.com/uroybd/python3-psycopg2-alpine/issues/2

Sample App:
https://github.com/teamkact/flask-rest-city-crud-postgresql/

Flask - AWS RDS - Postgres - CRUD
flask-aws-rds-postgres-crud-sqlite
https://github.com/rajasgs/flask-aws-rds-postgres-crud-sqlite.git

----------------------------------------------------------------------------------------------------

#
TORONNODB and TOURIST:
CREATE DATABASE TORONNODB;

\c toronnodb

DELETE FROM TOURIST;
DROP TABLE TOURIST;

CREATE TABLE TOURIST (
   ID serial PRIMARY KEY,
   NAME VARCHAR (50) UNIQUE NOT NULL,
   AGE INTEGER NOT NULL
);

INSERT INTO TOURIST (NAME, AGE) VALUES ('Kevin', 23);
INSERT INTO TOURIST (NAME, AGE) VALUES ('Jina', 19);

SELECT * FROM TOURIST WHERE age > 18;


PG Function:
create function get_city_count()
returns int
language plpgsql
as
$$
declare
   city_count integer;
begin
   select count(*) 
   into city_count
   from city;
   
   return city_count;
end;
$$;

select * from get_city_count();

	https://www.postgresqltutorial.com/postgresql-create-function/
	
	
----------------------------------------------------------------------------------------------------	
Json blob:

select
cityid,
jsonb_build_object(
    'cxh', jsonb_build_object(
        'environment', jsonb_build_object(
            'name', 'dev'
        ),
        'city_obj', jsonb_agg(
            jsonb_build_object(
                'city_name', cname,
                'location_state', state,
                'city_id', cityid
            )
        )
    )
) as city_payload
from city
group by cityid
order by cityid
;
----------------------------------------------------------------------------------------------------

https://github.com/kactlabs/flask-migrate-postgres/tree/master

python manage.py db init

python manage.py db stamp head

python manage.py db migrate -m "City Table added"

python manage.py db migrate

python manage.py db upgrade


Sample logs:
	python manage.py db stamp head
	INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
	INFO  [alembic.runtime.migration] Will assume transactional DDL.
	INFO  [alembic.runtime.migration] Running stamp_revision  -> 7046c3e54d66
	
	(py38)  ~/d/kaipulla_space/flask-migrate-postgres   master ±  python manage.py db migrate -m "City Table added"
	INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
	INFO  [alembic.runtime.migration] Will assume transactional DDL.
	INFO  [alembic.autogenerate.compare] Detected added table 'city'
	INFO  [alembic.autogenerate.compare] Detected added table 'my_user'
	  Generating /Users/rajacsp/d/kaipulla_space/flask-migrate-postgres/migrations/versions/2ff3b030eed_city_table_added.py ... done
	
	(py38)  ~/d/kaipulla_space/flask-migrate-postgres   master ±  python manage.py db upgrade
	INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
	INFO  [alembic.runtime.migration] Will assume transactional DDL.
	INFO  [alembic.runtime.migration] Running upgrade 7046c3e54d66 -> 2ff3b030eed, City Table added




----------------------------------------------------------------------------------------------------

# pg function

#
create function get_city_count()
returns int
language plpgsql
as
$$
declare
   city_count integer;
begin
   select count(*) 
   into city_count
   from city;
   
   return city_count;
end;
$$;


It should retrun "CREATE FUNCTION"

select * from get_city_count();




#
create function get_city()
returns int
language plpgsql
as
$$
declare
   city_count integer;
begin
   select count(*) 
   into city_count
   from city;
   
   return city_count;
end;
$$;



#
CREATE OR REPLACE FUNCTION get_city_2(c_city varchar(50))
  returns table (abc varchar(50), xyz varchar(50))
AS 
$$
BEGIN
    Return query 
       SELECT 
	   	cname as abc, 
	   	state AS xyz
       from city
	   where cname = c_city
	   ;
       
END;
$$
LANGUAGE plpgsql;

select * from get_city_2('hello'); -- it should return empty
select * from get_city_2('Montreal');

DROP FUNCTION get_city_2(varchar(50));


#
CREATE OR REPLACE FUNCTION get_city_3(c_city varchar(50))
  returns table (name varchar(50), c_state varchar(50))
AS 
$$
BEGIN
    Return query 
       SELECT 
	   	cname as name, 
	   	state AS c_state
       from city
	   where cname like c_city
	   ;
       
END;
$$
LANGUAGE plpgsql;

select * from get_city_3('%on%');

DROP FUNCTION get_city_3(varchar(50));


----------------------------------------------------------------------------------------------------


CREATE TABLE orders (
	id serial NOT NULL PRIMARY KEY,
	info json NOT NULL
);

INSERT INTO orders (info)
VALUES('{ "customer": "John Doe", "items": {"product": "Beer","qty": 6}}');

select * from orders;

delete * from orders;

drop table orders;

----------------------------------------------------------------------------------------------------


CREATE TABLE product (
	id serial NOT NULL PRIMARY KEY,
	info json
);

INSERT INTO product (info)
VALUES('{ "customer": "John Doe", "items": {"product": "Beer","qty": 6}}');

INSERT INTO product (info)
VALUES('Some content');

select * from product;

delete * from product;

drop table product;

-- to get the columns
SELECT column_name FROM information_schema.columns WHERE table_name ='product';



----------------------------------------------------------------------------------------------------


CREATE TABLE WEBENTRY (
    ID serial NOT NULL PRIMARY KEY,
    URL VARCHAR(500),
    SCHEDULE_ID INT,
    JOB_ID INT
);

INSERT INTO WEBENTRY (URL, SCHEDULE_ID, JOB_ID) VALUES('Url1', 2001, 3001);
INSERT INTO WEBENTRY (URL, SCHEDULE_ID, JOB_ID) VALUES('Url1', 2002, 3002);
INSERT INTO WEBENTRY (URL, SCHEDULE_ID, JOB_ID) VALUES('Url1', 2003, 3003);
INSERT INTO WEBENTRY (URL, SCHEDULE_ID, JOB_ID) VALUES('Url1', 2004, 3004);
INSERT INTO WEBENTRY (URL, SCHEDULE_ID, JOB_ID) VALUES('Url1', 2005, 3005);


SELECT * FROM WEBENTRY;

UPDATE WEBENTRY SET JOB_ID = 4002 WHERE SCHEDULE_ID = 2002;


----------------------------------------------------------------------------------------------------



Extensions:

#
Show extensions
\dx

or

SELECT * 
FROM pg_extension;
	https://stackoverflow.com/questions/21799956/using-psql-how-do-i-list-extensions-installed-in-a-database

select * from pg_available_extensions;
	https://blog.dbi-services.com/listing-the-extensions-available-in-postgresql/
	
#
CREATE EXTENSION cube
CREATE EXTENSION earthdistance


# Get into extension folder
docker exec -it pg11 bash
cd /usr/share/postgresql/14/extension


https://www.educba.com/postgresql-extensions/

------------------------------------------------------------------------------------


Install Git:

https://linoxide.com/how-to-install-git-on-debian/

https://git.postgresql.org/gitweb/?p=postgresql.git;a=summary
https://git.postgresql.org/gitweb/?a=project_list&s=postgresql&btnS=Search




------------------------------------------------------------------------------------


plpython3:

https://wiki.postgresql.org/wiki/WIP:plpython3

https://github.com/aureliengervasi/postgresql-plpython3/blob/master/Dockerfile




------------------------------------------------------------------------------------

Anonymous table:

select * from (values (1, 'Hello world'), (100, 'Another row')) as foo (mycol1, mycol2);





------------------------------------------------------------------------------------

Column to multiple rows:

SELECT s.token
FROM  
(values (1, 'One, Two'), (100, 'Another row')) as t (mycol1, mycol2), unnest(string_to_array(t.mycol2, ' ')) s(token)


SELECT s.token
FROM  
 unnest(string_to_array('One, Two', ' ')) s(token)





----------------------------------------------------------------------------------------------------

```

#### Ref :

  * []()
