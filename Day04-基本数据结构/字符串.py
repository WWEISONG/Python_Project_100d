"""
字符串作为一种数据结构
可以存储数字，字母，其他字符
其有很多有用的方法如下：

"""

def main():
    """展示字符串常用方法"""

    str1 = 'Hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize()) # Hello, world!
    # 将字符串所有内容改成大写
    print(str1.upper()) # HELLO, WORLD!
    # 从字符串中查找子串所在的位置
    print(str1.find('or')) # 8
    print(str1.find('shit')) # -1
    print(str1.rfind('or'))
    print(str1.lfind('shit'))
    # 与find类似但找不到子串时会引发一场
    # print(str1.index('or'))
    # print(str.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He')) # False
    print(str1.startswith('hel')) # True
    # 检查字符串以指定的字符串结尾
    print(str1.endswith('!')) # True
    # 将以字符串指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '$'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, '$'))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5]) # c12
    print(str2[2:]) # c123456
    print(str2[2::2]) # c246
    print(str2[::2]) # ac246
    print(str2[::-1]) # 654321cba
    print(str2[-3:-1]) # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())
    # 去除字符串左右两侧的空格
    print(str2.strip())

if __name__ == '__main__':
    main()