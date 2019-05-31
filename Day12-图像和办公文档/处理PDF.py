import time
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
'''
解析并读取PDF文件内容的方法，主要是学习pdfminer这个库
PDFminer是一个从PDF文档中提取信息的工具，与其他pdf相关的
工具不同，它完全专注于获取和分析文本数据。PDFminer允许获取
页面z中文本的确切位置，以及其他信息，比如字体或行。它包括一个
PDF转换器，可以将PDF文件转换成其他文本格式(如txt,HTML)，它有
一个可扩展的PDF解析器，可以用于其他目的而不是文本分析
'''
'''
这个有点难！多看看！内容也比较多
'''
text_path = r'words_words.pdf'

def parse():
    '''解析PDF文本， 并保存到TXT文件中'''
    fp = open(text_path, 'rb')
    # 用文件对象作为参数创建一个PDF文档分析器
    # 用于解析PDF文件，从文件中获取数据
    parser = PDFParser(fp)
    # 创建一个pdf文档对象
    doc = PDFDocument()
    # 连接分析器与文档对象
    # 建立连接之后呢，我们就可以通过分析器来访问原先的pdf了
    # 而新建的pdf doc我的理解是相当于原先的pdf的镜像
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF资源管理器来共享资源
        rm = PDFResourceManager()
        # 创建PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rm, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rm, device)

        # 循环遍历列表，每次处理一个page内容
        # doc.get_pages()获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里的layout是一个LTPage对象，里面存放着这个page解析出的各种对象
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'new.txt', 'a') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results)

if __name__ == '__main__':
    parse()
    time2 = time.time()
    print("总共消耗时间为:", time2 - time1)





































