# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountDelete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteAccount(object):
    def setupUi(self, deleteAccount):
        deleteAccount.setObjectName("deleteAccount")
        deleteAccount.resize(400, 300)
        deleteAccount.setStyleSheet("#deleteAccount{border-image:url(./1.jpg);}")
        self.label = QtWidgets.QLabel(deleteAccount)
        self.label.setGeometry(QtCore.QRect(20, 110, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(deleteAccount)
        self.id.setGeometry(QtCore.QRect(160, 110, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id.setFont(font)
        self.id.setText("")
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(deleteAccount)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.DeleteBtn = QtWidgets.QPushButton(deleteAccount)
        self.DeleteBtn.setGeometry(QtCore.QRect(160, 220, 221, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteBtn.setFont(font)
        self.DeleteBtn.setAutoFillBackground(True)
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.id_2 = QtWidgets.QLineEdit(deleteAccount)
        self.id_2.setGeometry(QtCore.QRect(160, 160, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_2.setFont(font)
        self.id_2.setText("")
        self.id_2.setObjectName("id_2")
        self.label_2 = QtWidgets.QLabel(deleteAccount)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 150, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(deleteAccount)
        QtCore.QMetaObject.connectSlotsByName(deleteAccount)

    def retranslateUi(self, deleteAccount):
        _translate = QtCore.QCoreApplication.translate
        deleteAccount.setWindowTitle(_translate("deleteAccount", "Dialog"))
        self.label.setText(_translate("deleteAccount", "账户号"))
        self.label_5.setText(_translate("deleteAccount", "删除账户"))
        self.DeleteBtn.setText(_translate("deleteAccount", "删除"))
        self.label_2.setText(_translate("deleteAccount", "客户身份证"))
