from Market_user import User
from Supermarket import Market
from shopping import ShoppingCar


def main():
    while True:
        print("*"*60)
        print("                     欢迎来到超级商城                              \n"
              "                          1.注册                              \n"
              "                          2.登录                              \n"
              "                          3.添加购物车                              \n"
              "                          4.查看购物车信息                              \n"
              "                           退出                              \n")
        print("*"*60)
        instruct = input("请输入您要进行的操作：")
        if instruct == "1":
            username = input("请输入您的姓名：")
            user = User(username)
            market = Market()
            user.go_market_register(market)
        elif instruct == "2":
            user = User()
            user.logon_user(market)


if __name__ == '__main__':
    # user = User("zhou")
    # market = Market()
    # user.go_market_register(market)
    # user.logon_user(market)
    # shoppingcar = ShoppingCar()
    # user.Add_shoppingCar(shoppingcar)
    # user.inquire_cart(shoppingcar)
    main()

