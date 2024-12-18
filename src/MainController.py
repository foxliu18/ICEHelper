import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import res.QtSheetStyle_rc
from res.root_ui import Ui_ICEHelper
from src.Controller.BMIController import BMIController


class MainController(QtWidgets.QMainWindow, Ui_ICEHelper):
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/res/img/apple.svg'))
        super().setWindowTitle("ICE Helper")  # 设置窗口标题


        self.bmi_page = BMIController()

        self.stackedWidget.addWidget(self.bmi_page)

        self.init_connection()

        self.switch_page(self.bmi_page)

    def init_connection(self):
        self.actionBMI.triggered.connect(lambda : self.switch_page(self.bmi_page))

    def switch_page(self, page):
        """切换到指定页面"""
        self.stackedWidget.setCurrentWidget(page)
