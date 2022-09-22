# Port Freight Management System with MySQL

The goal of this project is to assist us in learning by creating a database for the port freight management system.

Furthermore, we attempt to understand and design the conceptual and logical structure of the database.

## What is Port Freight Management System?

In brief,

- To manage the administrative procedures associated with a vessel's arrival and departure.
- To monitor the flow of traffic within the port basin.
- To stored information regarding port agents, types of cargo, and vehicles.

## Conceptual Database Design

### Bussiness Rule

Please refer to the ERD, and if necessary, the report.

### ERD

![ERD](https://github.com/soonkienyuan/database-project-1/blob/main/Image/ERD.jpg?raw=true)

### EERD   

![EERD](https://github.com/soonkienyuan/database-project-1/blob/main/Image/EERD.jpg?raw=true)

## Logical database Design 

### Data Definiton Language

Created 8 Tables in the Port Freight Management database using the following SQL commands:

``CREATE DATABASE``, ``CREATE TABLE table_name``

SQL Code for DDL - [code here](https://github.com/soonkienyuan/database-project-1/blob/main/Data%20Definiton%20Language/portDB%20DDL.sql)

![List of Table](https://github.com/soonkienyuan/database-project-1/blob/main/Image/DDL.jpg?raw=true)

### Data manipulation language

Insert data into the 8 tables using the following SQL commands:

``INSERT INTO table_name (column1, column2, column3,..) VALUES ( value1, value2, value3,..)`` or 

``INSERT INTO table_name VALUES (value1, value2, value3,…);``

Delete existing records from a table using the following SQL commands:

``DELETE FROM table_name WHERE some_condition; ``



SQL Code for DML - [code here](https://github.com/soonkienyuan/database-project-1/tree/main/Data%20manipulation%20language)

| Table Name        | Number of Rows | Image                                                        |
| ----------------- | ------------- | ------------------------------------------------------------ |
| agent             | 8             | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/agent.jpg?raw=true) |
| freight           | 202           | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/Freight.jpg?raw=true) |
| freighttype       | 10            | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/freight_type.jpg?raw=true) |
| historicalfreight | 411           | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/historicalfreight.jpg?raw=true) |
| list              | 1024          | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/list.jpg?raw=true) |
| request           | 44            | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/Request.jpg?raw=true) |
| targetinfo        | 8             | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/TargetInfo.jpg?raw=true) |
| vehicleinfo       | 9             | ![](https://github.com/soonkienyuan/database-project-1/blob/main/Image/vehicleinfo.jpg?raw=true) |



### Data Query langauge

refer to the [click here for Queries folder](https://github.com/soonkienyuan/database-project-1/tree/main/Data%20Query%20langauge)

### Normalizaton 

refer to the [click here for Normalization}(https://github.com/soonkienyuan/database-project-1/blob/main/Report/NORMALIZATION%202.0.docx)







Run the sql files in order to set up the database.
1. portDB DDL
2. portDB Data Entry
3. insert inlist request
4. insert outlist request
5. extraList
6. extra inlist insertion
7. extra outlist insertion \
Note that you can put them into a starter sql file using source path\filename 

The mysqlusingpython was to simulate the database under operation by generating random requests.
It could be easily extend into a software. \
Make sure that you install mysql python connector before running.
Run mysqlusingpython, and key in your database password, press enter
if you wish to run something.
