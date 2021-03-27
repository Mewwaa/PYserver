# Car's functions
# -----------------------------------------------
def deleteAllCars(mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM cars;"
    deleting = mycursor.execute(sqlQuery)
    mydb.commit()
    return deleting

def showAllCars(mydb):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM cars'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    return results

def addNewCar(carname, brandname, carhp, enginecapacity,manufacturedate,mydb):
    mycursor = mydb.cursor()
    newCar = "INSERT INTO CARS (NAME, BRAND, HP, ENGINE_CAPACITY,MANUFACTURE_DATE) VALUES (%s, %s, %s, %s, %s)" 
    newCarValues = (carname, brandname, carhp, enginecapacity,manufacturedate)
    adding = mycursor.execute(newCar, newCarValues)   
    mydb.commit()
    return adding

def deleteCarsById(id, mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM cars WHERE CAR_ID = {}".format(id)
    deleting = mycursor.execute(sqlQuery,id)
    mydb.commit()
    return deleting
# -----------------------------------------------

# User's functions
# -----------------------------------------------
def addNewUser(name, surname, pesel, mydb):
    mycursor = mydb.cursor()
    newUser = "INSERT INTO USER (NAME, SURNAME, PESEL) VALUES (%s, %s, %s)" 
    newUserValues = (name, surname, pesel)
    adding = mycursor.execute(newUser, newUserValues)   
    mydb.commit()
    return adding

def deleteAllUsers(mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM user;"
    deleting = mycursor.execute(sqlQuery)
    mydb.commit()
    return deleting

def showAllUsers(mydb):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM user'
    mycursor.execute(sql)
    showing = mycursor.fetchall()
    return showing

def deleteUserById(id, mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM user WHERE USER_ID = {}".format(id)
    deleting = mycursor.execute(sqlQuery,id)
    mydb.commit()
    return deleting

def deleteUserByPesel(pesel, mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM user WHERE PESEL = {}".format(pesel)
    deletingbypesel = mycursor.execute(sqlQuery,pesel)
    mydb.commit()
    return deletingbypesel

def checkIfUserExists(pesel,mydb):
    mycursor = mydb.cursor(buffered=True)
    checkIfUserExist = "Select * from user where user.PESEL={}".format(pesel)
    mycursor.execute(checkIfUserExist)
    result = mycursor.fetchone()   
    return result
# -----------------------------------------------

# Rental's functions
# -----------------------------------------------
def addNewRental(carId, userId, mydb):
    mycursor = mydb.cursor()
    newRental = "INSERT INTO RENTAL (CAR_ID, USER_ID) VALUES (%s, %s)" 
    newRentalValues = (carId, userId)
    adding = mycursor.execute(newRental, newRentalValues)   
    mydb.commit()
    return adding

def showAllRentals(mydb):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM RENTAL'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    return results

def deleteAllRentals(mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM RENTAL;"
    deleting = mycursor.execute(sqlQuery)
    mydb.commit()
    return deleting

def deleteRentalById(id, mydb):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM rental WHERE RENTAL_ID = {}".format(id)
    deleting = mycursor.execute(sqlQuery,id)
    mydb.commit()
    return deleting
# -----------------------------------------------