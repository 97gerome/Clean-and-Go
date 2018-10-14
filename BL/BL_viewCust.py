# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 02:26:45 2018

@author: Gerome Mandapat
"""

import sys
sys.path.append('../') #change this on another pc
from DAL.DAL_viewCust import DAL_viewCust

class BL_viewCust(object):
    def __init__(self):
        print("init")
    def getOrders(self, name):
        customer = DAL_viewCust()
        cust = customer.getOrders(name)
        return cust
    def checkPresence(self, name):
        customer = DAL_viewCust()
        testCust = customer.testOrder(name)
        print(testCust)
        if testCust is None:
            return 0
        else:
            return 1
        