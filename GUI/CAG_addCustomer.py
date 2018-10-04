# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_addCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 389)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Customer"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Address"))
        self.label_3.setText(_translate("Dialog", "Contact"))
        self.label_4.setText(_translate("Dialog", "Email"))
        self.OK_button.setText(_translate("Dialog", "Add"))
        self.cancel_Button.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

