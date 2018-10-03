
from PyQt5 import QtCore, QtGui, QtWidgets
from BL.BusinessLogic import Record

class Ui_Form(object):
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 504)
        self.label_requestForm = QtWidgets.QLabel(Form)
        self.label_requestForm.setGeometry(QtCore.QRect(20, 5, 111, 31))
        self.label_requestForm.setObjectName("label_requestForm")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        self.pushButton_add.setGeometry(QtCore.QRect(280, 460, 75, 23))
        self.pushButton_add.setObjectName("pushButton_add")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 401, 145))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_owner = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_owner.setObjectName("label_owner")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_owner)
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
        self.radioButton_pickUp = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_pickUp.setObjectName("radioButton_pickUp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.radioButton_pickUp)
        self.radioButton_delivery = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_delivery.setObjectName("radioButton_delivery")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.radioButton_delivery)
        self.label_dateReceived = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_dateReceived.setObjectName("label_dateReceived")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_dateReceived)
        self.lineEdit_dateReceived = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_dateReceived.setReadOnly(False)
        self.lineEdit_dateReceived.setObjectName("lineEdit_dateReceived")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dateReceived)
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(370, 460, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.groupBox_services = QtWidgets.QGroupBox(Form)
        self.groupBox_services.setGeometry(QtCore.QRect(20, 190, 401, 111))
        self.groupBox_services.setObjectName("groupBox_services")
        self.checkBox_press = QtWidgets.QCheckBox(self.groupBox_services)
        self.checkBox_press.setGeometry(QtCore.QRect(170, 40, 70, 17))
        self.checkBox_press.setObjectName("checkBox_press")
        self.checkBox_fold = QtWidgets.QCheckBox(self.groupBox_services)
        self.checkBox_fold.setGeometry(QtCore.QRect(170, 60, 70, 17))
        self.checkBox_fold.setObjectName("checkBox_fold")
        self.groupBox_washType = QtWidgets.QGroupBox(self.groupBox_services)
        self.groupBox_washType.setGeometry(QtCore.QRect(10, 20, 141, 80))
        self.groupBox_washType.setObjectName("groupBox_washType")
        self.radioButton_handWashed = QtWidgets.QRadioButton(self.groupBox_washType)
        self.radioButton_handWashed.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.radioButton_handWashed.setObjectName("radioButton_handWashed")
        self.radioButton_machineWashed = QtWidgets.QRadioButton(self.groupBox_washType)
        self.radioButton_machineWashed.setGeometry(QtCore.QRect(20, 40, 101, 17))
        self.radioButton_machineWashed.setObjectName("radioButton_machineWashed")
        self.radioButton_dryClean = QtWidgets.QRadioButton(self.groupBox_washType)
        self.radioButton_dryClean.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.radioButton_dryClean.setObjectName("radioButton_dryClean")
        self.groupBox_paymentMode = QtWidgets.QGroupBox(Form)
        self.groupBox_paymentMode.setGeometry(QtCore.QRect(20, 320, 401, 91))
        self.groupBox_paymentMode.setObjectName("groupBox_paymentMode")
        self.radioButton_fullPayment = QtWidgets.QRadioButton(self.groupBox_paymentMode)
        self.radioButton_fullPayment.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_fullPayment.setObjectName("radioButton_fullPayment")
        self.radioButton_downPayment = QtWidgets.QRadioButton(self.groupBox_paymentMode)
        self.radioButton_downPayment.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.radioButton_downPayment.setObjectName("radioButton_downPayment")
        self.lineEdit_downPayment = QtWidgets.QLineEdit(self.groupBox_paymentMode)
        self.lineEdit_downPayment.setGeometry(QtCore.QRect(80, 60, 151, 20))
        self.lineEdit_downPayment.setObjectName("lineEdit_downPayment")
        self.label_amountDownPayment = QtWidgets.QLabel(self.groupBox_paymentMode)
        self.label_amountDownPayment.setGeometry(QtCore.QRect(30, 60, 47, 13))
        self.label_amountDownPayment.setObjectName("label_amountDownPayment")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # functions to be added
        self.pushButton_cancel.clicked.connect(lambda: self.cancelClicked(Form))
        self.pushButton_add.clicked.connect(lambda: self.addRecord(Form))
        self.radioButton_downPayment.clicked.connect(lambda: self.enableAmount())
        self.radioButton_fullPayment.clicked.connect(lambda: self.enableAmount())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_requestForm.setText(_translate("Form", "Request Form: "))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.label_owner.setText(_translate("Form", "Owner: "))
        self.label_weight.setText(_translate("Form", "Weight: "))
        self.label_pickupOrDelivery.setText(_translate("Form", "Pick-up or Delivery: "))
        self.radioButton_pickUp.setText(_translate("Form", "Pick-up"))
        self.radioButton_delivery.setText(_translate("Form", "Delivery"))
        self.label_dateReceived.setText(_translate("Form", "Date (MM/DD/YYYY): "))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))
        self.groupBox_services.setTitle(_translate("Form", "Services:"))
        self.checkBox_press.setText(_translate("Form", "Press"))
        self.checkBox_fold.setText(_translate("Form", "Fold"))
        self.groupBox_washType.setTitle(_translate("Form", "Wash Type"))
        self.radioButton_handWashed.setText(_translate("Form", "Hand washed"))
        self.radioButton_machineWashed.setText(_translate("Form", "Machine washed"))
        self.radioButton_dryClean.setText(_translate("Form", "Dry cleaned"))
        self.groupBox_paymentMode.setTitle(_translate("Form", "Payment Mode:"))
        self.radioButton_fullPayment.setText(_translate("Form", "Full"))
        self.radioButton_downPayment.setText(_translate("Form", "Down Payment"))
        self.label_amountDownPayment.setText(_translate("Form", "Amount:"))
        self.getDate()
        self.lineEdit_dateReceived.setReadOnly(True)
        self.lineEdit_downPayment.setEnabled(False)

    #####ADDED Functions#######
    def addRecord(self, Form):
        print("add record")
        handWash = False
        machineWash = False
        dryClean = False
        press = False
        fold = False
        paid = False
        owner = self.lineEdit_owner.text()
        weight = self.lineEdit_weight.text()
        date = self.lineEdit_dateReceived.text()
        amount = 0
        '''
        if self.radioButton_pickUp.isChecked() == self.radioButton_delivery.isChecked():
            print("Please Select if Pick-up or Delivery")
            self.retranslateUi(Form)
        '''

        pickupOrDelivery = ""
        if self.radioButton_pickUp.isChecked() == True:
            pickupOrDelivery = "Pick-up"
        if self.radioButton_delivery.isChecked() == True:
            pickupOrDelivery = "Delivery"
        if self.radioButton_handWashed.isChecked() == True:
            handWash = True
        elif self.radioButton_machineWashed.isChecked() == True:
            machineWash = True
        elif self.radioButton_dryClean.isChecked() == True:
            dryClean = True
        if self.checkBox_fold.isChecked() == True:
            fold = True
        if self.checkBox_press.isChecked() == True:
            press = True
        if self.radioButton_fullPayment.isChecked() ==True:
            paid = True
        if self.radioButton_downPayment.isChecked() == True:
            paid = False
            amount = int(self.lineEdit_downPayment.text())
        rec = Record()
        rec.getValues(owner, weight, date, pickupOrDelivery, handWash,machineWash,dryClean,fold,press,paid,amount)
        Form.close()

    def enableAmount(self):
        if self.radioButton_downPayment.isChecked() == False:
            self.lineEdit_downPayment.setEnabled(False)
        else:
            self.lineEdit_downPayment.setEnabled(True)
    def getDate(self):
        recordDate = Record()
        date = recordDate.getDate()
        self.lineEdit_dateReceived.setText(date)


    def cancelClicked(self, Form):
        Form.close()

