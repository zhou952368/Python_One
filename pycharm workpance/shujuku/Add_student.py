import pymysql
import cgi
import requests
import cgitb

# def add_student():
form = cgi.FieldStorage()
id = form.getvalue("id")
name = form.getvalue("name")
sex = form.getvalue("sex")
age = form.getvalue("age")
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("127.0.0.1", "root", "952368", "student", charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = 'insert into student values ("%d","%s","%s","%d") % (id, name, sex, age)'
try:
    # 执行sql插入语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
