class Dog:
    def speak(self):
        print('wangwang~')


class Cat:
    def speak(self):
        print('miaomiao~')


def foo(obj):
    obj.speak()


foo(Dog())
foo(Cat())
