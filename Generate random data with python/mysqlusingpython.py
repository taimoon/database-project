from mysql.connector import (connection)
from portDataRandomGenerator import *

def cursorToList(cursor):
    res = []
    for i in cursor:
        res.append(i[0])
    return res
def getRequest():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM request")
    res = []
    for i in cursor:
        res.append(i[0])
    cursor.close()
    cnx.close()
    return res
def getInFreight():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT freightID FROM freight;")
    resList = []
    cursor.execute(query)
    for i in cursor:
        resList.append(i[0])
    cursor.close()
    cnx.close()
    return resList
def isFreightHere(cursor, freightID):
    query = (f"select freightID from list where freightID = \'{freightID}\';")
    cursor.execute(query)
    res = []
    for i in cursor:
        res.append(i)
    return res != []
def insertList(cursor, instance):
    query  = ("INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) "
                f"VALUES (\"{instance['listID']}\", \"{instance['freightID']}\", \"{instance['freightTypeID']}\","
                f"\"{instance['targetID']}\", {instance['freightDirection']}, \"{instance['origin']}\");"
            )
    f = open("extraList.sql", "a")
    f.write(query+"\n")
    f.close()
    cursor.execute(query)
def insertInList(instance):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    xLim = 100
    yLim = 100
    stackMax = 10
    if instance['freightDirection'] == False or isFreightHere(cursor, instance['freightID']) == True:
        return False
    insertList(cursor, instance)
    data = (instance['listID'], instance['freightID'], random.choice('ABCD'),
            random.randint(0,xLim),random.randint(0,yLim), random.randint(0,stackMax))
    addFreightQuery = ("INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) "
                       f"VALUES (\"{data[0]}\", \"{data[1]}\", now(), \"{data[2]}\",\"{data[3]}\", \"{data[4]}\", \"{data[5]}\");")
    cursor.execute(addFreightQuery)
    cnx.commit()
    cursor.close()
    cnx.close()
    f = open("extra inlist insertion.sql", "a")
    f.write(addFreightQuery + "\n")
    f.close()
    return True
def deleteFreight(freightID):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    dropFreight = (f"DELETE FROM freight WHERE freightID=\"{freightID}\";")
    cursor.execute(dropFreight)
    cnx.commit()
    cursor.close()
    cnx.close()
    f = open("deleteQuery.sql", "a")
    f.write(dropFreight + "\n")
    f.close()
def insertOutList(instance):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    if instance['freightDirection'] == True or isFreightHere(cursor, instance['freightID']) == False:
        return False
    insertList(cursor, instance)
    queryArrTime = (f"SELECT arrivalTime FROM freight WHERE freightID=\"{instance['freightID']}\"")
    queryInListID = (f"SELECT inListID FROM freight WHERE freightID=\"{instance['freightID']}\"")
    data = dict(freightID=instance['freightID'], outListID=instance['listID'])
    addHistoricalFreight = (f"INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) "
                       f"VALUES (\"{data['freightID']}\", now(), ({queryArrTime}),({queryInListID}), \"{data['outListID']}\");")
    cursor.execute(addHistoricalFreight)
    cnx.commit()
    cursor.close()
    cnx.close()
    deleteFreight(instance['freightID'])
    f = open("extra outlist insertion.sql", "a")
    f.write(addHistoricalFreight + "\n")
    f.close()


originList = ["United States", "China", "Indonesian", "Philippines", "United Kingdom", "Europe", "Japan",
              "South Africa", "Yemen", "Canada", "German", "France", "Brazil", "South Korean",
              "Malaysia", "Thailand"]
agentList = getAllAgent()
freightTypeList = getAllFreightType()
targetList = getAllTargetInfo()
directionDomain = ['IN', 'OUT', 'INOUT']
def randomRequest(direction, size = 1):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    generator = lambda : dict(agentID=random.choice(agentList),
                              documentID=''.join(random.choice('0123456789ABCDEF') for i in range(10)),
                              )
    f = open("requestList.sql", "a")
    for i in range(0, size):
        data = generator()
        query = ("INSERT INTO request(agentID, documentID, approval, direction) "
                 f"VALUES (\"{data['agentID']}\", \"{data['documentID']}\", TRUE, \"{direction}\");")
        f.write(query+"\n")
        cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    f.close()
def randomInListInsertion(listID, size):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(f"SELECT agentID FROM request WHERE listID={listID};")
    ownerCode = cursorToList(cursor)
    ownerCode = ownerCode[0]
    generatorIn = lambda : dict(listID=listID, freightID=randomFreightID(ownerCode),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=True,
                              origin=(random.choice(originList)))
    for i in range(0, size):
        insertInList(generatorIn())
def randomOutListInsertion(listID, size):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    generatorOut = lambda : dict(listID=listID, freightID=random.choice(getInFreight()),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=False,
                              origin=(random.choice(originList)))
    for i in range(0, size):
        insertOutList(generatorOut())

lastestID = getAllListID()
lastestID = lastestID[-1]
addAmt = 20
randomRequest("IN", size=addAmt)
for i in range(0,addAmt):
    lastestID += 1
    randomInListInsertion(lastestID, 30)
randomRequest("OUT", size=addAmt)
for i in range(0,addAmt):
    lastestID += 1
    randomOutListInsertion(lastestID, 20)