import socket
receiver = socket.socket()
receiver.bind(('192.168.50.7',12345))
receiver.listen(10)
while True:
    req, address = receiver.accept()
    print(req.recv(1024).decode('utf-8'))
    r = input("请输入你要回复的内容：")
    req.send(r.encode('utf-8'))
