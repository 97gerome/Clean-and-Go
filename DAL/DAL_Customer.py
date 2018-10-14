# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:44:52 2018

@author: Gerome Mandapat
"""

import sqlite3

class DAL_Customer(object):
    
    
    def __init__(self):
        #path = "C:\\Users\\Gerome Mandapat\\Desktop\\CAG\\Clean-and-Go\\Database\\Laundry.db"
        path = '../Database/Laundry.db'
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        
    def writeData(self, data):
        ins = "INSERT INTO Customers VALUES(?,?,?,?,?,?)"
        cursor = self.conn.cursor()
        cursor.execute(ins,data)
        self.conn.commit()
        self.closeDB()
        
    def closeDB(self):
        self.conn.close()
        
    def getID(self):
        if self.cursor.rowcount == 0:
            return 1
        else:
            highid = self.conn.execute('SELECT id FROM Customers ORDER BY id DESC LIMIT 1')
            highestid = highid.fetchone()[0]
            return highestid
    def getAll(self):
        allcust = self.conn.execute('SELECT * FROM Customers')
        customers = allcust.fetchall()
        return customers

test = DAL_Customer()
print(test.getAll())