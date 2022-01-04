from mysql.connector import (connection)
cnx = connection.MySQLConnection(user='root', password='20019', host='127.0.0.1', database='portmanagementdb')
cursor = cnx.cursor()
def getInFreight(cursor):
    query = ("SELECT listID, freightID FROM list "
             "WHERE freightDirection = TRUE;")
    cursor.execute(query)
    resList = []
    for i in cursor:
        resList.append(i)
    return resList
def insertInList(cursor, instance):
    addFreightQuery = ("INSERT INTO list(listID, freightID, freightTypeID, targetID, freightDirection, origin) "
                       "VALUES (%(listID)s, %(freightID)s, %(freightTypeID)s,"
                       "%(targetID)s, %(freightDirection)s, %(origin)s);"
                       )
    cursor.execute(addFreightQuery, instance)
def deleteFreight(cursor, freightID):
    dropFreight = (f"DELETE FROM list WHERE freightID='{freightID}';")
    cursor.execute(dropFreight)
instance = {
    'listID': "1",
    'freightID': "CMSU7773080",
    'freightTypeID': 1000,
    'targetID':"20G0",
    'freightDirection':True,
    'origin':"Lunarian"
    }
#insertInList(cursor, instance)
deleteFreight(cursor, "CMSU7773080")
#cnx.commit()
cnx.close()
