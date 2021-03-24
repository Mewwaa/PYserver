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