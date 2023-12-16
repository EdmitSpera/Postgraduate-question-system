#-*- codeing = utf-8 -*-
#@Time : 2023/12/11 23:52
#-*- codeing = utf-8 -*-
#@Time : 2023/12/8 11:43
from PyQt5.uic import loadUi

#-*- codeing = utf-8 -*-
#@Time : 2023/12/7 19:53
#-*- codeing = utf-8 -*-
#@Time : 2023/12/6 20:35

from Yanti_v4 import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and not self.isMaximized():
            self.m_flag = True
            self.m_Position = event.pos()  # 获取鼠标相对窗口位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, mouse_event):
        if mouse_event.buttons() == QtCore.Qt.LeftButton and self.m_flag:
            self.move(self.mapToGlobal(mouse_event.pos() - self.m_Position))  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))




    def on_Bt_main_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Bt_mine_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_Bt_main_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Bt_mine_5_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_Bt_main_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_mine_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def on_Bt_main_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_4_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)




    def on_lx_class1_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class2_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class3_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class4_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class5_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class6_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_lx_class7_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_Bt_back_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)

    def on_Bt_continue_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)

    def on_answe_sheet_1_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(2)
    def on_answer_sheet_back_1_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)


    def on_wr_class1_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_wr_class2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_wr_class3_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_wr_class4_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_wr_class5_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_wr_class6_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def on_Bt_back_3_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def on_Bt_continue_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def on_answer_sheet_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(2)
    def on_answer_sheet_back_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
