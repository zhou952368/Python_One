#创建一个手机类，要求有型号、颜色、价格、运行内存4个属性，行为有打电话、玩游戏、看视频。
# 在打电话中输出：颜色为XX的XX手机可以打电话，价钱是XX。在玩游戏中输出：XX手机可以玩游戏，
# 运行内存中共有XX，价钱是XX。看视频自由发挥。创建对象并调用函数执行。


class phone:
    def __init__(self,xinghao,color,price,yunxin):
        self.xinghao=xinghao
        self.color=color
        self.price=price
        self.yunxin=yunxin
    def daianhau(self):
        print("颜色为：%s 的%s手机可以打电话,价钱是：%d"%(self.color,self.xinghao,self.price))
    def playgame(self):
        print("%s手机可以打游戏,运行内存有%s G 价钱为：%d"%(self.xinghao,self.yunxin,self.price))
xinghao=phone("小米8","白色",2699,"6")
xinghao.daianhau()
xinghao.playgame()


# 先分析有哪些对象
# 再分析有什么类
# 接着分析每个类有什么属性和行为

class hand:
    def __init__(self):
        self.Card=None
class card:
    def __init__(self):
        self.num=""
        self.huase=""
class person:
    def __init__(self):
        self.left=None
        self.right=None
    def change(self):
        c=self.left
        self.left=self.right
        self.right=c

c1=card()
c1.num="3"
c1.huase="红桃"

c2=card()
c2.num="4"
c2.huase="黑桃"

l=hand()
l.Card=c1.num+c1.huase

r=hand()
r.Card=c2.num+c2.huase

p=person()
p.left=l
p.right=r
p.change()
print(p.left.Card,p.right.Card)
