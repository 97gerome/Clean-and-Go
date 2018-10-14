# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 03:13:26 2018

@author: Gerome Mandapat
"""

import sqlite3

class DAL_viewCust(object):
    def __init__(self):
        path = '../Database/Laundry.db'
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
    def getOrders(self, name):
        n = (name,)
        allorders = self.conn.execute('SELECT OrderNumber, Weight, TotalCost, DateReceived, ClaimMode, DateCompleted  FROM Laundry WHERE Owner=?', n)
        return allorders.fetchall()
    def testOrder(self, name):
        n = (name,)
        allorders = self.conn.execute('SELECT OrderNumber, Weight, TotalCost, DateReceived, ClaimMode, DateCompleted  FROM Laundry WHERE Owner=?', n)
        return allorders.fetchone()