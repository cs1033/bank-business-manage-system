# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loanAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loanAdd(object):
    def setupUi(self, loanAdd):
        loanAdd.setObjectName("loanAdd")
        loanAdd.resize(725, 562)
        loanAdd.setStyleSheet("#loanAdd{border-image:url(./1.jpg);}")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        loanAdd.setFont(font)
        self.label = QtWidgets.QLabel(loanAdd)
        self.label.setGeometry(QtCore.QRect(90, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loanAdd)
        self.label_2.setGeometry(QtCore.QRect(90, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.loan_id = QtWidgets.QLineEdit(loanAdd)
        self.loan_id.setGeometry(QtCore.QRect(280, 140, 161, 31))
        self.loan_id.setObjectName("loan_id")
        self.amount = QtWidgets.QLineEdit(loanAdd)
        self.amount.setGeometry(QtCore.QRect(280, 200, 161, 31))
        self.amount.setObjectName("amount")
        self.ts1 = QtWidgets.QLabel(loanAdd)
        self.ts1.setGeometry(QtCore.QRect(470, 140, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ts1.setFont(font)
        self.ts1.setStyleSheet("color:red")
        self.ts1.setText("")
        self.ts1.setObjectName("ts1")
        self.ts2 = QtWidgets.QLabel(loanAdd)
        self.ts2.setGeometry(QtCore.QRect(470, 200, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ts2.setFont(font)
        self.ts2.setStyleSheet("color:red")
        self.ts2.setText("")
        self.ts2.setObjectName("ts2")
        self.id1 = QtWidgets.QLineEdit(loanAdd)
        self.id1.setGeometry(QtCore.QRect(280, 260, 161, 31))
        self.id1.setObjectName("id1")
        self.ts3 = QtWidgets.QLabel(loanAdd)
        self.ts3.setGeometry(QtCore.QRect(470, 260, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ts3.setFont(font)
        self.ts3.setStyleSheet("color:red")
        self.ts3.setText("")
        self.ts3.setObjectName("ts3")
        self.label_6 = QtWidgets.QLabel(loanAdd)
        self.label_6.setGeometry(QtCore.QRect(90, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(loanAdd)
        self.label_7.setGeometry(QtCore.QRect(90, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.id2 = QtWidgets.QLineEdit(loanAdd)
        self.id2.setGeometry(QtCore.QRect(280, 320, 161, 31))
        self.id2.setObjectName("id2")
        self.ts4 = QtWidgets.QLabel(loanAdd)
        self.ts4.setGeometry(QtCore.QRect(470, 320, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ts4.setFont(font)
        self.ts4.setStyleSheet("color:red")
        self.ts4.setText("")
        self.ts4.setObjectName("ts4")
        self.label_9 = QtWidgets.QLabel(loanAdd)
        self.label_9.setGeometry(QtCore.QRect(90, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.id3 = QtWidgets.QLineEdit(loanAdd)
        self.id3.setGeometry(QtCore.QRect(280, 380, 161, 31))
        self.id3.setObjectName("id3")
        self.ts5 = QtWidgets.QLabel(loanAdd)
        self.ts5.setGeometry(QtCore.QRect(470, 380, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ts5.setFont(font)
        self.ts5.setStyleSheet("color:red")
        self.ts5.setText("")
        self.ts5.setObjectName("ts5")
        self.label_11 = QtWidgets.QLabel(loanAdd)
        self.label_11.setGeometry(QtCore.QRect(260, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:red")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(loanAdd)
        self.label_12.setGeometry(QtCore.QRect(90, 440, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:blue")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(loanAdd)
        self.pushButton.setGeometry(QtCore.QRect(500, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(loanAdd)
        QtCore.QMetaObject.connectSlotsByName(loanAdd)

    def retranslateUi(self, loanAdd):
        _translate = QtCore.QCoreApplication.translate
        loanAdd.setWindowTitle(_translate("loanAdd", "Dialog"))
        self.label.setText(_translate("loanAdd", "贷款号:"))
        self.label_2.setText(_translate("loanAdd", "贷款金额:"))
        self.label_6.setText(_translate("loanAdd", "申请人1身份证:"))
        self.label_7.setText(_translate("loanAdd", "申请人2身份证:"))
        self.label_9.setText(_translate("loanAdd", "申请人3身份证:"))
        self.label_11.setText(_translate("loanAdd", "申请贷款"))
        self.label_12.setText(_translate("loanAdd", "(注：最少1人，最多3人申请,申请人1不能为空)"))
        self.pushButton.setText(_translate("loanAdd", "申请"))
