from shopping import ShoppingCar


class User:
    def __init__(self, username):
        self.__username = username
        self.__password = None
        self.__user_id = None

    def get_username(self):
        return self.__username

    # 用户注册
    def go_market_register(self, market):
        market.register(self)

    # 用户登录
    def logon_user(self, market):
        market.logon(self)

    # 用户退出
    def exit_user(self, market):
        market.quit(self)

    # 用户添加购物车
    def Add_shoppingCar(self, shoppingcar):
        shoppingcar.istert_shopping(self)

    # 用户查询购物车清单
    def inquire_cart(self, shoppingcart):
        shoppingcart.inquire_shopping(self)



