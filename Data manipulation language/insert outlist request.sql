INSERT INTO request(agentID, documentID, approval, direction) VALUES ("MAC", "3C5B40A6E3", TRUE, "OUT");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU2833926", "20H0","1050", False, "United Kingdom");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU8391349", "22G1","8801", False, "German");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "CMSU7773080", "22G1","1450", False, "France");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU7073493", "20G0","1450", False, "United Kingdom");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU7937482", "22V0","2435", False, "Thailand");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU5376715", "22G1","1050", False, "China");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU3759870", "22B0","7709", False, "United States");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU6532411", "22G1","1136", False, "South Korean");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU1374870", "22H0","1000", False, "South Africa");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("4", "HTSU9862459", "22U1","1050", False, "Brazil");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU2833926", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU2833926"),(SELECT inListID FROM freight WHERE freightID="HTSU2833926"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU8391349", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU8391349"),(SELECT inListID FROM freight WHERE freightID="HTSU8391349"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("CMSU7773080", now(), (SELECT arrivalTime FROM freight WHERE freightID="CMSU7773080"),(SELECT inListID FROM freight WHERE freightID="CMSU7773080"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU7073493", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU7073493"),(SELECT inListID FROM freight WHERE freightID="HTSU7073493"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU7937482", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU7937482"),(SELECT inListID FROM freight WHERE freightID="HTSU7937482"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU5376715", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU5376715"),(SELECT inListID FROM freight WHERE freightID="HTSU5376715"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU3759870", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU3759870"),(SELECT inListID FROM freight WHERE freightID="HTSU3759870"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU6532411", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU6532411"),(SELECT inListID FROM freight WHERE freightID="HTSU6532411"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU1374870", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU1374870"),(SELECT inListID FROM freight WHERE freightID="HTSU1374870"), "4");
INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) VALUES ("HTSU9862459", now(), (SELECT arrivalTime FROM freight WHERE freightID="HTSU9862459"),(SELECT inListID FROM freight WHERE freightID="HTSU9862459"), "4");
DELETE FROM freight WHERE freightID="HTSU2833926";
DELETE FROM freight WHERE freightID="HTSU8391349";
DELETE FROM freight WHERE freightID="CMSU7773080";
DELETE FROM freight WHERE freightID="HTSU7073493";
DELETE FROM freight WHERE freightID="HTSU7937482";
DELETE FROM freight WHERE freightID="HTSU5376715";
DELETE FROM freight WHERE freightID="HTSU3759870";
DELETE FROM freight WHERE freightID="HTSU6532411";
DELETE FROM freight WHERE freightID="HTSU1374870";
DELETE FROM freight WHERE freightID="HTSU9862459";