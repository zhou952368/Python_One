"""
如何定义一个函数  remove_all 用来删除list中重复的元素
numbers=[1.2.2.2.2.5]
"""
# numbers=[1,2,2,2,2,2,2,5]
# def remove_all():
#     numbers.remove(2)
# for num in numbers:
#     if num==2:
#         remove_all()
# print(numbers)

# list1 = [1, 2, 3, 4, 51, 3, 4, 4, "a", "a"]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


"""
猴大哥背着一筐香蕉往山上跑，他每走5步要用3分钟，然后还要休息1分钟，
走了45步，才走到山顶，一共用了()分钟。（使用Python代码如何实现？）

"""
sum = 45
time = 0
l = 0
while l <= sum:
    l += 1
    if l % 5 == 0:
        time += 4
print(time)
