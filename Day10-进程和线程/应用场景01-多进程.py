from time import time

'''
完成一个1-100000000求和的计算密集型任务
'''

# 先用普通循环来解决，即一个进程

def main():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print(f'总计算时间：{end - start:.2f}')

if __name__ == '__main__':
    main()
'''
运行结果为：
5000000050000000
总计算时间：13.20
'''

# 接下来我们再用多个进程去解决，即将大的任务分而治之！
from multiprocessing import Process, Queue
from time import time

def task_handler(cur_list, result_queue):
    total = 0
    for number in cur_list:
        total += number
    result_queue.put(total)

def main():
    # 定义一个列表容易来放置所有的进程任务
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动八个进程将数据切片后进行计算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index: index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完花费的时间
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print(f'总计算时间：{end - start:.2f}')

if __name__ == '__main__':
    main()









