import mariadb as db
import sys
import os


#Connect to MariaDB Platform
try:
    conn = db.connect(
    user = '2010084_mvs0106',
    port = 3306,
    password = 'eduConnect+',
    host = '207.246.248.19',
    database = '2010084_mvs01062023',
    autocommit = True
    )
    print("Connected to MariaDB Platform")
except db.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


#Get cursor
cur0 = conn.cursor()
cur1 = conn.cursor()


#Returns a List of columns
def getColumnList():
    listColumns = []
    cur0.execute("DESCRIBE shield_db")
    for i in cur0:
        listColumns.append(i[0])
    #print(listColumns)
    return listColumns

listColumns = getColumnList()


#Function to get all records from the database
def getAllRecords():
    cur1.execute("SELECT * FROM shield_db")
    records = cur1.fetchall()
    print(records)
    return records


#Returning JSON object having all data of a user from the user ID
def getUserInfo(userId):
    cur1.execute("SELECT * from shield_db WHERE userId = ?", (userId,))
    records = cur1.fetchall()
    print(records)
    dictAll = {}
    if(len(records) != 0):
        for i in range(0, len(records[0])):
            dictAll[listColumns[i]] = records[0][i]
    print(dictAll)
    return dictAll


#Function to create a record in the database
#Arguments: {"username": "user", "userEmail": "xyz@abc", "userPassword": "pw"}
def createRecord(jsonData):
    listData = tuple(jsonData.values())
    print(listData)

    try:
        cur1.execute("INSERT INTO shield_db (username, userEmail, userPassword) VALUES (%s, %s, %s)", listData)
        print("Record inserted successfully")
        return 200
    except db.Error as e:
        print(f"Error: {e}")
        #Return an error code for duplicate entry
        sys.exit(1)


#Function to update a record in the database
#Arguments: {"userID": 1, "username": "user", "userEmail": "xyz@abc", "userPassword": "pw"}
def updateRecord(jsonData):
    listData = list(jsonData.values())
    print(listData)
    listData.append(listData[0])
    listData.pop(0)
    print(listData)

    try:
        cur1.execute("UPDATE shield_db SET username = %s, userEmail = %s, userPassword = %s WHERE userID = %s", listData)
        print("Record updated successfully")
        return 200
    except db.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


#Function to delete a record in the database
def deleteRecord(userID):
    try:
        cur1.execute("DELETE FROM shield_db WHERE userId = ?", (userID,))
        print("Record deleted successfully")
        return 200
    except db.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


def verifyUser(username, userPassword):
    print(username, userPassword)
    cur1.execute("SELECT * FROM shield_db WHERE username = ?", (username,))
    records = cur1.fetchall()
    if(len(records)!=0):
        if records[0][3] == userPassword:
            print("Successful Login")
            return 200
        else:
            print("Incorrect password")
            return 401 #Invalid password
    else:
        print("User doesn't exist")
        return 400 #User doesn't exist
    
