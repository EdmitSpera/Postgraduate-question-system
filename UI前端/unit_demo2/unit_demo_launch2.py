#-*- codeing = utf-8 -*-
#@Time : 2023/12/8 11:43

#-*- codeing = utf-8 -*-
#@Time : 2023/12/7 19:53
#-*- codeing = utf-8 -*-
#@Time : 2023/12/6 20:35

from unit_demo2 import *
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
    def on_Bt_setting_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_Bt_main_1_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_1_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_1_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Bt_setting_1_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_Bt_main_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Bt_setting_2_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_Bt_main_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Bt_exercise_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_Bt_wrong_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Bt_setting_3_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def on_ex_class2_1_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def on_exercise_back_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def on_exercise_view_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
    def on_exercise_back2_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    def on_ex_class1_3_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def on_wrong_back_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)
    def on_wrong_view_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(2)
    def on_wrong_back_2_clicked(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
