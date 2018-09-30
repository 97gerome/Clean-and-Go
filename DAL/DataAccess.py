#Author: Group-Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: ViewRecord

import sqlite3


class AccessData(object):
    def ReadfromLaundry(self):
        #Connect to database
        self.connectorDB = sqlite3.connect("C:\GitHub\Clean-and-Go\Laundry.db")
        self.laundryTableData = self.connectorDB.execute('SELECT * FROM Laundry')

    def CloseDB(self):
        self.connectorDB.close()

        '''
        #self.data1 = cursor1.fetchall()
        self.length = self.data1.__len__()
        self.Owner = [None] * length
        self.Weight = [0] * length
        self.TotalCost = [0] * length
        self.DateReceived = [None] * length
        self.OrderNumber = [None] * length
        self.PickUpOrDelivery = [None] * length

        #print(data1.__len__()) #number of items int the database
        x = 0
        while x < self.length:
            self.Owner[x] = data1[x][0]
            self.Weight[x] = data1[x][1]
            self.TotalCost[x] = data1[x][2]
            self.DateReceived[x] = data1[x][3]
            self.OrderNumber[x] = data1[x][4]
            self.PickUpOrDelivery[x] = data1[x][5]
            x = x + 1
        '''
    def PrintData(self):
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