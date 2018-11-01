"""
print(对象) 将优先执行__str__()
在交互模式中  直接输入对象将优先执行__repr__()
"""


class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print("__str__")
        return self.name

    def __repr__(self):
        print("__repr__")
        return self.name

a = A("aaaa")
s = a.__repr__()
print(s)





