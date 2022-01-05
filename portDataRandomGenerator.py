import random
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

def randomList(listID, ownerCode, size):
    query = "INSERT INTO list(freightID, listID, freightTypeID, targetID, freightDirection, origin) VALUES \n"
    for i in range(0, size):
        query += f"(\"{randomFreightID(ownerCode)}\",{listID}, 1000, \"20G0\", {random.choice(['TRUE', 'FALSE'])}, \"Gensokyo\")"
        query += ",\n"
    query += f"(\"{randomFreightID(ownerCode)}\",{listID}, 1000, \"20G0\",{random.choice(['TRUE', 'FALSE'])}, \"Gensokyo\");"
    return query