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

SQL Code - [code here](https://github.com/soonkienyuan/database-project-1/blob/main/Data%20Definiton%20Language/portDB%20DDL.sql)



### Data manipulation language

Insert data into the 8 tables 











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
