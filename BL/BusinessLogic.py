
#Author: Group- Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: BusinessLogic


import sys
sys.path.append('../') #change this on another pc

from DAL.DataAccess import Data_access

class Record(object):
    def __init__(self):
        self.owner = ""
        self.weight = 0
        self.cost = 0
        self.dateReceived = ""
        self.orderNumber = 0
        self.pickupOrDelivery = ""
        self.service = ""
        self.balance = 0


    def getValues(self, owner, weight, date, pickupOrDelivery, handWash, machineWash, dryClean, fold, press, paid, amount):
        print("getValues here")
        self.owner = owner
        self.weight = int(weight)
        self.cost = self.calculateCost(self.weight)
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
        data = (self.owner, self.weight, self.cost, self.dateReceived, self.orderNumber, self.pickupOrDelivery,self.service, self.balance)
        print(data)
        database = Data_access()

        #print("data: ",data)
        #database.writeToLaundry(self.owner,self.weight,self.cost,self.dateReceived,self.orderNumber,self.pickupOrDelivery)
        #print("got it all")

    def calculateCost(self, weight):
        if weight <= 4:
            cost = 50* weight
        if weight >= 5:
            cost = 40*weight
        return cost

    def getOrderNumber(self):
        readOrderNumber = Data_access()
        readOrderNumber.readFromLaundry()
        for rowNumber, rowData in enumerate(readOrderNumber.laundryTableData):
            for columnNumber, data in enumerate(rowData):
                if columnNumber == 4:
                    orderNumber = data
        newOrderNumber = orderNumber + 1
        return newOrderNumber

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
        print("date")
        return dateFormat

    def calculateBalance(self, payment, cost):
        balance = cost - payment
        return balance