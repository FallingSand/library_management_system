# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user_return.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 462)
        self.return_button = QtWidgets.QPushButton(Dialog)
        self.return_button.setGeometry(QtCore.QRect(160, 300, 271, 68))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 541, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.book_uuid_input = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.book_uuid_input.setFont(font)
        self.book_uuid_input.setText("")
        self.book_uuid_input.setObjectName("book_uuid_input")
        self.horizontalLayout.addWidget(self.book_uuid_input)
        self.find_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.find_button.setFont(font)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout.addWidget(self.find_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.return_button.setText(_translate("Dialog", "还书"))
        self.label.setText(_translate("Dialog", "书本uuid:"))
        self.book_uuid_input.setPlaceholderText(_translate("Dialog", "000000001"))
        self.find_button.setText(_translate("Dialog", "查询"))
