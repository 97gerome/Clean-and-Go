# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lemue\Desktop\MAPUA\COE125\Clean-and-Go-master\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_AddRequest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddRequest.setGeometry(QtCore.QRect(110, 190, 81, 31))
        self.pushButton_AddRequest.setObjectName("pushButton_AddRequest")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(110, 240, 81, 31))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionAdd_an_Order = QtWidgets.QAction(MainWindow)
        self.actionAdd_an_Order.setObjectName("actionAdd_an_Order")
        self.actionLog_out = QtWidgets.QAction(MainWindow)
        self.actionLog_out.setObjectName("actionLog_out")
        self.menuFile.addAction(self.actionLog_out)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd_an_Order)
        self.menuHelp.addAction(self.actionInfo)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_AddRequest.setText(_translate("MainWindow", "Add Request"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionAdd_an_Order.setText(_translate("MainWindow", "Add an Order"))
        self.actionLog_out.setText(_translate("MainWindow", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())