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

refer to the [click here for Normalization](https://github.com/soonkienyuan/database-project-1/blob/main/Report/NORMALIZATION%202.0.docx)

### DATA DICTIONARY

1. **Agent**

| **ATTRIBUTES** | **DATA TYPE** | **DESCRIPTION** | **CONSTRAINTS** | **EXAMPLE**                                           |
| -------------- | ------------- | --------------- | --------------- | ----------------------------------------------------- |
| agentID        | VARCHAR(3)    | agent ID        | PK              | AIS                                                   |
| agentName      | VARCHAR(125)  | agent name      | NOT NULL        | Albanian Int Shipping Agency                          |
| agentEmail     | VARCHAR(50)   | agent Email     | NOT NULL        | [arbagent@arbaship.com](mailto:arbagent@arbaship.com) |
| specialisation | VARCHAR(100)  | specialisation  | NOT NULL        | Shipping Agency                                       |

 

2. **Freight**

| **ATTRIBUTES** | **DATA TYPE** | **DESCRIPTION**     | **CONSTRAINTS** | **EXAMPLE**    |
| -------------- | ------------- | ------------------- | --------------- | -------------- |
| freightID      | VARCHAR(11)   | Freight ID          | PK              | CMSU8357727    |
| inListID       | INT           | inbound list ID     | FK              | 5              |
| arrivalTime    | TIMESTAMP     | arrival Time        | NOT NULL        | 1/10/2022 3:12 |
| areaID         | VARCHAR(2)    | area ID             |                 | A              |
| locX           | INT           | horizontal position |                 | 6              |
| locY           | INT           | vertical position   |                 | 17             |
| stackLvl       | INT           | stack level         |                 | 5              |

3. **Freighttype**

| **ATTRIBUTES**  | **DATA TYPE** | **DESCRIPTION**      | **CONSTRAINTS** | **EXAMPLE**               |
| --------------- | ------------- | -------------------- | --------------- | ------------------------- |
| freightTypeID   | VARCHAR(4)    | freight Type ID      | PK              | 20G0                      |
| freightTypeName | VARCHAR(50)   | freight Type Name    | NOT NULL        | General Purpose Container |
| freightHeight   | FLOAT         | freight Height       |                 | 2438                      |
| freightLength   | FLOAT         | freight Length       |                 | 3048                      |
| tareWeight      | FLOAT         | tare Weight          |                 | 2080                      |
| maxGrossWeight  | FLOAT         | maximum Gross Weight |                 | 30500                     |
| maxNetWeight    | FLOAT         | maximum Net Weight   |                 | 28300                     |

 

4. **Historicalfreight**

| **ATTRIBUTES** | **DATA TYPE** | **DESCRIPTION**  | **CONSTRAINTS** | **EXAMPLE**         |
| -------------- | ------------- | ---------------- | --------------- | ------------------- |
| freightID      | VARCHAR(11)   | freight ID       | PK1             | CMSU7773080         |
| arrivalTime    | TIMESTAMP     | arrival Time     | PK2             | 2022-01-10 03:12:10 |
| departureTime  | TIMESTAMP     | departure Time   | PK3             | 2022-01-10 03:12:10 |
| inListID       | INT           | inbound list ID  |                 | 1                   |
| outListID      | INT           | outbound list ID |                 | 2                   |

5. **List**

| **ATTRIBUTES**   | **DATA TYPE** | **DESCRIPTION**   | **CONSTRAINTS** | **EXAMPLE** |
| ---------------- | ------------- | ----------------- | --------------- | ----------- |
| listID           | INT           | list ID           | PK, FK          | 1           |
| freightID        | VARCHAR(11)   | freight ID        | PK              | CMSU7773080 |
| freightTypeID    | VARCHAR(4)    | freight type ID   | NOT NULL        | 1000        |
| targetID         | VARCHAR(20)   | target ID         | NOT NULL        | 20G0        |
| freightDirection | BOOLEAN       | freight Direction | NOT NULL        | 1           |
| origin           | VARCHAR(16)   | country of origin |                 | Lunarian    |

6. **Request**

| **ATTRIBUTES** | **DATA TYPE** | **DESCRIPTION** | **CONSTRAINTS** | **EXAMPLE** |
| -------------- | ------------- | --------------- | --------------- | ----------- |
| listID         | INT           | list ID         | PK              | 1           |
| agentID        | VARCHAR(3)    | agent ID        | FK              | CMS         |
| documentID     | VARCHAR(20)   | document ID     | NOT NULL        | MY10059     |
| approval       | BOOLEAN       | apporval        | NOT NULL        | 1           |
| direction      | VARCHAR(5)    | direction       | NOT NULL        | IN          |

7. **Targetinfo**

| **ATTRIBUTES** | **DATA TYPE** | **DESCRIPTION**          | **CONSTRAINTS** | **EXAMPLE**     |
| -------------- | ------------- | ------------------------ | --------------- | --------------- |
| targetID       | INT           | target ID                | PK              | 1000            |
| agentID        | VARCHAR(3)    | agent ID                 | FK              | GSK             |
| PICName        | VARCHAR(50)   | name of person in charge |                 | Marisa Kirisame |
| vehicleID      | VARCHAR(20)   | vehicle ID               |                 | RSD105998       |
| vehicleTypeID  | INT           | vehicle Type ID          | FK              | 1               |

8. **Vehicleinfo**

| **ATTRIBUTES**          | **DATA TYPE** | **DESCRIPTION**                | **CONSTRAINTS** | **EXAMPLE**                               |
| ----------------------- | ------------- | ------------------------------ | --------------- | ----------------------------------------- |
| vehicleTypeID           | INT           | vehicle Type ID                | PK              | 9                                         |
| vehicleName             | VARCHAR(20)   | vehicle Name                   |                 | Freuhauf                                  |
| vehicleMaxFreightCounts | INT           | vehicle Maximum Freight Counts |                 | 13                                        |
| vehicleCap              | FLOAT         | vehicle Capacity               |                 | 40000                                     |
| vehicleDescription      | VARCHAR(100)  | vehicle Description            |                 | Fantainer trailer. Carry dangerous liquid |

 







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
