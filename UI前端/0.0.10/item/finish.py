class FinishPageSet:
    def __init__(self, ui):
        self.ui = ui

    def practice_finish(self, right, wrong):
        print("finish", right, wrong)
        # text_style = '''
        #     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
        #     <html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
        #     p, li { white-space: pre-wrap; }
        #     hr { height: 1px; border-width: 0; }
        #     li.unchecked::marker { content: "\2610"; }
        #     li.checked::marker { content: "\2612"; }
        #     </style></head><body style=" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;">
        #     <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'SimSun'; font-size:36pt; font-weight:600;">20</span><span style=" font-family:'SimSun'; font-size:24pt;">/25</span></p></body></html>
        # '''

        # 获取当前的 HTML 内容
        current_html = self.ui.text_right.toHtml()

        # 寻找第一个 span 标签内的文本部分
        start_index = current_html.find("<span ")
        end_index = current_html.find("</span>", start_index)
        if start_index != -1 and end_index != -1:
            # 寻找下一个 span 标签
            next_start_index = current_html.find("<span ", end_index + 1)
            # 如果找到了下一个 span 标签，将第一个 span 标签内的文本内容更新
            if next_start_index != -1:
                start_text_index = current_html.find(">", start_index) + 1
                updated_html = current_html[:start_text_index] + str(right) + current_html[end_index:]
                self.ui.text_right.setHtml(updated_html)        # 正确数
                updated_html = current_html[:start_text_index] + str(wrong) + current_html[end_index:]
                self.ui.text_wrong.setHtml(updated_html)        # 错题数
                updated_html = current_html[:start_text_index] + str(25-right-wrong) + current_html[end_index:]
                self.ui.text_none.setHtml(updated_html)     # 未作答
