"""
类与类之间的关系有：
is-a 关系：继承
has-a 关系：关联/聚合/合成
use-a 关系：依赖
"""
'''
经验：符号常量总是优于字面常量 枚举类型是定义符号常量的最佳选择
'''

from enum import Enum, unique
import random

@unique
class Suite(Enum):
    """花色"""
    # 定义符号常量作为枚举的值, 根据源码介绍，一般把要枚举的值
    # 定义在类开头
    SPADE, HEART, CULB, DIAMOND = range(4)

    # Python魔术方法  定义 < 的行为
    def __It__(self, other):
        # 返回布尔值
        # self.value就是定义的枚举值
        return self.value < other.value

class Card():
    """牌"""
    # 对于一张牌呢 其有suite有face两个属性(抽象化实物)
    def __init__(self, suite, face):
        """初始化方法"""
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠', '❤', '♣', '◇']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'
# '''
# 插个空说一下__str__()魔术方法和__repr__()方法这两个的区别，总的来说当我们调用print()
# 函数时，__str__()返回人类可读的内容，__repr__()返回机器可读的内容，当然说这些你是不明白的
#
# 具体来说：repr, str其都需要调用return，都返回字符串。但是repr相当于是str的备胎。有str的
# 时候执行str,没有str的时候执行repr'''
    def __str__(self):
        return self.show()

    # 备胎
    def __repr__(self):
        return self.show()

class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        # 生成所有的cards---组合
        self.cards = [
            Card(suite, face) for suite in Suite for face in range(1, 14)
        ]

    def shuffle(self):
        """洗牌(随机乱序)"""

        # 调用random.shuffle()方法 把一个列表对象乱序化
        random.shuffle(self.cards)
        # 一旦重新洗牌 那么index也要归零(即一张牌都没法的状态)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)

# 定义玩家
class Player():
    """玩家"""

    # 作为玩家 他有名字 手上有他自己的牌
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort_card(self, comp=lambda card: (card.suite.value, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)

def main():
    """主函数"""
    poker = Poker()
    poker.shuffle()
    all_players = [Player('曹操'), Player('刘备'), Player('秦始皇'), Player('李世民')]
    while poker.has_more:
        # 每人每次获取一张牌
        for player in all_players:
            player.get_one(poker.deal())

    for player in all_players:
        player.sort_card()
        print(player.name, player.cards)

if __name__ == '__main__':
    main()



































