
#Author: Group- Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: BusinessLogic


import sys
sys.path.append('C:/GitHub/Clean-and-Go/') #change this on another pc

from DAL.DataAccess import AccessData

class Record(object):
    def __init__(self):
        self.owner = ""
        self.weight = 0
        self.cost = 0
        self.dateReceived = ""
        self.orderNumber = 0
        self.pickupOrDelivery = ""

    def getValues(self, owner, weight, date, pickupOrDelivery):
        self.owner = owner
        self.weight = int(weight)
        self.cost = self.calculateCost(self.weight)
        self.dateReceived = date
        self.orderNumber = self.getOrderNumber()
        self.pickupOrDelivery = pickupOrDelivery
        print("got it all")

        print("Owner: ",self.owner)
        print("Weight: ",self.weight)
        print("Cost: ",self.cost)
        print("Date of Order: ",self.dateReceived)
        print("Order Number: ", self.orderNumber)
        print("Pick-up or Delivery: ",self.pickupOrDelivery)
        print('\n')

    def calculateCost(self, weight):
        if weight <= 5:
            cost = 50* weight
        if weight > 5:
            cost = 40*weight
        return cost

    def getOrderNumber(self):
        readOrderNumber = AccessData()
        readOrderNumber.readFromLaundry()
        print("got the table")
        for rowNumber, rowData in enumerate(readOrderNumber.laundryTableData):
            for columnNumber, data in enumerate(rowData):
                #For Debugging
                #print("rowNumber: ",rowNumber)
                #print("columnNumber: ",columnNumber)
                #print("data: ",data)
                if columnNumber == 4:
                    orderNumber = data
                    #print("got data: ", orderNumber) -> debug
        newOrderNumber = orderNumber + 1
        return newOrderNumber






