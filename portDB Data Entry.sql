/*
use source path\filename.sql
is better
*/
USE portManagementDB;
INSERT INTO agent(agentID, agentName, agentEmail, specialisation)
	VALUES
	("GSK", "Gensokyo The Speedy", "gensokyo@gmail.com", "Fantasy Travel Logistic"),
	("CMS", "Commonwealth of Man", "commonwealthOfMan@stellaris.milkyway.earth", "FTL Instellar Logistic"),
    ("AIS", "Albanian Int Shipping Agency", "arbagent@arbaship.com", "Shipping Agency"),
    ("MAC", "Mory And Cie", "support@ruzave.com", "Freight Forwading"),
    ("PAB", "Promar Agencies Belgium", "ghent@promar-agencies.be", "Ship Spares Handling"),
    ("PGF", "Pasir Gudang Forwarding", "sales@pgship.com.my", "Shipment Pre-Alert"),
    ("HTS", "Harrisons Trading Sabah", "general@harrisons.com.my", "Fast Moving Consumer Goods"),
    ("CSB", "China Shipping Beijing", "info@ewtl.com", "Cargo Insurance");
INSERT INTO vehicleInfo(vehicleName, vehicleMaxFreightCounts, vehicleCap, vehicleDescription)
	VALUES
    ("Glorious Ark Ship", 1000, 50000, "Cutting edge technology made space ship with FTL technology. Able to carry vital goods"),
	("Magic Broom", 10, 10000, "the fruit of hardship of an oridnary human"),
    ("Escalade Chevy", 7, 45000, "Specialty trailer. Carry various of liquid"),
	("Chevrolet Roro", 12, 50000, "Specialty trailer. Carry various of liquid"),
    ("Volvo Appen", 10, 45000, "Fantainer trailer. Mechanically ventillation system"),
	("Freuhauf", 13, 40000, "Fantainer trailer. Mechanically ventillation system"),
    ("Hyundai Translead", 12, 50000, "Specialty trailer. Carry various of liquid"),
    ("Kentucky Trailer", 10, 48000, "Fantainer trailer. Mechanically ventillation system"),
	("Freuhauf", 13, 40000, "Fantainer trailer. Carry dangerous liquid");
INSERT INTO targetInfo(targetID, PICName, agentID, vehicleID, vehicleTypeID)
	VALUES
	(1000,  "Marisa Kirisame", "GSK", "RSD105998", 1),
	(1050, "Captain Ukewon Vulcan", "CMS",  "SUN388997", 2),
    (1450,  "Oliver Haaland", "AIS", "JKF234467", 1),
	(2435, "Erling Salah", "MAC",  "FUG776455", 2),
    (3221,  "Ahmad De Bruyne", "PAB", "BJK334241", 2),
	(7709, "Lionel Kante", "PGF",  "KSU777231", 1),
    (8801,  "Jacob Frye", "HTS", "KKB787890", 2),
	(1136, "Saka Smith Rowe", "CSB",  "SOK889077", 2);
INSERT INTO freightType(freightTypeID, freightTypeName, freightHeight, freightLength, tareWeight, maxGrossWeight, maxNetWeight)
	VALUES
	("20G0", "General Purpose Container", 2438, 3048, 2080, 30500, 28300),
    ("22G1", "General Purpose Container", 2086, 3007, 2250, 30480, 28300),
    ("20H0", "Insulated Container", 2591, 3048, 2275, 32311, 29635),
    ("20P1", "Flat (Fixed Ends)", 2438, 3048, 3172, 31788, 28341),
    ("20T5", "Tank Container", 2896, 12192, 3033, 30626, 29954),
    ("22B0", "Bulk Container", 2438, 6096, 3462, 30768, 29912),
    ("22H0", "Insulated Container", 2896, 7315, 3489, 32858, 30886),
    ("22U6", "Hardtop Container", 3421, 2444,3899,32884,29385),
	("22U1", "Open Top Container)", 2677, 4590, 3172, 31788, 28341),
	("22V0", "Ventilated Container", 2378, 2112, 3033, 33423,29954);
	

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