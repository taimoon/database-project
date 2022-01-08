INSERT INTO request(agentID, documentID, approval, direction) VALUES ('HTS', '092C11BD0C', TRUE, "IN");
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU0132721', '22H0',1000, 1, 'South Korean');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU0132721', now(), 'B',5, 7, 8);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU8293764', '20G0',8801, 1, 'Indonesian');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU8293764', now(), 'A',0, 1, 9);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU8399144', '20T5',1450, 1, 'Malaysia');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU8399144', now(), 'A',8, 10, 2);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU6520088', '22G1',1136, 1, 'China');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU6520088', now(), 'B',0, 2, 10);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU2050134', '20T5',8801, 1, 'Malaysia');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU2050134', now(), 'B',10, 1, 7);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU2003765', '20G0',1050, 1, 'South Africa');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU2003765', now(), 'A',7, 3, 0);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU5411945', '20H0',3221, 1, 'United States');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU5411945', now(), 'B',3, 5, 0);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU8080727', '22U6',1000, 1, 'Canada');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU8080727', now(), 'A',7, 9, 9);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU1580715', '22U1',2435, 1, 'China');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU1580715', now(), 'A',7, 8, 5);
INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) VALUES (3, 'HTSU0079416', '22G1',7709, 1, 'United States');
INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) VALUES (3, 'HTSU0079416', now(), 'B',1, 3, 4);