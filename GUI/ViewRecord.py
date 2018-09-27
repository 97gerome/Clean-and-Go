# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lemue\Desktop\MAPUA\COE125\Clean-and-Go-master\ViewRecord.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewRecord(object):
    def setupUi(self, ViewRecord):
        ViewRecord.setObjectName("ViewRecord")
        ViewRecord.resize(894, 329)
        self.tableWidget = QtWidgets.QTableWidget(ViewRecord)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 861, 221))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ViewRecord)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 361, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblSearch = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblSearch.setObjectName("lblSearch")
        self.horizontalLayout.addWidget(self.lblSearch)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_GoSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_GoSearch.setObjectName("pushButton_GoSearch")
        self.horizontalLayout.addWidget(self.pushButton_GoSearch)
        self.pushButton_Back = QtWidgets.QPushButton(ViewRecord)
        self.pushButton_Back.setGeometry(QtCore.QRect(690, 270, 75, 23))
        self.pushButton_Back.setObjectName("pushButton_Back")

        self.retranslateUi(ViewRecord)
        QtCore.QMetaObject.connectSlotsByName(ViewRecord)

    def retranslateUi(self, ViewRecord):
        _translate = QtCore.QCoreApplication.translate
        ViewRecord.setWindowTitle(_translate("ViewRecord", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewRecord", "Owner"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewRecord", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ViewRecord", "Total Cost"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ViewRecord", "Date Received"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ViewRecord", "Order Number"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ViewRecord", "Pick-up or Delivery"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ViewRecord", "Pick-up Date"))
        self.lblSearch.setText(_translate("ViewRecord", "Search:"))
        self.pushButton_GoSearch.setText(_translate("ViewRecord", "Go"))
        self.pushButton_Back.setText(_translate("ViewRecord", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewRecord = QtWidgets.QDialog()
    ui = Ui_ViewRecord()
    ui.setupUi(ViewRecord)
    ViewRecord.show()
    sys.exit(app.exec_())

