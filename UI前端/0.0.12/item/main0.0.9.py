# 更新时间：2023年12月24日19:46:42
# 内容：答题卡还有些bug，完成了考研倒计时和习题页面，完成了用户头像上传，完成了个人页面0.0.10预计完成：答题卡bug
# from functools import partial
from PyQt5.QtCore import QDate
from logindemo import *     # 登录UI
from Yanti_v4_new import *      # 主页UI
from shiftpage import *     # 切换页面
from answersheet import *   # 答题卡
from finish import *        # 完成习题页面
from setinform import *     # 设置个人信息
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import QMessageBox
import requests
from datetime import datetime, timedelta    #
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
        url = "http://172.29.1.106:8000/login/"
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        params = {"phone_number": account, "password": password}
        res = requests.post(url=url, data=params)
        print(res.json())
        self.account_data = res.json()[0]

        if self.account_data["success"]:
            self.practice_interface = MainWindow(self)
            self.practice_interface.show()  # 显示新窗口
            self.close()
        else:
            # 创建一个消息框
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("错误")  # 设置窗口标题
            message_box.setText(self.account_data["info"])  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

        # account = self.ui.lineEdit.text()
        # password = self.ui.lineEdit_2.text()
        # if account == "123" and password == "123":
        #     print("登录成功")
        #     self.practice_interface = MainWindow(self)
        #     self.practice_interface.show()  # 显示新窗口
        #
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
        classes = ["C语言", "数据结构", "操作系统", "计算机网络", "计算机组成原理", "数据库", "政治"]
        for idx, btn in enumerate([self.ui.lx_class1_2, self.ui.lx_class2_2, self.ui.lx_class3_2,
                                   self.ui.lx_class4_2, self.ui.lx_class5_2, self.ui.lx_class6_2,
                                   self.ui.lx_class7_2]):
            btn.clicked.connect(lambda _, idx=idx: self.request_question(classes[idx]))

        wrong_btns = [self.ui.wr_class1, self.ui.wr_class2, self.ui.wr_class3,
                      self.ui.wr_class4, self.ui.wr_class5, self.ui.wr_class6,
                      self.ui.wr_class7]
        for idx, wrong_btn in enumerate(wrong_btns):
            wrong_btn.clicked.connect(lambda _, idx=idx: self.request_wrong(classes[idx]))

        self.ui.exercise_next_3.clicked.connect(self.set_question)
        self.ui.exercise_next_2.clicked.connect(self.set_wrong)
        self.ui.Bt_shiftacount.clicked.connect(self.switching_accounts)
        self.ui.Bt_error.clicked.connect(self.wrong_ex)
        self.ui.Bt_error_2.clicked.connect(self.wrong_ex)
        self.ui.Bt_email.clicked.connect(self.set_inform)
        self.ui.Bt_save.clicked.connect(self.set_information)
        self.ui.Bt_exercise_7.clicked.connect(self.support_author)
        self.ui.bt_sign_in.clicked.connect(self.sign_in)
        self.ui.Bt_change.clicked.connect(self.select_image)
        self.ui.Bt_exercise_8.clicked.connect(self.help)
        self.ui.Bt_exercise_6.clicked.connect(self.massage)
        self.practice_data = None
        self.wrong_data = None
        self.switching = None
        self.right_number = 0
        self.wrong_number = 0
        self.practice_id = 0
        self.wrong_id = 0
        self.countdown_timer()
        self.connections = {
            "A": None, "B": None, "C": None, "D": None
        }
        self.login = login
        self.show()
        self.page_switch_handler = PageSwitchHandler(self.ui)
        self.page_switch_handler.connection_button()
        self.button_answers = {
            self.ui.Bt_A_ex_3: 1, self.ui.Bt_B_ex_3: 2, self.ui.Bt_C_ex_3: 3, self.ui.Bt_D_ex_3: 4,
            self.ui.Bt_A_ex_2: 5, self.ui.Bt_B_ex_2: 6, self.ui.Bt_C_ex_2: 7, self.ui.Bt_D_ex_2: 8
        }
        self.update_answer_sheet = AnswerSheet(self.ui)
        self.finish_page = FinishPageSet(self.ui)
        num_questions = 25
        self.selected_options = [None] * num_questions  # 初始化选项数组
        for i in range(1, 26):
            getattr(self.ui, f'exercise_Q{i}_3').clicked.connect(lambda _, idx=i: self.select_question(idx))
            getattr(self.ui, f'exercise_Q{i}_2').clicked.connect(lambda _, idx=i: self.select_question(idx))
        # 头像提前显示
        self.set_inform = SetInform(self.ui)
        self.set_inform.avatar(self.login.account_data)
    # 主页倒计时更新
    def countdown_timer(self):
        # 当前日期
        current_date = datetime.now()
        target_date = datetime(current_date.year, 12, 23)

        # 如果今天已经过了目标日期，就将目标日期设置为下一年的12月23日
        if current_date > target_date:
            target_date = datetime(current_date.year + 1, 12, 23)

        # 计算距离目标日期的时间差
        time_left = target_date - current_date
        remaining_days = time_left.days
        # 获取当前的 HTML 内容
        current_html = self.ui.text_today_2.toHtml()

        # 寻找 span 标签内的文本部分
        start_index = current_html.find("<span ")
        end_index = current_html.find("</span>", start_index)
        if start_index != -1 and end_index != -1:
            # 更新文本内容
            new_text = str(remaining_days)
            start_text_index = current_html.find(">", start_index) + 1
            # updated_html = current_html[:start_text_index] + new_text + current_html[end_index:]
            centered_text = f'<div style="text-align: center;">{new_text}</div>'  # 居中文本框内容的 HTML 结构
            updated_html = current_html[:start_text_index] + centered_text + current_html[end_index:]
            self.ui.text_today_2.setHtml(updated_html)

        # 获取当前日期并格式化为指定格式
        current_date = QDate.currentDate().toString(Qt.ISODate)  # 获取当前日期
        formatted_date = QDate.fromString(current_date, Qt.ISODate).toString("yyyy/MM/dd")  # 格式化日期
        # 在 QLabel 中显示当前日期
        self.ui.label_5.setText(formatted_date)

    # 签到
    def sign_in(self):
        button_style = '''
            QPushButton{
                background-color: rgb(20, 153, 13);
                color: rgb(255, 255, 255);
                border-radius:15px
            }
        '''
        self.ui.bt_sign_in.setStyleSheet(button_style)
        self.ui.bt_sign_in.setText("签到天数：12")
        self.ui.bt_sign_in.setEnabled(False)    # 禁止用户使用该按钮

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

    # 用户点击答题卡按钮跳转题目现场
    def select_question(self, question_id):
        self.ui.stackedWidget_4.setCurrentIndex(1)
        print(question_id)
        if self.selected_options[question_id] is None:
            self.practice_id = question_id - 1
            print("is None")
            self.set_question()
        else:
            print("question_id =", question_id)
            self.practice_id = question_id - 1
            print("else")
            option = self.practice_data.json()[self.practice_id]["answer"]
            if option == "A":
                answer = self.practice_data.json()[self.practice_id]["option_1"]
            elif option == "B":
                answer = self.practice_data.json()[self.practice_id]["option_2"]
            elif option == "C":
                answer = self.practice_data.json()[self.practice_id]["option_3"]
            else:
                answer = self.practice_data.json()[self.practice_id]["option_4"]
            self.ui.exercise_title_3.setText(self.practice_data.json()[self.practice_id]["question_description"])  # 将题目映射到文本框中
            self.ui.Bt_A_ex_3.setText(self.practice_data.json()[self.practice_id]["option_1"])
            self.ui.Bt_B_ex_3.setText(self.practice_data.json()[self.practice_id]["option_2"])
            self.ui.Bt_C_ex_3.setText(self.practice_data.json()[self.practice_id]["option_3"])
            self.ui.Bt_D_ex_3.setText(self.practice_data.json()[self.practice_id]["option_4"])
            shift = {
                'A': 1, 'B': 2, 'C': 3, 'D': 4
            }
            if self.selected_options[self.practice_id] in shift:
                btn = shift[self.selected_options[self.practice_id]]
                self.judge_answer(answer, btn)
    def request_question(self, subject_name):
        self.wrong_number = 0
        self.right_number = 0
        url = "http://172.29.1.106:8000/question/"
        myParams = {"type": subject_name}   # 发送科目名称
        response = requests.get(url=url, params=myParams)
        self.practice_data = response
        print(response.json())
        self.practice_id = 0
        self.set_question()
        self.update_answer_sheet.change_button('exercise')


    def set_question(self):
        # 设置按钮初始样式为灰色的（用户未做选择前的样式）
        button_style = 'background-color: rgb(208, 206, 199);border-radius: 15px'
        buttons = [self.ui.Bt_A_ex_3, self.ui.Bt_B_ex_3, self.ui.Bt_C_ex_3, self.ui.Bt_D_ex_3]
        for button in buttons:
            button.setStyleSheet(button_style)

        # 每次返回25道题，做完25道题需要重新向后端请求题目
        if self.practice_id < 24:
            self.ui.sigle_or_more_3.setText("题号：" + str(self.practice_id + 1))
            self.practice_id += 1

        else:
            print("25题已做完")
            self.finish_page.practice_finish(self.right_number, self.wrong_number)
            self.ui.stackedWidget_4.setCurrentIndex(3)
            self.practice_id = 0

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
        else:
            answer = self.practice_data.json()[self.practice_id]["option_4"]


        self.ui.exercise_title_3.setText(question)  # 将题目映射到文本框中
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
        option_mapping = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D'
        }
        # 在判断按钮编号时，使用映射字典设置选项
        print(btn)
        if btn in option_mapping and btn < 5:
            # print("用户选择", self.selected_options[])
            self.selected_options[self.practice_id] = option_mapping[btn]
            print("题号:", self.practice_id, "用户选择：", self.selected_options[self.practice_id], "答案", answer)
        # else:
        #     print("77")
        #     self.selected_options[self.wrong_id] = option_mapping[btn]

        for button, btn_value in self.button_answers.items():
            if btn_value == btn:
                if button.text() != answer:
                    button.setStyleSheet('background-color: red;border-radius: 15px')
                    # 答错题加入错题集，改变答题卡
                    if btn < 5:
                        self.wrong_number = self.wrong_number + 1  # 用户答错题数量＋1
                        self.update_answer_sheet.no_button('exercise', self.practice_id)
                        self.put_question()
                    else:

                        self.update_answer_sheet.yes_button('wrong', self.wrong_id)
                else:
                    self.right_number = self.right_number + 1  # 用户答对题数量＋1
                    print("正确数：", self.right_number)
                    button.setStyleSheet('background-color: green;border-radius: 15px')
                    if btn < 5:
                        self.update_answer_sheet.yes_button('exercise', self.practice_id)
                    else:
                        # 错题做对则将题目id发到后端请求删除错题记录
                        url = "http://172.29.1.106:8000/mistake/"
                        myParams = {"user_id": self.login.account_data["id"], "question_id": self.wrong_data.json()[self.wrong_id]["id"]}  # 发送用户ID以及科目ID
                        res = requests.delete(url=url, data=myParams)
                        print(res.text)
                        self.update_answer_sheet.no_button('wrong', self.wrong_id)

            # 如果用户选错，将正确答案打印出来
            elif button.text() == answer:
                print("--------")
                print("111",  button.text())
                print("222", answer)
                button.setStyleSheet('background-color: green;border-radius: 15px')
                print("222")


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
    def wrong_ex(self, btn):
        url = "http://172.29.1.106:8000/error/"

        myParams = {"question_id": self.practice_data.json()[self.practice_id]["id"]}

        res = requests.put(url=url, data=myParams)
        if res.text == "\"OK\"":
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("该题错误反馈成功")  # 设置文本内容
            message_box.setIcon(QMessageBox.Information)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

        else:
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("该题错误反馈失败，请稍后再试")  # 设置文本内容
            message_box.setIcon(QMessageBox.Critical)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()

    # 用户请求错题
    def request_wrong(self, subject_name):
        user_id = self.login.account_data["id"]
        url = "http://172.29.1.106:8000/mistake/"
        myParams = {"user_id": user_id, "question_type": subject_name}  # 发送用户ID以及科目名称
        res = requests.get(url=url, params=myParams)
        self.wrong_data = res
        if len(self.wrong_data.json()):
            self.set_wrong()
            self.update_answer_sheet.change_button('wrong')
        else:
            message_box = QMessageBox()
            # 设置消息框的属性
            message_box.setWindowTitle("研题提醒")  # 设置窗口标题
            message_box.setText("没有该题型错题")  # 设置文本内容
            message_box.setIcon(QMessageBox.information)  # 设置图标为警告
            message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮为确定
            # 显示消息框
            message_box.exec()
            self.wrong_id = -1

    def set_wrong(self):
        # 初始化按钮样式为灰色未选择状态
        button_style = 'background-color: rgb(208, 206, 199);border-radius: 15px'
        buttons = [self.ui.Bt_A_ex_2, self.ui.Bt_B_ex_2, self.ui.Bt_C_ex_2, self.ui.Bt_D_ex_2]
        for button in buttons:
            button.setStyleSheet(button_style)

        # 每次最多返回25道题，做完25道题需要重新向后端请求题目，如果后一位没题目了，
        if self.wrong_id < 25 and self.wrong_data.json()[self.wrong_id+1]["id"] is not None:
            self.wrong_id += 1
            print("错题:", self.wrong_id)
        else:
            self.ui.stackedWidget_3.setCurrentIndex(3)
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
        self.connections["A"] = self.ui.Bt_A_ex_2.clicked.connect(lambda: self.judge_answer(answer, 5))
        self.connections["B"] = self.ui.Bt_B_ex_2.clicked.connect(lambda: self.judge_answer(answer, 6))
        self.connections["C"] = self.ui.Bt_C_ex_2.clicked.connect(lambda: self.judge_answer(answer, 7))
        self.connections["D"] = self.ui.Bt_D_ex_2.clicked.connect(lambda: self.judge_answer(answer, 8))

    def set_inform(self):
        self.set_inform.inform(self.login.account_data)

    def set_information(self):
        self.set_inform.set_information(self.login.account_data)

    def support_author(self):
        pixmap = QPixmap('收款码.jpg')  # 替换为你自己的图片路径
        self.ui.label_3.setPixmap(pixmap.scaled(300, 300))
        self.ui.label_3.setAlignment(Qt.AlignCenter)

    def select_image(self):
        self.set_inform.select_image()

    def help(self):
        self.set_inform.help()

    def massage(self):
        self.set_inform.app_massage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())

