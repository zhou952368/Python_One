'''
用户信息: ['python',123456,1]  列表形式
           用户名,  密码, 排名
写一个用户数据类(类型不限) 通过类实例化对象修改数据

# 装饰器
def check_login(func):
    pass

class UserInfo:
    def __init__(self):
        self.users = ['python',123456,1]

    def check_user(self,username,password):
        pass

    @check_login
    def update_ranking(self,username,password,ranking):
        pass

功能: 登录成功后修改排名
需求:
    1.判断账号密码是否正确
        只能通过调用 check_user()判断,且该方法不可出现在同类的其他方法里
    2.账号密码错误3次则不能继续登录(返回None)
    3.通过验证登录成功后修改排名
    4.最后输出只允许执行一个函数(次数不限)
    user_info = UserInfo()
    user_info.update_ranking()
'''


def check_login(func):
    func.count = 0

    def zhuangsi(self, username, password, ranking):
        func.count += 1
        if func.count <= 3:
            user = self.check_user(username, password)
            if user:
                func(self, username, password, ranking)
                print("登录更新成功")
            else:
                print("账号密码错误，请重新输入！")
        if func.count > 3:
            print("错误超过三次，账号锁定")

    return zhuangsi


class UserInfo:
    def __init__(self):
        self.users = ['python', 123456, 1]

    def check_user(self, username, password):
        if self.users[:2] == [username, password]:
            return self.users

    @check_login
    def update_ranking(self, username, password, ranking):
        self.users[2] = ranking


if __name__ == '__main__':
    user = UserInfo()
    user.update_ranking('python', 12345, 2)
    user.update_ranking('python', 12345, 2)
    user.update_ranking('python', 123456, 2)
    user.update_ranking('python', 12345, 2)
