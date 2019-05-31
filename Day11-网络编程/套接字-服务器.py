from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

'''
套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程
在网络应用开发中被广泛使用。Python中也可以基于套接字来使用传输层提供的传输服务
并基于此开发自己的网络应用。实际开发中使用的套接字可以分为三类：流套接字(TCP
套接字)、数据报文套接字原始套接字

所谓TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口。在Python
中可以通过创建socket对象并指定type属性SOCK_STREAM来使用TCP套接字。
'''

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口(用以区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.1.2', 6789))
    # 3. 开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4. 通过循环接受客户端的连接并作出相应的处理(提供服务)
        # accept 方法是一个阻塞方法，如果没有客户端连接到服务器代码就不会往下执行
        # accept 方法返回一个元组，其中的第一个元素是客户端对象
        # 第二元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 5. 发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6. 断开连接
        client.close()

if __name__ == '__main__':
    main()

'''
需要注意的是，上面的服务器并没有使用多线程或者异步I/O的处理方式，这也意味着当
服务器与一个客户端处于通信状态时，其他的客户端只能排队等待。

下面通过设计一个线程类，来使用多线程技术处理多个用户请求的服务器，该服务器会向
连接到服务器的客户端发送一张图片。
'''

from socket import SOCKET, SOCK_STREAM, AF_INIT
from base64 import b64encode
from json import dumps
from threading import Thread

# 自定义线程类
class FileTransferHandler(Thread):

    def __init__(self, cclient, data):
        super().__init__()
        self.cclient = cclient
        self.data = data

    def run(self):
        my_dict = {}
        my_dict['filename'] = 'img.jpg'
        # JSON是纯文本不能携带二进制数据
        # 所以图片的二进制数据要处理成base64编码
        my_dict['filedata'] = self.data
        # 通过dumps函数将字典处理成JSON字符串
        json_str = dumps(my_dict)
        # 将生成的json_str字符串编码--二进制--
        self.cclient.send(json_str.encode('utf-8'))
        self.cclient.close()
def main():
    # 1. 创建套接字对象并指定使用哪种传输服务
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP地址和端口
    server.bind(('192.168.1.2', 5566))
    # 3. 开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器正在监听...')
    with open('img.jpg', 'rb') as f:
        # 将二进制文件处理成base64编码再解码成unicode编码的字符串
        # 因为python内部对字符串的处理是unicode编码
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client, data).start()

if __name__ == '__main__':
    main()




























