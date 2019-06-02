"""
ORM全称 Object Relational Mapping 即对象-关系映射，就是把关系数据库的一行
映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
"""

'''
编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架
想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码
'''
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=1234, name='SONGWEI', email='test@test.com', password='my-pas')
# 保存到数据库中
u.save()
'''
其中，父类Model和属性类型StringField, IntegerField是由ORM提供，剩下的魔术方法
比如save()全部由metaclass自动完成。虽然metaclass编写会比较复杂，但ORM的使用者用
起来却异常简单。
'''
class Field(object):
    """负责保存数据库表的字段名和字段类型"""

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'{self.__class__.__name__}:{self.name}'

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')

class ModelMetaclass(type):
    """自定义元类"""
    # 注意有一个点，attrs这个字典包括类的属性和方法
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)

        # 排除掉对Model类的修改
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 从类属性中删除该Field属性，否则，实例的属性会遮盖类的同名属性，运行错误
        for k in mappings.keys():
            attrs.pop(k)

        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        # 假设表名和列名一致
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    """只简单实现了INSERT功能"""

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))














































