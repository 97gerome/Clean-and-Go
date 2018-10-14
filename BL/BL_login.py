# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:18:02 2018

@author: Gerome Mandapat
"""

from DAL.DAL_login import DAL_login

class BL_login(object):
    
    def __init__(self):
        #print ("init")
        passwd = ""
    
    def check_pw(self, uPass, uLine):
        DA_pass = DAL_login()
        passw = DA_pass.get_pw(uLine)
        if uPass == passw:
            return 1
        else:
            return 0
    def check_user(self, uLine):
        DA_user = DAL_login()
        user = DA_user.get_user(uLine)
        if user is None:
            return 0
        else:
            return 1
        