# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login_guest_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(723, 607)
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(550, 540, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 151, 534, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.find_book_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.find_book_button.setFont(font)
        self.find_book_button.setObjectName("find_book_button")
        self.horizontalLayout.addWidget(self.find_book_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.user_about_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(45)
        self.user_about_button.setFont(font)
        self.user_about_button.setObjectName("user_about_button")
        self.verticalLayout_2.addWidget(self.user_about_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.exit_button.setText(_translate("Dialog", "退出系统"))
        self.label.setText(_translate("Dialog", "图书馆查阅系统Ver1.0"))
        self.label_2.setText(_translate("Dialog", "访客模式"))
        self.find_book_button.setText(_translate("Dialog", "查书"))
        self.user_about_button.setText(_translate("Dialog", "用户信息"))
