#-*- codeing = utf-8 -*-
#@Time : 2023/12/6 20:35

from logindemo import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow_2()
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

    def on_signin_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_account_had_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
