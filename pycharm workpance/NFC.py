class NPC:
    list1=[]
    def __init__(self):
        self.ID=None
        self.name=None
        self.jianjie=None

class Player:

    def __init__(self):
        self.list2=[]

    def add(self):
        bh=int(input("请选择队伍编号："))
        isHave=False
        # 遍历可选NPC列表
        for i in NPC.list1:
            # 判断输入的编号在不在列表中
            if bh==i.ID:
                self.list2.append(i)
                isHave=True
                break
            else:
                isHave=False
        if isHave==False:
            print("没有")
    def remove(self):
        bh=int(input("请输入要剔出的编号："))
        for i in self.list2:
            if bh==i.ID:
                self.list2.remove(i)
                break
        else:
            print("没有，不能删除")
    def show(self):
        for i in self.list2:
            print(i.ID,i.name,i.jianjie)
# 创建NPC对象
n1=NPC()
n1.ID=10
n1.name="阿尔萨斯"
n1.jianjie="使用霜之哀伤"
n2=NPC()
n2.ID=12
n2.name="吉安娜"
n2.jianjie="使用奥数法术"
n3=NPC()
n3.ID=31
n3.name="乌瑟尔"
n3.jianjie="使用圣光力量"
NPC.list1.append(n1)
NPC.list1.append(n2)
NPC.list1.append(n3)
# 创建玩家对象
p = Player()
# 遍历NPC列表
while True:
    print("可选列表")
    for i in NPC.list1:
        print(i.ID, i.name, i.jianjie)
    print("当前列表")
    p.show()
    print("请选择操作")
    print("1.邀请组队")
    print("2.剔出")
    print("3.完成")
    bh = int(input())
    if bh == 1:
        p.add()
    elif bh == 2:
        p.remove()
    elif bh == 3:
        exit()





