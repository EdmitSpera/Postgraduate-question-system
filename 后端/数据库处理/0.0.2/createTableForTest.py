import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="test",
    charset="utf8",
    user="root",
    password="Wjj123456"
)

# 打开数据库可能会有风险，所以添加异常捕捉
try:
    with conn.cursor() as cursor:
        sql = '''drop table if exists app_question'''
        cursor.execute(sql)
        # 准备SQL语句
        sql = '''
            create table app_question(
            id bigint primary key auto_increment,
            question_description varchar(1024),
            question_picture longblob,
            option_1 varchar(256),
            option_2 varchar(256),
            option_3 varchar(256),
            option_4 varchar(256),
            option_5 varchar(256),
            answer char(1),
            analysis varchar(512),
            question_type varchar(32)
            )
        '''
        # 执行SQL语句
        cursor.execute(sql)
        # 执行完SQL语句后的返回结果都是保存在cursor中
        # 所以要从cursor中获取全部数据
except Exception as e:
    print("数据库操作异常：\n", e)
finally:
    # 不管成功还是失败，都要关闭数据库连接
    conn.close()


