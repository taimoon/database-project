USE portManagementDB;

/*
1. Produce a list of information about the documents and agents 
who are successfully gain approval that freights were sent out to Japan. 
*/
select agent.agentName, agent.agentID, request.documentID,list.freightID
from agent,request,list
where agent.agentID=request.agentID and
request.listID=list.listId
and  list.origin in ("Japan")
and request.approval like '1%'
and list.freightDirection like '0%';

/*
2. produce a list of information about the freight's location, 
freight type, maximum gross weight that from Japan 
*/

select targetinfo.targetID, freight.areaID,freight.locx, freight.locY, freight.stackLVl,
freightType.freightTypename, freightType.maxgrossWeight
from targetinfo, freight,freightType,list
where targetinfo.targetID = list.targetID
and list.freightID=freight.freightID
and list.freighttypeid=freighttype.freighttypeid
and list.origin in ("Japan")
order by freight.areaID asc ,freight.locx asc, freight.locY asc, freight.stackLVl asc;

/*
3. list all person in charge of freight from japan and their transportation information
*/


select distinct targetinfo.PICname, targetinfo.targetID, vehicleinfo.vehiclename
,vehicleinfo.vehicleMaxFreightCounts,vehicleinfo.vehicledescription
from vehicleinfo, list, targetinfo
where targetinfo.targetID = list.targetID 
and targetinfo.vehicletypeid =vehicleinfo.vehicletypeid
and list.origin in ("Japan")
order by targetinfo.PICname asc ;

/*
4. produce the list of first 10 person in charge name, agent name and agent contact 
email that handled outbound of freight based on the departure time.
*/

select agent.agentname, agent.agentemail,targetinfo.PICname,
historicalFreight.departureTime,historicalFreight.freightID
from agent, targetinfo,historicalFreight,list
where agent.agentID = targetinfo.agentID
and list.targetID = Targetinfo.targetID
and list.freightID=historicalFreight.freightID
order by historicalFreight.departureTime asc
LIMIT 10;

/*
5. retrieve a list of  freight that located at stack level of 10
*/

select freight.freightID, freight.areaID, freight.locx
from freight
group by freight.areaID,freight.locx, freight.locy,freight.stacklvl
having freight.stacklvl=10
order by freight.areaID asc ,freight.locx asc, freight.locy asc,freight.locy;

/*
4. produce the list of first 10 person in charge name, agent name and agent contact 
email that handled outbound of freight based on the departure time.
*/

/*
6. Heaviest loadable freight type information
*/
select freighttypeName as Heaviest_Freight_Name,freighttypeID,freightheight,freightlength,tareweight
,max(freighttype.maxgrossweight) as Gross_Weight
from freighttype;

/*
7. To update the departureTime in historicalfreight table for correction
*/

update historicalfreight 
set departureTime ="2022-12-20 05:05:05"
where freightID in ("PABU2841438","PABU2454948","PABU2615908");

/*
8. To calculate the number of freight in each area
*/

select areaid as Area,count(areaID) as FreightCount
from freight
group by areaID
order by areaid asc;


/*
9.  To search all information of vehicle info regarding transportation 
of high risk liquid cargo by using related keywords
*/

select *
from vehicleinfo	
where vehicleDescription like '%danger%' or  '%dangerous%' 
or '%hazardous%' or '%risk%' or '%liquid%' or '%fluid%'
or '%solution%';


/*
10.   Find all the freight ID and area id where location x is not in the range of 1 and 60,
 location y is not in the range of 1 and 60 and stack level is in the range of 1 and 3. 

*/

select freightID, areaID
from freight
where locx not between 1 and 60
and locy not between 1 and 60
and stacklvl between 1 and 3
order by areaID asc ;