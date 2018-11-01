import re


# number = "166156767476151684abciacaicbaic"
# # 匹配数字
# p = re.compile("(\d+)")
# a = re.match(p,number)
# print(a.groups())


def is_phone(phone):
    """
    电话号码必须是以数字组成   长度为十一位  以数字1开头
    :param phone:
    :return:
    """
    p = re.compile('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$')
    a = re.match(p, phone)
    if a is not None:
        return True
    return False


def get_count(html):
    p = re.compile('<textarea.*">(.*)</textarea>', flags=re.M)
    # findall() 返回值为一个list
    a = p.findall(html)
    for i in a:
        print(i)


if __name__ == '__main__':
    print(is_phone("15571383682"))
    print(is_phone("16571383682"))
    with open("古诗文大全_古诗文网.html", encoding="utf-8") as f:
        html = str(f.read())
        get_count(html)
