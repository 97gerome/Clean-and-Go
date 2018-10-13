
#Author: Group- Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: BusinessLogic


import sys
sys.path.append('../') #change this on another pc
from DAL.DAL_record import DAL_record
from PyQt5.QtWidgets import QMessageBox
class BL_record(object):
   def __init__(self):
        self.owner = "None"
        self.weight = 0
        self.cost = 0
        self.dateReceived = "N/A"
        self.orderNumber = 0
        self.pickupOrDelivery = "N/A"
        self.service = "None"
        self.balance = 0
        self.dateCompleted = "NA"

   def getValues(self, owner, weight, date, pickupOrDelivery, handWash, machineWash, dryClean, fold, press, paid, amount):
        print("getValues here")
        self.owner = owner
        self.weight = int(weight)
        self.cost = self.calculateCost(self.weight, handWash, machineWash, dryClean, fold, press)
        self.dateReceived = date
        self.orderNumber = self.getOrderNumber()
        self.pickupOrDelivery = pickupOrDelivery
        print("before services")
        service1 = ""
        service2 = ""
        service3 = ""
        if handWash == True:
            service1 = "Hand Wash"
        if machineWash == True:
            service1 = "Machine Wash"
        if dryClean == True:
            service1 = "Dry Clean"
        if fold == True:
            service2 = ", Fold"
        if press == True:
            service3 = ", Press"
        if paid == False:
            self.balance = self.calculateBalance(amount, self.cost)
        elif paid == True:
            self.balance = 0
        if self.balance == 0:
            self.payment = "Paid"
        else:
            self.payment = "Balance needs to be paid"

        self.service = service1 + service2 + service3

        data = (self.owner, self.weight,self.service, self.cost, self.dateReceived, self.orderNumber, self.pickupOrDelivery,self.balance, "Ongoing", self.dateCompleted)#self.service, self.balance)
        database = DAL_record()
        database.writeToLaundry(data)

   def calculateCost(self, weight, handWash, machineWash, dryClean, pressService, foldService):
       washCost = 0
       pressCost = 0
       foldCost = 0

       #hand wash cost calculation
       if handWash == True:
            if weight <= 4:
                washCost = 75*weight
            if weight > 4:
                washCost = 60*weight

       #machine wash cost calculation
       if machineWash == True:
            if weight <= 4:
                washCost = 50 * weight
            if weight > 4:
                washCost = 40 * weight

       # Dry Clean cost calculation
       if dryClean == True:
           piece = weight
           if piece <= 5:
               washCost = 100 * piece
           if piece > 5:
               washCost = 80 * piece

       #other services cost calculation
       if pressService == True:
            pressCost = weight * 20

       if foldService == True:
            foldCost = 0

       #Total Cost of Services
       cost = washCost + pressCost + foldCost
       return cost

   def getOrderNumber(self):
        newOrderNumber = 0
        orderNumber = 0
        readOrderNumber = DAL_record()
        laundryTableData = readOrderNumber.readFromLaundry()
        for rowNumber, rowData in enumerate(laundryTableData):
            for columnNumber, data in enumerate(rowData):
                if columnNumber == 5: #column number of order number
                    orderNumber = data
                    print(data)
        newOrderNumber = orderNumber + 1
        return newOrderNumber

   #Get Present Date
   def getDate(self):
        import datetime
        date = datetime.datetime.now()
        dateMM = str(date.month)
        dateDD = str(date.day)
        if date.month < 10:
            dateMM = "0" + dateMM
        if date.day < 10:
            dateDD = "0" + dateDD
        dateYYYY = str(date.year)
        dateFormat = dateMM + "/" + dateDD + "/" + dateYYYY
        return dateFormat

   def calculateBalance(self, payment, cost):
        balance = cost - payment
        return balance

   def getTableLaundry(self,status):
        dataTable = DAL_record()
        laundryData =dataTable.readLaundry(status)
        return laundryData

   def changeStatus(self,orderNumber):
       balance = self.checkBalance(orderNumber)
       msgBox = QMessageBox()
       if balance[0] == 0:
           msgBox.setIcon(QMessageBox.Information)
           msg = "No balance remaining. Status Changed."
           status = DAL_record()
           date = self.getDate()
           status.updateStatus(orderNumber,date)
       else:
           msgBox.setIcon(QMessageBox.Warning)
           msg = "Please pay remaining balance! Status not changed."
       msgBox.setText(msg)
       msgBox.setWindowTitle("Status Message")
       msgBox.addButton('Ok', QMessageBox.YesRole)
       msgBox.exec()

   def checkBalance(self,orderNumber):
       getBalance = DAL_record()
       return getBalance.readBalance(orderNumber)
   def closeDB(self, dataTable):
       dataTable.closeDB()