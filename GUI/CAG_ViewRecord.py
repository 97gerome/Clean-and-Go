#Author: Group- Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: ViewRecord
import sys
sys.path.append('../') #change this on another pc
from PyQt5 import QtCore, QtGui, QtWidgets
from DAL.DataAccess import Data_access
from CAG_Form import Ui_Form
#from CAG_main import Ui_CAG_main


class Ui_ViewRecord(object):
    def setupUi(self, ViewRecord,CAG_main):
        #self.CAG_main = QtWidgets.QMainWindow()
        #self.ui = Ui_CAG_main()
        #self.ui.setupUi(self.CAG_main)
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
        self.pushButton_addRequest = QtWidgets.QPushButton(ViewRecord)
        self.pushButton_addRequest.setGeometry(QtCore.QRect(600, 270, 75, 23))
        self.pushButton_addRequest.setObjectName("pushButton_addRequest")

        self.retranslateUi(ViewRecord)
        QtCore.QMetaObject.connectSlotsByName(ViewRecord)

        #Select tablerow
        #self.tableWidget.pressed(self.rowSelected)
        #self.pushButton_GoSearch.clicked.connect(self.DisplayData)

        self.pushButton_addRequest.clicked.connect(self.AddForm)
        self.pushButton_Back.clicked.connect(lambda: self.backToMain(ViewRecord,CAG_main))

    def retranslateUi(self, ViewRecord):
        _translate = QtCore.QCoreApplication.translate
        ViewRecord.setWindowTitle(_translate("ViewRecord", "Records"))
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
        self.pushButton_addRequest.setText(_translate("ViewRecord", "Add Request"))
        self.DisplayData()
    def DisplayData(self):
        x = Data_access()
        x.readFromLaundry()
        #Initialize table
        self.tableWidget.setRowCount(0)
        #Display database values into the QTable
        for rowNumber, rowData in enumerate(x.laundryTableData):
            self.tableWidget.insertRow(rowNumber)
            for columnNumber, data in enumerate(rowData):
                self.tableWidget.setItem(rowNumber, columnNumber, QtWidgets.QTableWidgetItem(str(data)))
        x.closeDB()

    #Function used to display request form
    def AddForm(self):
        Form = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setup(Form)
        Form.show()

    def rowSelected(self):
        print("row select")
    #Function used to exit the viewrecord ui
    def backToMain(self, ViewRecord, CAG_main):
        CAG_main.show()
        ViewRecord.close()
'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ViewRecord = QtWidgets.QDialog()
    ui = Ui_ViewRecord()
    ui.setupUi(ViewRecord)
    ViewRecord.show()
    ui.DisplayData()
    sys.exit(app.exec_())
'''

