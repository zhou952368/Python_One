'''
__str__()
内置函数，自动执行
打印对象名字输出的是地址值
打印对象名默认调用的是__str__()

重写：重写一遍，覆盖原来的函数
__str__()默认打的是地址值

__repr__():和__str__()一样
'''

class Person:
    def __init__(self):
        self.name=None
        self.age=None
        self.sex=None
        self.height=None

    def __str__(self):
        return "10"
    def __repr__(self):
        return "姓名%s，年龄：%d，性别%s，身高%d"%(self.name,self.age,self.sex,self.height)
p1=Person()
p1.name="张三"
p1.age=10
p1.sex="男"
p1.height=170
print(p1)
#print("姓名%s，年龄：%d，性别%s，身高%d"%(p1.name,p1.age,p1.sex,p1.height))

# p2=Person()
# p2.name="李四"
# p2.age=20
# p2.sex="男"
# p2.height=170
# print(p2)
# print("姓名%s，年龄：%d，性别%s，身高%d"%(p2.name,p2.age,p2.sex,p2.height))


# print(p1)
# print(p1.__str__())

'''
访问限制
私有：只能自己使用的，别人不能使用
好处：外部不能随意更改，安全性提高
        数据过滤
'''

class Person:
    def __init__(self):
        self.name=None
        self.__age=None

    def setAge(self,a):
        if a<0:
            print("不合法")
        else:
            self.__age=a
            print("合法")

    def getAge(self):
        return self.__age

p1=Person()
p1.setAge(-10)
print(p1.getAge())

