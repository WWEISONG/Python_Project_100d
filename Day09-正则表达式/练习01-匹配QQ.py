import re
'''
验证用户输入用户名和qq号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6-20个字符之间，qq号是
5-12位数字，且首位不能是0
'''

def main():
    username = input('请输入用户名：')
    qq = input('请输入qq号：')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    # 注意{}指定两个数字是不能加空格。
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效账号：')
    if m1 and m2:
        print('你输入的信息是有效的！')

if __name__ == '__main__':
    main()
'''
注意：上面书写正则表达式时使用了'原始字符串'的写法(在字符串前面加上了r)
所谓'原始字符串'就是字符串中的每个字符都是它原始的意义，说的更直接一点就是
字符串中没有所谓的转义字符。因为正则表达式中有很多元字符和需要转义的地方。
'''


































