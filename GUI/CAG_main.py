# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAG_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from CAG_ViewRecord import Ui_ViewRecord
from CAG_cOrders import Ui_completedOrders
from CAG_addCustomer import Ui_addCustomer
from CAG_viewCustomers import Ui_viewCustomers
class Ui_CAG_main(object):
    def setupUi(self, CAG_main, CAG_login):
        CAG_main.setObjectName("CAG_main")
        CAG_main.resize(751, 324)
        self.centralwidget = QtWidgets.QWidget(CAG_main)
        self.centralwidget.setObjectName("centralwidget")
        self.orders_button = QtWidgets.QPushButton(self.centralwidget)
        self.orders_button.setGeometry(QtCore.QRect(30, 240, 151, 31))
        self.orders_button.setObjectName("orders_button")
        self.cOrders_Button = QtWidgets.QPushButton(self.centralwidget)
        self.cOrders_Button.setGeometry(QtCore.QRect(210, 240, 151, 31))
        self.cOrders_Button.setObjectName("cOrders_Button")
        self.newCustomer_Button = QtWidgets.QPushButton(self.centralwidget)
        self.newCustomer_Button.setGeometry(QtCore.QRect(390, 240, 151, 31))
        self.newCustomer_Button.setObjectName("newCustomer_Button")
        self.viewCustomer_Button = QtWidgets.QPushButton(self.centralwidget)
        self.viewCustomer_Button.setGeometry(QtCore.QRect(570, 240, 151, 31))
        self.viewCustomer_Button.setObjectName("viewCustomer_Button")
        self.labelOrders = QtWidgets.QLabel(self.centralwidget)
        self.labelOrders.setGeometry(QtCore.QRect(30, 30, 151, 191))
        self.labelOrders.setText("")
        self.labelOrders.setObjectName("labelOrders")
        self.labelcOrders = QtWidgets.QLabel(self.centralwidget)
        self.labelcOrders.setGeometry(QtCore.QRect(210, 30, 151, 191))
        self.labelcOrders.setText("")
        self.labelcOrders.setObjectName("labelcOrders")
        self.labelCustomer = QtWidgets.QLabel(self.centralwidget)
        self.labelCustomer.setGeometry(QtCore.QRect(390, 30, 151, 191))
        self.labelCustomer.setText("")
        self.labelCustomer.setObjectName("labelCustomer")
        self.labelCustomers = QtWidgets.QLabel(self.centralwidget)
        self.labelCustomers.setGeometry(QtCore.QRect(570, 30, 151, 191))
        self.labelCustomers.setText("")
        self.labelCustomers.setObjectName("labelCustomers")
        CAG_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CAG_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CAG_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CAG_main)
        self.statusbar.setObjectName("statusbar")
        CAG_main.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(CAG_main)
        self.actionSettings.setObjectName("actionSettings")
        self.actionLog_Out = QtWidgets.QAction(CAG_main)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.actionExit = QtWidgets.QAction(CAG_main)
        self.actionExit.setObjectName("actionExit")
        self.action_Exit = QtWidgets.QAction(CAG_main)
        self.action_Exit.setObjectName("action_Exit")
        self.actionAbout = QtWidgets.QAction(CAG_main)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAccount.addAction(self.actionSettings)
        self.menuAccount.addAction(self.actionLog_Out)
        self.menuFile.addAction(self.action_Exit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        orderspix = QtGui.QPixmap("machine.png")
        self.labelOrders.setScaledContents(True)
        self.labelOrders.setPixmap(orderspix)
        
        completedpix = QtGui.QPixmap("completed.png")
        self.labelcOrders.setScaledContents(True)
        self.labelcOrders.setPixmap(completedpix)
        
        newpix = QtGui.QPixmap("new.png")
        self.labelCustomer.setScaledContents(True)
        self.labelCustomer.setPixmap(newpix)

        existpix = QtGui.QPixmap("existing.png")
        self.labelCustomers.setScaledContents(True)
        self.labelCustomers.setPixmap(existpix)

        self.retranslateUi(CAG_main)
        QtCore.QMetaObject.connectSlotsByName(CAG_main)
        
        self.orders_button.clicked.connect(lambda: self.viewRecord(CAG_main))
        self.cOrders_Button.clicked.connect(lambda: self.completedRecord(CAG_main))
        self.newCustomer_Button.clicked.connect(lambda: self.addCustomer(CAG_main))
        self.action_Exit.triggered.connect(lambda: self.closeMain(CAG_main))
        self.actionLog_Out.triggered.connect(lambda: self.logOut(CAG_main, CAG_login))
        self.viewCustomer_Button.clicked.connect(lambda: self.viewCustomers(CAG_main))

    def retranslateUi(self, CAG_main):
        _translate = QtCore.QCoreApplication.translate
        CAG_main.setWindowTitle(_translate("CAG_main", "MainWindow"))
        self.orders_button.setText(_translate("CAG_main", "Orders"))
        self.cOrders_Button.setText(_translate("CAG_main", "Completed Orders"))
        self.newCustomer_Button.setText(_translate("CAG_main", "New Customer"))
        self.viewCustomer_Button.setText(_translate("CAG_main", "View Customers"))
        self.menuAccount.setTitle(_translate("CAG_main", "Account"))
        self.menuFile.setTitle(_translate("CAG_main", "File"))
        self.menuHelp.setTitle(_translate("CAG_main", "Help"))
        self.actionSettings.setText(_translate("CAG_main", "Settings"))
        self.actionLog_Out.setText(_translate("CAG_main", "Log Out"))
        self.actionExit.setText(_translate("CAG_main", "Exit"))
        self.action_Exit.setText(_translate("CAG_main", "Exit"))
        self.actionAbout.setText(_translate("CAG_main", "About"))
    
    #display ongoing orders
    def viewRecord(self,CAG_main):
        ViewRecord = QtWidgets.QDialog()
        ui = Ui_ViewRecord()
        ui.setupUi(ViewRecord,CAG_main,ui)
        CAG_main.hide()
        ViewRecord.show()

    #display completed orders
    def completedRecord(self,CAG_main):
        completedOrders = QtWidgets.QDialog()
        ui = Ui_completedOrders()
        ui.setupUi(completedOrders, CAG_main)
        CAG_main.hide()
        completedOrders.show()
        
    #display the add customer form
    def addCustomer(self,CAG_main):
        self.newCustomer = QtWidgets.QDialog()
        self.newCust = Ui_addCustomer()
        self.newCust.setupUi(self.newCustomer, CAG_main)
        CAG_main.hide()
        self.newCustomer.show()
        
    def viewCustomers(self, CAG_main):
        viewCustomers = QtWidgets.QDialog()
        viewCust = Ui_viewCustomers()
        viewCust.setupUi(viewCustomers, CAG_main)
        CAG_main.hide()
        viewCustomers.show()

    def closeMain(self, CAG_main):
        CAG_main.close()

    def logOut(self, CAG_main, CAG_login):
        CAG_login.show()
        CAG_main.close()


