# 更新时间：
from functools import partial

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
        self.ui.signin.clicked.connect(self.register)
        self.practice_interface = None  # 添加一个实例变量来保存InterfaceWindow的引用
        self.show()
    def go_to_main(self):
        # url = "http://172.29.1.106:8000/login/"
        # account = self.ui.lineEdit.text()
        # password = self.ui.lineEdit_2.text()
        # params = {"phone_number": account, "password": password}
        # res = requests.post(url=url, data=params)
        # if res.text == "登录成功":
        #     self.practice_interface = MainWindow()
        #     self.practice_interface.show()  # 显示新窗口
        #     self.close()
        # else:
        #     # 创建一个消息框
        #     message_box = QMessageBox()
        #     # 设置消息框的属性
        #     message_box.setWindowTitle("错误")  # 设置窗口标题
        #     message_box.setText("账号或密码错误")  # 设置文本内容
        #     message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
        #     message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
        #     # 显示消息框
        #     message_box.exec()

        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if account == "123" and password == "123":
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
    def register(self):
        account = self.ui.account_2.text()
        password = self.ui.password_2.text()
        confirm = self.ui.password_confirmed.text()
        if password == confirm:
            url = "http://172.29.1.106:8000/register/"
            params = {"phone_number": account, "password": password}
            res = requests.post(url=url, data=params)
            if res.text == "注册成功":
                self.ui.stackedWidget1.setCurrentIndex(0)

            else:
                # 创建一个消息框
                message_box = QMessageBox()
                # 设置消息框的属性
                message_box.setWindowTitle("错误")  # 设置窗口标题
                message_box.setText(res.text)  # 设置文本内容
                message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
                message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
                # 显示消息框
                message_box.exec()


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
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.ex_class2_1.clicked.connect(partial(self.request_question, "政治"))
        self.ui.exercise_next.clicked.connect(self.set_question)
        self.data = None
        self.IP = -1
        self.connections = {
            "A": None,
            "B": None,
            "C": None,
            "D": None
        }
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

    def request_question(self, subjectName):

        url = "http://172.29.1.106:8000/question/"
        myParams = {"type": subjectName}   # 发送科目名称
        response = requests.get(url=url, params=myParams)
        self.data = response
        print(response.json())
        self.set_question()


    def set_question(self):
        self.ui.Bt_A_ex.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_B_ex.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_C_ex.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_D_ex.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')

        # 每次返回25道题，做完25道题需要重新向后端请求题目
        if self.IP < 25:
            self.IP += 1
            print(self.IP)
        else:
            self.IP = -1
            return 0
        question = self.data.json()[self.IP]["question_description"]   # 题目
        option = self.data.json()[self.IP]["answer"]     # 数据库中存储的答案选项

        # 将答案选项转为选项内容进行匹配
        if option == "A":
            answer = self.data.json()[self.IP]["option_1"]
        elif option == "B":
            answer = self.data.json()[self.IP]["option_2"]
        elif option == "C":
            answer = self.data.json()[self.IP]["option_3"]
        elif option == "D":
            answer = self.data.json()[self.IP]["option_4"]
        else:
            print("E")

        self.ui.exercise_title.setText(question)
        self.ui.Bt_A_ex.setText(self.data.json()[self.IP]["option_1"])
        self.ui.Bt_B_ex.setText(self.data.json()[self.IP]["option_2"])
        self.ui.Bt_C_ex.setText(self.data.json()[self.IP]["option_3"])
        self.ui.Bt_D_ex.setText(self.data.json()[self.IP]["option_4"])
        print("题目刷新成功")

        # 断开之前的链接
        for btn, connection in self.connections.items():
            if connection is not None:
                getattr(self.ui, f"Bt_{btn}_ex").clicked.disconnect(connection)

        # 建立新连接
        self.connections["A"] = self.ui.Bt_A_ex.clicked.connect(lambda: self.judge_answer(answer, 1))
        self.connections["B"] = self.ui.Bt_B_ex.clicked.connect(lambda: self.judge_answer(answer, 2))
        self.connections["C"] = self.ui.Bt_C_ex.clicked.connect(lambda: self.judge_answer(answer, 3))
        self.connections["D"] = self.ui.Bt_D_ex.clicked.connect(lambda: self.judge_answer(answer, 4))


    # 判断答案是否正确
    def judge_answer(self, answer, btn):

        if btn == 1:
            if self.ui.Bt_A_ex.text() != answer:
                self.ui.Bt_A_ex.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        elif btn == 2:
            if self.ui.Bt_B_ex.text() != answer:
                self.ui.Bt_B_ex.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        elif btn == 3:
            if self.ui.Bt_C_ex.text() != answer:
                self.ui.Bt_C_ex.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        else:
            if self.ui.Bt_D_ex.text() != answer:
                self.ui.Bt_D_ex.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()


        if self.ui.Bt_A_ex.text() == answer:
            self.ui.Bt_A_ex.setStyleSheet('background-color: green;border-radius: 15px')
        elif self.ui.Bt_B_ex.text() == answer:
            self.ui.Bt_B_ex.setStyleSheet('background-color: green;border-radius: 15px')
        elif self.ui.Bt_C_ex.text() == answer:
            self.ui.Bt_C_ex.setStyleSheet('background-color: green;border-radius: 15px')
        else:
            self.ui.Bt_D_ex.setStyleSheet('background-color: green;border-radius: 15px')

    # 将错题put给后端，加入数据库中
    def put_question(self):
        url = "http://172.29.1.106:8000/question/"
        myParams = {"user_id": "3", "question_id": self.data.json()[self.IP]["id"]}  # 发送用户ID以及科目ID
        res = requests.put(url=url, data=myParams)
        print(res.text)
        if res.text == "\"OK\"":
            print("该题加入用户错题集成功")
        else:
            print("该题已在用户错题集中")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())

