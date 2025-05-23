import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from ui.excel_filter_ui import Ui_excel_filter_form
from src.utils.ReadExcelUtil import ReadExcelUtil
from PyQt5.QtWidgets import QTableWidgetItem, \
    QFileDialog, QWidget
import threading

# def resource_path(relative_path):
#     try:
#         # 获取 PyInstaller 打包后的临时目录
#         base_path = sys._MEIPASS
#     except Exception:
#         # 如果在开发环境中，返回当前路径
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

class ExcelFilterController(QWidget):


    def __init__(self):
        super().__init__()
        # 创建 ICEHelper 实例
        self.filter_list = None
        self.data = None
        self.ui = Ui_excel_filter_form()

        # 设置 UI
        self.ui.setupUi(self)

        self.ui.slt_file_btn.setIcon(QIcon(':/res/img/addfile32.svg'))
        self.ui.slt_file_btn.setIconSize(QSize(34, 34))


        self.ui.input_tableWidget.horizontalScrollBar().setMinimum(1000)
        self.ui.checkBox.setChecked(True)
        self.ui.checkBox.setEnabled(True)
        self.ui.filter_type_comboBox.addItems(['起始', '包含', '结尾'])
        self.ui.filter_type_comboBox.setCurrentText('起始')

        self.excelUtil = ReadExcelUtil()

        self.init_connect()
        print("root manager init")

    ## 初始化链接
    def init_connect(self):
        self.ui.file_read_pbtn.clicked.connect(self.clicked_file_btn)
        self.ui.filter_pbtn.clicked.connect(self.clicked_filter_btn)
        self.ui.output_pushButton.clicked.connect(self.output_file)
        self.ui.slt_file_btn.clicked.connect(self.open_file_dialog)

    def output_file(self):
        is_split = self.ui.checkBox.isChecked()
        if self.filter_list is None:
            return
        res = self.excelUtil.write_to_excel(self.filter_list, is_split)
        if res[0]:
            self.ui.out_textb.append(res[1])
        else:
            self.ui.out_textb.append("创建路径失败: " + res[1])
            self.ui.out_textb.append( "请尝试手动创建路径：" + res[2])
    ## 打开过滤
    def open_filter(self):
        input_filter = self.ui.filter_lineEdit.text()
        if input_filter == "" or input_filter is None:
            self.ui.out_textb.append("筛选条件为空......")
            self.show_view(self.data, 5)
            return
        if "," in input_filter:
            self.filter_list = input_filter.split(",")
        elif "，" in input_filter:
            self.filter_list = input_filter.split("，")
        else:
            self.filter_list = [input_filter]
        df_out_dict = self.excelUtil.filter_excel(self.filter_list, self.ui.filter_type_comboBox.currentIndex())

        self.ui.out_textb.append("筛选完成")
        for input_filter in self.filter_list:
            self.ui.out_textb.append("筛选条件：" + input_filter)
            self.ui.out_textb.append("结果列数：" + str(len(df_out_dict.get(input_filter).columns)))
            self.show_view(df_out_dict.get(input_filter), 0)

    def open_file_dialog(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",  # 起始目录 (空字符串表示当前目录)
            "所有文件 (*.*);;文本文件 (*.txt);;Python 文件 (*.py)"  # 文件类型过滤器
        )

        if file_path:
            self.ui.file_lineEdit.setText(file_path)
            self.ui.sheet_lineEdit.setText("")

    def show_view(self, df, num):
        if df is None:
            return
        # 限制显示前num行
        if num == 0:
            df_to_display = df
        else:
            df_to_display = df.head(num)

        # 设置列数和行数
        self.ui.input_tableWidget.setColumnCount(len(df_to_display.columns))
        self.ui.input_tableWidget.setRowCount(len(df_to_display))

        # 将 DataFrame 的列名设置为表格的列名
        column_headers = df_to_display.columns.tolist()
        self.ui.input_tableWidget.setHorizontalHeaderLabels(column_headers)

        # 填充 TableWidget 的数据
        for row in range(len(df_to_display)):
            for col in range(len(df_to_display.columns)):
                value = str(df_to_display.iloc[row, col])
                self.ui.input_tableWidget.setItem(row, col, QTableWidgetItem(value))


    def open_excel_file(self):
        self.ui.out_textb.append("打开文件中......")
        file_name = self.ui.file_lineEdit.text()
        sheet_name = self.ui.sheet_lineEdit.text()

        if not os.path.exists(file_name):
            self.ui.out_textb.append("文件不存在：" + file_name)
            return
        if  not file_name.lower().endswith('.xlsx') and not file_name.lower().endswith('.xlsx'):
            self.ui.out_textb.append("文件必须是xlsx或xlx：" + file_name)
            return
        if self.excelUtil.set_file_name(file_name):
            self.data = self.excelUtil.open_file(sheet_name)

        if self.data is not None:
           self.show_view(self.data, 5)
           self.ui.out_textb.append("文件已打开......")
        else:
            self.ui.out_textb.append("文件打开失败......")



    def clicked_file_btn(self):
        # 创建线程，传入任务函数和回调
        task_thread = threading.Thread(target=self.open_excel_file, args=())
        task_thread.start()  # 启动线程

    def clicked_filter_btn(self):
        if self.data is None:
            return
        # 创建线程，传入任务函数和回调
        self.open_filter()
        # task_thread = threading.Thread(target=self.open_filter, args=())
        # task_thread.start()  # 启动线程
