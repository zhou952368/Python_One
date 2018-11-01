'''
ATM:
    属性：用户列表（存储所有开卡人的信息的）
    行为：开户、查询、存款、取款、转账、改密、锁定、解锁、销户、
'''
import random
from card import Card
from user import User

class ATM:

    def __init__(self):
        self.user_dic={}

    def printOptionUI(self):
        print("************************************")
        print("*      开户(1)     查询(2)           *")
        print("*      取款(3)     存款(4)           *")
        print("*      转账(5)     改密(6)           *")
        print("*      锁定(7)     解锁(8)           *")
        print("*      销户(9)     退出(t)           *")
        print("************************************")

    def createUser(self):
        '''
        1.提示输入姓名、身份证号、手机号、2次密码、存款金额
        2.判断2次密码是否一致，不一致：开户失败，回到主界面
        :return:
        '''
        name=input("请输入姓名：")
        id=input("请输入身份证号：")
        phone=input("请输入手机号：")
        passwd1=input("请输入密码：")
        passwd2=input("请再次输入密码：")
        if passwd1!=passwd2:
            print("2次密码不一致，开户失败。。。")
            return False
        money=int(input("请输入存款金额，不得低于10："))
        if money<10:
            print("钱太少了，开户失败。。。。")
            return False
        #证明前面输入的信息都没有问题，可以开户
        #随机一个卡号(6)
        cardNum=""
        for i in range(6):
            a = random.randint(0, 10)
            cardNum+=str(a)
        #创建卡对象
        card=Card(cardNum,passwd1,money)
        #创建用户对象
        user=User(name,phone,id,card)
        self.user_dic[cardNum]=user
        print("开户成功！！！卡号是：%s"%cardNum)

    def serach(self):
        '''
        1.检测卡号有没有出现过
        2.检测密码
        3.打印对应的信息
        :return:
        '''

        cardNum=input("请输入要查询的卡号：")
        user = self.user_dic.get(cardNum)
        # for i in self.user_dic.keys():
        #     if cardNum!=i:
        #         print("卡号不存在，查询失败。。。")
        #         return False

        if user==None:
            print("卡号不存在，查询失败。。。")
            return False
        #检测卡有没有被锁定
        if user.card.isLock==True:
            print("您的卡已被锁定，查询失败。。。请解锁")
            return False
        for i in range(3):
            passwd = input("请输入密码：")
            if passwd != user.card.passwd:
                print("密码错误，查询失败。。。")
                print("剩余%d次机会："%(2-i))
            else:
                break
        else:
            #处理锁卡的逻辑
            print("3次机会用尽，卡已被锁定。。。")
            user.card.isLock=True
            return False

        print("账户余额为：%.2f" % user.card.yu)

    def saveMoney(self):
        '''
        1.检测卡号
        2.检测卡是否锁定
        2.输入密码3次机会
        3.输入存款金额
        4.将输入的金额加入到余额中，显示
        {卡号(cardNum):用户(user)}
        :return:
        '''
        cardNum=input("请输入要存款的卡号：")
        #根据键去查值（根据卡号去找用户）
        user=self.user_dic[cardNum]
        if user==None:
            print("没有这个卡号，存款失败。。。")
            return False
        if user.card.isLock==True:
            print("卡已被锁定，请解锁。。。存款失败")
            return False
        for i in range(3):
            passwd = input("请输入密码：")
            if passwd != user.card.passwd:
                print("密码不正确，存款失败")
            else:
                break
        else:
            print("3次机会用完，卡已被锁定。。。")
            user.card.isLock=True
            return False
        #如果能走到这步，证明前面都没问题
        money=int(input("请输入存款金额："))
        user.card.yu+=money
        print("存款成功，余额为：%.2f"%user.card.yu)

    def zhuan(self):
        '''
        1.输入自己的卡号，检测卡号是否存在
        2.检测卡是否锁定
        3.输入3次密码
        :return:
        '''
        cardNum=input("请输入您的卡号：")
        user=self.user_dic.get(cardNum)
        if user!=None:
            if user.card.isLock!=True:

                for i in range(3):
                    passwd=input("请输入密码：")
                    if passwd==user.card.passwd:
                        cardNum2=input("请输入要转账的卡号：")
                        user2 = self.user_dic.get(cardNum2)
                        if user2!=None:
                            money=int(input("请输入转账金额："))
                            if money>user.card.yu:
                                print("转账失败，余额不足，您的余额为：%.2f"%user.card.yu)
                                return False
                            else:
                                user.card.yu-=money
                                print("转账成功，余额为：%.2f"%user.card.yu)
                                user2.card.yu+=money
                        break
                    else:
                        print("密码错误，剩余次数%d"%(2-i))
                else:
                    print("3次机会用完，卡已锁定")
                    user.card.isLock=True


