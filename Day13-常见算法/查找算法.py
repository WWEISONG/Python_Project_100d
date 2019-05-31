"""
查找算法(顺序查找、折半查找)
"""

'''顺序查找'''
def seq_search(items, key):
    """顺序查找"""
    # 这里enumerate()接受一个可迭代的对象作为参数，如列表、元组、字符串
    # 然后列出数据和下标(0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1 # 返回-1即没有找到

'''二分查找'''
def bin_search(items, key):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1 # 没有找到

'''
补充一个知识点：生成式语法
生成式可以用来生成列表、集合和字典   
'''

prices = {
    'AAPLE': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'LENOV': 100
}

# 用股票价格大于100的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}

































