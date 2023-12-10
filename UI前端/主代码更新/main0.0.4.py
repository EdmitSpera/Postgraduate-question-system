# 更新时间：
from logindemo import *
from unit_demo2 import  *
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
        self.ui.login_button.clicked.connect(self.go_to_main)
        self.practice_interface = None  # 添加一个实例变量来保存InterfaceWindow的引用
        self.show()
    def go_to_main(self):
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
            self.practice_interface = MainWindow()
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

    # 用户注册
    # def register(self):
    #     account = self.ui.account_2.text()
    #     password = self.ui.password_2.text()
    #     confirm = self.ui.password_confirmed.text()
    #     if password == confirm:
    #         url = "http://172.29.1.106:8000/register/"
    #         params = {"account":account,"password":password}
    #         res = requests.post(url=url,data=params)
    #         if res.text == "注册成功":
    #             self.ui.stackedWidget1.setCurrentIndex(0)


    # 页面拖拽
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
        self.ui.stackedWidget1.setCurrentIndex(1)

    def on_account_had_clicked(self):
        self.ui.stackedWidget1.setCurrentIndex(0)

class MainWindow(QMainWindow):
    IP = 0  # 题目序号
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.exercise_next.clicked.connect(self.request_question)

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

    def request_question(self):
        MainWindow.IP += 1  # 从第一题开始（可修改从做题进度开始）
        self.ui.Bt_A_ex.setStyleSheet('background-color: lightgray')
        self.ui.Bt_B_ex.setStyleSheet('background-color: lightgray')
        self.ui.Bt_C_ex.setStyleSheet('background-color: lightgray')
        self.ui.Bt_D_ex.setStyleSheet('background-color: lightgray')
        url = "http://cainfose.cn/question/"
        subjectName = "数据结构"
        myParams = {"type": subjectName}   # 发送科目名称
        response = requests.get(url=url, params=myParams)
        print(response.json())

        question = response.json()[MainWindow.IP]["question_description"]   # 题目
        option = response.json()[MainWindow.IP]["answer"]     # 答案
        if option == "A":
            answer = response.json()[MainWindow.IP]["option_1"]
        elif option == "B":
            answer = response.json()[MainWindow.IP]["option_2"]
        elif option == "C":
            answer = response.json()[MainWindow.IP]["option_3"]
        elif option == "D":
            answer = response.json()[MainWindow.IP]["option_4"]
        else:
            print("E")
        self.ui.exercise_title.setText(question)
        self.ui.Bt_A_ex.setText(response.json()[MainWindow.IP]["option_1"])
        self.ui.Bt_B_ex.setText(response.json()[MainWindow.IP]["option_2"])
        self.ui.Bt_C_ex.setText(response.json()[MainWindow.IP]["option_3"])
        self.ui.Bt_D_ex.setText(response.json()[MainWindow.IP]["option_4"])

        self.ui.Bt_A_ex.clicked.connect(lambda: self.judge_answer(answer))
        self.ui.Bt_B_ex.clicked.connect(lambda: self.judge_answer(answer))
        self.ui.Bt_C_ex.clicked.connect(lambda: self.judge_answer(answer))
        self.ui.Bt_D_ex.clicked.connect(lambda: self.judge_answer(answer))


    def judge_answer(self,answer):

        sender = self.sender()  # 获取触发信号的按钮
        print(sender.text())
        print(answer)
        if sender.text() == answer:
            sender.setStyleSheet('background-color: green')   # 答案正确时按钮变绿
        else:
            sender.setStyleSheet('background-color: red')  # 答案错误时按钮变红

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win =LoginWindow()
    sys.exit(app.exec_())

