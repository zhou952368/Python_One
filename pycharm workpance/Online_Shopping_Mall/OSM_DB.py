import sqlite3


class DB:
    def __init__(self):
        self.__conn = sqlite3.connect('Market.db')
        self.__cursor = self.__conn.cursor()

    # 用户注册
    def insert_user(self, user_id, username, password):
        sql = 'insert into OSM_user(user_id, username, password) values (?,?,?)'
        self.__cursor.execute(sql, (user_id, username, password))
        self.__conn.commit()

    # 用户登录，更新状态
    def update_logging_status(self, user_id, password, logging_status):
        sql = 'update OSM_user set logging_status = ? where user_id = ? and password = ? '
        self.__conn.execute(sql, (user_id, password, logging_status))
        self.__conn.commit()

    # 用户添加商品到购物车
    def insert_shopping_cart(self, username, trade_name, quantity, total_price, buying_time):
        sql = 'insert into shopping_cart(username,trade_name, quantity, total_price, Buying_Time) values(?,?,?,?,?)'
        self.__cursor.execute(sql, (username, trade_name, quantity, total_price, buying_time))
        self.__conn.commit()

    # 用户修改购物内的信息 （商品数量的增减）
    def update_shopping_quantity(self, username, trade_name):
        sql = 'select quantity from shopping_cart where username = ? and trade_name = ? '
        count = list(next(self.__cursor.execute(sql, (username, trade_name))))[0]
        print(count)

    # 用户查询购物车中的信息
    def inquire_shopping_cart(self, username):
        sql = 'select * from shopping_cart where username = ?'
        self.__cursor.execute(sql, (username,))
        data = self.__cursor.fetchall()
        print("用户名\t\t商品名\t\t\t商品数量\t\t\t商品总价\t\t添加购物车时间")
        for i in data:
            username = i[0]
            tarde_name = i[1]
            quantity = i[2]
            total_price = i[3]
            buying_time = i[4]
            print("{0}\t\t{1}\t\t\t{2}\t\t\t{3}\t\t{4}"
                  .format(username, tarde_name, quantity, total_price, buying_time))

    # 打印商城商品清单表
    def inquire(self):
        sql = 'select * from inventory'
        self.__cursor.execute(sql)
        results = self.__cursor.fetchall()
        print("商品名\t\t\t商品数量\t\t\t商品价格")
        for i in results:
            tarde_name = i[0]
            quantity = i[1]
            price = i[2]
            print("{0}\t\t\t{1}\t\t\t\t\t{2}".format(tarde_name, quantity, price))
