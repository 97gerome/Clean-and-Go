# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:18:02 2018

@author: Gerome Mandapat
"""

from DAL.DataAccess import Data_access

class Login_logic(object):
    
    def __init__(self):
        print ("init")
    
    def check_pw(self, uPass, uLine):
        DA_pass = Data_access()
        passw = DA_pass.get_pw(uLine)
        if uPass == passw:
            return 1
        else:
            return 0
    def check_user(self, uLine):
        DA_user = Data_access()
        user = DA_user.get_user(uLine)
        if user is None:
            return 0
        else:
            return 1
        
        #print(cursor.fetchone()[1])
