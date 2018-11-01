# a=int(input("请输入您的身高："))
# b=int(input("请输入您妻子的身高："))
# while True:
#     sex=input("请输入您孩子的性别：")
#     if sex=="男":
#         sum=(a+b)/2*1.08
#         break
#     elif sex=="女":
#         sum=(a+b-13)/2
#         break
#     else:
# 	    print("输入有误，请重新输入")
# print(sum)



while True:
    year=int(input("请输入一个年份："))
    month=int(input("请输入一个月份："))
    if month in [1,3,5,7,8,10,12]:
        print("%d 年 %d 月有31天"%(year,month))
        break
    if month in [4,6,9,11]:
        print("%d 年 %d 月有30天"%(year,month))
        break
    if month==2:
        if year%4==0 and year%100!=0 or year%400==0:
            print("%d 年 %d 月有29天"%(year,month))
        else:
            print("%d 年 %d 月有28天"%(year,month))
        break
    if month not in range(1,13):
        print("月份输入有误，请重新输入")

