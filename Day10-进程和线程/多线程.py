from random import randint
from threading import Thread
from time import time, sleep
'''
线程和进程在代码实现上特别的想，从抽象理解上其都是任务
通过使用封装好的threading模块中的Thread类
'''
# def download(filename):
#     print(f'开始下载{filename}')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filename} 下载完成，耗费了{time_to_download}秒')
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Sydney Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print(f'总共耗时{end - start:.3f}')
#
# if __name__ == '__main__':
#     main()

'''
我们可以直接使用threading模块的Thread类来创建线程
'''
class DownloadTask(Thread):
    """下载线程类"""
    def __init__(self, filename):
        # 初始化其继承的父类
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'开始下载{self._filename}')
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print(f'{self._filename}下载完成！耗时{time_to_download}')

def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Sydney Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总耗时{end - start:.2f}')

if __name__ == '__main__':
    main()



































