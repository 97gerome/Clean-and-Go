# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_viewCustomers.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox
import sys
sys.path.append('../')
from BL.BL_viewCust import BL_viewCust

class Ui_viewCustomers(object):
    def setupUi(self, viewCustomers, CAG_main):
        viewCustomers.setObjectName("Dialog")
        viewCustomers.resize(660, 457)
        self.groupBox = QtWidgets.QGroupBox(viewCustomers)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 641, 441))
        self.groupBox.setObjectName("groupBox")
        self.searchLine = QtWidgets.QLineEdit(self.groupBox)
        self.searchLine.setGeometry(QtCore.QRect(80, 30, 221, 20))
        self.searchLine.setObjectName("searchLine")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.goButton = QtWidgets.QPushButton(self.groupBox)
        self.goButton.setGeometry(QtCore.QRect(320, 30, 75, 23))
        self.goButton.setObjectName("goButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 621, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 601, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.textName = QtWidgets.QLabel(self.groupBox)
        self.textName.setGeometry(QtCore.QRect(20, 70, 161, 16))
        self.textName.setText("")
        self.textName.setObjectName("textName")
        self.textContact = QtWidgets.QLabel(self.groupBox)
        self.textContact.setGeometry(QtCore.QRect(20, 100, 161, 16))
        self.textContact.setText("")
        self.textContact.setObjectName("textContact")
        self.textEmail = QtWidgets.QLabel(self.groupBox)
        self.textEmail.setGeometry(QtCore.QRect(200, 70, 421, 16))
        self.textEmail.setText("")
        self.textEmail.setObjectName("textEmail")
        self.textAddress = QtWidgets.QLabel(self.groupBox)
        self.textAddress.setGeometry(QtCore.QRect(200, 100, 421, 16))
        self.textAddress.setText("")
        self.textAddress.setObjectName("textAddress")
        self.closeButton = QtWidgets.QPushButton(self.groupBox)
        self.closeButton.setGeometry(QtCore.QRect(540, 410, 91, 23))
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(viewCustomers)
        QtCore.QMetaObject.connectSlotsByName(viewCustomers)
        self.closeButton.clicked.connect(lambda: self.backMain(viewCustomers, CAG_main))
        self.goButton.clicked.connect(lambda: self.search())
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Customers"))
        self.label.setText(_translate("Dialog", "Search"))
        self.goButton.setText(_translate("Dialog", "Go"))
        self.groupBox_2.setTitle(_translate("Dialog", "Order History"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Order Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Date Received"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Pick Up/Delivery"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Date Completed"))
        self.closeButton.setText(_translate("Dialog", "Close"))
    
    def backMain(self, viewCustomers, CAG_main):
        CAG_main.show()
        viewCustomers.close()
        
    def DisplayData(self):
        x = BL_viewCust()
        dataTable = x.getCustomer()
        for rowNumber, rowData in enumerate(dataTable):
            self.tableWidget.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                if columnNumber < 5:
                    self.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
                    
    def search(self):
        x = BL_viewCust()
        if self.searchLine.text() == "":
            nfound = QMessageBox()
            nfound.setIcon(QMessageBox.Information)
            nfound.setText("Please fill up the search line.")
            nfound.setWindowTitle("Empty search line")
            nfound.setStandardButtons(QMessageBox.Ok)
            nfound.exec_()
        elif x.checkPresence(self.searchLine.text()) == 0:
            nfound = QMessageBox()
            nfound.setIcon(QMessageBox.Information)
            nfound.setText("User not found in database.")
            nfound.setWindowTitle("Search failed")
            nfound.setStandardButtons(QMessageBox.Ok)
            nfound.exec_()
            
        else:
            data = x.getOrders(self.searchLine.text())
            for rowNumber, rowData in enumerate(data):
                self.tableWidget.insertRow(rowNumber)
                for columnNumber, data in enumerate(rowData):
                    if columnNumber < 6:
                        self.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
