"""
1.封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
封装方法，求总分，平均分，以及打印学生的信息。
"""


class Student:
    def __init__(self, name, age, sex, english, mush, chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.english = english
        self.mush = mush
        self.chinese = chinese
        print("姓名{0},年龄{1}, 性别{2}, 各科成绩为英语：{3} 数学：{4} 语文：{5}".format(self.name, self.age, self.sex,
                                                                     self.english, self.mush, self.chinese))

    def total(self):
        print("%s的各科总分为%d" % (self.name, self.english + self.mush + self.chinese))

    def average(self):
        print("%s的各科平均分为%f" % (self.name, (self.english + self.mush + self.chinese) / 3))


stu1 = Student("zhou", 23, "男", 66, 77, 88)
stu1.total()
stu1.average()

"""
2.创建一个Cat类，属性:姓名，年龄 方法：抓老鼠
创建老鼠类，属性：姓名，型号。
一只猫抓一只老鼠，再创建一个测试类：创建一个猫对象，再创建一个老鼠对象，
打印观察猫抓的老鼠的姓名和型号。
例如：一个5岁的名叫tom的猫抓到了一只名叫jerry的小老鼠。
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Mouse:
    def __init__(self, name1, model):
        self.name1 = name1
        self.model = model


class test(Cat, Mouse):
    def __init__(self, name, age, name1, model):
        Cat.__init__(self, name, age)
        Mouse.__init__(self, name1, model)

    def catch_mouse(self):
        print("一直%d岁的名叫%s的猫抓到了一直名叫%s的%s老鼠" % (self.age, self.name, self.name1, self.model))


cat_mouse = test("tom", 5, "jerry", "小")
cat_mouse.catch_mouse()

"""
3.创建一个学生(Student)类：
学生应该有姓名(name)、年龄(age)、性别(sex)，班级号(classNum)，座位号(sno)。
提供一个方法(displayInfo())用来显示这个学生的姓名、年龄、性别、所在的班级和他的座位号。
在测试模块中创建两个学生对象，分别调用displayInfo()方法显示各自的信息。
"""


class Student:
    def __init__(self, name, age, sex, classNum, sno):
        self.name = name
        self.age = age
        self.sex = sex
        self.classNum = classNum
        self.sno = sno

    def displayInfo(self):
        print("姓名：{0} 年龄：{1} 性别：{2} 班级号：{3} 座位号：{4}".format(self.name, self.age, self.sex,
                                                            self.classNum, self.sno))


student1 = Student("zhou", 23, "男", "14班", "三排五座")
student1.displayInfo()
student2 = Student("feng", 21, "女", "14班", "三排六座")
student2.displayInfo()
"""
4.定义一“圆”Cirlcle类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系。
点类
X  y
圆类:
圆心点和半径
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cirlcle(Point):
    def __init__(self, x, y, r):
        Point.__init__(self, x, y)
        self.r = r

    def area(self):
        print("面积为：{0}".format(3.14 * self.r ** 2))

    def perimeter(self):
        print("周长为：{0}".format(self.r * 3.14 * 2))

    def localhost(self):
        pass

yuan = Cirlcle(5, 6, 4)
yuan.area()
yuan.perimeter()
