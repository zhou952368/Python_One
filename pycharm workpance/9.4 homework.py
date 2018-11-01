"""
1. 【需求】
定义一个变量result的值为5
使用input接收用户输入的数字，
并判断用户输入的数字是不是5

2. 【需求】
从网络上搜集判断体重是否标准的公式。
然后，根公式做一个自动根据身高和体重的输入值判断体重是否标准的一个命令行应用程序。

"""
result=5
while True:
    a=int(input("请输入一个数字:"))
    if a==result:
        print("用户输入的数字无误")
        break
    elif a!=result:
        print("用户输入的数字有误")



height = int(input("请输入您的身高："))
weight=int(input("请输入您的体重："))
nan=(height-80)*0.7
nv=(height-70)*0.6
while True:
    sex=input("请输入您的性别：")
    if sex=="男":
        if nan*0.9<= weight <=nan*1.1:
            print("您的体重为标准体重")
        elif nan*0.8<= weight <=nan*0.9:
            print("您的体重过轻")
        elif nan*1.1<= weight <=nan*1.2:
            print("您的体重过重")
            break
    elif sex=="女":
        if nv*0.9<= weight <=nv*1.1:
            print("您的体重为标准体重")
        elif nv*0.8<= weight <=nv*0.9:
            print("您的体重过轻")
        elif nv*1.1<= weight <=nv*1.2:
            print("您的体重过重")
            break
    else:
        print("性别输入有误，请重新输入")




