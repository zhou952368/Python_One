# def f(n):
#     if n==1:
#         return 1
#     else:
#         return f(n-1)+n
#
# print(f(100))

import random
t = ["石头", "剪刀", "布"]
def caiquan():
    while True:
        x = input("请输入剪刀，石头，布：")
        j = t.index(x)
        n = random.randint(0, 2)
        y = t[n]
        if j == n:
            continue
        elif (j == 1 and n == 2) or (j == 2 and n == 0) or (j == 0 and n == 1):
            print("你赢了")
            break
        else:
            print("你输了")
            break
caiquan()


