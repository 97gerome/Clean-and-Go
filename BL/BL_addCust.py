# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:34:50 2018

@author: Gerome Mandapat
"""

import sys
sys.path.append('../') #change this on another pc
from DAL.DAL_Customer import DAL_Customer
class BL_addCust(object):
    
    def __init__(self):
        print("init")
        self.db = DAL_Customer()
    def customerValues(self, name, contact, email, address):
        data = (name, contact, email, "", address, self.checkID())
        self.db.writeData(data)
        
    def checkID(self):
        if self.db.getID() == 1:
            return 1
        else:
            return self.db.getID() + 1