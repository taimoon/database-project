## Join

### Produce a list of information about the documents and agents who are successfully gain approval that freights were sent out to Japan. 


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

### produce a list of information about the freight's location, freight type, maximum gross weight that from Japan

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

### list all person in charge of freight from japan and their transportation information

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

````sql
select agent.agentname, agent.agentemail,targetinfo.PICname,historicalFreight.departureTime
from agent, targetinfo,historicalFreight,list
where agent.agentID = targetinfo.agentID
and list.targetID = Targetinfo.targetID
and list.freightID=historicalFreight.freightID
and agent.agentID in ("MAC");
````

