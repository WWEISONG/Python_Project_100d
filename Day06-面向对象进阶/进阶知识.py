# @property装饰器
import time
"""
为了能将属性设置为私有，并且能检查赋给属性的值是否有效
引入@property装饰器，当我们调用@property装饰器的时候
同时生成了@attr.setter装饰器，来给属性重新赋指，是会对
赋的值是否有效进行检查
"""
# 示例代码
class Person(object):
    """初始化人的特征，名字和年龄"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 装饰器作为访问器-getter方法
    @property
    def name(self):
        return self._name

    # 装饰器作为访问器-getter方法
    @property
    def age(self):
        return self._age

    # 修改器-setter方法
    @age.setter
    def age(self, value):
        # 对新赋的值进行检查
        if isinstance(value, int) and  0 < value <= 100:
                self._age = value
        else:
            raise ValueError

def main():
    person = Person('SONGWEI', 18)
    print(person.age)
    person.age = 22
    print(person.age)

if __name__ == '__main__':
    main()

# __slots__魔法
'''
如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过__slot__变量
来进行限定，需要注意的是__slot__的限定只能对当前类的对象生效，对子类并不起
任何作用
'''
# 示例代码
class Person(object):
    """初始化人的特征，名字和年龄"""
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 装饰器作为访问器-getter方法
    @property
    def name(self):
        return self._name

    # 装饰器作为访问器-getter方法
    @property
    def age(self):
        return self._age

    # 修改器-setter方法
    @age.setter
    def age(self, value):
        # 对新赋的值进行检查
        if isinstance(value, int) and  0 < value <= 100:
                self._age = value
        else:
            raise ValueError

def main_1():
    person = Person('SONGWEI', 18)
    print(person.age)
    person.age = 22
    print(person.age)

# 静态方法
'''
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息
实际上，我们写在类中的方法并不是需要都是对象的，例如我们定义一个'三角形'类，
通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边未必能
构造除三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形
这个方法很显然就不是对象方法，因此在调用这个方法时三角形对象尚未创建出来，所以
这个方法是属于三角形类而并不是属于三角形对象的。我们可以用静态方法来解决这类问题。
'''

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a)) * \
               (half - self._b) * (half - self._c))

def main_2():
    a, b, c  = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

# 类方法
'''
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个
参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，
有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的
信息并且可以创建出类的对象，代码如下所示。
'''

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

def main_3():
    # 通过类方法创建对象并获取系统时间
    # 调用类方法，其返回值作为新建类对象的初始参数
    clock = Clock.now()
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()

# 类与类之间的关系
'''
简单的说，类与类之间的关系有三种：is-a, has-a和use-a关系
-- is-a 关系也叫继承或者泛化，比如学生和人的关系，手机和电子产品的关系都属于继承关系
-- has-a 关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系
    关联关系如果是整体和部分的关联，关联关系如果是整体和部分的关联，那么我们称之为
    聚合关系，如果整体进一步负责了部分的生命周期，整体和部分同时同在同时消亡
    那么这种就是最强的关联关系，我们称之为合成关系
-- use-a 关系通常称之为依赖，比如司机有一个驾驶的行为(方法)，其中(参数)使用到了汽车
    司机和汽车就是依赖关系
'''
















































































