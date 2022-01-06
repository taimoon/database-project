import random
from mysql.connector import (connection)
dbName = "portmanagementdb"
sqlPass = "20019"
def getAllCountry():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database='sakila')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT country FROM country")
    originList = []
    for i in cursor:
        originList.append(i[0])
    cursor.close()
    cnx.close()
    return originList
def getAllAgent():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT agentID FROM agent")
    agentList = []
    for i in cursor:
        agentList.append(i[0])
    cursor.close()
    cnx.close()
    return agentList
def getAllFreightType():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT freightTypeID FROM freightType")
    freightList = []
    for i in cursor:
        freightList.append(i[0])
    cursor.close()
    cnx.close()
    return freightList
def getAllTargetInfo():
    cnx = connection.MySQLConnection(user='root', password=sqlPass, host='127.0.0.1', database=dbName)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT agentID FROM agent")
    targetList = []
    for i in cursor:
        targetList.append(i[0])
    cursor.close()
    cnx.close()
    return targetList

alphabetDict ={}
starting = 10
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    alphabetDict[i] = starting
    starting = starting + 1
    if starting%11 == 0:
        starting = starting + 1
def getCheckDigit(ID):
    sum = 0
    digitIdx = 0
    length = len(ID)
    for i in range(0, length-1):
        ch = ID[i]
        if ch.isalpha():
            sum += alphabetDict[ch]*2**digitIdx
        elif ch.isdigit():
            sum += int(ch)*2**digitIdx
        digitIdx = digitIdx + 1
    if sum%11 > 9:
        return 0
    else:
        return sum%11

def checkFreightID(ID):
    return getCheckDigit(ID)==int(ID[-1])
def randomFreightID(ownerCode):
    freightID = str(ownerCode)
    freightID += "U"
    for i in range(0,6):
        freightID += str(random.randint(0,9))
    freightID += str(getCheckDigit(freightID+"0"))
    return freightID

originList = ["United States", "China", "Indonesian", "Philippines", "United Kingdom", "Europe", "Japan",
              "South Africa", "Yemen", "Canada", "German", "France", "Brazil", "South Korean",
              "Malaysia", "Thailand"]
freightTypeList = getAllFreightType()
targetList = getAllTargetInfo()

def randomList(listID, ownerCode, size):
    f = open("port DB freight.sql", 'w')
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    dataQuery= lambda : (f"(\"{randomFreightID(ownerCode)}\",{listID}, {random.choice(freightTypeList)}, \"{random.choice(targetList)}\", "
                 f"{random.choice(['TRUE', 'FALSE'])}, \"{random.choice(originList)}\")")
    for i in range(0, size):
        query += dataQuery()+",\n"
    query += dataQuery()+";"
    f.write(query)
    return query