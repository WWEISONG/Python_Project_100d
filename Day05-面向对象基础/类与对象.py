"""
基本概念：
类：类就是拥有相同或者相似属性的一系列对象的集合
    像鸟类，所有的鸟都属于鸟类，他们有相似的特征
    比如说都有翅膀。
对象：对象就是类中的实例，比如说，某个麻雀。
继承：继承就是字面意思，就是子类继承父类的所有特征
    就像你继承你父亲的基因。。。
多态：子类也不用完全相同于其父类，也可以有不同的地方
    不同的子类可以自己定义属于自己的特殊的东西，这就是
    多态。
封装：封装就是隐藏一切可以隐藏的实现细节，只向外界暴露
    简单的编程接口。比如说在类定义的方法其实就是把数据
    和对数据的操作封装起来，在我们创建了对象之后，只需要
    给对象发送一个消息(调用方法)就可以执行方法中的代码，
    也就是说我们只需要知道方法的名字和传入的参数(方法的外部视图)
    而不需要知道方法内部的实现细节(方法的内部视图)
"""

# 定义类
class StudentBoy(object):
    """定义一个男学生类"""

    # __init__是一个特殊方法用于创建对象时进行初始化操作
    # 通过这个方法我们可以对学生绑定name和age属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 驼峰命名法
    def Study(self, course_name):
        print(f'{self.name} 正在学习{course_name}')

    def WatchVideo(self):
        if self.age < 18:
            print(f'{self.name} 只能观看熊出没。')
        else:
            print(f'{self.name} 可以看爱情故事片。')
# 创建对象
def main():
    # 创建学生对象并置顶姓名和年龄
    stu1 = Student('SONGWEI', 18)
    # 给对象study消息
    stu1.Study('Python 程序设计')
    # 给对象发WatchVideo消息
    stu1.WatchVideo()

# 访问可见性的问题
'''
在python中，属性和方法的访问权限只有两种，也就是公开的和私有的
如果希望属性是私有的，在给属性命名时，可以用两个下划线作为开头。
但是，Pyhton并没有从语法上严格保证私有属性或方法的私密性，它只是给
私有属性换了个名字来妨碍对其的访问，事实上你知道更换名字的规则仍然
可以访问到他们。在实际的开发中，只是用单下划线来标记属性是受保护的
单下划线开头的属性和方法外界依然可以访问到，所以更多时候其只是一种
标记或者隐喻。
'''
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main_text_1():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)

def main_test_2():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)
if __name__ == '__main__':
    main()
