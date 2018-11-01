# class Person:
#
#     def __init__(self):
#         self.gun=None
#
#     def shoot(self):
#         self.gun.fire()
#
# class Gun:
#
#     def __init__(self):
#         self.count=0
#
#     def fire(self):
#         if self.count<=0:
#             print("没子弹了")
#             return
#         self.count-=1
#         print("子弹发射出去了，还剩%d"%self.count)
#
# g1=Gun()
# g1.count=5
# p=Person()
# p.gun=g1
# p.shoot()
# p.shoot()
# p.shoot()
# p.shoot()
# p.shoot()
# p.shoot()


# class car:
#     def __init__(self,color):   #当创建实体类的时候，系统会自动调用构造方法 实现对类的初始化操作
#         self.color=color
#         print(self.color)
#     def toot(self):
#         print("%s的车在鸣笛.."%(self.color))
# CAR=car("黑色")
# z=car("baise")
# CAR.toot()


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("%s %d"%(name,age))
#     def __del__(self):     #可以删除一个对象  四方他所占用的资源
#         print("******del*********")
#
# z=person("name",22)


