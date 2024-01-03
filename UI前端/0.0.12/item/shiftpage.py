class PageSwitchHandler:
    def __init__(self, ui):
        self.ui = ui

    def connection_button(self):
        self.ui.Bt_main.clicked.connect(self.on_Bt_main_clicked)
        self.ui.Bt_exercise.clicked.connect(self.on_Bt_exercise_clicked)
        self.ui.Bt_wrong.clicked.connect(self.on_Bt_wrong_clicked)
        self.ui.Bt_mine.clicked.connect(self.on_Bt_mine_clicked)
        self.ui.Bt_main_2.clicked.connect(self.on_Bt_main_2_clicked)
        self.ui.Bt_exercise_5.clicked.connect(self.on_Bt_exercise_5_clicked)
        self.ui.Bt_wrong_5.clicked.connect(self.on_Bt_wrong_5_clicked)
        self.ui.Bt_mine_5.clicked.connect(self.on_Bt_mine_5_clicked)
        self.ui.Bt_main_3.clicked.connect(self.on_Bt_main_3_clicked)
        self.ui.Bt_exercise_3.clicked.connect(self.on_Bt_exercise_3_clicked)
        self.ui.Bt_mine_3.clicked.connect(self.on_Bt_mine_3_clicked)
        self.ui.Bt_main_4.clicked.connect(self.on_Bt_main_4_clicked)
        self.ui.Bt_exercise_4.clicked.connect(self.on_Bt_exercise_4_clicked)
        self.ui.Bt_wrong_4.clicked.connect(self.on_Bt_wrong_4_clicked)
        self.ui.lx_class1_2.clicked.connect(self.on_lx_class1_2_clicked)
        self.ui.lx_class2_2.clicked.connect(self.on_lx_class2_2_clicked)
        self.ui.lx_class3_2.clicked.connect(self.on_lx_class3_2_clicked)
        self.ui.lx_class4_2.clicked.connect(self.on_lx_class4_2_clicked)
        self.ui.lx_class5_2.clicked.connect(self.on_lx_class5_2_clicked)
        self.ui.lx_class6_2.clicked.connect(self.on_lx_class6_2_clicked)
        self.ui.lx_class7_2.clicked.connect(self.on_lx_class7_2_clicked)
        self.ui.Bt_back_2.clicked.connect(self.on_Bt_back_2_clicked)
        self.ui.Bt_back_3.clicked.connect(self.on_Bt_back_3_clicked)
        self.ui.Bt_continue.clicked.connect(self.on_Bt_continue_clicked)
        self.ui.Bt_continue_2.clicked.connect(self.on_Bt_continue_2_clicked)
        self.ui.answe_sheet_1.clicked.connect(self.on_answe_sheet_1_clicked)
        self.ui.answer_sheet_2.clicked.connect(self.on_answer_sheet_2_clicked)
        self.ui.answer_sheet_back_1.clicked.connect(self.on_answer_sheet_back_1_clicked)
        self.ui.answer_sheet_back_2.clicked.connect(self.on_answer_sheet_back_2_clicked)
        self.ui.Bt_email.clicked.connect(self.on_Bt_email_clicked)
        self.ui.Bt_setting.clicked.connect(self.on_Bt_setting_clicked)
        self.ui.Bt_exercise_7.clicked.connect(self.on_Bt_exercise_7_clicked)
        self.ui.Bt_back_5.clicked.connect(self.on_Bt_back_5_clicked)
        self.ui.Bt_back_4.clicked.connect(self.on_Bt_back_4_clicked)
        self.ui.Bt_back_6.clicked.connect(self.on_Bt_back_6_clicked)

    def on_Bt_back_6_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def on_Bt_back_4_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def on_Bt_back_5_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def on_Bt_email_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(3)
    def on_Bt_setting_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def on_Bt_exercise_7_clicked(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
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
    def on_Bt_back_3_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def on_Bt_continue_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def on_answer_sheet_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(2)
    def on_answer_sheet_back_2_clicked(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)