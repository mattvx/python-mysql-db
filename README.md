# python-mysql-db
A procedure to deploy a test database as a docker container and a simple python program using pymysql to execute some queries.

Tested on :
     $ uname -a : Linux warmachine 5.11.0-40-generic #44~20.04.2-Ubuntu SMP Tue Oct 26 18:07:44 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

First ensure you have installed:
  
  -docker
  
  -mysql
  
  -python module pymysql
  
**1: Deploying the test database is as simple as writin this one-liner:**

   _docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=docker -d mysql:latest_

**2: With docker ps now you should see it running.**

**3: You should now be able to connect to it via command line:**

*$ mysql -h 127.0.0.1 -u root --password=docker -P 3306*

**4: You can now create a new database with a test table. i created a database namd "test" with a table in it called "animali" wich contains some random
animal names along with their birthdate, sex and owner info. I later added a primary key to unique identify each record:**

  mysql> CREATE DATABASE test;
  
  mysql> USE test
  
  mysql> CREATE TABLE animali (nome VARCHAR(20), proprietario VARCHAR(30),
       specie VARCHAR(20), sesso CHAR(1), nascita DATE);
       
  mysql> ALTER TABLE animali ADD identificativo INT AUTO_INCREMENT PRIMARY KEY;
  
**5: Now we can drop in the table some data to start practicing queries:**

  _mysql> INSERT INTO animali VALUES ('animal_name','owner_name','species_name','M or F','date ad YYYY-MM-DD');_
  
**6: Ok, we can now leave the database:**

_mysql> exit_
  
**7: We can now run our python script to execute queries. YaY!**
