# 1. 写一个装饰器，其作用是在执行被装饰器的函数后，输出个人签名。
def our_decorator(func):
    def wrapper():
        print("~" * 30)
        func()
        print("~" * 30)

    return wrapper


@our_decorator
def f():
    print("不知你所知，我不知所止")


f()
"""
2. 装饰器的使用：
def add(a, b):
return a + b
为该功能增加新功能： 连续调用的情况下 只要在第一次调用时返回结果 其他情况下返回 None
"""


def decorator(func):
    func.count = 0

    def wrap(a, b):
        func.count += 1
        if func.count == 1:
            print(func(a, b))
        else:
            print("None")

    return wrap


@decorator
def add(a, b):
    return a + b


add(2, 4)
add(1, 2)
add(2, 3)
"""
3. 利用递归完成传入数字n，求出 1^1 + 2^2 + 3^3 + ... n^n 的和
"""


def sum1(n):
    if n == 1:
        return 1
    else:
        return sum1(n - 1) + n ** n


n = int(input("请输入要求和的数字："))
print(sum1(n))

"""
4. 设计一个函数，传入两个代表日期的字符串，如“2018-2-26”、“2017-12-12”，计算两个日期相差多少天
"""
import time


def time_difference(start_time, end_time):
    # 先将输入时间转换为标准时间 然后转换为时间戳
    start_array = time.mktime(time.strptime(start_time, "%Y-%m-%d"))
    end_array = time.mktime(time.strptime(end_time, "%Y-%m-%d"))
    # 取两时间戳的差值的绝对值并处以一天
    tim = abs(start_array - end_array) / (24 * 60 * 60)
    print(tim)


start_time = input("请以 年-月-日 的形式传入开始时间：")
end_time = input("请以 年-月-日 的形式传入结束时间：")
time_difference(start_time, end_time)

"""
5. 将以下功能使用对应的代码表达
str0 = “abcdokokokzhongqiukuaile”
1. 获取 m 第一次出现的位置
2. 获取 m 出现的所有位置
"""


def func(str0):
    inquire = input("请输入先查询的字符：")
    for i in range(len(str0)):
        if str0[i] == inquire:
            print(i, end=" ")


str0 = input("请输入一个字符串：")
func(str0)
