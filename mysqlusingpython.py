from mysql.connector import (connection)
import datetime
import random
def getInFreight(cursor):
    query = ("SELECT listID, freightID FROM list "
             "WHERE freightDirection = TRUE;")
    resList = []
    cursor.execute(query)
    for i in cursor:
        resList.append(i)
    return resList
def isFreightHere(cursor, freightID):
    query = (f"select freightID from list where freightID = '{freightID}';")
    i = cursor.execute(query)
    return i == None
def insertInList(cursor, instance):
    xLim = 10
    yLim = 10
    stackMax = 10
    if instance['freightDirection'] == False or isFreightHere(cursor, instance['freightID']) != True :
        return
    addFreightQuery = ("INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) "
                       "VALUES (%(listID)s, %(freightID)s, %(freightTypeID)s,"
                       "%(targetID)s, %(freightDirection)s, %(origin)s);"
                       )
    cursor.execute(addFreightQuery, instance)
    addFreightQuery = ("INSERT INTO freight(inListID, freightID, arrivalTime, areaID,locX, locY, stackLvl) "
                       "VALUES (%s, %s, now(), %s,%s, %s, %s);")
    data = (instance['listID'], instance['freightID'], random.choice('ABCD'),
            random.randint(0,xLim),random.randint(0,yLim), random.randint(0,stackMax))
    cursor.execute(addFreightQuery, data)


def deleteFreight(cursor, freightID):
    dropFreight = (f"DELETE FROM list WHERE freightID='{freightID}';")
    cursor.execute(dropFreight)

cnx = connection.MySQLConnection(user='root', password='20019', host='127.0.0.1', database='portmanagementdb')
cursor = cnx.cursor(buffered=True)
instance = {
    'listID': "1",
    'freightID': "CMSU7773080",
    'freightTypeID': 1000,
    'targetID':"20G0",
    'freightDirection':True,
    'origin':"Lunarian"
    }

#deleteFreight(cursor, "CMSU7773080")
insertInList(cursor, instance)
print(getInFreight(cursor))


#cnx.commit()
cnx.close()
