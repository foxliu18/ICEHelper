# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BMI_Form(object):
    def setupUi(self, BMI_Form):
        BMI_Form.setObjectName("BMI_Form")
        BMI_Form.resize(1208, 734)
        BMI_Form.setMinimumSize(QtCore.QSize(980, 650))
        self.verticalLayout = QtWidgets.QVBoxLayout(BMI_Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(BMI_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.height_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_label.sizePolicy().hasHeightForWidth())
        self.height_label.setSizePolicy(sizePolicy)
        self.height_label.setMinimumSize(QtCore.QSize(90, 30))
        self.height_label.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.height_label.setFont(font)
        self.height_label.setObjectName("height_label")
        self.gridLayout.addWidget(self.height_label, 0, 0, 1, 1)
        self.height_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height_lineEdit.sizePolicy().hasHeightForWidth())
        self.height_lineEdit.setSizePolicy(sizePolicy)
        self.height_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.height_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.height_lineEdit.setFont(font)
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.gridLayout.addWidget(self.height_lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.bmi_lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.bmi_lcdNumber.setMinimumSize(QtCore.QSize(0, 60))
        self.bmi_lcdNumber.setMaximumSize(QtCore.QSize(1677215, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.bmi_lcdNumber.setFont(font)
        self.bmi_lcdNumber.setObjectName("bmi_lcdNumber")
        self.gridLayout.addWidget(self.bmi_lcdNumber, 0, 3, 2, 1)
        self.bmi_res_label = QtWidgets.QLabel(self.groupBox)
        self.bmi_res_label.setMinimumSize(QtCore.QSize(200, 60))
        self.bmi_res_label.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.bmi_res_label.setFont(font)
        self.bmi_res_label.setText("")
        self.bmi_res_label.setObjectName("bmi_res_label")
        self.gridLayout.addWidget(self.bmi_res_label, 0, 4, 2, 1)
        self.wight_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wight_label.sizePolicy().hasHeightForWidth())
        self.wight_label.setSizePolicy(sizePolicy)
        self.wight_label.setMinimumSize(QtCore.QSize(90, 30))
        self.wight_label.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.wight_label.setFont(font)
        self.wight_label.setObjectName("wight_label")
        self.gridLayout.addWidget(self.wight_label, 1, 0, 1, 1)
        self.weight_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight_lineEdit.sizePolicy().hasHeightForWidth())
        self.weight_lineEdit.setSizePolicy(sizePolicy)
        self.weight_lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.weight_lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.weight_lineEdit.setFont(font)
        self.weight_lineEdit.setObjectName("weight_lineEdit")
        self.gridLayout.addWidget(self.weight_lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.arpi_groupBox = QtWidgets.QGroupBox(BMI_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.arpi_groupBox.setFont(font)
        self.arpi_groupBox.setObjectName("arpi_groupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.arpi_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.AST_label = QtWidgets.QLabel(self.arpi_groupBox)
        self.AST_label.setMinimumSize(QtCore.QSize(50, 30))
        self.AST_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.AST_label.setFont(font)
        self.AST_label.setObjectName("AST_label")
        self.gridLayout_7.addWidget(self.AST_label, 0, 0, 1, 1)
        self.AST_lineEdit = QtWidgets.QLineEdit(self.arpi_groupBox)
        self.AST_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.AST_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AST_lineEdit.setFont(font)
        self.AST_lineEdit.setObjectName("AST_lineEdit")
        self.gridLayout_7.addWidget(self.AST_lineEdit, 0, 1, 1, 1)
        self.AST_unit_label = QtWidgets.QLabel(self.arpi_groupBox)
        self.AST_unit_label.setMinimumSize(QtCore.QSize(50, 30))
        self.AST_unit_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.AST_unit_label.setFont(font)
        self.AST_unit_label.setObjectName("AST_unit_label")
        self.gridLayout_7.addWidget(self.AST_unit_label, 0, 2, 1, 1)
        self.ULN_label = QtWidgets.QLabel(self.arpi_groupBox)
        self.ULN_label.setMinimumSize(QtCore.QSize(250, 30))
        self.ULN_label.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ULN_label.setFont(font)
        self.ULN_label.setObjectName("ULN_label")
        self.gridLayout_7.addWidget(self.ULN_label, 0, 3, 1, 1)
        self.arp_lcdNumber = QtWidgets.QLCDNumber(self.arpi_groupBox)
        self.arp_lcdNumber.setMinimumSize(QtCore.QSize(200, 60))
        self.arp_lcdNumber.setMaximumSize(QtCore.QSize(16777215, 60))
        self.arp_lcdNumber.setObjectName("arp_lcdNumber")
        self.gridLayout_7.addWidget(self.arp_lcdNumber, 0, 4, 2, 1)
        self.arp_res_label = QtWidgets.QLabel(self.arpi_groupBox)
        self.arp_res_label.setMinimumSize(QtCore.QSize(200, 60))
        self.arp_res_label.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.arp_res_label.setFont(font)
        self.arp_res_label.setText("")
        self.arp_res_label.setObjectName("arp_res_label")
        self.gridLayout_7.addWidget(self.arp_res_label, 0, 5, 2, 1)
        self.AST_label_2 = QtWidgets.QLabel(self.arpi_groupBox)
        self.AST_label_2.setMinimumSize(QtCore.QSize(50, 30))
        self.AST_label_2.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.AST_label_2.setFont(font)
        self.AST_label_2.setObjectName("AST_label_2")
        self.gridLayout_7.addWidget(self.AST_label_2, 1, 0, 1, 1)
        self.PLT_lineEdit = QtWidgets.QLineEdit(self.arpi_groupBox)
        self.PLT_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.PLT_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PLT_lineEdit.setFont(font)
        self.PLT_lineEdit.setObjectName("PLT_lineEdit")
        self.gridLayout_7.addWidget(self.PLT_lineEdit, 1, 1, 1, 1)
        self.PLT_unit_label = QtWidgets.QLabel(self.arpi_groupBox)
        self.PLT_unit_label.setMinimumSize(QtCore.QSize(70, 30))
        self.PLT_unit_label.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PLT_unit_label.setFont(font)
        self.PLT_unit_label.setObjectName("PLT_unit_label")
        self.gridLayout_7.addWidget(self.PLT_unit_label, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.arpi_groupBox)
        self.fib4_groupBox = QtWidgets.QGroupBox(BMI_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fib4_groupBox.setFont(font)
        self.fib4_groupBox.setObjectName("fib4_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fib4_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.age_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.age_label.setEnabled(True)
        self.age_label.setMinimumSize(QtCore.QSize(120, 30))
        self.age_label.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.age_label.setFont(font)
        self.age_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.age_label.setObjectName("age_label")
        self.horizontalLayout.addWidget(self.age_label)
        self.age_lineEdit = QtWidgets.QLineEdit(self.fib4_groupBox)
        self.age_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.age_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.age_lineEdit.setFont(font)
        self.age_lineEdit.setText("")
        self.age_lineEdit.setObjectName("age_lineEdit")
        self.horizontalLayout.addWidget(self.age_lineEdit)
        self.age_unit_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.age_unit_label.setMinimumSize(QtCore.QSize(80, 30))
        self.age_unit_label.setMaximumSize(QtCore.QSize(81, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.age_unit_label.setFont(font)
        self.age_unit_label.setObjectName("age_unit_label")
        self.horizontalLayout.addWidget(self.age_unit_label)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fib_ast_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.fib_ast_label.setMinimumSize(QtCore.QSize(50, 30))
        self.fib_ast_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fib_ast_label.setFont(font)
        self.fib_ast_label.setObjectName("fib_ast_label")
        self.horizontalLayout_3.addWidget(self.fib_ast_label)
        self.fib_ast_lineEdit = QtWidgets.QLineEdit(self.fib4_groupBox)
        self.fib_ast_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.fib_ast_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fib_ast_lineEdit.setFont(font)
        self.fib_ast_lineEdit.setObjectName("fib_ast_lineEdit")
        self.horizontalLayout_3.addWidget(self.fib_ast_lineEdit)
        self.fib_ast_unit_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.fib_ast_unit_label.setMinimumSize(QtCore.QSize(50, 30))
        self.fib_ast_unit_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fib_ast_unit_label.setFont(font)
        self.fib_ast_unit_label.setObjectName("fib_ast_unit_label")
        self.horizontalLayout_3.addWidget(self.fib_ast_unit_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bcc_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.bcc_label.setMinimumSize(QtCore.QSize(120, 30))
        self.bcc_label.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.bcc_label.setFont(font)
        self.bcc_label.setObjectName("bcc_label")
        self.horizontalLayout_2.addWidget(self.bcc_label)
        self.bcc_lineEdit = QtWidgets.QLineEdit(self.fib4_groupBox)
        self.bcc_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.bcc_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bcc_lineEdit.setFont(font)
        self.bcc_lineEdit.setText("")
        self.bcc_lineEdit.setObjectName("bcc_lineEdit")
        self.horizontalLayout_2.addWidget(self.bcc_lineEdit)
        self.bcc_unit_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.bcc_unit_label.setMinimumSize(QtCore.QSize(80, 30))
        self.bcc_unit_label.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bcc_unit_label.setFont(font)
        self.bcc_unit_label.setObjectName("bcc_unit_label")
        self.horizontalLayout_2.addWidget(self.bcc_unit_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fib_alt_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.fib_alt_label.setMinimumSize(QtCore.QSize(50, 30))
        self.fib_alt_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fib_alt_label.setFont(font)
        self.fib_alt_label.setObjectName("fib_alt_label")
        self.horizontalLayout_4.addWidget(self.fib_alt_label)
        self.fib_alt_lineEdit = QtWidgets.QLineEdit(self.fib4_groupBox)
        self.fib_alt_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.fib_alt_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.fib_alt_lineEdit.setFont(font)
        self.fib_alt_lineEdit.setText("")
        self.fib_alt_lineEdit.setObjectName("fib_alt_lineEdit")
        self.horizontalLayout_4.addWidget(self.fib_alt_lineEdit)
        self.fib_alt_unit_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.fib_alt_unit_label.setMinimumSize(QtCore.QSize(50, 30))
        self.fib_alt_unit_label.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.fib_alt_unit_label.setFont(font)
        self.fib_alt_unit_label.setObjectName("fib_alt_unit_label")
        self.horizontalLayout_4.addWidget(self.fib_alt_unit_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fib4_lcdNumber = QtWidgets.QLCDNumber(self.fib4_groupBox)
        self.fib4_lcdNumber.setMinimumSize(QtCore.QSize(100, 60))
        self.fib4_lcdNumber.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fib4_lcdNumber.setObjectName("fib4_lcdNumber")
        self.horizontalLayout_5.addWidget(self.fib4_lcdNumber)
        self.fib_res_label = QtWidgets.QLabel(self.fib4_groupBox)
        self.fib_res_label.setMinimumSize(QtCore.QSize(200, 60))
        self.fib_res_label.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.fib_res_label.setFont(font)
        self.fib_res_label.setText("")
        self.fib_res_label.setObjectName("fib_res_label")
        self.horizontalLayout_5.addWidget(self.fib_res_label)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.shbv_checkBox = QtWidgets.QCheckBox(self.fib4_groupBox)
        self.shbv_checkBox.setMinimumSize(QtCore.QSize(300, 30))
        self.shbv_checkBox.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.shbv_checkBox.setFont(font)
        self.shbv_checkBox.setObjectName("shbv_checkBox")
        self.horizontalLayout_6.addWidget(self.shbv_checkBox)
        self.fl_checkBox = QtWidgets.QCheckBox(self.fib4_groupBox)
        self.fl_checkBox.setMinimumSize(QtCore.QSize(240, 30))
        self.fl_checkBox.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fl_checkBox.setFont(font)
        self.fl_checkBox.setObjectName("fl_checkBox")
        self.horizontalLayout_6.addWidget(self.fl_checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.fib4_groupBox)
        self.ts_groupBox = QtWidgets.QGroupBox(BMI_Form)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ts_groupBox.setFont(font)
        self.ts_groupBox.setObjectName("ts_groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ts_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.si_label = QtWidgets.QLabel(self.ts_groupBox)
        self.si_label.setMinimumSize(QtCore.QSize(200, 30))
        self.si_label.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.si_label.setFont(font)
        self.si_label.setObjectName("si_label")
        self.gridLayout_4.addWidget(self.si_label, 0, 0, 1, 1)
        self.si_lineEdit = QtWidgets.QLineEdit(self.ts_groupBox)
        self.si_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.si_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.si_lineEdit.setFont(font)
        self.si_lineEdit.setText("")
        self.si_lineEdit.setObjectName("si_lineEdit")
        self.gridLayout_4.addWidget(self.si_lineEdit, 0, 1, 1, 1)
        self.ts_lcdNumber = QtWidgets.QLCDNumber(self.ts_groupBox)
        self.ts_lcdNumber.setMinimumSize(QtCore.QSize(100, 60))
        self.ts_lcdNumber.setMaximumSize(QtCore.QSize(16777215, 60))
        self.ts_lcdNumber.setObjectName("ts_lcdNumber")
        self.gridLayout_4.addWidget(self.ts_lcdNumber, 0, 2, 2, 1)
        self.ts_res_label = QtWidgets.QLabel(self.ts_groupBox)
        self.ts_res_label.setMinimumSize(QtCore.QSize(200, 60))
        self.ts_res_label.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ts_res_label.setFont(font)
        self.ts_res_label.setText("")
        self.ts_res_label.setObjectName("ts_res_label")
        self.gridLayout_4.addWidget(self.ts_res_label, 0, 3, 2, 1)
        self.fec_label = QtWidgets.QLabel(self.ts_groupBox)
        self.fec_label.setMinimumSize(QtCore.QSize(200, 30))
        self.fec_label.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fec_label.setFont(font)
        self.fec_label.setObjectName("fec_label")
        self.gridLayout_4.addWidget(self.fec_label, 1, 0, 1, 1)
        self.fec_lineEdit = QtWidgets.QLineEdit(self.ts_groupBox)
        self.fec_lineEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.fec_lineEdit.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fec_lineEdit.setFont(font)
        self.fec_lineEdit.setText("")
        self.fec_lineEdit.setObjectName("fec_lineEdit")
        self.gridLayout_4.addWidget(self.fec_lineEdit, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ts_groupBox)
        self.textBrowser = QtWidgets.QTextBrowser(BMI_Form)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(BMI_Form)
        QtCore.QMetaObject.connectSlotsByName(BMI_Form)

    def retranslateUi(self, BMI_Form):
        _translate = QtCore.QCoreApplication.translate
        BMI_Form.setWindowTitle(_translate("BMI_Form", "Form"))
        self.groupBox.setTitle(_translate("BMI_Form", "BMI计算"))
        self.height_label.setText(_translate("BMI_Form", "身高: "))
        self.label.setText(_translate("BMI_Form", "米"))
        self.wight_label.setText(_translate("BMI_Form", "体重:"))
        self.label_2.setText(_translate("BMI_Form", "公斤"))
        self.arpi_groupBox.setTitle(_translate("BMI_Form", "天门冬氨酸氨基转移酶与血小板比值(APRI)评分"))
        self.AST_label.setText(_translate("BMI_Form", "AST:"))
        self.AST_unit_label.setText(_translate("BMI_Form", "IU/L"))
        self.ULN_label.setText(_translate("BMI_Form", "ULN(AST上限值):(40)IU/L"))
        self.AST_label_2.setText(_translate("BMI_Form", "PLT:"))
        self.PLT_unit_label.setText(_translate("BMI_Form", "10^9/L"))
        self.fib4_groupBox.setTitle(_translate("BMI_Form", "慢性肝病患者肝纤维化FIB-4指数"))
        self.age_label.setText(_translate("BMI_Form", "年龄:"))
        self.age_unit_label.setText(_translate("BMI_Form", "岁"))
        self.fib_ast_label.setText(_translate("BMI_Form", "AST:"))
        self.fib_ast_unit_label.setText(_translate("BMI_Form", "IU/L"))
        self.bcc_label.setText(_translate("BMI_Form", "血小板计数:"))
        self.bcc_unit_label.setText(_translate("BMI_Form", "10^9/L"))
        self.fib_alt_label.setText(_translate("BMI_Form", "ALT:"))
        self.fib_alt_unit_label.setText(_translate("BMI_Form", "IU/L"))
        self.shbv_checkBox.setText(_translate("BMI_Form", "慢性乙型肝炎或丙型肝炎"))
        self.fl_checkBox.setText(_translate("BMI_Form", "非酒精性脂肪肝"))
        self.ts_groupBox.setTitle(_translate("BMI_Form", "转铁蛋白饱和度"))
        self.si_label.setText(_translate("BMI_Form", "血清铁(微克/分升):"))
        self.fec_label.setText(_translate("BMI_Form", "总铁结合能力(ug/dL):"))
