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
        print("data fetched")
        return self.laundryTableData.fetchall()

    def readLaundry(self,requestedStatus):
        status = (requestedStatus, )
        self.laundryOngoing = self.conn.execute('SELECT * FROM Laundry WHERE Status=?',status)
        return self.laundryOngoing.fetchall()

    def readBalance(self,orderNumber):
        data = (orderNumber,)
        textCommand = "SELECT Balance FROM Laundry WHERE OrderNumber=?"
        balance = self.conn.execute(textCommand,data)

        return balance.fetchone()
    def writeToLaundry(self,data):
        #print("got here")
        ins = "INSERT INTO Laundry VALUES(?,?,?,?,?,?,?,?,?,?)"
        cursor = self.conn.cursor()
        cursor.execute(ins,data)
        self.conn.commit()
        self.closeDB()

    def updateStatus(self,orderNumber,date):
        print("DAL change stat")
        statusData = (orderNumber,)
        dateData = (date,orderNumber)
        statusChange = "UPDATE Laundry SET Status='Done' WHERE OrderNumber=?"
        dateCompleteChange = "UPDATE Laundry SET DateCompleted=? WHERE OrderNumber=?"
        self.cursor.execute(statusChange,statusData)
        self.cursor.execute(dateCompleteChange,dateData)
        self.conn.commit()
        self.closeDB()
        print("done")

    def closeDB(self):
        self.conn.close()

        