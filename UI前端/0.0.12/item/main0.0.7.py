# 更新时间：
from functools import partial


from logindemo import *
from Yanti_v41 import *
from shiftpage import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
import requests
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

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
        self.account_data = None
        self.show()

    def go_to_main(self):
        # url = "http://172.29.1.106:8000/login/"
        # account = self.ui.lineEdit.text()
        # password = self.ui.lineEdit_2.text()
        # params = {"phone_number": account, "password": password}
        # res = requests.post(url=url, data=params)
        # print(res.json())
        # self.account_data = res.json()[0]
        #
        # if self.account_data["success"]:
        #     self.practice_interface = MainWindow(self)
        #     self.practice_interface.show()  # 显示新窗口
        #     self.close()
        # else:
        #     # 创建一个消息框
        #     message_box = QMessageBox()
        #     # 设置消息框的属性
        #     message_box.setWindowTitle("错误")  # 设置窗口标题
        #     message_box.setText(self.account_data["info"])  # 设置文本内容
        #     message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
        #     message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
        #     # 显示消息框
        #     message_box.exec()
        #
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if account == "123" and password == "123":
            print("登录成功")
            self.practice_interface = MainWindow(self)
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
        print("注册测试")
        if password == confirm:
            print("密码一致")
            url = "http://172.29.1.106:8000/register/"
            params = {"phone_number": account, "password": password}
            res = requests.post(url=url, data=params)
            print(res.json())
            self.account_data = res.json()[0]

            print(self.account_data["success"])
            if self.account_data["success"]:
                self.ui.stackedWidget1.setCurrentIndex(0)
                self.ui.lineEdit.setText(account)
                print("注册成功")
            else:
                # 创建一个消息框
                print("注册失败")
                message_box = QMessageBox()
                # 设置消息框的属性
                message_box.setWindowTitle("错误")  # 设置窗口标题
                message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
                if "phone_number" in self.account_data.keys():

                    message_box.setText("手机号已存在")  # 设置文本内容
                    pass
                elif "password" in self.account_data.keys():
                    message_box.setText("密码长度不能少于8个字符")
                    pass
                message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
                # 显示消息框
                message_box.exec()
        else:
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("错误")  # 设置窗口标题
            message_box.setText("密码不一致，请重试")  # 设置文本内容
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

    def __init__(self, login):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.lx_class1_2.clicked.connect(partial(self.request_question, "C语言"))
        self.ui.lx_class2_2.clicked.connect(partial(self.request_question, "数据结构"))
        self.ui.lx_class3_2.clicked.connect(partial(self.request_question, "操作系统"))
        self.ui.lx_class4_2.clicked.connect(partial(self.request_question, "计算机网络"))
        self.ui.lx_class5_2.clicked.connect(partial(self.request_question, "计算机组成原理"))
        self.ui.lx_class6_2.clicked.connect(partial(self.request_question, "数据库"))
        self.ui.lx_class7_2.clicked.connect(partial(self.request_question, "政治"))
        self.ui.wr_class1.clicked.connect(partial(self.request_wrong, "C语言"))
        self.ui.wr_class2.clicked.connect(partial(self.request_wrong, "数据结构"))
        self.ui.wr_class3.clicked.connect(partial(self.request_wrong, "操作系统"))
        self.ui.wr_class4.clicked.connect(partial(self.request_wrong, "计算机网络"))
        self.ui.wr_class5.clicked.connect(partial(self.request_wrong, "计算机组成原理"))
        self.ui.wr_class6.clicked.connect(partial(self.request_wrong, "数据库"))
        self.ui.wr_class7.clicked.connect(partial(self.request_wrong, "政治"))
        self.ui.exercise_next_3.clicked.connect(self.set_question)
        self.ui.exercise_next_2.clicked.connect(self.set_wrong)
        self.ui.Bt_shiftacount.clicked.connect(self.switching_accounts)
        self.ui.Bt_error.clicked.connect(self.wrong_ex)
        self.practice_data = None
        self.wrong_data = None
        self.switching = None
        self.practice_id = -1
        self.wrong_id = -1
        self.countdown_timer()
        self.connections = {
            "A": None,
            "B": None,
            "C": None,
            "D": None
        }
        self.login = login
        self.show()
        self.page_switch_handler = PageSwitchHandler(self.ui)
        self.page_switch_handler.connection_button()


    # 主页倒计时更新
    def countdown_timer(self):
        # 获取当前的 HTML 内容
        current_html = self.ui.text_today_2.toHtml()

        # 寻找 span 标签内的文本部分
        start_index = current_html.find("<span ")
        end_index = current_html.find("</span>", start_index)
        if start_index != -1 and end_index != -1:
            # 更新文本内容（替换现有文本为新文本）
            new_text = "6"
            start_text_index = current_html.find(">", start_index) + 1
            updated_html = current_html[:start_text_index] + new_text + current_html[end_index:]
            self.ui.text_today_2.setHtml(updated_html)

    # 切换用户
    def switching_accounts(self):
        self.switching = LoginWindow()
        self.switching.show()
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

    def request_question(self, subject_name):

        url = "http://172.29.1.106:8000/question/"
        myParams = {"type": subject_name}   # 发送科目名称
        response = requests.get(url=url, params=myParams)
        self.practice_data = response
        print(response.json())
        self.set_question()

    def set_question(self):
        self.ui.Bt_A_ex_3.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_B_ex_3.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_C_ex_3.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_D_ex_3.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')

        # 每次返回25道题，做完25道题需要重新向后端请求题目
        if self.practice_id < 25:
            self.practice_id += 1
            print(self.practice_id)
        else:
            print("25题已做完")
            self.ui.stackedWidget_4.setCurrentIndex(3)
            self.practice_id = -1

            return 0
        question = self.practice_data.json()[self.practice_id]["question_description"]   # 题目
        option = self.practice_data.json()[self.practice_id]["answer"]     # 数据库中存储的答案选项

        # 将答案选项转为选项内容进行匹配
        if option == "A":
            answer = self.practice_data.json()[self.practice_id]["option_1"]
        elif option == "B":
            answer = self.practice_data.json()[self.practice_id]["option_2"]
        elif option == "C":
            answer = self.practice_data.json()[self.practice_id]["option_3"]
        elif option == "D":
            answer = self.practice_data.json()[self.practice_id]["option_4"]
        else:
            print("E")

        self.ui.exercise_title_3.setText(question)
        self.ui.Bt_A_ex_3.setText(self.practice_data.json()[self.practice_id]["option_1"])
        self.ui.Bt_B_ex_3.setText(self.practice_data.json()[self.practice_id]["option_2"])
        self.ui.Bt_C_ex_3.setText(self.practice_data.json()[self.practice_id]["option_3"])
        self.ui.Bt_D_ex_3.setText(self.practice_data.json()[self.practice_id]["option_4"])

        # 断开之前的链接
        for btn, connection in self.connections.items():
            if connection is not None:
                getattr(self.ui, f"Bt_{btn}_ex_3").clicked.disconnect(connection)
        # 建立新连接
        self.connections["A"] = self.ui.Bt_A_ex_3.clicked.connect(lambda: self.judge_answer(answer, 1))
        self.connections["B"] = self.ui.Bt_B_ex_3.clicked.connect(lambda: self.judge_answer(answer, 2))
        self.connections["C"] = self.ui.Bt_C_ex_3.clicked.connect(lambda: self.judge_answer(answer, 3))
        self.connections["D"] = self.ui.Bt_D_ex_3.clicked.connect(lambda: self.judge_answer(answer, 4))

    # 判断答案是否正确
    def judge_answer(self, answer, btn):

        if btn == 1:
            if self.ui.Bt_A_ex_3.text() != answer:
                self.ui.Bt_A_ex_3.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        elif btn == 2:
            if self.ui.Bt_B_ex_3.text() != answer:
                self.ui.Bt_B_ex_3.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        elif btn == 3:
            if self.ui.Bt_C_ex_3.text() != answer:
                self.ui.Bt_C_ex_3.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()
        else:
            if self.ui.Bt_D_ex_3.text() != answer:
                self.ui.Bt_D_ex_3.setStyleSheet('background-color: red;border-radius: 15px')
                self.put_question()


        if self.ui.Bt_A_ex_3.text() == answer:
            self.ui.Bt_A_ex_3.setStyleSheet('background-color: green;border-radius: 15px')
        elif self.ui.Bt_B_ex_3.text() == answer:
            self.ui.Bt_B_ex_3.setStyleSheet('background-color: green;border-radius: 15px')
        elif self.ui.Bt_C_ex_3.text() == answer:
            self.ui.Bt_C_ex_3.setStyleSheet('background-color: green;border-radius: 15px')
        else:
            self.ui.Bt_D_ex_3.setStyleSheet('background-color: green;border-radius: 15px')

    # 将错题put给后端，加入数据库中
    def put_question(self):
        url = "http://172.29.1.106:8000/question/"
        myParams = {"user_id": self.login.account_data["id"], "question_id": self.practice_data.json()[self.practice_id]["id"]}  # 发送用户ID以及科目ID
        res = requests.put(url=url, data=myParams)
        if res.text == "\"OK\"":
            print("该题加入用户错题集成功")
        else:
            print("该题已在用户错题集中")

    # 习题报错按钮
    def wrong_ex(self):
        url = "http://172.29.1.106:8000/error/"
        myParams = {"question_id": self.practice_data.json()[self.practice_id]["id"]}
        res = requests.put(url=url, data=myParams)

        if res.text == "OK":
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("")  # 设置窗口标题
            message_box.setText("该题错误反馈成功")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

        else:
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("")  # 设置窗口标题
            message_box.setText("该题错误反馈失败，请稍后再试")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    # 用户请求错题
    def request_wrong(self, subject_name):
        print(self.login.account_data["id"])
        user_id = self.login.account_data["id"]
        url = "http://172.29.1.106:8000/mistake/"
        myParams = {"user_id": user_id, "question_type": subject_name}  # 发送用户ID以及科目名称
        res = requests.get(url=url, params=myParams)
        self.wrong_data = res
        print("错题集：")
        print(res.json())
        if len(self.wrong_data.json()):
            self.set_wrong()
        else:
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("注意")  # 设置窗口标题
            message_box.setText("没有该题型错题")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    def set_wrong(self):
        self.ui.Bt_A_ex_2.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_B_ex_2.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_C_ex_2.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')
        self.ui.Bt_D_ex_2.setStyleSheet('background-color: rgb(208, 206, 199);border-radius: 15px')

        # 每次最多返回25道题，做完25道题需要重新向后端请求题目，如果后一位没题目了，
        if self.wrong_id < 25 and self.wrong_data.json()[self.wrong_id+1]["id"] is not None:
            self.wrong_id += 1
        else:
            self.wrong_id = -1
            print("已无错题")
            return 0
        question = self.wrong_data.json()[self.wrong_id]["question_description"]   # 题目
        option = self.wrong_data.json()[self.wrong_id]["answer"]     # 数据库中存储的答案选项

        # 将答案选项转为选项内容进行匹配
        if option == "A":
            answer = self.wrong_data.json()[self.wrong_id]["option_1"]
        elif option == "B":
            answer = self.wrong_data.json()[self.wrong_id]["option_2"]
        elif option == "C":
            answer = self.wrong_data.json()[self.wrong_id]["option_3"]
        else:
            answer = self.wrong_data.json()[self.wrong_id]["option_4"]


        self.ui.exercise_title_2.setText(question)
        self.ui.Bt_A_ex_2.setText(self.wrong_data.json()[self.wrong_id]["option_1"])
        self.ui.Bt_B_ex_2.setText(self.wrong_data.json()[self.wrong_id]["option_2"])
        self.ui.Bt_C_ex_2.setText(self.wrong_data.json()[self.wrong_id]["option_3"])
        self.ui.Bt_D_ex_2.setText(self.wrong_data.json()[self.wrong_id]["option_4"])

        # 断开之前的链接
        for btn, connection in self.connections.items():
            if connection is not None:
                getattr(self.ui, f"Bt_{btn}_ex_2").clicked.disconnect(connection)
        # 建立新连接
        self.connections["A"] = self.ui.Bt_A_ex_2.clicked.connect(lambda: self.judge_answer(answer, 1))
        self.connections["B"] = self.ui.Bt_B_ex_2.clicked.connect(lambda: self.judge_answer(answer, 2))
        self.connections["C"] = self.ui.Bt_C_ex_2.clicked.connect(lambda: self.judge_answer(answer, 3))
        self.connections["D"] = self.ui.Bt_D_ex_2.clicked.connect(lambda: self.judge_answer(answer, 4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())

