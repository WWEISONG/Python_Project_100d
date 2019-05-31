'''
排序算法(选择、冒泡和归并)
'''

def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    # 复制原始列表
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        # 开始选择，每一轮都从后边选择一个最小的值
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        # 一轮选择之后，把得到的最小值放到前面i的位置
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """简单冒泡排序"""
    # 复制原始列表
    items = origin_items[:]
    # 要冒泡的趟数
    for p in range(len(items) - 1, 0, -1):
        swapped = False
        # 每一趟冒泡
        for i in range(0, p):
            if comp(items[i], items[i + 1]):
                temp = items[i + 1]
                items[i + 1], items[i] = items[i], temp
                flag = True
        # 如果发现某一趟并没有冒泡，那么证明已全部有序
        # 那就可以结束程序了！
        if not swapped:
            break
    return items

'''
高质量的冒泡: 对于一趟来说：去的时候冒泡走一遍，回来的时候冒泡再走一遍！
相比于简单冒泡来说，同一样多了一个回来冒泡的过程。效率就更高了。
'''
def better_bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量的冒泡排序(搅拌排序)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        # 去的时候冒泡
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # 如果去的时候冒泡了，那么回来的时候也冒泡一遍
        # 这样回去的时候也冒泡同时也保证了前面的成了最小的
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j -1] = items[j - 1], items[j]
                    swapped = True
        # 如果不发生冒泡了，那证明全部有序了，程序可以结束了。
        if not swapped:
            break
    return items

'''归并排序(分治法)'''
def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    # 一直递归的去拆分成其子问题
    # 拆分到只剩下一个元素，然后层层向上返回
    # 最终输出排好序的结果
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)

# 子问题的合并函数
def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

if __name__ == '__main__':
    select_sort([2, 4, 5, 3, 1], comp=lambda x, y: x < y)
    bubble_sort([2, 4, 5, 3, 1], comp=lambda x, y: x > y)







































