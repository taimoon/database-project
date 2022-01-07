from mysql.connector import (connection)
sqlPass="20019"
cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='portmanagementdb')
cursor = cnx.cursor(buffered=True)
from portDataRandomGenerator import *



def getInFreight(cursor):
    query = ("SELECT freightID FROM freight;")
    resList = []
    cursor.execute(query)
    for i in cursor:
        resList.append(i[0])
    return resList
def isFreightHere(cursor, freightID):
    query = (f"select freightID from list where freightID = \'{freightID}\';")
    cursor.execute(query)
    i = cursor
    return i != None
def insertList(cursor, instance):
    addList = ("INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) "
                       "VALUES (%(listID)s, %(freightID)s, %(freightTypeID)s,"
                       "%(targetID)s, %(freightDirection)s, %(origin)s);"
                       )
    cursor.execute(addList, instance)
def insertInList(cursor, instance):
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
    return True
def deleteFreight(cursor, freightID):
    dropFreight = (f"DELETE FROM freight WHERE freightID=\"{freightID}\";")
    cursor.execute(dropFreight)
    cnx.commit()
def insertOutList(cursor, instance):
    if instance['freightDirection'] == True or isFreightHere(cursor, instance['freightID']) == False:
        return False
    insertList(cursor, instance)
    query = (f"SELECT arrivalTime, inListID FROM freight WHERE freightID=\"{instance['freightID']}\"")
    cursor.execute(query)
    temp = []
    for i in cursor:
        temp.append(i[0])
        temp.append(i[1])
    data = dict(freightID=instance['freightID'], arrivalTime=temp[0],inListID=temp[1], outListID=instance['listID'])
    addHistoricalFreight = ("INSERT INTO historicalFreight(freightID, departureTime, arrivalTime,inListID, outListID) "
                       "VALUES (%(freightID)s, now(), %(arrivalTime)s,%(inListID)s, %(outListID)s);")
    cursor.execute(addHistoricalFreight, data)
    deleteFreight(cursor, instance['freightID'])

originList = ["United States", "China", "Indonesian", "Philippines", "United Kingdom", "Europe", "Japan",
              "South Africa", "Yemen", "Canada", "German", "France", "Brazil", "South Korean",
              "Malaysia", "Thailand"]
agentList = getAllAgent()
freightTypeList = getAllFreightType()
targetList = getAllTargetInfo()
directionDomain = ['IN', 'OUT', 'INOUT']
def randomRequest(cursor, size, direction):
    addRequestQuery = ("INSERT INTO request(agentID, documentID, approval, direction) "
                       f"VALUES (%(agentID)s, %(documentID)s, TRUE, \"{direction}\");")
    generator = lambda : dict(agentID=random.choice(agentList),
                              documentID=''.join(random.choice('0123456789ABCDEF') for i in range(10)),
                              )
    for i in range(0, size):
        cursor.execute(addRequestQuery, generator())
def randomInListInsertion(listID, ownerCode, size):
    f = open("port DB freight.sql", 'w')
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    generatorIn = lambda : dict(listID=listID, freightID=randomFreightID(ownerCode),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=True,
                              origin=(random.choice(originList)))

    for i in range(0, size):
        insertInList(cursor,  generatorIn())
    f.close()
def randomOutListInsertion(listID, ownerCode, size):
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    cursor = cnx.cursor(buffered=True)
    generatorOut = lambda : dict(listID=listID, freightID=random.choice(getInFreight(cursor)),
                              freightTypeID=random.choice(freightTypeList),
                              targetID=random.choice(targetList),
                              freightDirection=False,
                              origin=(random.choice(originList)))
    for i in range(0, size):
        insertOutList(cursor, generatorOut())

'''sqlPass = input("key in the sql server password: ")'''

print(getInFreight(cursor))
randomRequest(cursor, 10, 'INOUT')
for i in range(0,10):
    randomInListInsertion(random.choice(getAllListID()), random.choice(agentList), 3)
print(getInFreight(cursor))
#cnx.commit()
cnx.close()
