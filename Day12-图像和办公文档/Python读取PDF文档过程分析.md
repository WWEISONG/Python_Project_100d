### Python读取PDF文档过程分析

PDF格式不是规范格式，尽管它被叫做PDF文档。PDF的表现更像一张图片，PDF更像是在一张纸的各个准确的位置上把内容都摆放出来。大部分情况下， 没有逻辑结构，比如句子或者段落，并且不能自适应页面大小的调整。PDFMiner尝试通过猜测他们的布局来重建他们的结构，但是不保证一定能工作。

下图显示了PDFMiner中各个类之间的关系：1. 首先呢我们通过PDF文件创建一个PDFParse解析器。相当于是用来'通信'的 2. 然后创建一个PDFDocument对象，也就是我们在程序中操作的对象，我的理解是它相当于是原PDF的一个影子。3. 我们需要创建一个PDFInterpreter解释器，用来解释page， 4. 我们需要有一个PDFDevice对象，用来产出我们需要的内容。5. PDFResourceManager就是连接解释器和设备对象的。解释器解释过之后就将内容放在资源对象中共享，这个时候我们可以通过设备对象直接获取。具体如下图：

![img](https://images2018.cnblogs.com/blog/1226410/201809/1226410-20180908194653103-1131895419.png)

由于PDF文件有如此大和复杂的结构，完整解析PDF文件很费时费力，大多数PDF工作中，很多模块是不需要加进来的，因此PDFMiner采用了一个惰性分析的策略。就是只分析所需要的部分。解析时候，至少需要两个核心类，PDFParser和PDFDocument。这两个配合其他模块来使用。

PDFParser     从文件中获取数据、DFDocument   存储文档数据结构到内存中、PDFPageInterpreter 解析page内容、PDFDevice    把解析到的内容转化为你需要的东西、PDFResourceManager存储共享资源，例如字体或图片

第一步：

![img](https://images2018.cnblogs.com/blog/1226410/201808/1226410-20180806154250549-1560801383.png)

第二步：

![img](https://images2018.cnblogs.com/blog/1226410/201808/1226410-20180806154852105-13055420.png)

第三步：

![img](https://images2018.cnblogs.com/blog/1226410/201808/1226410-20180806160352546-33401924.png)

最后对layout使用get_text()方法，获取每一页的text，需要注意的是在PDF文档中不只有text还可能有图片等等，为了确保不出错先判断对象是否具有get_text()方法

参考文章：[https://www.cnblogs.com/wj-1314/p/9429816.html]