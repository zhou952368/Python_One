"""
文件操作
"""
# path=r"F:\QQ文件\1.mp3"
# path2=r"F:\QQ文件\2.mp3"
# f=open(path,"rb")
#读取文件所有内容
# str=(f.read())
# f1=open(path2,"wb")
#读取指定的字符
#print(f.read(3))
#一次读取一行
#print(f.readline())
#读取多行 并将每一行的内容添加到列表中
#print(f.readlines())
# f1.write(str)
# f.close()
# f1.close()


'''
time
'''
# import time
# # 从1970年1月1日0点开始到现在的时间差的秒数
# # 时间戳
# print(time.time())
# c=time.time()
# # 获取本地时间 存在元组中
# print(time.localtime())
# tuple1=time.localtime()
# # 获取本地时间 字符串
# print(time.ctime())
# # 将时间元组转成字符串 不写也可以和ctime一样
# print(time.asctime(tuple1))
# # 将时间元组转为时间戳
# print(time.mktime(tuple1))
# # 将时间戳转为时间元组，不写默认是本地时间元组
# print(time.gmtime(c))
# # 2018-7-19 16：14
# # 将时间元组转为指定格式的字符串
# str1=time.strftime("%Y年%m月%d日 %H:%M:%S",tuple1)
# print(str1)
# print(time.strptime(str1,"%Y年%m月%d日 %H:%M:%S"))
# time.sleep(2)# 程序运行中会休眠两秒
# print("over")

import calendar

# 获取指定年份的日历表
# print(calendar.calendar(2018))
# 打印指定月份的日历
# print(calendar.month(2018,7))
# 打印周几  从0开始，周一是0
# print(calendar.weekday(2018,7,2))
# print(calendar.week(3,1))

# """
# 自定义模块
# 一个py文件就是一个模块
# 在其他地方调用函数要使用函数的值的时候 需要return返回函数的值
# """
# from  student import addStuInfo
# addStuInfo()

import time
print(time.clock())
sum=0
for i in range(99999999):
    sum+=1
print(time.clock())
