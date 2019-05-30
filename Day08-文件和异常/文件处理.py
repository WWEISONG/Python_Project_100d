import requests
'''
python中的文件处理主要包括三种文件的处理：1. 文本文件 2. json文件 3. 二进制文件
在python中实现文件的读写操作其实非常简单，通过Python内置的open函数，我们可以指定
文件名、操作模式、编码信息等来获得操作文件的对象，接下来就可以对文件进行读写操作了。
这里所说的操作模式是指要打开什么样的文件(字符文件还是二进制文件)以及什么样的操作。

操作模式：
    'r' : 读取(默认)
    'w' : 写入(会先截断之前的内容)
    'x' : 写入，如果文件以及存在会产生异常
    'a' : 追加，将内容写入到已有文件的末尾
    'b' : 二进制模式
    't' : 文本模式(默认)
    '+' : 更新(既可以读又可以写)
'''

# 读取文本文件
'''
    1. read() 直接把文本内容全部读取出来
    2. readline() 逐行读取，调用一次返回一行
    3. readlines() 逐行读取，调用一次返回所有行，返回一个列表
'''
def main_txt():
    with open('test_1.txt', 'r', encoding='utf-8') as file:
        # 直接把文本内容全部读取出来
        file_content = file.read()
        print(file_content)
        # 逐行读取，调用一次返回一行
        line = file.readline()
        print(line)
        # 逐行读取，调用一次返回所有行(包含换行符)，返回一个列表
        all_lines = file.readlines()

def main_bit_file():
    # 读取二进制文件
    with open('bit_file.jpg', 'rb') as file:
        data = file.read()

'''
json是JavaScriptObjectNotation的缩写，它本来是JavaScript语言中创建对象
的一种字面量语法，现在已经被广泛的应用于跨平台跨语言的数据交换，原因很简单，
因为json也是纯文本，任何系统任何编程语言处理纯文本都是没有问题的。

json数据类型和python数据类型有如下对应关系：
    json               python
---------------------------------
    object             dict
    array              list/tuple
    string             str
    number             int/float
    true/false         True/False
    null               None

json模块主要有四个比较重要的函数：
    dump() 将Python对象按照json格式序列化到文件中
    dumps() 将python对象处理成json格式的字符串
    load() 将文件中的json数据反序列化成对象
    loads() 将字符串的内容反序列化成python对象
'''

if __name__ == '__main__':
    main_txt()
    main_bit_file()




























































