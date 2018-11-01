user={"zhou":952368}
gwc=[]
sum=0
def denglu():
    while True:
        name=input("请输入用户名：")
        passwd=int(input("请输入密码："))
        if name in user.keys():
            mima=user.get(name)
            if mima==passwd:
                print("登录成功")
                break
            else:
                print("密码有误 请重新输入")
        elif "name:passwd" not in user:
            print("登录失败")
def jingri():
    global sum
    print("***** 1 连衣裙 59")
    print("***** 2 运动鞋 69")
    print("***** 3 风衣   99")
    bh=int(input("请输入编号："))
    if bh==1:
        gwc.append("连衣裙 59")
        sum+=59
    elif bh==2:
        gwc.append("运动鞋 69")
        sum+=69
    elif bh==3:
        gwc.append("风衣   99")
        sum+=99
    print('购买成功,是否继续y/n')
    isY=input()
    if isY=="y":
        jingri()
    else:
        print("购物车商品有：")
        for i in gwc:
            print(i)
        isN=input("请输入n返回上一级")
        if isN=="n":
            shou()
def shou():
    print("***************欢迎进入手机淘宝***************")
    print("***************1 今日特卖***************")
    print("***************2 女生服装***************")
    print("***************3 男生服装***************")
    print("***************4 美食糕点***************")
    print("***************5 结算***************")
    a=int(input("请输入你要进行的操作："))
    if a==1:
        jingri()
    elif a==2:
        pass
    elif a==3:
        pass
    elif a==4:
        pass
    elif a==5:
        jiesuan()
def jiesuan():
    print("购物车商品有：")
    for i in gwc:
        print(i)
    print("本次总共消费：%d"%sum)
print("**************1 登录**************")
print("**************2 退出**************")
caozuo=int(input("请输入你要进行的操作:"))
if caozuo==1:
    denglu()
    shou()
elif caozuo==2:
    print()

