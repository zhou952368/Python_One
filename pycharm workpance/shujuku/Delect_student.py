import pymysql


def delect_student():
    id = int(input("请输入要删除的学生的学号："))
    # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
    db = pymysql.connect("127.0.0.1", "root", "952368", "student", charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "delete  from student where id='%d'" % (id)
    try:
        # 执行sql条件语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("数据删除成功")
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()

if __name__ == "__main__":
    delect_student()
