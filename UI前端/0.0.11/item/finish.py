import re
class FinishPageSet:
    def __init__(self, ui):
        self.ui = ui

    def practice_finish(self, right, wrong):
        print("finish", right, wrong)
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

    def wrong_finish(self, right, wrong, length):
        print("finish", right, wrong)
        # 获取当前的 HTML 内容
        html_style = f'''
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style=" font-family:'SimSun'; font-size:36pt; font-weight:600;">{str(right)}</span>
            <span style=" font-family:'SimSun'; font-size:24pt;">/{str(length)}</span>
        </p>
        '''
        self.ui.text_right_2.setHtml(html_style)
        html_style = f'''
                <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                    <span style=" font-family:'SimSun'; font-size:36pt; font-weight:600;">{str(wrong)}</span>
                    <span style=" font-family:'SimSun'; font-size:24pt;">/{str(length)}</span>
                </p>
                '''
        self.ui.text_wrong_2.setHtml(html_style)
        html_style = f'''
                        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                            <span style=" font-family:'SimSun'; font-size:36pt; font-weight:600;">{str(length-wrong-right)}</span>
                            <span style=" font-family:'SimSun'; font-size:24pt;">/{str(length)}</span>
                        </p>
                        '''
        self.ui.text_none_2.setHtml(html_style)




        # # 寻找第一个 span 标签内的文本部分
        # start_index = current_html.find("<span ")
        # end_index = current_html.find("</span>", start_index)
        # if start_index != -1 and end_index != -1:
        #     # 寻找下一个 span 标签
        #     next_start_index = current_html.find("<span ", end_index + 1)
        #     # 如果找到了下一个 span 标签，将第一个 span 标签内的文本内容更新
        #     if next_start_index != -1:
        #         start_text_index = current_html.find(">", start_index) + 1
        #         updated_html = current_html[:start_text_index] + str(right) + current_html[end_index:]
        #         self.ui.text_right_2.setHtml(updated_html)        # 正确数
        #         updated_html = current_html[:start_text_index] + str(wrong) + current_html[end_index:]
        #         self.ui.text_wrong_2.setHtml(updated_html)        # 错题数
        #         updated_html = current_html[:start_text_index] + str(length-right-wrong) + current_html[end_index:]
        #         self.ui.text_none_2.setHtml(updated_html)     # 未作答


        # pattern = r'<span[^>]*>([^<]+)</span><span[^>]*>([^<]+)</span>'
        # matches = re.findall(pattern, current_html)
        #
        # if matches:
        #     for match in matches:
        #         # 修改匹配到的内容，这里只是举例，你可以根据需要修改
        #         modified_first_span_content = str(right)  # 修改后的内容
        #         modified_second_span_content = "/"+str(length)  # 修改后的内容
        #
        #         # 使用 re.sub() 替换匹配到的内容
        #         updated_html = re.sub(pattern, f'<span>{modified_first_span_content}</span><span>{modified_second_span_content}</span>', current_html)
        #         self.ui.text_right_2.setHtml(updated_html)



        # # 使用正则表达式找到第二个 span 标签内的文本部分
        # pattern = r'weight:600;">(\d+)</span>'
        # match = re.search(pattern, current_html)
        # if match:
        #     print("1")
        #     updated_html = re.sub(pattern, f'weight:600;">{str(right)}</span>', current_html)
        #     # print(updated_html)
        #     self.ui.text_right_2.setHtml(updated_html)  # 正确数
        #     updated_html = re.sub(pattern, f'weight:600;">{str(wrong)}</span>', current_html)
        #     self.ui.text_wrong_2.setHtml(updated_html)  # 错题数
        #     updated_html = re.sub(pattern, f'weight:600;">{str(length-right-wrong)}</span>', current_html)
        #     self.ui.text_none_2.setHtml(updated_html)  # 未作答
        #
        # # 使用正则表达式找到第二个 span 标签内的文本部分
        # pattern = r'font-size:24pt;">/(\d+)</span>'
        # match = re.search(pattern, current_html)
        # if match:
        #     print("2")
        #     updated_html = re.sub(pattern, f'font-size:24pt;">/{str(length)}</span>', current_html)
        #     # print(updated_html)
        #     self.ui.text_right_2.setHtml(updated_html)
        #     self.ui.text_wrong_2.setHtml(updated_html)
        #     self.ui.text_none_2.setHtml(updated_html)

    # def wrong_finish(self, right, wrong, length):
    #     print("finish", right, wrong)
    #     # 获取当前的 HTML 内容
    #     current_html = self.ui.text_right_2.toHtml()
    #
    #     # 寻找第一个 span 标签内的文本部分
    #     start_index = current_html.find("<span ")
    #     end_index = current_html.find("</span>", start_index)
    #     if start_index != -1 and end_index != -1:
    #         # 寻找下一个 span 标签
    #         next_start_index = current_html.find("<span ", end_index + 1)
    #         # 如果找到了下一个 span 标签，将第一个 span 标签内的文本内容更新
    #         if next_start_index != -1:
    #             start_text_index = current_html.find(">", start_index) + 1
    #             updated_html = current_html[:start_text_index] + str(right) + current_html[end_index:]
    #             self.ui.text_right_2.setHtml(updated_html)  # 正确数
    #             updated_html = current_html[:start_text_index] + str(wrong) + current_html[end_index:]
    #             self.ui.text_wrong_2.setHtml(updated_html)        # 错题数
    #             updated_html = current_html[:start_text_index] + str(length-right-wrong) + current_html[end_index:]
    #             self.ui.text_none_2.setHtml(updated_html)     # 未作答
    #
    #     # 寻找第二个 span 标签内的文本部分
    #     start_index_2 = current_html.find("<span ", end_index + 1)
    #     end_index_2 = current_html.find("</span>", start_index_2)
    #     if start_index_2 != -1 and end_index_2 != -1:
    #         start_text_index_2 = current_html.find(">", start_index_2) + 1
    #         updated_html_2 = current_html[:start_text_index_2] + "/"+str(length) + current_html[end_index_2:]
    #         self.ui.text_right_2.setHtml(updated_html_2)
    #         self.ui.text_wrong_2.setHtml(updated_html_2)
    #         self.ui.text_none_2.setHtml(updated_html_2)

