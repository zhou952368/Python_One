"""
遍历一个文件夹中所有的文件  并统计各种文件都有多少
"""
import os
import os.path

list1 = []
list2 = []
dict1 = {}


def folder(path):
    """
    遍历一个文件夹中所有的文件  并统计各种文件都有多少
    :param path: 传入一个路径  统计该路径下所有文件的数量
    :return: 已字典的形式返回不同类型的文件的数量  key：文件的后缀名  value:文件的数量
    """
    # 判断该路径下是不是文件夹
    if os.path.isdir(path):
        # 遍历该文件夹 并将结果赋给folder_list
        folder_list = os.listdir(path)
        for i in folder_list:
            # 循环folder_list 与原路径拼接成一个新的路径
            path1 = os.path.join(path, i)
            # 判断新路径下的内容是不是文件夹 是就重新调用函数（递归）
            if os.path.isdir(path1):
                folder(path1)
            elif os.path.isfile(path1):
                list1.append(i)


if __name__ == "__main__":
    folder("D:/pycharm workpance")
    for a in list1:
        # 遍历出来的文件以'.'分隔 取到取到最后一个
        suffix = a.split('.')[-1]
        # 将取到的后缀名重新添加到一个新的列表
        list2.append(suffix)
        # 使用字典 列表的内置函数count()  统计各个元素出现的次数
        dict1[suffix] = list2.count(suffix)
    print(dict1)
