import re
'''
从一段文字中提取手机号，手机号可能位于文字的任何地方
也有可能有其他的数字存在。
'''

def main():
    # 创建正则表达式对象，使用前瞻和回顾来保证手机号前后不应该出现数字
    # (?<=exp) 表示匹配exp后边的位置！这里表示的是匹配非数字后边的内容
    # (?=exp) 表示匹配exp前面的位置,这里表示匹配非数字前面的内容
    pattern = re.compile(r'(?<=\D)1[345678]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('----------分割线-----------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    # 返回三个match对象，放在了迭代器中
    for temp in pattern.finditer(sentence):
        # 对match对象使用group()方法，返回match对象的字符串形式
        print(temp.group())
    print('---------分割线---------')
    # 通过search函数指定搜索位置找出所有匹配
    # search()是匹配到一个就会返回
    # 通过循环指定位置来匹配所有,而match对象的end()方法，就是返回
    # match对象的最后一个字符在原字符串的位置index
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())
if __name__ == '__main__':
    main()

























