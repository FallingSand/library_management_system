# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user_find_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(853, 630)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uuid_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.uuid_radioButton.setObjectName("uuid_radioButton")
        self.horizontalLayout_3.addWidget(self.uuid_radioButton)
        self.name_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.name_radioButton.setObjectName("name_radioButton")
        self.horizontalLayout_3.addWidget(self.name_radioButton)
        self.email_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.email_radioButton.setObjectName("email_radioButton")
        self.horizontalLayout_3.addWidget(self.email_radioButton)
        self.level_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.level_radioButton.setObjectName("level_radioButton")
        self.horizontalLayout_3.addWidget(self.level_radioButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reg_time_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.reg_time_radioButton.setObjectName("reg_time_radioButton")
        self.horizontalLayout_2.addWidget(self.reg_time_radioButton)
        self.read_count_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.read_count_radioButton.setObjectName("read_count_radioButton")
        self.horizontalLayout_2.addWidget(self.read_count_radioButton)
        self.read_time_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.read_time_radioButton.setObjectName("read_time_radioButton")
        self.horizontalLayout_2.addWidget(self.read_time_radioButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upSORT_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.upSORT_radioButton.setObjectName("upSORT_radioButton")
        self.horizontalLayout.addWidget(self.upSORT_radioButton)
        self.downSORT_radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.downSORT_radioButton.setObjectName("downSORT_radioButton")
        self.horizontalLayout.addWidget(self.downSORT_radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("汉仪文黑-85W")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.find_input = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find_input.setFont(font)
        self.find_input.setText("")
        self.find_input.setObjectName("find_input")
        self.horizontalLayout_6.addWidget(self.find_input)
        self.find_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.find_button.setFont(font)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout_6.addWidget(self.find_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "精确查找"))
        self.uuid_radioButton.setText(_translate("Dialog", "UUID"))
        self.name_radioButton.setText(_translate("Dialog", "用户名"))
        self.email_radioButton.setText(_translate("Dialog", "邮箱"))
        self.level_radioButton.setText(_translate("Dialog", "等级（0 1 2）"))
        self.label_3.setText(_translate("Dialog", "排序查找"))
        self.reg_time_radioButton.setText(_translate("Dialog", "注册时间"))
        self.read_count_radioButton.setText(_translate("Dialog", "阅读次数"))
        self.read_time_radioButton.setText(_translate("Dialog", "阅读时长"))
        self.upSORT_radioButton.setText(_translate("Dialog", "升序"))
        self.downSORT_radioButton.setText(_translate("Dialog", "降序"))
        self.label.setText(_translate("Dialog", "内容："))
        self.find_input.setPlaceholderText(_translate("Dialog", "000000001"))
        self.find_button.setText(_translate("Dialog", "查询"))
