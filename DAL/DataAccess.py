#Author: Group-Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: ViewRecord

import sqlite3


class AccessData(object):
    def __init__(self):
        self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")# change this path to "..\Database\Laundry.db"

    def readFromLaundry(self):
        #self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")
        self.laundryTableData = self.connectorDB.execute('SELECT * FROM Laundry')


    def writeToLaundry(self, owner, weight, cost, date, orderNumber,pickupOrDelivery):
        cursor = self.connectorDB.cursor()
        ins ='''INSERT INTO Laundry(owner, weight, cost, date, orderNumber, pickupOrDelivery) VALUES(?,?,?,?,?,?)'''
        laundryTableData = self.connectorDB.execute('SELECT * FROM Laundry')



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


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewRecord = QtWidgets.QDialog()
    viewer = Ui_ViewRecord()
    viewer.setupUi(ViewRecord)
    ViewRecord.show()
    sys.exit(app.exec_())

AccessData = DataAccess()
AccessData.ReadData()
viewer.
'''