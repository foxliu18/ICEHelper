import os
import sys
import res.QtSheetStyle_rc
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from src.MainController import MainController
def resource_path(relative_path):
    try:
        # 获取 PyInstaller 打包后的临时目录
        base_path = sys._MEIPASS
    except Exception:
        # 如果在开发环境中，返回当前路径
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)         # 创建一个QApplication，即将开发的软件app

    # 从文件加载样式表
    # with open(":/res/QSS/Aqua.qss", "r", encoding='utf-8') as file:
    #     app.setStyleSheet(file.read())
    # 加载 QSS 样式表
    # 加载 QSS 样式表
    qss_file = QFile(":/res/QSS/MacOS.qss")  # 使用资源路径加载 QSS 文件
    if qss_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(qss_file)
        qss = stream.readAll()
        app.setStyleSheet(qss)  # 应用样式表

    # app.setStyle("Fusion")  # 使用 Fusion 样式（接近 macOS）
    MainWindow = QtWidgets.QMainWindow()    #QMainWindow装载需要的组件
    rootManager = MainController()
    # ui = rootManager.rootUi
    # rootManager.setupUi(rootManager)                                 #执行类中的setupUi方法
    rootManager.show()
    sys.exit(app.exec_())                                     #exit()或点击按钮退出app