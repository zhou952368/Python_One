"""
1.验证用户输入的 IP 地址是否正确
ip的格式0.0.0.0 总共四位  每一位上的取值范围是0-255
2.验证用户输入的密码是否符合要求【用户输入的字符串长度为6-16位 不得包含%@#&等特殊符号】
"""
import re


def IP(ip):
    p = re.compile(r"(^((25[0-5]|2[0-4]\d|[0-1]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[0-1]?\d\d?$))")
    i = re.match(p, ip)
    if i is not None:
        return True
    return False


def Password(password):
    p = re.compile("(^\w{6,16}$)")
    a = re.match(p, password)
    if a is not None:
        return True
    return False


if __name__ == '__main__':
    print(IP("254.252.50.44"))
    print(Password("zjafmr周9523_1234"))
