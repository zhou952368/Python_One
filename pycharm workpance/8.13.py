class person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print("姓名：%s  年龄：%d  性别：%s "%(name,age,sex))

class tercher(person):
    def __init__(self):
        self.gongage=None
        print("姓名：%s  年龄：%d  性别：%s 工龄：%d"%(self.name,self.age,self.sex,self.gongage))
        print("我承诺，我会认真教课")
        print("王飞喜欢打篮球")
class student(person):
    def __init__(self):
        self.id=None
        print("我承诺，我会好哈学习")
        print("小明喜欢踢足球")
tersher=person("王飞","男","30")
