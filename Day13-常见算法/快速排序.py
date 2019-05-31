"""
快速排序 选择枢轴对元素进行划分 左边都比枢轴小 右边都比枢轴大
"""

'''
快速排序的核心思想依然是分治思想

大佬们都说是分治思想，那么是怎么分治的呢？如果你要分治的话，是不是先要找一个标准？
用以分成不同的群体，这个标准的呢就是pivot主元。也就是列表中的一个数，那么怎么分呢？
分成比pivot大的元素集合和比pivot小的元素集合。

那么问题又来了，怎么分？具体过程如下：如果我们每次都选择列表的最后一个元素(假如说)
那么我们就遍历当前的列表拿着每个元素跟pivot比较，如果比pivot小，那么我们就将其放到列表
的前面，否则呢(也就是比pivot大)那么我们就不进行交换。

然后你可能又迷惑了，那pivot明明还在最后一个，怎么就说是小的在pivot左边，大的在pivot
的右边了？别急！等遍历完了当前列表所有的元素，出来以后就把pivot放在真正中间的位置！
而这个位置呢，也是pivot这个元素最终排完序之后应该待的位置！为什么呢？因为左边的都比它
小，右边的都比它大，那这个位置不就是它应该待的位置了吗？从这里也可以看出，我们在一轮
分治之后，解决了一个元素(pivot)的位置！那么我们有N个元素，所以正常情况下其时间复杂度
就是NlogN。--------不正常情况就是，元素一直等于pivot，这种情况下即使了换了位置，效果
还是跟原先的效果一样，也就起不到分治的作用！所以这种情况下就是N^2。
'''
def quick_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items

def _quick_sort(items, start, end, comp):
    if start < end:
        # 找到分治的点即找到pivot
        pos = _partition(items, start, end, comp)
        # 到这个时候就像我说的已经解决了当前pivot的真正位置
        # 所以我们去分开处理左边的 和 右边的
        # 递归调用 重新选出了新的pivot 解决....
        # 所以最终就是一个pivot一个pivot的层层递归解决了！
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)

def _partition(items, start, end, comp):
    # 选pivot
    # 有很多种选择方法 1. 选最后一个 2. 选中间的 3. 选第一个
    # 相对比较好的选择是 选三个的中位数 这样分治更均匀
    pivot = items[end]
    i = start - 1
    # 关于交换元素的这个操作 画个列表模拟一遍就明白了
    # 如果不发生交换 i 的位置就没有变 为什么？因为i相当于是要保证的都是比
    # pivot要小的元素！
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1






























