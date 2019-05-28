from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法"""
        self.x = x
        self.y = y

    def MoveTo(self, x, y):
        """移动到指定位置"""
        self.x = x
        self.y = y

    def MoveBy(self, dx, dy):
        """移动指定的增量"""
        self.x += dx
        self.y += dy

    def DistanceTo(self, other):
        """计算与另外一个点的距离"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)
def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.MoveBy(-1, 2)
    print(p2)
    print(p1.DistanceTo(p2))

if __name__ == '__main__':
    main()











































