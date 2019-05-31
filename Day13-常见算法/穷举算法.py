'''
穷举法，又称暴力破解法，对所有的可能性进行验证，直到找到正确答案
'''
# 例子：百钱百鸡和五人分鱼
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
'''
如果全买公鸡的话 最多能买20只
如果全买母鸡的话 最多能买33只
如果全买小鸡的话 最多能买100只
'''
def find_chicken():
    for x in range(20):
        for y in range(33):
            z = 100 - (x + y)
            # 注意 买的小鸡的数量必须得是3的倍数
            if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                # 输出所有的结果
                print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
'''
使用枚举法：从总共1条鱼开始
根据这5个人的分鱼操作 我们能想到 每次分完之后鱼的数量减一就都是5的倍数
所以 从1条鱼开始枚举 直到分5次都还是5的倍数
'''
def fish():
    fish_num = 1
    while True:
        total = fish_num
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish_num)
            break
        fish_num += 1
    return fish_num

if __name__ == '__main__':
    fish()





























