/*
use source path\filename.sql
is better
*/
USE portManagementDB;
INSERT INTO agent(agentID, agentName, agentEmail, specialisation)
	VALUES
	("GSK", "Gensokyo The Speedy", "gensokyo@gmail.com", "Fantasy Logistic"),
	("CMS", "Commonwealth Men Space", "spaceX@email.com", "Interstellar Logistic");
INSERT INTO vehicleInfo(vehicleName, vehicleMaxFreightCounts, vehicleCap, vehicleDescription)
	VALUES
	("Miracle Broom", 10, 1, "Fruit of Hard work. Western Magic but studied in the way of Eastern"),
	("Glorious Carrier", 500, 1000, "The first commercial interstellar spaceship");
INSERT INTO targetInfo(targetID, PICName, agentID, vehicleID, vehicleTypeID)
	VALUES
	(1000,  "Marisa Kirisame", "GSK", "RSD105998", 1),
	(1050, "Captain Ukewon Vulcan", "CMS",  "SUN3889977", 2);
INSERT INTO freightType(freightTypeID, freightTypeName, freightHeight, freightLength, tareWeight, maxGrossWeight, maxNetWeight)
	VALUES
	("20G0", "general purpose container", 2438, 3048, 2080, 30500, 28300);
	

INSERT INTO request(agentID, documentID, approval, direction)
	VALUES
	("CMS", "MY10059", TRUE, "IN"),
	("GSK", "MY10060", TRUE, "INOUT");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin)
	VALUES
	(1, "GSKU3053054", 1000,"20G0", TRUE, "Gensokyo"),
	(1, "CMSU7773080", 1000,"20G0", TRUE, "Lunarian"),
	(2, "CMSU7773078", 1000,"20G0", TRUE, "the Mars"),
	(2, "GSKU3053078", 1000,"20G0", FALSE, "Gensokyo");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl)
	VALUES
	(1, "GSKU3053054", now(), 'A', 0,1,2),
	(1, "CMSU7773080", now(), 'A', 0,1,3),
	(2, "CMSU7773078", now(), 'B', 0,1,3);