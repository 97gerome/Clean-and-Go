# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_addCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BL.BL_addCust import BL_addCust
sys.path.append('../')
class Ui_addCustomer(object):
    def setupUi(self, addCustomerUI, CAG_main):
        addCustomerUI.setObjectName("Dialog")
        addCustomerUI.resize(332, 389)
        self.groupBox = QtWidgets.QGroupBox(addCustomerUI)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 371))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setGeometry(QtCore.QRect(100, 300, 191, 20))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_Contact = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Contact.setGeometry(QtCore.QRect(100, 260, 191, 20))
        self.lineEdit_Contact.setObjectName("lineEdit_Contact")
        self.lineEdit_Name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Name.setGeometry(QtCore.QRect(100, 180, 191, 21))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Address = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Address.setGeometry(QtCore.QRect(100, 220, 191, 20))
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 121, 121))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.OK_button = QtWidgets.QPushButton(self.groupBox)
        self.OK_button.setGeometry(QtCore.QRect(100, 340, 91, 23))
        self.OK_button.setObjectName("OK_button")
        self.cancel_Button = QtWidgets.QPushButton(self.groupBox)
        self.cancel_Button.setGeometry(QtCore.QRect(200, 340, 91, 23))
        self.cancel_Button.setObjectName("cancel_Button")

        self.retranslateUi(addCustomerUI)
        QtCore.QMetaObject.connectSlotsByName(addCustomerUI)
        
        self.cancel_Button.clicked.connect(lambda: self.backtoMain(addCustomerUI, CAG_main))
        self.OK_button.clicked.connect(lambda: self.writeToCustomers())

    def retranslateUi(self, addCustomerUI):
        _translate = QtCore.QCoreApplication.translate
        addCustomerUI.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Customer"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Contact"))
        self.label_4.setText(_translate("Dialog", "Email"))
        self.OK_button.setText(_translate("Dialog", "Add"))
        self.cancel_Button.setText(_translate("Dialog", "Cancel"))
        
    def backtoMain(self, addCustomerUI, CAG_main):
        CAG_main.show()
        addCustomerUI.close()
        
    def writeToCustomers(self):
        name = self.lineEdit_Name.text()
        contact = self.lineEdit_Contact.text()
        email = self.lineEdit_email.text()
        address = self.lineEdit_Address.text()
        
        if self.lineEdit_Name.text() == "" or self.lineEdit_Contact.text() == "" or self.lineEdit_email.text() == "" or self.lineEdit_Address.text() == "":
            missing = QMessageBox()
            missing.setIcon(QMessageBox.Information)
            missing.setText("Please fill up all fields.")
            missing.setWindowTitle("Missing Fields")
            missing.setStandardButtons(QMessageBox.Ok)
            missing.exec_()
        else:
            rec = BL_addCust()
            rec.customerValues(name, contact, email, address)
            success = QMessageBox()
            success.setIcon(QMessageBox.Information)
            success.setText("Customer successfully added.")
            success.setWindowTitle("Add successful")
            success.setStandardButtons(QMessageBox.Ok)
            success.exec_()
            self.lineEdit_Name.setText("")
            self.lineEdit_Contact.setText("")
            self.lineEdit_email.setText("")
            self.lineEdit_Address.setText("")
        
        

