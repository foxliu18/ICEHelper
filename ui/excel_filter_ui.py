# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/liu/Code/ICEHelper/ui/excel_filter.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_excel_filter_form(object):
    def setupUi(self, excel_filter_form):
        excel_filter_form.setObjectName("excel_filter_form")
        excel_filter_form.resize(894, 674)
        self.gridLayout = QtWidgets.QGridLayout(excel_filter_form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(excel_filter_form)
        self.frame.setMinimumSize(QtCore.QSize(800, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.file_label = QtWidgets.QLabel(self.frame)
        self.file_label.setMinimumSize(QtCore.QSize(50, 0))
        self.file_label.setObjectName("file_label")
        self.horizontalLayout_4.addWidget(self.file_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.file_lineEdit.setMinimumSize(QtCore.QSize(520, 30))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.file_lineEdit.setObjectName("file_lineEdit")
        self.horizontalLayout.addWidget(self.file_lineEdit)
        self.slt_file_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slt_file_btn.sizePolicy().hasHeightForWidth())
        self.slt_file_btn.setSizePolicy(sizePolicy)
        self.slt_file_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.slt_file_btn.setMaximumSize(QtCore.QSize(35, 35))
        self.slt_file_btn.setStyleSheet("#slt_file_btn{\n"
"border: none\n"
"/*border-image: url(:/res/img/addfile32.svg) */\n"
"}\n"
"")
        self.slt_file_btn.setText("")
        self.slt_file_btn.setObjectName("slt_file_btn")
        self.horizontalLayout.addWidget(self.slt_file_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.sheet_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.sheet_lineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.sheet_lineEdit.setMaximumSize(QtCore.QSize(200, 60))
        self.sheet_lineEdit.setObjectName("sheet_lineEdit")
        self.horizontalLayout_4.addWidget(self.sheet_lineEdit)
        self.file_read_pbtn = QtWidgets.QPushButton(self.frame)
        self.file_read_pbtn.setMinimumSize(QtCore.QSize(80, 30))
        self.file_read_pbtn.setMaximumSize(QtCore.QSize(160, 60))
        self.file_read_pbtn.setObjectName("file_read_pbtn")
        self.horizontalLayout_4.addWidget(self.file_read_pbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter_label = QtWidgets.QLabel(self.frame)
        self.filter_label.setMinimumSize(QtCore.QSize(50, 0))
        self.filter_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.filter_label.setObjectName("filter_label")
        self.horizontalLayout_2.addWidget(self.filter_label)
        self.filter_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.filter_lineEdit.setMinimumSize(QtCore.QSize(400, 30))
        self.filter_lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.filter_lineEdit.setPlaceholderText("")
        self.filter_lineEdit.setObjectName("filter_lineEdit")
        self.horizontalLayout_2.addWidget(self.filter_lineEdit)
        self.filter_type_comboBox = QtWidgets.QComboBox(self.frame)
        self.filter_type_comboBox.setMinimumSize(QtCore.QSize(150, 32))
        self.filter_type_comboBox.setStyleSheet("")
        self.filter_type_comboBox.setObjectName("filter_type_comboBox")
        self.horizontalLayout_2.addWidget(self.filter_type_comboBox)
        self.filter_pbtn = QtWidgets.QPushButton(self.frame)
        self.filter_pbtn.setMinimumSize(QtCore.QSize(80, 30))
        self.filter_pbtn.setMaximumSize(QtCore.QSize(80, 60))
        self.filter_pbtn.setObjectName("filter_pbtn")
        self.horizontalLayout_2.addWidget(self.filter_pbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.input_tableWidget = QtWidgets.QTableWidget(self.frame)
        self.input_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.input_tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_tableWidget.setObjectName("input_tableWidget")
        self.input_tableWidget.setColumnCount(0)
        self.input_tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.input_tableWidget)
        self.out_textb = QtWidgets.QTextBrowser(self.frame)
        self.out_textb.setMinimumSize(QtCore.QSize(770, 100))
        self.out_textb.setMaximumSize(QtCore.QSize(16777215, 200))
        self.out_textb.setObjectName("out_textb")
        self.verticalLayout.addWidget(self.out_textb)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setMinimumSize(QtCore.QSize(100, 40))
        self.checkBox.setMaximumSize(QtCore.QSize(150, 40))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.output_pushButton = QtWidgets.QPushButton(self.frame)
        self.output_pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.output_pushButton.setMaximumSize(QtCore.QSize(120, 40))
        self.output_pushButton.setObjectName("output_pushButton")
        self.horizontalLayout_3.addWidget(self.output_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(excel_filter_form)
        QtCore.QMetaObject.connectSlotsByName(excel_filter_form)

    def retranslateUi(self, excel_filter_form):
        _translate = QtCore.QCoreApplication.translate
        excel_filter_form.setWindowTitle(_translate("excel_filter_form", "Form"))
        self.file_label.setText(_translate("excel_filter_form", "文件"))
        self.file_lineEdit.setPlaceholderText(_translate("excel_filter_form", "file dir"))
        self.sheet_lineEdit.setPlaceholderText(_translate("excel_filter_form", "sheet or null"))
        self.file_read_pbtn.setText(_translate("excel_filter_form", " 读取"))
        self.filter_label.setText(_translate("excel_filter_form", "筛选字符"))
        self.filter_pbtn.setText(_translate("excel_filter_form", "筛选"))
        self.checkBox.setText(_translate("excel_filter_form", "分文件输出"))
        self.output_pushButton.setText(_translate("excel_filter_form", "输出"))
