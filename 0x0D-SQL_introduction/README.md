# --- SQL - Introduction ---

**Learning objectives**
-------------
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

**Requirements**
-------------
**General**
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

**More Info**
-------------
**Comments for your SQL file:**
        $ cat my_script.sql
        -- 3 first students in the Batch ID=3
        -- because Batch 3 is the best!
        SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
        $

**Install MySQL 5.7 on Ubuntu 14.04 LTS**
        $ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
        $ sudo apt-get update
        $ sudo apt-get install mysql-server-5.7
        ...
        $ mysql --version
        mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
        $

Don’t forget your root password

Connect to your MySQL server:
        $ mysql -hlocalhost -uroot -p
        Password: 
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 42
        Server version: 5.7.8-rc MySQL Community Server (GPL)

        Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql> 
        mysql> quit
        Bye
        $

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common.

**Use “container-on-demand” to run MySQL**
- Ask for container Ubuntu 14.04 - Python 3.4
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

        $ service mysql start
         * MySQL Community Server 5.7.8-rc is started
        $
        $ cat 0-list_databases.sql | mysql -uroot -p my_database
        Enter password: 
        Database
        information_schema
        mysql
        performance_schema
        sys
        $

In the container, credentials are root/root.

**Tasks**
-------------
- 0 - Write a script that lists all databases of your MySQL server.
- 1 - Write a script that creates the database hbtn_0c_0 in your MySQL server.
- 2 - Write a script that deletes the database hbtn_0c_0 in your MySQL server.
- 3 - Write a script that lists all the tables of a database in your MySQL server.
- 4 - Write a script that creates a table called first_table in the current database in your MySQL server.
- 5 - Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
- 6 - Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
- 7 - Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
- 8 - Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
- 9 - Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
- 10 - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
- 11 - Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- 12 - Write a script that updates the score of Bob to 10 in the table second_table.
- 13 - Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
- 14 - Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.
- 15 - Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
- 16 - Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

**Advanced Tasks**
-------------
- 17 - Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
- 18 - Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
- 19 - Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).
- 20 - Write a script that displays the max temperature of each state (ordered by State name).
