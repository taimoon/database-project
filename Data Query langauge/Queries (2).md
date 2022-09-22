## Queries

### 1. Produce a list of information about the documents and agents who are successfully gain approval that freights were sent out to Japan. 


````sql
select agent.agentName, agent.agentID, request.documentID,list.freightID
from agent,request,list
where agent.agentID=request.agentID and
request.listID=list.listId
and  list.origin in ("Japan")
and request.approval like '1%'
and list.freightDirection like '0%';
````

![image-20220111113649136](C:\Users\soon kien yuan\Desktop\ump\sem 3\database\project\photo\image-20220111113649136.png)

next, location and arrival time--- HAVING condition

### 2. produce a list of information about the freight's location, freight type, maximum gross weight that from Japan

`````sql
select targetinfo.targetID, freight.areaID,freight.locx, freight.locY, freight.stackLVl,
freightType.freightTypename, freightType.maxgrossWeight
from targetinfo, freight,freightType,list
where targetinfo.targetID = list.targetID
and list.freightID=freight.freightID
and list.freighttypeid=freighttype.freighttypeid
and list.origin in ("Japan")
order by freight.areaID asc ,freight.locx asc, freight.locY asc, freight.stackLVl asc;
`````

![image-20220111135407096](photo/image-20220111135407096.png)

### 3. list all person in charge of freight from japan and their transportation information

````sql
select distinct targetinfo.PICname, targetinfo.targetID, vehicleinfo.vehiclename
,vehicleinfo.vehicleMaxFreightCounts,vehicleinfo.vehicledescription
from vehicleinfo, list, targetinfo
where targetinfo.targetID = list.targetID 
and targetinfo.vehicletypeid =vehicleinfo.vehicletypeid
and list.origin in ("Japan")
order by targetinfo.PICname asc ;
````

![image-20220111193955706](photo/image-20220111193955706.png)

### 4. produce the list of first 10 person in charge name, agent name and agent contact email that handled outbound of freight based on the departure time.
````sql
select agent.agentname, agent.agentemail,targetinfo.PICname,historicalFreight.departureTime,historicalFreight.freightID
from agent, targetinfo,historicalFreight,list
where agent.agentID = targetinfo.agentID
and list.targetID = Targetinfo.targetID
and list.freightID=historicalFreight.freightID
order by historicalFreight.departureTime asc
LIMIT 10;
````

![image-20220112132718038](photo/image-20220112132718038.png)

### 5. retrieve a list of  freight that located at stack level of 10

````sql
select freight.freightID, freight.areaID, freight.locx
from freight
group by freight.areaID,freight.locx, freight.locy,freight.stacklvl
having freight.stacklvl=10
order by freight.areaID asc ,freight.locx asc, freight.locy asc,freight.locy;
````

![image-20220112135548910](photo/image-20220112135548910.png)

### 6. Heaviest loadable freight type information
````sql
select freighttypeName as Heaviest_Freight_Name,freighttypeID,freightheight,freightlength,tareweight
,max(freighttype.maxgrossweight) as Gross_Weight
from freighttype;
````

![image-20220112143448780](photo/image-20220112143448780.png)

### 7. To update the departureTime in historicalfreight table for correction

````sql
update historicalfreight 
set departureTime ="2022-12-20 05:05:05"
where freightID in ("PABU2841438","PABU2454948","PABU2615908");
````

![image-20220112145458212](photo/image-20220112145458212.png)

![image-20220112145534981](photo/image-20220112145534981.png)

### 8. To calculate the number of freight in each area

````sql
select areaid as Area,count(areaID) as FreightCount
from freight
group by areaID
order by areaid asc;
````

![image-20220112151106050](photo/image-20220112151106050.png)

### 9.  To search all information of vehicle info regarding transportation of high risk liquid cargo by using related keywords

`````sql
select *
from vehicleinfo	
where vehicleDescription like '%danger%' or  '%dangerous%' 
or '%hazardous%' or '%risk%' or '%liquid%' or '%fluid%'
or '%solution%';
`````

![image-20220112153101891](photo/image-20220112153101891.png)

### 10.   Find all the freight ID and area id where location x is not in the range of 1 and 60, location y is not in the range of 1 and 60 and stack level is in the range of 1 and 3. 

`````sql
select freightID, areaID
from freight
where locx not between 1 and 60
and locy not between 1 and 60
and stacklvl between 1 and 3
order by areaID asc ;
`````

![image-20220112153814413](photo/image-20220112153814413.png)
