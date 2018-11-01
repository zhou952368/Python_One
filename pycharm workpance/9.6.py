#获取指定目录下以.py结尾的文件名
import os
s1=os.listdir(r"D:\pycharm workpance")
for a in s1:
    if a.endswith(".py"):
        print(a)