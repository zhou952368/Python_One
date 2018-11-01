1.#做一个类似计算器的效果，键盘录入2个数字，在录入一个符号（+ - * %），判断符号是加减乘除哪一个，如果是+就输出2数之和，如果是减就输出2数之差
a=float(input("请输入一个数字"))
b=float(input("请输入一个数字"))
fuhao=str(input("请输入：(+,-,*,%)"))
if fuhao=="+":
    print(a+b)
elif fuhao=="-":
    print("a-b")
elif fuhao=="*":
    print(a*b)
elif fuhao=="%":
    print(a%b)


#2.写一段代码判断一个人的体重是否合格：公式：（身高-108）*2=体重，可以有10斤左右的浮动

shengao=float(input("请输入你的身高"))
tizhong=float(input("请输入你的体重"))
if abs(((shengao-108)*2)-tizhong)<10:
    print("体重合格")
else:
    print("体重不合格")


#3.int a=10;int b=20;对a和b进行交换，让a=20,b=10
a=int(input("输入一个数"))
b=int(input("输入一个数"))
c=b
b=a
a=c
print(a,b)


#4.预习：循环  for和while循环，尝试做出下面的题：循环键盘录入5名学生的成绩并计算总分和平均分，案例效果如下：




