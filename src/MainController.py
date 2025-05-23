import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.root_ui import Ui_ICEHelper
from src.Controller.BMIController import BMIController
from src.Controller.ExcelFilterController import ExcelFilterController


def resource_path(relative_path):
    try:
        # 获取 PyInstaller 打包后的临时目录
        base_path = sys._MEIPASS
    except Exception:
        # 如果在开发环境中，返回当前路径
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainController(QtWidgets.QMainWindow, Ui_ICEHelper):
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/res/img/apple.icns'))
        super().setWindowTitle("ICE Helper")  # 设置窗口标题


        self.excel_filter_page = ExcelFilterController()
        self.bmi_page = BMIController()

        self.stackedWidget.addWidget(self.excel_filter_page)
        self.stackedWidget.addWidget(self.bmi_page)


        self.init_connection()

        self.switch_page(self.excel_filter_page)

    def init_connection(self):
        self.actionBMI.triggered.connect(lambda : self.switch_page(self.bmi_page))
        self.actionExcelColFilter.triggered.connect(lambda: self.switch_page(self.excel_filter_page))

    def switch_page(self, page):
        """切换到指定页面"""
        self.stackedWidget.setCurrentWidget(page)
