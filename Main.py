import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream

from src.MainController import MainController

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)         # 创建一个QApplication，即将开发的软件app

    qss_file = QFile(":/res/QSS/MacOS.qss")  # 使用资源路径加载 QSS 文件
    if qss_file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(qss_file)
        qss = stream.readAll()
        app.setStyleSheet(qss)  # 应用样式表

    MainWindow = QtWidgets.QMainWindow()    #QMainWindow装载需要的组件
    rootManager = MainController()

    rootManager.show()
    sys.exit(app.exec_())                                     #exit()或点击按钮退出app