import pymysql


def chaxun():
    # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
    db = pymysql.connect("127.0.0.1", "root", "952368", "student", charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # sqlyuju
    sql = "select * from student"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print("学号\t\t\t姓名\t\t\t性别\t\t\t年龄")
        for data in results:
            id = data[0]
            name = data[1]
            sex = data[2]
            age = data[3]
            print("{0}\t\t\t\t{1}\t\t\t{2}\t\t\t\t{3}".format(id, name, sex, age))

    except:
    # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()


if __name__ == "__main__":
    chaxun()
