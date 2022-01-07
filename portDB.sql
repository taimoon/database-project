/*
use source path\filename.sql
is better
*/
DROP DATABASE portManagementDB;
CREATE DATABASE portManagementDB;
USE portManagementDB;

CREATE TABLE agent(
	agentID 			VARCHAR(3) PRIMARY KEY NOT NULL,
	agentName 			VARCHAR(125) NOT NULL,
	agentEmail 			VARCHAR(50) NOT NULL,
	specialisation  	VARCHAR(100) NOT NULL
);
CREATE TABLE request(
	listID				INT PRIMARY KEY AUTO_INCREMENT,
	agentID				VARCHAR(3),
	FOREIGN KEY(agentID) REFERENCES agent(agentID),
	documentID			VARCHAR(20) NOT NULL,
	approval			BOOLEAN NOT NULL,
	direction			VARCHAR(5) NOT NULL
);
CREATE TABLE freightType(
	freightTypeID	VARCHAR(4) PRIMARY KEY,
	freightTypeName VARCHAR(50) NOT NULL,
	freightHeight	FLOAT,
	freightLength	FLOAT,
	tareWeight		FLOAT,
	maxGrossWeight	FlOAT,
	maxNetWeight	FLOAT
);
CREATE TABLE list(
	listID				INT NOT NULL,
	freightID			VARCHAR(11) NOT NULL,
	FOREIGN KEY(listID) REFERENCES request(listID),
	PRIMARY KEY(listID, freightID),
	freightTypeID		VARCHAR(4) NOT NULL,
	targetID			VARCHAR(20) NOT NULL, 
	freightDirection 	BOOLEAN NOT NULL,
	origin				VARCHAR(16)
);

CREATE TABLE freight(
	freightID		VARCHAR(11) NOT NULL,
	inListID		INT NOT NULL,
	arrivalTime		TIMESTAMP NOT NULL,
	areaID			VARCHAR(2),
	locX			INT,
	locY			INT,
	stackLvl		INT
);
CREATE TABLE historicalFreight(
	freightID		VARCHAR(11) NOT NULL,
	arrivalTime		TIMESTAMP NOT NULL,
	departureTime	TIMESTAMP NOT NULL,
	inListID		INT NOT NULL,
	outListID		INT NOT NULL
);
CREATE TABLE vehicleInfo(
	vehicleTypeID 				INT PRIMARY KEY AUTO_INCREMENT,
	vehicleName					VARCHAR(20) NOT NULL,
	vehicleMaxFreightCounts 	INT,
	vehicleCap					FLOAT,
	vehicleDescription			VARCHAR(100)
);
CREATE TABLE targetInfo(
	targetID		INT PRIMARY KEY,
	agentID			VARCHAR(3),
	FOREIGN KEY(agentID) REFERENCES agent(agentID),
	PICName			VARCHAR(50),
	vehicleID		VARCHAR(20) UNIQUE,
	vehicleTypeID	INT,
	FOREIGN KEY(vehicleTypeID) REFERENCES vehicleInfo(vehicleTypeID)
);