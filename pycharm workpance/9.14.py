# 在路径前加一个r  可以让路径中的字符没有特殊含义
# f = open(r"C:\Users\fer miss together\Desktop\桃花源记.txt", encoding="gbk")
# #  最保险推荐的写法
# f1 = open("C:/Users/fer miss together/Desktop/桃花源记.txt", encoding="gbk")
# print(f1.read())


#  1. 文件过滤。显示一个文件的所有行，过滤掉以'#'开头的行。
# with open("text.txt", "r", encoding="GBK") as f:
#     for line in f.readlines():
#         if line.startswith('#'):
#             continue
#         print(line)
#  2. 提示输入数字n，文件f，输出文件的f的前n行。
# source = input("请输入文件所在的路径：")
# line2 = int(input("请输入要打印的文件的行数："))
# with open(source, "r", encoding="GBK") as f1:
#     for i in range(line2):
#         print(f1.readline())

#  3. 获得一个文件的总行数。
# with open("text.txt", "r", encoding="GBK") as f2:
#     print(len(f2.readlines()))
#     print(type(f2.readlines()))
#  4. 提示输入文件f，默认显示前5行，提示输入数字n，每次输入n则显示文件的后续5行。
# source = input("请输入文件所在的路径：")
# with open("text.txt", "r", encoding="utf-8") as f3:
#     list1 = f3.readlines()
#     print(list1[:5])
#     i = 5
#     j = 10
#     while i <= len(list1):
#         n = input("是否继续进行操作y/n:")
#         if n == "y":
#             print(list1[i:j])
#             i += 5
#             j += 5
#         else:
#             break
#  5. 附加题：写一个从文件读入考试成绩的程序。（自行设计存储考试成绩的文本格式）（提示：可以使用join、split
# import json
# def append():
#         dict1 = {}
#         student_name = input("请输入学生的名字：")
#         score_mush = input("请输入数学成绩：")
#         score_english = input("请输入英语成绩：")
#         score_computer = input("请输入计算机的成绩：")
#         dict1.update({"name": student_name, "mush": score_mush, "english": score_english, "computer": score_computer})
#         print("添加成功！")
#         h = dict1
#         return str(h)
#
#
# def list_student():
#     print("编号\t名字\t数学\t英语\t计算机")
#     with open("kaoshi.txt", "r", encoding="utf-8") as f5:
#         for i, lin in enumerate(f5.readlines()):
#             dic = eval(lin)
#             print("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}".format(i+1, dic["name"], dic["mush"],
#                                                            dic["english"], dic["computer"]))
#
#
# def del_student():
#
#     pass
# list_student()
# # with open("kaoshi.txt", "a+", encoding="utf-8") as f4:
# #     f4.write(str(append()+'\n'))

#  6. 附加题：写一个计算器calc.py。
#  7. 附加题：让计算机接受命令行参数，例如 ：  python calc.py 2 + 2