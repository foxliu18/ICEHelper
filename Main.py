import sys

from PyQt5 import QtWidgets
from res.QSS.ExcelOffice import qss
from src.MainController import MainController


if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)         # 创建一个QApplication，即将开发的软件app

    # 从文件加载样式表
    # with open("./res/ExcelOffice.qss", "r", encoding='utf-8') as file:
    #     app.setStyleSheet(file.read())
    Qss = qss
    app.setStyleSheet(Qss)
    MainWindow = QtWidgets.QMainWindow()    #QMainWindow装载需要的组件
    rootManager = MainController()
    # ui = rootManager.rootUi
    # rootManager.setupUi(rootManager)                                 #执行类中的setupUi方法
    rootManager.show()
    sys.exit(app.exec_())                                     #exit()或点击按钮退出app