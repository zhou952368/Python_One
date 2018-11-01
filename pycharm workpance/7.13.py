"""
abs():   求绝对值
max():   求最大值
min():   求最小值
pow():   求a的b次方
round():   四舍五入（逗号后数字为保留几位小数）
sum():    求和（参数为列表）
type():   检测变量类型
数学模块 math
math.ceil():  向上取整
math.floor():  向下取整
math.sqrt():   开方
math.modf():  返回小数和整数部分
随机数模块 random
random.random(): 取零到一之间的随机数的小数 取不到一）
（）底层代码中变量为self  不用给它赋值
random.randint(a,b): 取a到b之间的整数可以取到b
random.randrange(a,b): 取a到b之间的整数取不到b 只写一个数默认从0开始
只要用到模块就要先导入该模块（模块：包  命名空间）
在多个py文件中肯出现相同的名字（变量  函数 类）为了不让名字冲突把不同的py文件放在不同的文件夹中
"""
import math
import random
# print(abs(-10))
# print(max(12,45,457,4313,1,89))
# print(min(12,45,457,4313,1,89))
# print(pow(5,3))
# print(round(5.5))
# print(math.sqrt(8))
# print(math.modf(3.14))
# print(random.random())
# print(random.randint(1,3))
# print(random.randrange(1,10,2)) #2是步长
# print(random.uniform(1,3))   #随机1到3之间的小数
# print(random.choice(["a","b",1,2]))  #从指定列表中随机一个元素
# print(random.sample(["a","b",1,2]),2)  #从列表中指定几个个元素


# print(random.sample(["abcdefghijklmnopqrstuvwsyz",1,2,3,4,5,6,7,8,9,"ABCDEFGHIJKLMNOPQRSTUVWSYZ"],random.randint(4,6)))
#
#
# i=int(input("请输入一个数字："))
# z=0
# while True:
#
#     a=random.randint(1,100)
#     z+=1
#     if i>a:
#         print("数字猜大了")
#     elif i<a:
#         print("数字猜小了")
#     else:
#         print("恭喜你，猜中了")
#         break
# print(z)


"""
字符串一旦创建不可更改3
在字符串中每个字符都有自己对应的位置
位置一般叫做下标或者索引
下标从左到右从0依次开始递增（空格也占据一个位置）
 +:加法运算是把字符串拼接起来
 *：字符串只能和整数相乘 乘几就重复几次
 len():计算字符串的长度 length（长度）
 index():  根据元素查找下标,从左到右查找
 rindex():  根据元素查找下标,从右到左查找
 find()和index()是一个作用的
 find()找不到就会报-1  index（）找不到就报错

"""
a="hello world"
print(a[9])
print(a.index("l"))
print(a[:2])#截取（切片）0到2的字符串 不包含最大值
print(a[2::2])#两个冒号  后面的数字是步长,每隔2取一个
print(a.upper())  #将字符串全部转换为大写
print(a.lower())  #将字符串全部转换为小写
print(a.swapcase())  #大写换小写  小写换大写
print(a.title())    #首字母大写
print(a.capitalize())  #将整个字符串的第一个字母大写
