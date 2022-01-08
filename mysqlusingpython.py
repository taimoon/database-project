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
    addList = ("INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) "
                       "VALUES (%(listID)s, %(freightID)s, %(freightTypeID)s,"
                       "%(targetID)s, %(freightDirection)s, %(origin)s);"
                       )
    cursor.execute(addList, instance)
def insertInList(instance):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    xLim = 10
    yLim = 10
    stackMax = 10
    if instance['freightDirection'] == False or isFreightHere(cursor, instance['freightID']) == True:
        return False

    insertList(cursor, instance)
    addFreightQuery = ("INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) "
                       "VALUES (%s, %s, now(), %s,%s, %s, %s);")
    data = (instance['listID'], instance['freightID'], random.choice('ABCD'),
            random.randint(0,xLim),random.randint(0,yLim), random.randint(0,stackMax))
    cursor.execute(addFreightQuery, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True
def deleteFreight(freightID):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    dropFreight = (f"DELETE FROM freight WHERE freightID=\"{freightID}\";")
    cursor.execute(dropFreight)
    cnx.commit()
    cursor.close()
    cnx.close()
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
                       f"VALUES (%(freightID)s, now(), ({queryArrTime}),({queryInListID}), %(outListID)s);")
    cursor.execute(addHistoricalFreight, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    deleteFreight(instance['freightID'])


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
    addRequestQuery = ("INSERT INTO request(agentID, documentID, approval, direction) "
                       f"VALUES (%(agentID)s, %(documentID)s, TRUE, \"{direction}\");")
    generator = lambda : dict(agentID=random.choice(agentList),
                              documentID=''.join(random.choice('0123456789ABCDEF') for i in range(10)),
                              )
    for i in range(0, size):
        cursor.execute(addRequestQuery, generator())
    cnx.commit()
    cursor.close()
    cnx.close()
def randomInListInsertion(listID, size):
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
    cursor = cnx.cursor(buffered=True)
    f = open("port DB freight.sql", 'w')
    cursor.execute(f"SELECT agentID FROM request WHERE listID={listID};")
    ownerCode = cursorToList(cursor)
    ownerCode = ownerCode[0]
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    generatorIn = lambda : dict(listID=listID, freightID=randomFreightID(ownerCode),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=True,
                              origin=(random.choice(originList)))

    for i in range(0, size):
        insertInList(generatorIn())
    f.close()
def randomOutListInsertion(listID, size):
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    cursor = cnx.cursor(buffered=True)
    generatorOut = lambda : dict(listID=listID, freightID=random.choice(getInFreight()),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=False,
                              origin=(random.choice(originList)))
    for i in range(0, size):
        insertOutList(generatorOut())

lastestID = getAllListID()
lastestID = lastestID[-1]
addAmt = 10
randomRequest("IN", size=addAmt)
for i in range(0,addAmt):
    lastestID += 1
    randomInListInsertion(lastestID, 30)
randomRequest("OUT", size=addAmt)
for i in range(0,addAmt):
    lastestID += 1
    randomOutListInsertion(lastestID, 20)