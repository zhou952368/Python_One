import pymysql


def update_student():
    name = input("请输入学生的姓名：")
    sex = input("请输入学生的性别：")
    age = int(input("请输入学生的年龄："))
    Id = int(input("请输入学生的学号："))
    # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
    db = pymysql.connect("127.0.0.1", "root", "952368", "student", charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update student set name='{0}',sex='{1}',age='{2}' where Id='{3}'".format(name, sex, age, Id)
    try:
        # 执行sql条件语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()

if __name__ == "__main__":
    update_student()
