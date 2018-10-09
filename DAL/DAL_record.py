#from ViewRecord import Ui_ViewRecord
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys
sys.path.append('../')


class DAL_record(object):
    
    def __init__(self):
        print ("init")
        path = "../Database/Laundry.db"
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()


    def readFromLaundry(self):
        #self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")
        self.laundryTableData = self.conn.execute('SELECT * FROM Laundry')
        #self.laundryTableData.fetchall()
        return self.laundryTableData.fetchall()

    def readOngoingLaumdry(self):
        isOngoing = ("Ongoing",)
        self.laundryOngoing = self.conn.execute('SELECT * FROM Laundry WHERE Status=?',isOngoing)
        return self.laundryOngoing.fetchall()

    def writeToLaundry(self,data):
        print("got here")
        ins = "INSERT INTO Laundry VALUES(?,?,?,?,?,?,?,?)"
        cursor = self.conn.cursor()
        cursor.execute(ins,data)
        self.conn.commit()
        self.closeDB()


    def closeDB(self):
        self.conn.close()

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
            
    
        
        #print(cursor.fetchone()[1])
        