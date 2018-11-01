def lol():
    a=100
    b=100
    while True:
        i=int(input("请选择你释放的技能 1 德玛西亚 2 小陀螺:"))
        if i==1:
            a-=20
            b-=10
            print("移动速度增加！攻击造成沉默！德玛西亚！")
            print("当前法力值：%d"%a)
            print("敌方剩余血量%d"%b)
            print("="*60)
            if a<20:
                print("法力不够")
                break
            if b<=0:
                print("成功击杀敌方英雄")
                break
        if i==2:
            a-=10
            b-=20
            print("我是小陀螺，刷刷刷转起来")
            print("当前法力值：%d"%a)
            print("敌方剩余血量%d"%b)
            print("="*60)
            if a<10:
                print("法力不够")
                break
            if b<=0:
                print("成功击杀敌方英雄")
                break
lol()


import random
a=3
while True:
    b=int(input("请输入验证码的位数："))
    if b<4:
        b=4
        print("验证码不能低于4位，我已经给你改成4位了")
    elif b>6:
        b=6
        print("验证码太长了，最大6位构成。")
    i=random.sample(('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'),b)
    str1="".join(i)
    str2=str1.lower()
    print(str2)
    break
while True:
    str=input("请对照上面输入验证码：")
    yan=str.lower()
    if yan==str2:
        print("验证成功")
        break
    elif yan!=str2:
        a-=1
        print("验证错误，您好有%d次机会"%a)
    if a==0:
        print("验证失败")




