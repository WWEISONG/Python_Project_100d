from random import randint
from time import time, sleep
'''
用来对比使用多进程的程序与不使用多进程的程序的区别

在强调一下进程的概念，虽然我现在还是不太懂...但是肯定会懂的！
进程就是操作系统中执行的一个程序，操作系统以进程为单位分配存储空间，每个进程都有
都有自己的地址空间、数据栈以及其他用于跟踪进程执行的辅助数据，操作系统管理所有进程
的执行，为他们合理的分配资源。进程可以通过fork或spawn的方式来创建新的进程来执行其
它的任务，不过新的进程也有自己独立的内存空间，因此必须通过进程间通信机制(IPC,
Inter Process Communication)来实现数据共享，具体的方式包括管道、信号、套接字
共享内存区等。
'''
不使用多进程的程序
def download_task(filename):
    print(f'开始下载{filename}')
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f'{filename}下载完成！耗费了{time_to_download}秒')

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Sydney Hot.avi')
    end = time()
    print(f'总共耗费了{end-start:.2f}秒')

if __name__ == '__main__':
    main()

'''
运行结果：

开始下载Python从入门到住院.pdf
Python从入门到住院.pdf下载完成！耗费了9秒
开始下载Sydney Hot.avi
Sydney Hot.avi下载完成！耗费了10秒
总共耗费了19.02秒
'''

# 使用多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print(f'启动下载进程，进程号[{getpid()}]')
    print(f'开始下载{filename}')
    time_to_download =randint(5, 10)
    sleep(time_to_download)
    print(f'{filename} 下载完成！耗时{time_to_download}秒')

def main():
    start = time()
    p1 = Process(target=download_task, args=('Pyhton从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Sydney Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'总耗时{end-start:.2f}秒')

if __name__ == '__main__':
    main()
'''
执行结果：

启动下载进程，进程号[4224]
开始下载Sydney Hot.avi
启动下载进程，进程号[12112]
开始下载Pyhton从入门到住院.pdf
Pyhton从入门到住院.pdf 下载完成！耗时9秒
Sydney Hot.avi 下载完成！耗时10秒
总耗时10.37秒

'''

'''
总结：
运行使用了多线程的代码，可以明显发现两个下载任务'同时'启动了，而且程序
的执行时间将大大缩短，不再是两个任务时间总和。

另外需要注意的是，当我们在程序中创建进程的时候，子进程复制了父进程以及
所有的数据结构，每个子进程有自己独立的内存空间。
'''















































