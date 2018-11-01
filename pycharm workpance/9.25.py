"""
面向对象编程
定义类首字母大写
类中的函数一般称作方法 : method
"""


class Animal:

    def __init__(self, breed, name, sex):
        """
        实例化一个对象
        :param breed: 品种
        :param name: 姓名
        :param sex: 性格
        :return:
        """
        self.breed = breed
        self.name = name
        self.sex = sex

    def eat(self):
        print("%s在吃饭" % self.name)

    def fight(self):
        print("%s不是在打架就是在去打架的路上" % self.name)


stu1 = Animal("猫科", "东北虎", "公")
stu1.eat()
stu2 = Animal("鼬科", "平头哥", "公")
stu2.fight()
