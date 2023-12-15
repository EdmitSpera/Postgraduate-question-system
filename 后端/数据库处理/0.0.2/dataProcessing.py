import pymysql
from docx import Document
import re
from pymysql.converters import escape_string
import os

def insert():
    list = dataProcessing()

    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        database="database_for_softwareProject",
        # database="test",
        charset="utf8mb4",
        user="root",
        password="Wjj123456",
        connect_timeout=10,
    )
    for index, item in enumerate(list):
        try:
            with open(item["question_picture"], 'rb') as f:
                img = f.read()
        except FileNotFoundError:
            img = None
        try:
            with conn.cursor() as cursor:
                # 准备SQL语句
                sql = f'''INSERT INTO app_question (question_description, option_1, option_2, option_3, option_4, option_5, answer, question_type)
                VALUES
                 (
                    "{item['question_description']}",
                    "{item['option_1']}",
                    "{item['option_2']}",
                    "{item['option_3']}",
                    "{item['option_4']}",
                    "{item['option_5']}",
                    "{item['answer']}",
                    "{item['question_type']}"
                 )
                '''
                # 执行SQL语句
                cursor.execute(sql)
                # 执行完SQL语句后的返回结果都是保存在cursor中
                # 所以要从cursor中获取全部数据
                sql = '''update app_question set question_picture=%s where id=%s'''
                cursor.execute(sql, (img, index+1))
                # cursor.close()
        except Exception as e:
            print("数据库操作异常：", e, index+1, item)

    conn.commit()
    conn.close()

def dataProcessing():
    doc = Document(r"D:\pycharmProjects\SoftwareProjectQuestion\题库修改整合版.docx")

    list = []
    temp = []


    pattern_question = re.compile(r'\[(.|\n)*答案:')
    pattern_question_description = re.compile(r'(\[(.|\n)*?)A[.)、）．。]')
    pattern_answer = re.compile(r'.*?答案:(.)')
    pattern_type = re.compile(r'\[.* .*]')
    pattern_option_1 = re.compile(r'.*?A[.)、）． 。](.*?)B[.)、）． 。]')
    pattern_option_2 = re.compile(r'.*?B[.)、）． 。](.*?)C[.)、）． 。]')
    pattern_option_3 = re.compile(r'.*?C[.)、）． 。](.*?)D[.)、）． 。]')
    pattern_option_4 = re.compile(r'.*?D[.)、）． 。](.*?)(E[.)、）． 。]|答案[：:])')
    pattern_option_5 = re.compile(r'.*?E[.)、）． 。](.*?)答案[：:]')
    pattern_option_list = [pattern_option_1, pattern_option_2, pattern_option_3, pattern_option_4, pattern_option_5]

    i = 0
    # 遍历段落并匹配正则表达式
    for paragraph in doc.paragraphs:
        temp.append(paragraph.text)
        text = "".join(temp)
        question_match = pattern_question.search(text)
        if question_match:
            dir = {
                "question_description": None,
                "question_picture": None,
                "option_1": None,
                "option_2": None,
                "option_3": None,
                "option_4": None,
                "option_5": None,
                "answer": None,
                "question_type": None
            }

            # 处理题干
            question_text = re.sub(r'\xa0', " ", text)
            if "'" in question_text or "\"" in question_text:
                question_text = escape_string(question_text)
            question_description_match = pattern_question_description.search(question_text)
            # print(question_text)
            if question_description_match:
                # print(question_description_match.group(1))
                # i += 1  # 3842
                dir["question_description"] = question_description_match.group(1)

                # 处理选项
                for index, item in enumerate(pattern_option_list):
                    option_match = item.search(question_text)
                    if option_match:
                        # print(option_match.group(1))
                        dir[f"option_{index+1}"] = option_match.group(1)

                # 处理答案
                answer_match = pattern_answer.search(question_text)
                if answer_match:
                    # print(answer_match.group(1))
                    # i += 1  # 4179
                    dir["answer"] = answer_match.group(1)

                # 处理题型
                type_match = pattern_type.search(question_text)
                if type_match:
                    # i += 1  # 3880
                    # print(type_match.group(0))
                    type_text = type_match.group(0)
                    type_text = "".join(type_text.split("[")).split("]")[0].split(" ")
                    dir["question_type"] = type_text[0]

                    # 处理图片
                    type_text.insert(1, " ")
                    type_text.append(".png")
                    type_text.insert(0, "images\\")
                    type_text.insert(0, os.path.dirname(__file__) + "\\")
                    type_text = "".join(type_text)
                    dir["question_picture"] = type_text

            if dir["question_description"] and dir["option_1"] and dir["option_2"] and dir["option_3"] and dir["option_4"] and dir["question_type"]:
                list.append(dir)
            temp = []
            # break
    # print(list)
    # print(len(list))
    return list


if __name__ == "__main__":
    insert()
    # dataProcessing()