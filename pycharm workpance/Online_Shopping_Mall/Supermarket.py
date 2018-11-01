import random
from Market_user import User
from OSM_DB import DB


class Market:
    def __init__(self):
        self._db = DB()
        self.__password = None
        self.__user_id = None
        self.__username = None

    def register(self, user):
        self.__username = user.get_username()
        self.__password = input("请输入您的密码;")
        self.__user_id = random.sample(range(10000, 999999), 1)[0]
        self._db.insert_user(self.__user_id, self.__username, self.__password)
        print("恭喜您已经注册成功！您的账号为：{0}，密码为：{1}".format(self.__user_id, self.__password))

    def logon(self):
        self.__user_id = input("请输入您的账号：")
        self.__password = input("请输入您的密码：")
        self._db.update_logging_status(self.__user_id, self.__password, 'True')
        print("登录成功")

    def quit(self):
        self._db.update_logging_status(self.__user_id, self.__password, 'False')
        print("成功退出")

