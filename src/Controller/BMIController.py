from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QWidget

from res.BMI_ui import Ui_BMI_Form
import math


def define_bmi(bmi):
    """计算 BMI 并返回分类结果"""
    if bmi < 18.5:
        category = "低体重"
        font_format = "color:blue ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
    elif 18.5 <= bmi < 23.9:
        category = "正常"
        font_format = "color:green ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
    elif 24.0 <= bmi < 27.9:
        category = "超重"
        font_format = "color:orange ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
    else:
        category = "肥胖"
        font_format = "color:red ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
    return bmi, category, font_format


def define_fib4(age, fib4):
    if age is None:
        return 0
    if age <= 64:
        if fib4 < 1.3:
            state = " 排除"
            font_style = "color:green ; font-size: 35px; font-weight: bold; font-family: 微软雅黑; text-align: center;"
        elif 1.3 <= fib4 <= 2.67:
            state = " 进一步评估"
            font_style = "color:orange ; font-size: 35px; font-weight: bold; font-family: 微软雅黑; text-align: center;"
        else :
            state = " 可能"
            font_style = "color:red ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
    else:
        if fib4 < 2.0:
            state = " 排除"
            font_style = "color:green ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
        elif 2.0 <= fib4 <= 2.67:
            state = " 进一步评估"
            font_style = "color:orange ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"
        else :
            state = " 可能"
            font_style = "color:red ; font-size: 35px; font-weight: bold; font-family: 微软雅黑;text-align: center;"

    return  state, font_style

class BMIController(QWidget, Ui_BMI_Form):
    def __init__(self):
        super().__init__()
        self.fib_4 = 0.0
        self.setupUi(self)

        self.ts = 0.0
        self.bmi = 0.0
        self.arp = 0.0

        self.initialize_ui()

    def initialize_ui(self):
        self.height_lineEdit.setValidator(QDoubleValidator())
        self.weight_lineEdit.setValidator(QDoubleValidator())

        self.AST_lineEdit.setValidator(QDoubleValidator())
        self.PLT_lineEdit.setValidator(QDoubleValidator())
        self.age_lineEdit.setValidator(QIntValidator())
        self.bcc_lineEdit.setValidator(QDoubleValidator())

        self.fib_alt_lineEdit.setValidator(QDoubleValidator())
        self.fib_ast_lineEdit.setValidator(QDoubleValidator())

        self.si_lineEdit.setValidator(QDoubleValidator())
        self.fec_lineEdit.setValidator(QDoubleValidator())

        self.height_lineEdit.textChanged.connect(self.calc_bmi)
        self.weight_lineEdit.textChanged.connect(self.calc_bmi)

        self.height_lineEdit.editingFinished.connect(self.log_bmi)
        self.weight_lineEdit.editingFinished.connect(self.log_bmi)

        self.AST_lineEdit.textChanged.connect(self.calc_arp)
        self.PLT_lineEdit.textChanged.connect(self.calc_arp)

        self.AST_lineEdit.editingFinished.connect(self.log_arp)
        self.PLT_lineEdit.editingFinished.connect(self.log_arp)

        self.age_lineEdit.textChanged.connect(self.calc_fib_4)
        self.bcc_lineEdit.textChanged.connect(self.calc_fib_4)
        self.fib_alt_lineEdit.textChanged.connect(self.calc_fib_4)
        self.fib_ast_lineEdit.textChanged.connect(self.calc_fib_4)

        self.age_lineEdit.editingFinished.connect(self.log_fib4)
        self.bcc_lineEdit.editingFinished.connect(self.log_fib4)
        self.fib_alt_lineEdit.editingFinished.connect(self.log_fib4)
        self.fib_ast_lineEdit.editingFinished.connect(self.log_fib4)

        self.si_lineEdit.textChanged.connect(self.calc_ts)
        self.fec_lineEdit.textChanged.connect(self.calc_ts)

        self.si_lineEdit.editingFinished.connect(self.log_ts)
        self.fec_lineEdit.editingFinished.connect(self.log_ts)

        self.fl_checkBox.clicked.connect(lambda:self.hbv_change(0))
        self.shbv_checkBox.clicked.connect(lambda:self.hbv_change(1))

    def hbv_change(self, num):
        if num == 0 and self.fl_checkBox.isChecked():
            self.shbv_checkBox.setChecked(False)
        if num == 1 and self.shbv_checkBox.isChecked():
            self.fl_checkBox.setChecked(False)



    def calc_bmi(self):
        if self.height_lineEdit.text() == "" or self.weight_lineEdit.text() == "":
            return
        height = float(self.height_lineEdit.text())
        weight = float(self.weight_lineEdit.text())
        if weight == 0:
            self.bmi = 0
            self.bmi_lcdNumber.display(0)
            self.bmi_res_label.setText("")
            return
        bmi = weight / (height * height)
        self.bmi = bmi
        self.bmi_lcdNumber.display(bmi)
        bmi_res = define_bmi(self.bmi)
        self.bmi_res_label.setAlignment(Qt.AlignCenter)
        self.bmi_res_label.setText(bmi_res[1])
        self.bmi_res_label.setStyleSheet(bmi_res[2])

    def log_bmi(self):
        if self.height_lineEdit.text() == "" or self.weight_lineEdit.text() == "" or self.bmi == 0:
            return
        self.textBrowser.append("身高: " + self.height_lineEdit.text() +"   体重: " + self.weight_lineEdit.text() + "  ===>   BMI: " + str(self.bmi))

    def log_arp(self):
        if self.AST_lineEdit.text() == "" or self.PLT_lineEdit.text() == "" or self.arp == 0:
            return
        self.textBrowser.append("AST: " + self.AST_lineEdit.text() +"   PLT: " + self.PLT_lineEdit.text() + "  ===>   天门冬氨酸氨基转移酶与血小板比值: " + str(self.arp))

    def log_fib4(self):
        if self.fib_4 == 0 or self.age_lineEdit.text() == "" or self.bcc_lineEdit.text() == "" or self.fib_alt_lineEdit.text() == ""  or self.fib_ast_lineEdit.text() == "":
            return
        self.textBrowser.append("年龄: " + self.age_lineEdit.text() +"   血小板计数: " + self.bcc_lineEdit.text()
                                + "   ALT: " + self.fib_alt_lineEdit.text() + "   AST: " + self.fib_ast_lineEdit.text()
                                + "  ===>   FIB-4慢性肝病患者肝纤维化: " + str(self.fib_4))

    def log_ts(self):
        if self.ts == 0 or self.si_lineEdit.text() == "" or self.fec_lineEdit.text() == "":
            return
        self.textBrowser.append("血清铁: " + self.si_lineEdit.text() +"   总铁结合能力: " + self.fec_lineEdit.text()
                                + "  ===>   转铁蛋白饱和度: " + str(self.ts))

    def calc_arp(self):
        if  self.AST_lineEdit.text() == "" or self.PLT_lineEdit.text() == "" :
            return

        ast = float(self.AST_lineEdit.text())
        plt = float(self.PLT_lineEdit.text())
        if plt == 0:
            self.arp = 0
            self.arp_lcdNumber.display(self.arp)
            return
        arp = ast / plt * 100
        self.arp = arp
        self.arp_lcdNumber.display(arp)

    def calc_fib_4(self):
        if self.age_lineEdit.text() == "" or self.bcc_lineEdit.text() == "" or self.fib_alt_lineEdit.text() == ""  or self.fib_ast_lineEdit.text() == "":
            return
        age = float(self.age_lineEdit.text())
        bcc = float(self.bcc_lineEdit.text())
        fib_alt = float(self.fib_alt_lineEdit.text())
        fib_ast = float(self.fib_ast_lineEdit.text())

        if bcc * math.sqrt(fib_alt) == 0:
            self.fib_4 = 0
            self.fib4_lcdNumber.display(self.fib_4)
            self.fib_res_label.setText("")
            return
        fib_4 = (age * fib_ast) / (bcc * math.sqrt(fib_alt))
        self.fib_4 = fib_4
        self.fib4_lcdNumber.display(fib_4)

        res = define_fib4(age, fib_4)
        self.fib_res_label.setText(res[0])
        self.fib_res_label.setStyleSheet(res[1])

    def calc_ts(self):
        if self.si_lineEdit.text() == "" or self.fec_lineEdit.text() == "":
            return

        si = float(self.si_lineEdit.text())
        fec = float(self.fec_lineEdit.text())
        if fec == 0:
            self.ts = 0
            self.ts_lcdNumber.display(self.ts)
            return

        ts = si / fec * 100
        self.ts = ts
        self.ts_lcdNumber.display(ts)