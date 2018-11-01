mov_list = [{"name": "大话西游", "type": "爱情", "time": "1995"},
            {"name": "复仇者联盟", "type": "科幻", "time": "2018"},
            {"name": "夏洛特烦恼", "type": "喜剧", "time": "2014"}]


def append():
    dict = {}
    movie_name = input("请输入电影的名字：")
    movie_type = input("请输入电影的类别：")
    movie_time = input("请输入电影发行的年代：")
    for movie in mov_list:
        if movie["name"] == movie_name:
            print("该电影已经存在，不用重复添加")
            break
    else:
        dict.update({"name": movie_name, "type": movie_type, "time": movie_time})
        print("电影添加成功！")
        mov_list.append(dict)


def chaxun_movie():
    name = input("请输入电影的名字：")
    for movie in mov_list:
        if movie["name"] == name:
            print("你要找的电影是 {0} ，属于 {1} 类型电影，上映于 {2} 年".format(movie["name"], movie["type"], movie["time"]))


def del_movie():
    list_movie()
    name = input("请输入要删除的电影名字：")
    for movie in mov_list:
        if movie["name"] == name:
            print("你要删除的电影是 {0} ，属于 {1} 类型电影，上映于 {2} 年".format(movie["name"], movie["type"], movie["time"]))
            print(mov_list.remove(movie))


def list_movie():
    print("编号\t\t电影名字\t\t\t类型\t\t\t上映时间")
    for i, movie in enumerate(mov_list):
        print("{0}\t\t\t{1}\t\t{2}\t\t\t{3}".format(i+1, movie["name"], movie["type"], movie["time"]))


def main():
    while True:
        print("*"*30)
        print("所有操作列表")
        print("查询单部电影，请按1  ")
        print("添加一部电影，请按2  ")
        print("删除一部电影，请按3  ")
        print("查询所有电影，请按4")
        print("退出操作请按其他键")
        print("*"*30)
        i = int(input("请输入您要进行的操作："))
        if i == 1:
            chaxun_movie()
        elif i == 2:
            append()
        elif i == 3:
            del_movie()
        elif i==4:
            list_movie()
        else:
            break

main()
