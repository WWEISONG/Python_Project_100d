from socket import socket

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接服务器(需要指定IP地址和端口)
    client.connect(('192.168.1.2', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()

'''
多线程情况下的客户端
Base64是一种用64个字符表示所有二进制数据的编码方式，通过将二进制数据每
6为一组的方式重新组织，刚好可以使用0-9的数字，大小写字母以及'+'和'/'总共
64个字符表示000000到111111的64种状态。
'''

from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.1.2', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接受1024字节
    data = client.recv(1024)
    while data:
        # 将接收来的数据拼起来
        in_data += data
        data = client.recv(1024)
    # 将接收到的二进制数据解码成JSON字符串并转换成Python数据结构：字典
    # loads函数的作用就是将JSON的字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    # 现在的filedata是字符串，那么需要编码成其原有的编码格式
    filedata = my_dict['filedata'].encode('utf-8')
    with open('E:/img' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存...')

if __name__ == '__main__':
    main()
























