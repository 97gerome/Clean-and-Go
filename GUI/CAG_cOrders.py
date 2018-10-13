# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_cOrders.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from BL.BL_record import BL_record
sys.path.append('../')

class Ui_completedOrders(object):
    def setupUi(self, completedOrdersUI, CAG_main):
        completedOrdersUI.setObjectName("Dialog")
        completedOrdersUI.resize(817, 279)
        self.tableWidget = QtWidgets.QTableWidget(completedOrdersUI)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 801, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.ownerDetails_Button = QtWidgets.QPushButton(completedOrdersUI)
        self.ownerDetails_Button.setGeometry(QtCore.QRect(10, 240, 121, 31))
        self.ownerDetails_Button.setObjectName("ownerDetails_Button")

        self.pushButton_Back = QtWidgets.QPushButton(completedOrdersUI)
        self.pushButton_Back.setGeometry(QtCore.QRect(150, 240, 121, 31))
        self.pushButton_Back.setObjectName("pushButton_Back")

        self.retranslateUi(completedOrdersUI)
        QtCore.QMetaObject.connectSlotsByName(completedOrdersUI)
        self.pushButton_Back.clicked.connect(lambda: self.backToMain(completedOrdersUI, CAG_main))
        self.ownerDetails_Button.clicked.connect(lambda: self.viewCustomer(self.tableWidget.currentRow()))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Completed Orders"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Owner"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Cost"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Date received"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Services"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Order Number"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Pick Up/Delivery"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Date Completed"))
        self.ownerDetails_Button.setText(_translate("Dialog", "View Owner Details"))

        self.pushButton_Back.setText(_translate("ViewRecord", "Go Back"))
        self.DisplayData()

    def DisplayData(self):
        x = BL_record()
        status = "Done"
        dataTable = x.getTableLaundry(status)
        for rowNumber, rowData in enumerate(dataTable):
            self.tableWidget.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                if columnNumber != 7:
                    self.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
                if columnNumber >= 8:
                    self.tableWidget.setItem(rowNumber, columnNumber-2, QtWidgets.QTableWidgetItem(str(data)))

    def viewCustomer(self, currentRow):
        customerName = self.tableWidget.item(currentRow,0).text()
        print(customerName)

    def backToMain(self, completedOrdersUI, CAG_main):
        CAG_main.show()
        completedOrdersUI.close()