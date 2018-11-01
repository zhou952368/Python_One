#输出20-80之间能被3整除的数，每5个一行
i=0
for a in range(20,81):
    if a%3==0:
        i+=1
        print(a,end=" ")
    if i%5==0:
        print("")

#利用循环和判断做一个登陆效果，有3次登陆机会。
i=3
print("----------欢迎来到登录界面-------------")
while True:
    name=input("请输入用户名：")
    password=input("请输入密码：")
    if name=="zhou" and password=="952368":
        print("登录成功")
        break
    if name!="zhou" or password!="952368":
        i-=1
        print("登录失败，您还有%d次机会"%i)
    if i==0:
        print("连续三次登录失败，账号已锁定")
        break

# i=3
# money=1000
# print("欢迎使用ATM机")
# print("----------请插入您的银行卡-------------")
# while True:
#
#     password=input("请输入密码：")
#     if password=="952368":
#         print("读卡成功")
#         def mian():
#             while True:
#                 print("请选择您要进行的操作：1 查询账户余额 2 存款 3 取款 4 退出")
#                 key=int(input("请输入你的选择："))
#                 if key==1:
#                     chaxun()
#                 elif key==2:
#                     cunkuan()
#                 elif key==3:
#                     qumoney()
#                 elif key==4:
#                     tuichu()
#                     break
#         def chaxun():
#             print("当前卡内余额为：%d"%money)
#         def cunkuan():
#             cunmoney=int(input("请输入存款金额："))
#             print("存入金额为：%d  当前账户余额为：%d"%(cunmoney,money+cunmoney))
#         def qumoney():
#             qumonet=int(input("请输入取款金额："))
#             if qumoney>money:
#                 print("账户余额不足，请重新输入")
#             else:
#                 print("取款金额为：%d  当前账户余为："%(qumoney,money-qumoney))
#         def tuichu():
#             print("请收好您的磁卡")
#     if password!="952368":
#         i-=1
#         print("密码错误，您还有%d次机会",i)
#     if i==0:
#         print("连续三次密码错误，账号已锁定")
#         break


#模拟ATM机存取款操作
i=3
money=1000
print("欢迎使用ATM机")
print("----------请插入您的银行卡-------------")
while True:

    password=input("请输入密码：")
    if password=="952368":
        print("读卡成功")
        print("请选择您要进行的操作：1 查询账户余额 2 存款 3 取款 4 退出")
        while True:
            key=int(input("请输入你的选择："))
            if key==1:
                print("当前卡内余额为：%d"%money)
                print("="*50)
            elif key==2:
                cunmoney=int(input("请输入存款金额："))
                money=cunmoney+money
                print("存入金额为：%d  当前账户余额为：%d"%(cunmoney,money))
                print("="*50)
            elif key==3:
                while True:
                    qumoney=int(input("请输入取款金额："))
                    if qumoney>money:
                        print("账户余额不足，请重新输入")
                        print("="*50)
                    else:
                        money=money-qumoney
                        print("取款金额为:",qumoney,"  当前账户余为：",money)
                        print("="*50)
                        break
            elif key==4:
                print("请收好您的磁卡")
                break
        break
    if password!="952368":
        i-=1
        print("密码错误，您还有",i,"次机会")
        print("="*50)
    if i==0:
        print("连续三次密码错误，账号已锁定")
        print("="*50)
        break



#4.扩展题：输出1-3+5-7+9-…..101的和
for i in range(1,102,2):
    b=2*i-1
    c=2*i
    print(b)
print(b-c)

#逻辑思维题：有一对兔子，从出生后第3个月起每个月都生一对兔子，，假如兔子都不死，问每个月的兔子总数为多少？
i= 1
j=1
a=0
while a< 100:
    a+=1
    print("第 %d 个月有 %d 对兔子"%(a,i))
    i=j
    j=i+j