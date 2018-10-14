# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:09:06 2018

@author: Gerome Mandapat
"""
import sqlite3

class DAL_login(object):
    
    def __init__(self):
        print ("init")
        #path = "C:\\Users\\Gerome Mandapat\\Desktop\\CAG\\Clean-and-Go\\Database\\Laundry.db"
        path = '../Database/Laundry.db'
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        
    
    def get_pw(self, uLine):
        pw_cursor = self.conn.cursor()
        pw_cursor.execute('SELECT * FROM Accounts WHERE Username=?', uLine)
        pw = pw_cursor.fetchone()[1]
        
        return  pw
    def get_user(self, uLine):
        user_cursor = self.conn.cursor()
        user_cursor.execute('SELECT * FROM Accounts WHERE Username=?', uLine)
        return user_cursor.fetchone()