'''
在python3中 我们通常使用纯python的三方库pymysql来访问MySql数据库，它应该是目前最好
的选择 我们需要先安装pymysql模块
'''

import pymysql

# 添加一个部门
def main():
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地：')
    # 1. 创建数据库连接
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='ShermanLemon0301')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得结果，result返回的是影响的行数
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)' , (no, name, loc)
            )
        if result == 1:
            print('添加成功！')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()

# 删除一个部门
def delete_dept():
    no = int(input('编号：'))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='ShermanLemon0301',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            # result返回的是影响的行数
            result = cursor.execute(
                'delete from tb_dept where dno=%s', (no, )
            )
        if result == 1:
            print('删除成功！')
    finally:
        con.close()

# 更新一个部门
def update_dept():
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地：')
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='ShermanLemon0301',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            # result返回的是影响的行数
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
        if result == 1:
            print('更新成功')
    finally:
        con.close()

# 查询所有部门
from pymysql.cursors import DictCursor
def querry():
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='ShermanLemon0301',
                          )
    try:
        # 把cursor参数设置为DictCursor类，表中的每一行就以一个字典的形式返回，整个就是一个装满字典的列表
        # 每个字典(对应每一行)其键为属性名(列名) 值就是对应每一行的值
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()

# 分页查询 LIMIT
class Emp(object):

    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'

def querry_page():
    page = int(input('页码：'))
    size = int(input('大小：'))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='ShermanLemon0301')
    try:
        with con.cursor() as cursor:
            # limit--分页查询
            cursor.execute(
                'select eno as no, ename as name, job, sal from tb_emp limit %s, %s',
                ((page -1) * size, size)
            )
        results = cursor.fetchall()
        for emp_tuple in results:
            # 拿到的是元组，可以直接作为参数那创建对象！nice!
            emp = Emp(*emp_tuple)
            print(emp)
    finally:
        con.close()

if __name__ == '__main__':
    querry_page()




























