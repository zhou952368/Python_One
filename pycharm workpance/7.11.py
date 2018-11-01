# s = 'Yes,he doesn\'t'
# print(s, type(s), len(s))


"""
print可以直接打印数字和变量（变量可不为整型）
右边的值符给左边
"""
# a=10.111
# print(a)


"""
type() 内置函数，检测变量是什么类型
整数 int
小数 float
字符串 str
布尔  bool  用来判断对错Tru正确 False错误
空值 None  这个变量没有值
"""
age=10.00
print(age,type(age))
name="zhou"
print(name,type(name))
inhave=True
print(type(inhave))

"""
字符串做加法结果是拼接
整数和字符串不能做运算
整数和字符串做加法运算，在字符串的内容是数字，可以吧字符串转换为整型
转换方式： int（要转换的数据/变量）
"""
a="10"
b=10
print(int(a)+b)
print(a+str(b))

"""
取整  //  pythno取整直接舍弃后面的小数
求余 %
幂运算 **
复合运算符
+=  -=(基本运算后面加等号)
a=a+2  a+=2等同
关系运算符
> < >= <= !=(不等) ==（等于）
逻辑运算符
and(并且) or（或者） not（非）取反
位运算符
&(位与运算符 先转换为二进制 两者都为1 才为1)
| （ 先转换为二进制有1 为1）
^  (先转换为二进制两者不同则为1)
<<  （先转换为二进制 高位丢弃低位补0）
>>  （先转换为二进制 高位补0低位丢弃）
"""
a=10
b=2
print(a%b)
print(a>b and a<b)
print(a>b or a<b)
print(not a>b)
print(5&7)
print(5^7)
print(5<<2)
print(5>>2)

"""
判断语句 if  else  elif
max（）python内置函数  制动判断最大值
chr() 会将数字转换成ASCII值
a 97(后面依次递减)
A 65
"""





name=394837238
password=123
name=int(input("请输入用户账号"))
password=int(input("请输入用户密码"))
if name==123456 and password==123:
    print("登录成功")
else:
    print("登录失败")

java=float(input("请输入java成绩"))
music=float(input("请输入音乐成绩"))
if (java>90 and music>80) or (java==100 and music>70):
    print("老师奖励他")
else:
    print("123456")

a=int(input("请输入一个数："))
b=int(input("请输入一个数："))
if (a/b==0 or a+b>1000):
    print(a)
else:
    print(b)

a=int(input("请输入学员成绩"))
if a>=90:
    print("优秀")
elif a>=80:
    print("良好")
elif a>=70:
    print("中等")
elif a<60:
    print("差")


a=int(input("请输入月份:"))
if (1<=a<=3):
    print("春季")
elif (4<=a<=6):
    print("夏季")
elif (7<=a<=9):
    print("秋季")
elif (10<=a<=12):
    print("冬季")


a=int(input("请输入a:"))
b=int(input("请输入b:"))
c=int(input("请输入c:"))
if (a>b and a<c):
    print(c)
elif (a>c and a<b):
    print(b)
elif (a>b and a>c):
    print(a)
else:
    print("三个数中有相等的数")

a=int(input("请输入小明的成绩："))
if a==100:
    print("买辆车")
elif a>90:
    print("买MP4")
elif (60<a<90):
    print("买本参考书")
else:
    print("啥也不买")


a=int(input("请输入快捷号码："))
if a==1:
    print("拨爸爸的号码")
elif a==2:
    print("拨妈妈的号码")
elif a==3:
    print("拨爷爷的号码")
elif a==4:
    print("拨奶奶的号码")
else:
    print("输入有误，重新输入")



year=int(input("请输入年份"))
if(year%400==0) or ( (year%4==0) and (year%100!=0)):
    print("闰年")
else:
    print("平年")


