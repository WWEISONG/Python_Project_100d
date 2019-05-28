"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
# abc指的是抽象基类
# 主要定义了基本类和最基本的抽象方法，可以为子类定义共有的API，不需要具体实现
# 抽象基类可以不实现具体的方法(当然也可以实现，只不过子类如果想要调用抽象基类中定义的
# 方法需要使用super())，而是留给其子类来实现，比如下面代码中的get_salary。
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """初始化"""
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod # 为子类定义共有的API
    def get_salary(self):
        """获取月薪"""
        pass

class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class SalesMan(Employee):
    """销售员"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    # 创建三类对象实例，并将其放在列表中
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), SalesMan('荀彧'),
        SalesMan('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(f'请输入{emp.name}本月工作时间：'))
        elif isinstance(emp, SalesMan):
            emp.sales = float(input(f'请输入{emp.name}本月销售额：'))
        # 同样是接收get_salary这个消息，但是不同的员工表现出了不同的行为(多态)
        print(f'{emp.name} 本月工资为：{emp.get_salary()}')

if __name__ == '__main__':
    main()





















