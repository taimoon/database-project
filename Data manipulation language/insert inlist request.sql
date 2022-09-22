INSERT INTO request(agentID, documentID, approval, direction) VALUES ("HTS", "F5DA587E04", TRUE, "IN");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU5376715", "22U6","1450", True, "South Korean");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU7073493", "20P1","1450", True, "Europe");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU3759870", "22V0","1050", True, "Indonesian");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU9862459", "20P1","3221", True, "Brazil");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU7937482", "22V0","3221", True, "Europe");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU8391349", "20G0","2435", True, "Malaysia");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU1374870", "22U6","1050", True, "Japan");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU2833926", "20T5","3221", True, "France");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU4336298", "20H0","7709", True, "Brazil");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES ("3", "HTSU6532411", "20H0","3221", True, "South Korean");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU5376715", now(), "D","27", "51", "4");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU7073493", now(), "D","1", "20", "0");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU3759870", now(), "A","94", "54", "5");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU9862459", now(), "B","26", "75", "3");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU7937482", now(), "C","77", "60", "10");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU8391349", now(), "B","42", "45", "0");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU1374870", now(), "B","66", "42", "7");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU2833926", now(), "A","91", "16", "3");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU4336298", now(), "B","87", "38", "7");
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES ("3", "HTSU6532411", now(), "C","15", "57", "8");