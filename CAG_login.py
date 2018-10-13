import sys
#sys.path.append('C:/GitHub/Clean-and-Go/')
sys.path.append('../')
from BL.BL_login import BL_login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from CAG_main import Ui_CAG_mai

class Ui_Login(object):
    def setupUi(self, Dialog):
        #####################################################################
        self.CAG_main = QtWidgets.QMainWindow()
        self.ui = Ui_CAG_main()
        self.ui.setupUi(self.CAG_main, Dialog)     
        ######################################################################
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
        
        
        self.loginButton.clicked.connect(lambda: self.loginClicked(Dialog))
        self.cancelButton.clicked.connect(lambda: self.cancelClicked(Dialog))       

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
        logic = BL_login()
        uname = (self.username_line.text(),)
        
        if logic.check_user(uname) == 1:
            if logic.check_pw(self.password_line.text(), uname):
                loginSuccess = QMessageBox()
                loginSuccess.setIcon(QMessageBox.Information)
                loginSuccess.setText("Welcome")
                loginSuccess.setWindowTitle("Login Successful")
                loginSuccess.setStandardButtons(QMessageBox.Ok)       
                self.CAG_main.show()
                self.username_line.setText("")
                self.password_line.setText("")
                loginSuccess.exec_()
                Dialog.close()
                
            else:
                loginFail = QMessageBox()
                loginFail.setIcon(QMessageBox.Information)
                loginFail.setText("Login failed")
                loginFail.setWindowTitle("Please enter a valid username\password")
                loginFail.setStandardButtons(QMessageBox.Ok)
                loginFail.exec_()
        else:
            loginFail = QMessageBox()
            loginFail.setIcon(QMessageBox.Information)
            loginFail.setText("Please enter a valid username\password")
            loginFail.setWindowTitle("Login failed")
            loginFail.setStandardButtons(QMessageBox.Ok)
            loginFail.exec_()
            

    def cancelClicked(self,CAG_login):
        CAG_login.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

