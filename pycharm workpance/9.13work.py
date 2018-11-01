# 1.简述普通参数、指定参数、默认参数、可变长参数的区别
# 2.写函数，计算传入字符串中单个【数字】、【字母】、【空格] 以及 【其他】的个数


# def statistics(s):
#     num = 0
#     sum1 = 0
#     space = 0
#     other = 0
#     for n in s:
#         a = ord(n)
#         if 48 <= a <= 57:
#             num += 1
#         elif (65 <= a <= 90) or (97 <= a <= 122):
#             sum1 += 1
#         elif a == 32:
#             space += 1
#         else:
#             other += 1
#     return num, sum1, space, other
#
# s = input("请输入一个字符串：")
# print(statistics(s))


# 3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5

# 4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有[],'',(),None或{}。

def judgement(iter):
    if not iter:
        return "参数为空"
    l = []
    for inem in iter:
        for i, a in enumerate([], '', (), None, {}):
            if inem == a:
                l.append(i)
        return l
list1 = [(), [], 2, "a", None]
print(judgement(list1))

#  5.定义一个函数，输入不定个数的数字，返回所有数字的和


def qiuhe(*args):
    sum2 = 0
    try:
        for i in args:
            sum2 += i
    except Exception as e:
        print(e)
        return "参数的类型有误！"
    return sum2
print(qiuhe(1, 2))




