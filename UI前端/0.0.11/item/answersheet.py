class AnswerSheet:
    def __init__(self, ui):
        self.ui = ui

    def change_button(self, kind):
        # 将答题卡中的题目按钮都设为灰色未做题样式
        button_style = '''
            QPushButton{
                background-color: rgb(195, 195, 195);
                border-radius:15px}
            QPushButton:pressed{
                padding-left:5px;
                padding-top:5px;
            }
            QPushButton:hover{
                background-color: rgb(217, 217, 217);
                border-radius:15px
            }
        '''
        # 将练习部分的答题卡按钮样式都更改
        if kind == 'exercise':
            buttons = [getattr(self.ui, f'exercise_Q{i}_3') for i in range(1, 26)]
            for button in buttons:
                button.setStyleSheet(button_style)
        else:
            buttons = [getattr(self.ui, f'exercise_Q{i}_2') for i in range(1, 26)]
            for button in buttons:
                button.setStyleSheet(button_style)

    # 根据用户对错进行样式更改
    def yes_button(self, kind, number):
        print("number = ", number)
        button_style = '''
            QPushButton{
                background-color: rgb(168, 239, 160);
                border-radius:15px
            }
            QPushButton:hover{
                background-color: rgb(217, 217, 217);
                border-radius:15px
            }
            QPushButton:pressed{
                padding-left:5px;
                padding-top:5px;
            }
        '''
        if kind == 'exercise':
            button = getattr(self.ui, f'exercise_Q{number}_3')
        else:
            button = getattr(self.ui, f'exercise_Q{number}_2')

        button.setStyleSheet(button_style)

    def no_button(self, kind, number):
        print("number = ", number)
        button_style = '''
            QPushButton{
                background-color: rgb(244, 157, 170);
                border-radius:15px
            }
            QPushButton:hover{
                background-color: rgb(217, 217, 217);
                border-radius:15px
            }
            QPushButton:pressed{
                padding-left:5px;
                padding-top:5px;
            }
        '''
        if kind == 'exercise':
            button = getattr(self.ui, f'exercise_Q{number}_3')
            button.setStyleSheet(button_style)
        else:
            button = getattr(self.ui, f'exercise_Q{number}_2')
            button.setStyleSheet(button_style)