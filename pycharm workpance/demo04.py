# 高阶函数
def add(x, y, func):
    return func(x) + func(y)


print(add(1, 2, abs))  # 输出结果: 3

'''函数式编程'''
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
l = [1, 2, 3, 4, 5]
s = map(str, l)
print(list(s))  # 输出结果: ['1', '2', '3', '4', '5']

# str.capitalize()  将第一个字母转成大写,其他的小写
print('abc'.capitalize())

l1 = ['aBC', 'CBA', 'ADE']
s1 = list(map(lambda name: name.capitalize(), l1))
print(s1)  # 输出结果: ['Abc', 'Cba', 'Ade']

# reduce(函数对象,可迭代对象)
# 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算 (((x1+x2)+x3)+...)
from functools import reduce

str_reduce = ['1', '2', '3', '4', '5']
int_reduce = [1, 2, 3, 4, 5]

r1 = reduce(lambda x, y: x + y, str_reduce)
print(r1)  # 输出结果: 12345 (type = str)

r2 = reduce(lambda x, y: x + y, int_reduce)
print(r2)  # 输出结果: 15 (累计计算,输出最后的结果)

# map & reduce 联用
# 将字符串转为数字

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

sum1 = reduce(lambda x, y: x * 10 + y, map(lambda z: DIGITS[z], ['1', '2', '3', '4']))
print(sum1)  # 传入['1', '2', '3', '4'] 输出结果 1234（type = int）

# filter(函数,可迭代对象)(过滤)
# 函数是返回True或者False的函数
# 可迭代对象中的每一个元素传给函数，如果返回值是True就保留
# 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
numbers = [1, 2, 3, 4, 5, 7, 9, 10, 11]
# 返回偶数
print(list(filter(lambda x: x % 2 == 0, numbers)))  # 输出结果 [2, 4, 10]


# 闭包,记录函数被调用次数
def created_count():
    # created_count.count 一种全局变量的表达方式 函数名.变量名
    created_count.count = 0

    def count():
        created_count.count += 1
        return created_count.count

    return count


f1 = created_count()

print(f1())  # 1
print(f1())  # 2
print(f1())  # 3
