"""
1. 3个孩子吃3个饼需要3分钟，99个孩子吃99个饼需要多长时间？
2. 一列数按“1，4，2，8，5，7，1，4，2，8，5，7，1，4，2，8，5，7„”
排列，问第50个数字是几？第96个数字是几？
3. 猴大哥背着一筐香蕉往山上跑，他每走5步要用3分钟，然后还要休息1分钟，走了45步，才走到山顶，一共用了()分钟。
4. 一捆绳子，第一次用去一半，第二次用去剩下的一半，这时还剩10米，这捆绳子原来多长？
5. 军军今年2岁，爸爸26岁，几年之后爸爸的年龄是军军的3倍？
6. 鸭免同笼，共有45个头，146只脚，笼中兔、鸭各有多少只？

"""

# for tu in range(1, 46):
#     if tu * 4 + (45 - tu) * 2 == 146:
#         print(tu)

list = [1, 2, 1, 4, 10, 5, 6, 2, 8, 9, -1, 0]
for i in range(0, len(list)):
    for j in range(i, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
            print(list)
print(list)


def binary_search(numbers, n):
    mid = int(len(numbers) / 2)
    if len(numbers) >= 1:
        if numbers[mid] > n:
            return binary_search(numbers[:mid], n)
        elif numbers[mid] < n:
            return binary_search(numbers[mid:], n)
        else:
            return numbers[mid]
    else:
        return


print(binary_search([1, 2, 4, 6], 5))
