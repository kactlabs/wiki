/ [Home](index.md)

# MySQL Docker

**Note:** Mysql Docker on Mac and Ubuntu



#### Run MySQL container
```
docker pull mysql

docker run -d --name=mysql1 -e MYSQL_ROOT_PASSWORD=’mypassword’ -v /storage/mysql1/mysql-datadir:/var/lib/mysql mysql

docker run -d --name=mysql2 -e MYSQL_ROOT_PASSWORD=’mypassword’ -v /storage/mysql2/mysql-datadir:/var/lib/mysql mysql
```


#### Mysql Setup - Mac - Docker:
```
docker run -p 3306:3306 --name kactmysql -e MYSQL_ROOT_PASSWORD=kaipulla -d mysql:latest

mysql -uroot -pkaipulla -h127.0.0.1 -P3306
```

#### If any firewall issue, try this on Mac:
```
sudo vi /usr/local/etc/my.cnf
bind-address = 0.0.0.0
brew services restart mysql
```

#### Create DB and Table
```
Create database kactdb;
GRANT ALL PRIVILEGES ON kactdb.* TO 'root'@'localhost';
flush privileges;
use kactdb;

CREATE TABLE CITY(
  ID SERIAL PRIMARY KEY,
	NAME VARCHAR(50),
	STATE VARCHAR(50),
	COUNTRY VARCHAR(50)
);

INSERT INTO CITY (NAME, STATE, COUNTRY) VALUES ('Toronto', 'Ontario', 'Canada');

SELECT * FROM CITY;
```

##### Ref:
[MySQL Firewall Enable in MacOS](https://dba.stackexchange.com/questions/55958/cant-remote-access-mysql-server-running-on-mac-os-x)


#### Test code in Python
```
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", 
                     user="root",      
                     passwd="kaipulla",
                     db="kactdb")     

cur = db.cursor()

cur.execute("SELECT * FROM CITY")

counter = 0
for row in cur.fetchall():
    try:
        counter = counter + 1
        title = str(row[2])
        company = str(row[3])
        print(str(counter) + " - " +  title + " - " + company)
    except ValueError as e:
        print('Error')

db.close()
```

##### Credits :

  * [Mysql Docker]([file](https://severalnines.com/blog/mysql-docker-building-container-image))
