# 静态方法 （就是一个简单的函数  不关注函数内的对象）可以在类中被调用self.方法名() 或者 类名.方法名()
# 在类外被调用 类名.方法名()


class A:
    def __init__(self):
        pass

    def a(self):
        A.test()

    @staticmethod
    def test():
        print("zhoujainaan")
i = A()
i.a()
A.test()


class A:
    number = 0
    obj = None

    def __init__(self, value):
        self.value = value

    @classmethod
    def test(cla, *args):
        # if cla.number < 1:
        #     cla.number += 1
        #     cla.obj = cla(*args)
        # return cla.obj
        if cla.obj is None:
            cla.obj = cla(*args)
            return cla.obj
        else:
            return cla.obj

    def __str__(self):
        return self.value

a = A.test("a")
b = A.test("b")
c = A.test("c")
print(a, b, c)
