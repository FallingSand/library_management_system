# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_admin_update_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 437)
        self.find_button_2 = QtWidgets.QPushButton(Dialog)
        self.find_button_2.setGeometry(QtCore.QRect(150, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.find_button_2.setFont(font)
        self.find_button_2.setObjectName("find_button_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 381, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.find_input = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input.setFont(font)
        self.find_input.setText("")
        self.find_input.setObjectName("find_input")
        self.horizontalLayout.addWidget(self.find_input)
        self.find_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.find_button.setFont(font)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout.addWidget(self.find_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.find_input_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input_2.setFont(font)
        self.find_input_2.setText("")
        self.find_input_2.setObjectName("find_input_2")
        self.horizontalLayout_2.addWidget(self.find_input_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.find_input_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input_3.setFont(font)
        self.find_input_3.setText("")
        self.find_input_3.setObjectName("find_input_3")
        self.horizontalLayout_3.addWidget(self.find_input_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.find_input_6 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input_6.setFont(font)
        self.find_input_6.setText("")
        self.find_input_6.setObjectName("find_input_6")
        self.horizontalLayout_6.addWidget(self.find_input_6)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.find_input_4 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input_4.setFont(font)
        self.find_input_4.setText("")
        self.find_input_4.setObjectName("find_input_4")
        self.horizontalLayout_4.addWidget(self.find_input_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.find_input_5 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input_5.setFont(font)
        self.find_input_5.setText("")
        self.find_input_5.setObjectName("find_input_5")
        self.horizontalLayout_5.addWidget(self.find_input_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.find_button_2.setText(_translate("Dialog", "删除用户"))
        self.label.setText(_translate("Dialog", "uuid："))
        self.find_input.setPlaceholderText(_translate("Dialog", "000000001"))
        self.find_button.setText(_translate("Dialog", "更改"))
        self.label_2.setText(_translate("Dialog", "违规次数"))
        self.label_3.setText(_translate("Dialog", "用户名"))
        self.label_6.setText(_translate("Dialog", "等级（0 1 2）"))
        self.label_4.setText(_translate("Dialog", "阅读时长"))
        self.label_5.setText(_translate("Dialog", "阅读次数"))