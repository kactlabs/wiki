/ [Home](index.md)

# SQLite

**Note:** notes


SQLite  - How to install in Ubuntu?
```
sudo apt-get update
sudo apt-get install sqlite3
sqlite3 --version
```
*[Ref](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/)


SQLite - How to install in Mac?
```
TBW
```

SQLite  - How to install in Windows?
```
TBW
```


SQLiteBrowser (DBBrowser) - How to install in Ubuntu?
```
sudo apt-get install sqlitebrowser
```
*[Ref](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/)


### Basic SQL Commands for SQLite
```
CREATE TABLE CITY(
	ID INTEGER PRIMARY KEY,
	NAME TEXT,
	STATE TEXT
);

INSERT INTO CITY (NAME, STATE) VALUES ('San Francisco', 'CA',);
INSERT INTO CITY (NAME, STATE) VALUES ('Chennai', 'TA');
INSERT INTO CITY (NAME, STATE) VALUES ('Madurai', 'TA');
INSERT INTO CITY (NAME, STATE) VALUES ('Bengalore', 'KA');

SELECT * FROM CITY;

SELECT NAME FROM CITY;

SELECT NAME, CITY FROM CITY WHERE ID > 2;


Verify SQLite in Python:
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 
Course work: 
@author:
Source:
    
'''
import sqlite3
import random
from sqlite3 import Error

database = "test" # db location

def start():
    """
    Query all rows in the CITY table
    :param conn: the Connection object
    :return:
    """    
    conn = None
    
    try:
        conn = sqlite3.connect(database)        
    except Error as e:
        print(e) 
        return
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM CITY")
 
    rows = cur.fetchall()
    
    print('rows count : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row)

if __name__ == '__main__':
    start() 

```
[ref](https://github.com/teamkact/simple-crud-python-sqlite)

```

# Sources :

  * [Name](file)
