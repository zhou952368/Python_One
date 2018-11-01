import time
from OSM_DB import DB


class ShoppingCar:
    def __init__(self):
        self.__db = DB()
        self.__trade_name = None
        self.__quantity = None
        self.__price = None
        self.__buying_time = None

    def get_shopping(self):
        return self.__trade_name, self.__quantity, self.__price, self.__buying_time

    # 添加购物车
    def istert_shopping(self, user):
        usernamr = user.get_username()
        self.__db.inquire()
        self.__trade_name = input("请输入您要添加的商品名：")
        self.__quantity = input("请输入您要添加的商品数量：")
        self.__price = input("请输入您要添加的商品的价格：")
        self.__buying_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        total_price = eval(self.__quantity) * eval(self.__price)
        self.__db.insert_shopping_cart(usernamr, self.__trade_name, self.__quantity, total_price, self.__buying_time)
        print("商品添加成功您添加的商品是：{0}，数量为：{1}，单价为：{2}，总价为：{3}"
              .format(self.__trade_name, self.__quantity, self.__price, total_price))

    # 查询购物车内的信息
    def inquire_shopping(self, user):
        username = user.get_username()
        self.__db.inquire_shopping_cart(username)

    # 先查询当前用户的要修改的商品的数量  然后进行增加或者减少获得新的数量 进行更新操作
    def quantity_shopping(self):
        pass
