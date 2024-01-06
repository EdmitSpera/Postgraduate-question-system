import pymysql
from docx import Document
import re
from pymysql.converters import escape_string
import os

def insert():
    list = dataProcessing()

    # 连接数据库，找到由module.py创建的问题表
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
    # 遍历列表
    for index, item in enumerate(list):
        # 通过图片的路径打开图片文件
        try:
            with open(item["question_picture"], 'rb') as f:
                img = f.read()
        # 由于不一定存在所以需要进行异常捕捉
        except FileNotFoundError:
            img = None
        try:
            with conn.cursor() as cursor:
                # 编写SQL语句
                # 将列表中每个字典对应的值传入到表中（不包括图片）
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
                # 在这里更新图片
                sql = '''update app_question set question_picture=%s where id=%s'''
                cursor.execute(sql, (img, index+1))
        except Exception as e:
            print("数据库操作异常：", e, index+1, item)

    # 提交
    conn.commit()
    conn.close()

def dataProcessing():
    doc = Document(r"D:\pycharmProjects\SoftwareProjectQuestion\题库修改整合版.docx")

    list = []
    temp = []

    # 下面定义各种正则表达式，用于提取文档中的内容
    # 用于匹配整个题目，包括题干、选项、答案
    pattern_question = re.compile(r'\[(.|\n)*答案:')
    # 用于匹配题干
    pattern_question_description = re.compile(r'(\[(.|\n)*?)A[.)、）．。]')
    # 用于匹配答案部分
    pattern_answer = re.compile(r'.*?答案:(.)')
    # 用于匹配题目类型
    pattern_type = re.compile(r'\[.* .*]')
    # 用于匹配选项一
    pattern_option_1 = re.compile(r'.*?A[.)、）． 。](.*?)B[.)、）． 。]')
    # 用于匹配选项二
    pattern_option_2 = re.compile(r'.*?B[.)、）． 。](.*?)C[.)、）． 。]')
    # 用于匹配选项三
    pattern_option_3 = re.compile(r'.*?C[.)、）． 。](.*?)D[.)、）． 。]')
    # 用于匹配选项四
    pattern_option_4 = re.compile(r'.*?D[.)、）． 。](.*?)(E[.)、）． 。]|答案[：:])')
    # 用于匹配选项五
    pattern_option_5 = re.compile(r'.*?E[.)、）． 。](.*?)答案[：:]')
    # 将以上正则表达式用于匹配选项的放进列表中
    pattern_option_list = [pattern_option_1, pattern_option_2, pattern_option_3, pattern_option_4, pattern_option_5]

    # 遍历段落并匹配正则表达式
    # 我们直接遍历对象中的paragraphs获取到每个段落
    # 这里需要注意的是，在文档中只要遇到空格或者换行都会被对象视为一个段落，也就是会被截断
    for paragraph in doc.paragraphs:
        # 将段落放入中间变量列表中
        temp.append(paragraph.text)
        # 将列表的元素连接成字符串
        text = "".join(temp)
        # 使用用于匹配整一条题目的正则表达式去匹配这个字符串
        question_match = pattern_question.search(text)
        # 如果匹配成功，即字符串中出现了一道完整的题目（包括题干、选项和答案），则进一步细分
        if question_match:
            # 这里我们定义一个字典，方便存储不同的内容
            dir = {
                # 题干
                "question_description": None,
                # 图片路径
                "question_picture": None,
                # 选项一
                "option_1": None,
                # 选项二
                "option_2": None,
                # 选项三
                "option_3": None,
                # 选项四
                "option_4": None,
                # 选项五
                "option_5": None,
                # 答案
                "answer": None,
                # 题型
                "question_type": None
            }

            # 定义好字典后，正式开始细分处理
            # 处理题干
            question_text = re.sub(r'\xa0', " ", text)
            # 这一步我们需要检查整条题目中是否存在英文形式的单引号和双引号；因为在实际操作，这个模块不在django框架中，所以无法使用封装好的接口对数据表进行操作
            # 言下之意就是要老老实实写sql语句
            # 那么题目是以字符串的形式存入到相应字段中的，如果出现了英文形式的单引号或者双引号，就会影响到sql语句的语法
            if "'" in question_text or "\"" in question_text:
                # 这里我们检测到题目中有英文单双引号后，我们调用一下方法对这些符号进行转义
                # 这样就不会影响到我们所书写的sql语句
                question_text = escape_string(question_text)

            # 拿到处理好的新的题目后开始对各个部分进行分离
            # 这里我们先开始处理题干
            question_description_match = pattern_question_description.search(question_text)
            if question_description_match:
                # 匹配成功后将题干存入字典相应的键中
                dir["question_description"] = question_description_match.group(1)

                # 处理选项
                # 之前将匹配选项的正则表达式放入列表中就是为了方便用循环进行操作
                for index, item in enumerate(pattern_option_list):
                    option_match = item.search(question_text)
                    if option_match:
                        # 匹配成功后放入字典相应的键中
                        dir[f"option_{index+1}"] = option_match.group(1)

                # 处理答案
                answer_match = pattern_answer.search(question_text)
                if answer_match:
                    dir["answer"] = answer_match.group(1)

                # 处理题型
                type_match = pattern_type.search(question_text)
                if type_match:
                    type_text = type_match.group(0)
                    type_text = "".join(type_text.split("[")).split("]")[0].split(" ")
                    dir["question_type"] = type_text[0]

                    # 拿到题型后，我们需要根据题型和编号去爬取的图片文件中查找是否有相应的题目图片
                    # 处理图片
                    # 这里我们对图片的路径进行处理，拼接出相应的地址去寻找
                    type_text.insert(1, " ")
                    type_text.append(".png")
                    type_text.insert(0, "images\\")
                    type_text.insert(0, os.path.dirname(__file__) + "\\")
                    type_text = "".join(type_text)
                    # 把相应的地址放入到字典中
                    dir["question_picture"] = type_text

            # 这里我们检查字典中的必要属性中是否有值，有则将字典放入列表中
            if dir["question_description"] and dir["option_1"] and dir["option_2"] and dir["option_3"] and dir["option_4"] and dir["question_type"]:
                list.append(dir)
            temp = []

    # 当这个文档处理完后，返回收集好的列表
    return list


if __name__ == "__main__":
    insert()
    # dataProcessing()