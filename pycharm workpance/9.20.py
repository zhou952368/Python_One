# 2. 使用函数式编程，获得1970~2018所有的闰年
# 过滤器
print(list(filter(lambda n: n % 4 == 0 and n % 100 != 0 or n % 400 == 0, range(1970, 2019))))

"""
1. 使用map进行函数式编程实现如下功能：
将  [1,2,3,4,5]  和  ['a','b','c','d','e'] 合并为
{[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]}
"""
# map()函数
l = [1, 2, 3, 4, 5]
l1 = ['a', 'b', 'c', 'd', 'e']
m = list(map(lambda x, y: (x, y), l, l1))
print("{" + str(m) + "}")

dict = {"name": "zhou", "age": 23, "sex": "男"}
# 遍历字典中所有的键
for i in dict.keys():
    print(i)
# 遍历字典中所有的值
for j in dict.values():
    print(j)
# 遍历字典中所哟的键值对
for key, value in dict.items():
    print(key, value)
