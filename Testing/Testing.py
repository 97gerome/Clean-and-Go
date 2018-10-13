##TESTING

import sys
sys.path.append('../')
import unittest
from BL.BL_record import BL_record
from BL.BL_login import BL_login
from DAL.DAL_login import DAL_login

class Testing(unittest.TestCase):
    
#       record logic test
    def test_CalculateCost(self):
        x = 3
        y = 6
        rec = BL_record()
        print(rec.calculateCost(x))
        print(rec.calculateCost(y))
    def test_GetDate(self):
        rec = BL_record()
        date = rec.getDate()
        print(date)
        
    def test_calculateBalance(self):
        rec = BL_record()
        print(rec.calculateBalance(50,300))

    def test_getTableValue(self):
        rec = BL_record()
        print(rec.getTableValues)
        
    def test_closeDB(self):
        rec = BL_record()
        rec.closeDB()
        print("closed")

        
#       login logic test
    def test_check_pw(self):
        login = BL_login()
        uname = ("Gerome",)
        
        print(login.check_pw("grm",uname))
       
    def test_check_user(self):
        login = BL_login()
        uname = ("Gerome",)
        
        print(login.check_user(uname))

#       login access test

    def test_get_pw(self):
        login = DAL_login()
        uname = ("Gerome",)
        
        print (login.get_pw(uname))
        
    def test_get_user(self):
        login = DAL_login()
        uname = ("Gerome",)
        print (login.get_user(uname))
        
#DAL_record tests
    def test_readFromLaundry(self):
        readData = DAL_record()
        readData.readFromLaundry()
        print(readData.laundryTableData)
    def test_writeToLaundry(self):
        writeData = DAL_record()
        data = ("Lemuel Garcia",3,150,"10/05/2018",13,"Delivery",False)
        writeData.writeToLaundry(data)
        
        


"""MAIN"""
unittest.main()
