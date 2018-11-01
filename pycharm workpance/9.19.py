def outer(func):
    def inner():
        print("*"*30)
        func()
    return inner


@outer
def f():
    print("这是一个函数;")
f()


def our_decorator(func):
    """
    进行管理员操作前进行判断  该用户是否拥有管理员权限
    :param func:要进行装饰的函数
    :return:
    """
    dict1 = {"zhou": "952368", "feng": "123456"}

    def wrap(name, password):
        if name in dict1.keys():
            mima = dict1[name]
            if mima == password:
                func(name, password)
            else:
                print("用户名或者密码不正确，请重新输入")
    return wrap


@our_decorator
def f(name, password):
    print("登录成功,接下来可执行管理员操作了")


def login():
    name = input("请输入用户名：")
    password = input("请输入密码：")
    f(name, password)
login()
