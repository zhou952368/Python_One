"""
1.列表
  相当于一个容器  可以存储多个数据 一次性可以处理多个数据
变量 只能存放一个数据  一次也只能处理一个数据

在列表中添加数据
list.append() 在列表的末尾添加数据  一次只能添加一条数据 加的是列表当做一个数据处理
list.extend()  在列表的末尾添加多个数据  添加数据类型只能是列表   会将所添加列表中的数据挨个拆分存在列表中
list.insert()   在列表指定位置加入数据  不会覆盖原数据  原数据回依次往后推
列表的运算
+ ：拼接操作
* ：重复操作

列表的判断
in ： 判断某一元素在不在列表中 在为True  不在为False
not in :  判断元素不在列表中  在为False  不在为True

列表的删除
list.remove() : 删除指定元素  没有改元素就报错
list.pop()  : 根据下标来删除元素并返回该元素 不写参数就默认删除最后一个
list.clear() : 清空列表中所以元素

列表的查找
list.len() : 查询列表的长度
list.index(): 根据元素查下标
list.count(): 查找元素出现的次数

列表的特点
 列表的单词是list标志[]
 列表是可变的
 列表可村存储不同类型的数据
 列表是有序的
 列表有下标
列表的遍历


"""
# age_list=[10,15,154,4,6,46,64,1,64,31,64,11,64,1,64,1,64,1,64,1,64,64,97,6,6,6]
# age_list.append(23)
# print(age_list)
# age_list.extend([45,56,78])
# age_list.insert(1,45)
# print(type(age_list))
# print(len(age_list))
# print(sum(age_list))
# print(max(age_list))
# print(age_list)

#列表运算
# list1=[1,2,3]
# list2=[4,5,6]
# list3=list1+list2
# print(list3)
# print(list1*3)


#列表的判断
# list4=[1,2,"a","b"]
# print(10 in list4)
# print(10 not in list4)

#列表的查找
# list6=[1,2,3,45,6,9,45]
# print(list6.index(45))
# print(list6.count(45))
# print(list6[:3])  #从零开始  截取不到最大值
# print(list6[3:])  #从3开始到末尾
# list6.sort() # 排序  从小到大
# print(list6)
# list6.reverse() #排序  使用reverse先用sort排序  在倒序
# print(list6)


"""
在程序中运行内存一般分为2块内存
变量存栈 值存堆
栈：整数 小数 布尔类型的变量存在栈中
堆：列表 字符串等其他的都在堆中
列表的复制
=复制的是地址值  一个改变会影响另一个（浅拷贝）
copy复制的数据 不会影响到别人（深拷贝）
"""
# list9=[1,2,3]
# list10=list9 #[1,2,3]
# list10[0]=100 #[100,2,3]
# list11=list9.copy()
# list11[0]=200
# print(list9)
# print(list10)
# print(list11)


#
# a=10
# b=a
# b=20
# print(a)
# print(b)
# print(id(list9))
# print(id(list10))


"""1.元组的单词是tuple  标志是()
2.元组一旦创建不能更改
3.元组的操作：截取 查找(查长度、查下标、查次数)
            拼接(+) 复制(=)  转
4.因为不能更改所以比较安全
5.元组有下标
6.元组是有序的
"""
# 创建一个空元组
# tuple1=()
# print(type(tuple1))
# 创建一个有多个数据的元组
# tuple2=(1,2,3,4)
# print(tuple2)
# # 创建有一个元素的元组
# tuple3=(1,)
# print(tuple3)
#
# print(tuple2[1:])
# tuple4=(1,2,"a","b")
# print(tuple4.index(2))
# print(tuple4.count("a"))
#
# tuple5=("c","d")
# tuple6=tuple4+tuple5
# print(tuple6)
#
#
# tuple7=tuple5
# print(tuple7)
#
# tuple8=("a","b","c")
# list1=list(tuple8)
# list1[0]="aa"
# print(list1)
# print(tuple8)
# tuple9=tuple(list1)
# print(tuple9)



'''
字典：是一个键值对形式的数据结构
    字典是没有下标的
    字典是无序的
    字典的键是唯一的
    字典的单词dict  标志{}
'''
# 创建字典
# print(dic["张三"])
# print(dic["刘效洋"])
# print(dic)
# # 在字典中添加值
# dic["王五"]=90
# dic.update({"aaa":30})
# # 根据键去删除
# dic.pop("刘效洋1")
# # 字典是无序的，到底谁是最后一个不知道，会报错
# # dic.pop()
# print(dic)
# print("----------------")
# 报错
# print(dic["张三1"])
# None空值 不报错
# print(dic.get("张三1"))


'''
遍历键
'''
dic={"张三":100,
     "刘效洋":10,
     "李四":"zhou",
     "asd":1,
     "abc":2,
     "刘效洋1": 10}
if dic["李四"]=="zhou":
    print(123456)
# for i in dic:
#     print(i)
# print("-----根据键得到值------")
# for i in dic:
#     #print(dic[i])
#     print(dic.get(i))
# print("------遍历值-----")
# for i in dic.keys():
#     print(i)
# print("------遍历键和值-----")
# for i,j in dic.items():
#     print(i,j)


'''
遍历：一个一个获取
for循环的变量指的就是列表中的数据，不是下标
while循环的变量可以当做下标来处理，不是元素
'''
# list1=["a","b","c","d"]
# for i in list1:
#     print(i)
#
# print(i)
# i=0
# while i<len(list1):
#     print(list1[i])
#     i+=1
#
# for i in list1:
#     print(i)
#
# for i in range(30,40):
#     print(i)

"""
创建set集合 必须依靠列表 元祖 字典来完成
set集合中没有下标 没有重复 无序
add()  : 一次添加有一个数据
updata(): 一次添加多个数据
remove(): 根据元素删除
pop():   随机删除
没有下标 只能通过for循环遍历
"""
# s1=set([1,2,1,2,1,1,1,])
# s1.add(3)
# for i in s1:
#     print(i)
# print(s1)