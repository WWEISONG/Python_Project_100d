'''
贪婪算法：在对问题求解时，总是做出在当前看来最好的选择，不追求最优解
快速找到满意解。即每一步都选择当前看来最好的
'''

# 一个背包 最多能装20公斤
# 物品 电脑200元 20kg
# 收音机 20元 4kg
# 钟表 175元 10kg
# 花瓶 50元  2kg
# 书 10元  1kg
# 油画 90元 9kg

class Thing(object):
    """物品"""
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    # 方法属性化
    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight

def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def greedy():
    """贪婪算法思想求解"""
    # map(func, iterable....) 跟filter有些类似(只不过filter是过滤作用)
    # map函数其功能是根据提供的函数对指定序列做映射，返回函数作用之后的结果
    # 比如代码中的那个int()作用于输入的每一个元素，然后以本来的格式返回
    # 举个例子：map(square, [1, 2, 3, 4]) 返回：[1, 4, 9, 16] 迭代器
    # 但是你可以把它转成其他类型比如：list(map(square, [1, 2, 3, 4])) ---返回列表了
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    # 贪婪思想：把每个物品的价格重量比排个序，每次都选价格重量比最大的
    # 这样 在当前看来 每次都是最好的选择 但是整体而言不一定是最优解
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'装入{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值：{total_price}')

if __name__ == '__main__':
    main()























