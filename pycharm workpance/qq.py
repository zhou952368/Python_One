import win32gui
import win32con
import win32clipboard as w

def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

if __name__ == '__main__':
    # 测试
    # 这是发送10次的
    for i in range(10):
        to_who='python 1805 徐鑫'
        msg='测试消息，代码测试  不要理会'
        send_qq(to_who, msg)

    # 这是无限发送的
    # while True:
    #     to_who = '姜俊杰'
    #     msg = '测试消息，代码测试  不要理会'
    #     send_qq(to_who, msg)

