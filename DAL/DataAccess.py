#from ViewRecord import Ui_ViewRecord
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys
sys.path.append('../')


class Data_access(object):
    
    def __init__(self):
        print ("init")
        path = "C:\\Users\\Gerome Mandapat\\Desktop\\CAG\\Clean-and-Go\\Database\\Laundry.db"
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        
    
    def get_pw(self, uLine):
        pw_cursor = self.conn.cursor()
        pw_cursor.execute('SELECT * FROM Accounts WHERE Username=?', uLine)
        pw = pw_cursor.fetchone()[1]
        print (pw)
        return  pw
    def get_user(self, uLine):
        user_cursor = self.conn.cursor()
        user_cursor.execute('SELECT * FROM Accounts WHERE Username=?', uLine)
        return user_cursor.fetchone()

    def readFromLaundry(self):
        #self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")
        self.laundryTableData = self.conn.execute('SELECT * FROM Laundry')
        #print(self.laundryTableData.fetchall())


    def writeToLaundry(self, owner,weight,cost,dateReceived,orderNumber,pickupOrDelivery):
        print("got here")
        #ins = "INSERT INTO Laundry VALUES(?,?,?,?,?,?)"
        self.laundryTableData = self.conn.execute('SELECT * FROM Laundry')
        cursor = self.conn.cursor()
        ################ERROR CAN'T INSERT DATA INTO TABLE##################################
        with self.conn:
            cursor.execute("INSERT INTO Laundry VALUES(?,?,?,?,?,?)",(owner,weight,cost,dateReceived,orderNumber,pickupOrDelivery))
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
        