# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(400, 264)
        self.username_line = QtWidgets.QLineEdit(Dialog)
        self.username_line.setGeometry(QtCore.QRect(140, 100, 231, 20))
        self.username_line.setObjectName("username_line")
        self.password_line = QtWidgets.QLineEdit(Dialog)
        self.password_line.setGeometry(QtCore.QRect(140, 140, 231, 20))
        self.password_line.setObjectName("password_line")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 210, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 100, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        
        self.conn = sqlite3.connect("Laundrys.db")  
        self.cursor = self.conn.cursor()
        
        self.loginButton.clicked.connect(self.loginClicked)
                

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        

    def loginClicked(self,Dialog):
        uname = (self.username_line.text(),)
        
        self.cursor.execute('SELECT * FROM Accounts WHERE Username=?', uname)
        
        if self.password_line.text() == self.cursor.fetchone()[1]:
            loginSuccess = QMessageBox()
            loginSuccess.setIcon(QMessageBox.Information)
            loginSuccess.setText("Welcome")
            loginSuccess.setStandardButtons(QMessageBox.Ok)
            loginSuccess.exec_()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

