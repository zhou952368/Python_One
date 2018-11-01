"""
1.做一个模拟吃饭的小程序，吃5天，钱不够了或者5天到了就结束程序。
2.用户录入商品的名称和价格，将商品的名称和价格存储到一个列表或者字典中。
要求：录入商品名称和价格的时候一起录入用逗号分隔。每录完3条商品就提示是否继续录入。

当录入结束后就打印当前商品的信息列表。
3.随机出一道推荐菜，提示：今日推荐菜为XXX打8折。
4.到此商品列表和推荐菜都有了。现在开始吃饭，总共吃5天，每天都有推荐菜。推荐菜都是打8折。
5.定义一个金钱变量。
6.第一天吃饭：让用户在商品列表中选择要购买的商品，每个商品都有编号。
  输入对应的编号检测钱是否够吃饭，够就扣掉这个钱，不够就重新选择。
  当吃完5天或者没钱吃饭之后结束程序。在最后输出每天吃饭的商品信息和价格，输出还剩多少钱
"""
import random
name_list=[]
price_list=[]
money=100
count=0
xf_list=[]
while True:
    info=input("请输入商品信息：")
    li1=info.split(",")    #将输入的字符串以逗号分隔  形成一个列表
    name_list.append(li1[0])
    price_list.append(float(li1[1]))
    count+=1
    if count%3==0:
        isY=input("是否继续")
        if isY=="n":
            break
print("商品信息如下：")
i=0
while i<len(name_list):
    print(i+1,name_list[i],price_list[i])
    i+=1
day=1
index=random.randint(0,len(name_list)-1)
while day<=5:
    print("第%d天"%day)
    print("特价菜是%s，价格是%.2f"%(name_list[index],price_list[index]*0.8))
    bh=int(input("吃啥："))
    # 获取编号所对应的价格
    price=price_list[bh-1]
    if money>=price:
        money-=price
        print("剩余%.2f"%money)
        xf_list.append(name_list[bh-1]+" "+str(price))
        day += 1
        index = random.randint(0, len(name_list) - 1)
    else:
        print('钱不够，重新选择')
        m= min(price_list)
        if money<m:
            print("吃不起了，再见")
            break
print("总共吃了%d天，总共消费%f"%(day-1,100-money))
print("消费清单：")
for i in xf_list:
    print(i)