import socket
import time
def send(ip_first,port=2425):
    ip_list = [ip_first+str(i) for i in range(0,255)]
    for ip in ip_list:
        sender = socket.socket()
        try:
            sender.connect((ip, port))
            print("{ip}的端口{port}是开放的.........".format(ip=ip, port=port))
        except:
            print("{ip}的端口{port}没有开放".format(ip=ip, port=port))
        sender = socket.socket(type=socket.SOCK_DGRAM)
        count = '1:15:zhou:zhou:288:代码测试。。。。。'.encode('GBK')
        sender.sendto(count,(ip,port))
        # time.sleep(10)



if __name__ == '__main__':
    send("192.168.50.")










