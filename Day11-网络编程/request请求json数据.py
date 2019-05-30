from time import time
from threading import Thread
import requests

'''
通过requests来实现一个访问网络数据接口并从中获取并从中获取美女图片下载链接
然后下载美女图片到本地的程序，程序中使用天行数据提供的API
响应的内容根据请求的url来决定
'''

# 继承Thread类创建自定义的线程类
class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[(self.url.rfind('/') + 1):]
        # 这里传入的是具体图片的url
        # 响应的内容就是一张图片
        resp = requests.get(self.url)
        with open('E:/img/' + filename, 'wb') as f:
            # resp.content就返回的内容
            f.write(resp.content)

def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的API
    resp = requests.get('http://api.tianapi.com/meinv/?\
        key=491b586b00237a92094ae592526ca53d&num=10')
    # resp就是一个请求的响应对象，其包含很多属性和方法
    # 调用JSON()方法就是将这个对象中的JSON数据解析出来
    # 将服务器返回的JSON格式的数据解析为字典
    # 此时resp就是JSON格式的数据
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()





























