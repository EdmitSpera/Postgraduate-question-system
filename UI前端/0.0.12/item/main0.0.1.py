# 更新时间：
from 练习UI1 import *
from 错题UI1 import *
from 错题UI2 import *
from 练习UI2 import *
from 答题卡UI1 import *
from logindemo import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import requests
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow_2()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.login_button.clicked.connect(self.go_to_inter)
        # self.ui.account_had.clicked.connect(self.frameController)
        # self.ui.signin_button.clicked.connect(self.frameController)   #使用函数调用时候可以使用，适用于page多的情况
        self.practice_interface = None  # 添加一个实例变量来保存InterfaceWindow的引用
        self.show()
    def go_to_inter(self):
        # url = "http://172.29.1.106:8000/login/"
        account=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        # params = {"phone_number": account, "password": password}
        # res = requests.post(url=url, data=params)
        # if res.text == "登录成功":
        #     self.practice_interface = PracticeWindow()
        #     self.practice_interface.show()  # 显示新窗口
        #
        #     self.close()
        # else:
        #     # 创建一个消息框
        #     message_box = QMessageBox()
        #     # 设置消息框的属性
        #     message_box.setWindowTitle("错误")  # 设置窗口标题
        #     message_box.setText(res.text)  # 设置文本内容
        #     message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
        #     message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
        #     # 显示消息框
        #     message_box.exec()
        if account =="123" and password=="123":
            self.practice_interface = PracticeWindow()
            self.practice_interface.show()  # 显示新窗口

            self.close()
        else:
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("错误")  # 设置窗口标题
            message_box.setText("账号或密码错误")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()
        # 拖拽界面

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

    # 点击注册按钮
    def frameController(self):  # 页面控制函数
        sender = self.sender().objectName()  # 获取当前信号 sender
        index = {
            "account_had": 0,  # page_0
            "signin_button": 1,  # page_1
            # "pushButton_3": 2,  # page_2
        }
        try:
            self.ui.stackedWidget.setCurrentIndex(index[sender])  # 根据信号 index 设置所显示的页面
        except KeyError:
            print(f"未找到信号 {sender} 对应的页面索引")


class PracticeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_practice1()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Bt_wrong.clicked.connect(self.go_to_wrong)
        self.ui.ex_class1.clicked.connect(self.go_to_practice)
        self.show()

    def go_to_practice(self):
        self.practice_window = PracticeWindow2()
        self.practice_window.show()
        self.close()

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

    def go_to_wrong(self):
        self.wrong_interface = WrongWindow()
        self.wrong_interface.show()
        self.close()

class PracticeWindow2(PracticeWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_practice2()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Bt_wrong.clicked.connect(self.go_to_wrong)
        self.ui.Bt_exercise.clicked.connect(self.go_to_practice)
        self.show()
    def go_to_wrong(self):
        super().go_to_wrong()
        self.close()

    def go_to_practice(self):
        self.practice_window = PracticeWindow()
        self.practice_window.show()
        self.close()


class WrongWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_wrong()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Bt_exercise.clicked.connect(self.go_to_practice)
        self.ui.wr_class1.clicked.connect(self.go_to_wrong2)
        self.show()

    def go_to_practice(self):
        self.practice_interface = PracticeWindow()
        self.practice_interface.show()
        self.close()

    def go_to_wrong2(self):
        self.wrong_interface2 = WrongWindow2()
        self.wrong_interface2.show()
        self.close()

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


class WrongWindow2(WrongWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_wrong2()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.Bt_exercise.clicked.connect(self.go_to_practice)
        self.ui.Bt_wrong.clicked.connect(self.go_to_wrong)
        self.ui.wrong_view.clicked.connect(self.go_to_answer)
        self.show()

    def go_to_practice(self):
        # 继承父类，跳转到练习页面
        super().go_to_practice()
        self.close()

    def go_to_wrong(self):
        self.wrong_interface = WrongWindow()
        self.wrong_interface.show()
        self.close()

    def go_to_answer(self):
        self.answer_interface = AnswerWindow()
        self.answer_interface.show()
        self.close()

class AnswerWindow(WrongWindow2):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_answer1()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.Bt_exercise.clicked.connect(self.go_to_practice)
        self.ui.Bt_wrong.clicked.connect(self.go_to_wrong)
        self.ui.Bt_back_wr.clicked.connect(self.back_to_window)
        self.show()

    def go_to_practice(self):
        # 继承父类，跳转到练习页面
        super().go_to_practice()
        self.close()

    def go_to_wrong(self):
        self.wrong_interface = WrongWindow()
        self.wrong_interface.show()
        self.close()

    def back_to_window(self):
        self.wrong_interface2 = WrongWindow2()
        self.wrong_interface2.show()
        self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win =LoginWindow()
    sys.exit(app.exec_())

