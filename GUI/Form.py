#Author: Group- Garcia-Mandapat
#ProjectName: Clean-and-Go
#Filename: Form
from PyQt5 import QtCore, QtGui, QtWidgets
from BL.BusinessLogic import Record
#from ViewRecord import Ui_ViewRecord

class Ui_Form(object):
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 381)
        self.label_Form = QtWidgets.QLabel(Form)
        self.label_Form.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label_Form.setObjectName("label_Form")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(250, 250, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 90, 401, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_owner = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_owner.setObjectName("lineEdit_owner")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_owner)
        self.label_weight = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_weight.setObjectName("label_weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_weight)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_weight)
        self.label_pickupOrDelivery = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_pickupOrDelivery.setObjectName("label_pickupOrDelivery")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_pickupOrDelivery)
        self.radioButton_pickup = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_pickup.setObjectName("radioButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.radioButton_pickup)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.label_dateReceived = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dateReceived.setObjectName("label_dateReceived")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_dateReceived)
        self.lineEdit_dateReceived = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_dateReceived.setObjectName("lineEdit_dateReceived")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dateReceived)
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(340, 250, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_cancel.clicked.connect(lambda: self.cancelClicked(Form))
        self.pushButton_add.clicked.connect(lambda: self.addRecord(Form))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_Form.setText(_translate("Form", "Form: "))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.label_2.setText(_translate("Form", "Owner: "))
        self.label_weight.setText(_translate("Form", "Weight: "))
        self.label_pickupOrDelivery.setText(_translate("Form", "Pick-up or Delivery: "))
        self.radioButton_pickup.setText(_translate("Form", "Pick-up"))
        self.radioButton_2.setText(_translate("Form", "Delivery"))
        self.label_dateReceived.setText(_translate("Form", "Date (MM/DD/YYYY): "))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))

    def addRecord(self,Form):
        print ("records")
        owner = self.lineEdit_owner.text()
        #print ("got owner")
        weight = self.lineEdit_weight.text()
        #print("got weight")
        date = self.lineEdit_dateReceived.text()
        #print("got date")
        if self.radioButton_pickup.isChecked()==True:
            pickupOrDelivery = "Pick-up"
        if self.radioButton_2.isChecked()==True:
            pickupOrDelivery = "Delivery"
        print("Owner: ", owner)
        print("Weight: ", weight)
        print("Date of Order: ", date)
        print("Pick-up or Delivery: ", pickupOrDelivery)
        print("\n\n")
        rec = Record()
        rec.getValues(owner, weight, date, pickupOrDelivery)
        Form.close()
    def cancelClicked(self,Form):
        Form.close()

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
'''
