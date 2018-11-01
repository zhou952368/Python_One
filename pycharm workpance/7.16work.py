#去除列表中重复的元素
# list1=[1,2,3,4,51,3,4,4,"a","a"]
# list2=[]
# for i in list1:
#     if not i in list2:
#         list2.append(i)
# print(list2)


#输入商品名字和商品价格，将名字和商品价格存储到列表、元组、字典、set中都可，自己选择，
#每次录入完一个商品信息就询问是否继续录入，y继续，n退出。退出后打印商品列表信息。
# dic={"水":2,"饼干":5,"笔":2}
# while True:
#     i=input("请输入y或者n:")
#     if i=="y":
#         key=input("input key:")
#         value=int(input("input value"))
#         dic.update({key:value})
#     elif i=="n":
#         break
# for i,j in dic.items():
#     print(i,j)


#3.做一个登陆注册的案例
# python字典中get用于返回指定键的值
dic1={"zhou":952368,"feng":123456,"aaa":123}
while True:
    i=input("已有账号请输入1进行登录，请输入2进行注册,3 退出:")
    if i=="1":
        name=input("input name:")
        password=input("input password:")
        if name in dic1.keys():
            mima=dic1.get(name)
            if mima==password:
                print("登录成功")
            else:
                print("密码有误 请重新输入")
        elif "name:password" not in dic1:
            print("登录失败")
            continue
    elif i=="2":
        name=input("input name:")
        password=input("input password:")
        if name in dic1.keys():
            print("已经注册过了")
        else:
            dic1.update({name:password})
            print("注册成功")
    elif i==3:
        break


#4.模拟斗地主洗牌发
import random
list1=["红桃","梅花","方块","黑桃"]
list2=["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
list3=["大王","小王"]
for i in list1:
    for j in list2:
        pai=i+j
        list3.append(pai)
random.shuffle(list3)
play1=[]
play2=[]
play3=[]
dp=[]
# 发牌 51
i=0
while i<51:
    if i%3==0:
        play1.append(list3[i])
    elif i%3==1:
        play2.append(list3[i])
    elif i%3==2:
        play3.append(list3[i])
    i+=1
j=51
while j<54:
    dp.append(list3[j])
    j+=1
print(play1)
print(play2)
print(play3)
print(dp)




