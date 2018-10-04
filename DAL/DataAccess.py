#Author: Group-Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: ViewRecord

import sqlite3


class Data_access(object):
    def __init__(self):
        self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")# change this path to "..\Database\Laundry.db"

    def readFromLaundry(self):
        #self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")
        self.laundryTableData = self.connectorDB.execute('SELECT * FROM Laundry')


    def writeToLaundry(self, owner,weight,cost,dateReceived,orderNumber,pickupOrDelivery):
        print("got here")
        #ins = "INSERT INTO Laundry VALUES(?,?,?,?,?,?)"
        self.laundryTableData = self.connectorDB.execute('SELECT * FROM Laundry')
        cursor = self.connectorDB.cursor()
        ################ERROR CAN'T INSERT DATA INTO TABLE##################################
        with self.connectorDB:
            cursor.execute("INSERT INTO Laundry VALUES(?,?,?,?,?,?)",(owner,weight,cost,dateReceived,orderNumber,pickupOrDelivery))
            self.closeDB()


    def closeDB(self):
        self.connectorDB.close()

    def printData(self):
        i = 0
        while i < self.length:
            print("Owner: ",self.Owner[i])
            print("Weight: ",self.Weight[i])
            print("Cost: ",self.TotalCost[i])
            print("Date of Order: ",self.DateReceived[i])
            print("Order Number: ", self.OrderNumber[i])
            print("Pick-up or Delivery: ",self.PickUpOrDelivery[i])
            print('\n')
            i = i + 1
