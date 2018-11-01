"""
函数的关键字参数
函数传参默认按照顺序传参   默认参数要放在最后

"""
# def fun(name,age):
#     print("姓名:%s,年龄:%d"%(name,age))
# fun("feng",22)

"""
不定长参数
在参数前面加*  不定长参数放在函数最后
*b 元祖
**b 字典
"""
# def feng(a,*b):
#     print(a)
#     print(b)
# feng(1,2,3,4,5)

"""
递归函数
函数自己调用自己  如果没有一个条件的话就相当于一个死循环
"""
# def feng1(a):
#     print(a)
#     a-=1
#     if a>0:
#         feng1(a)
# feng1(5)
# print("over")

# def feng2(a):
#     if a==1:
#         return  1
#     return a*feng2(a-1)
# print(feng2(5))

# def feng3():
#     name=input("请输入：")
#     if name=="张三":
#         print("ok")
#     else:
#         feng3()
# feng3()
"""
os模块
os.name  :查看操作系统类型
os.uname  :打印操作系统的详细信息（windows不支持）
os.environ  :获取操作系统的环境变量
os.environ.get() :获取指定的环境变量
os.getcwd(): 查看当前文件的路径
os.listdir():不指定路径默认获取当前文件夹下所有文件和文件夹 不能深层获取
             指定路径获取指定文件夹下所有文件和文件夹 不能深层获取
在路径前加一个r  可以让路径中的字符没有特殊含义
os.mkdir():  创建一个文件夹
os.makedirs(): 在指定路径下创建多层级文件夹
os.rmdir():  删除文件夹
os.rename():  重命名文件夹

nt---widows  posix---linux/unix/mac os

"""
# import os
# import os.path
# print(os.name)
# #print(os.uname())
# print(os.environ)
# print(os.environ.get("PATH"))
# print(os.getcwd())
#print(os.listdir(r"E:\zhou\a\b"))
#print(os.mkdir("E:\zhou"))
#print(os.makedirs())
#print(os.rmdir("E:\zhou"))
#print(os.path.abspath(""))


'''
获取指定文件夹下所有的文件，深层获取
1.写好路径
2.获取当前目录下所有文件
3.判断所有文件是文件夹还是文件
4.如果是文件就输出，是文件夹继续获取
'''
# import os
# import os.path
# def lujin(p):
#     if os.path.isdir(p):
#         i=os.listdir(p)
#         for z in i:
#             d=os.path.join(p,z)
#             if os.path.isfile(d):
#                 print(z)
#             elif os.path.isdir(d):
#                 lujin(d)
# lujin(p=r"D:\daima")
