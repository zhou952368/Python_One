"""
循环结构
for循环 while循环
循环：重复的做某一件事情
占位符 :  %d 整型   %f（%.2f  保留两位小数  保留一位回知道四舍五入） 小数  %s 字符串
break: 结束整个循环
continue:结束本次循环 进行下次循环
pass:空函数 在模块中不知道写什么的时候可以使用  让程序运行起来
循环条件：1,定义起始值 2，些循环条件 3， 初值递增（递减）
注意：在程序中0代表False 其他数字都代表True
while.....else:在循环正常结束的时候执行else语句 非正常结束（break）就不会执行else语句
for循环
for 变量名称 in 列表
for回结合range()函数结合使用
range():生成一堆数据，将数据存储在列表（容器）中,range范围内无法打印最大值
列表 list[]
"""
i=int(input("请输入第一个数:"))
sum=0
while i<10:
    i+=1
    sum=sum+i
print(sum)


i=int(input("请输入第一个数:"))
sum=0
while i<100:
    i+=2
    sum=sum+i
print(sum)

i=1
sum=0
while i<=100:
    if i%3==0:
        sum+=i

    i+=1
print(sum)


i=100
while 100<=i<1000:
    c=i%10
    b=i//10%10
    a=i//10//10%10
    if a**3+b**3+c**3==i:
        print(i)
    i+=1

i=10000  #回文数
num=0
while 10000<=i<100000:
    a=i//10000
    b=i//1000%10
    c=i//100%100%10
    d=i%100//10
    e=i%10
    if a==e and b==d and a+b+d+e==c:
        print(i)
        num+=1
    i+=1
print(num)

i=1
num=0
while 1<=i<1000:
    if (i%3==2)and(i%5==3)and(i%7==2):
        print(i)
        num+=1
    i+=1
print(num)


sum=0
num=0
while True:
    i=input("请录入一个学生的成绩:")
    if i=="over":
        print("录入结束")
        break
    elif int(i)<0:
        print("输入有误，请重新输入")
        continue

    sum+=int(i)
    num+=1
    pingjun=sum/num
print(sum,pingjun,num)


i=100
num=0
for i in range(100,1000):
    c=i%10
    b=i//10%10
    a=i//10//10%10
    if a**3+b**3+c**3==i:
        print(i)
    i+=1


