from PIL import Image

'''
1.在计算集中，我们可以将红、绿、蓝三种色光以不同的比例叠加来组合成其他颜色
因此这三种颜色就是色光三原色，所以我们通常会将一个颜色表示为一个RGB值或RGBA
值(其中的A表示Alpha通道，它决定了透过这个图像的像素，也就是透明度)。

2.像素。对于一个由数字序列表示的图像来说，最小的单位就是图像上单一颜色的小方格
这些小方格都有一个明确的位置和被分配的色彩数值，而这些一方格的颜色和位置决定了该
图像最终呈现出来的样子，他们是不可分割的单位，我们通常称之为像素(pixel)。每一个图像
都包含了一定量的像素，这些像素决定图像在屏幕上所呈现的大小。

3.Pillow是由著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像
压缩和图像处理等各种操作，Pillow中最重要的是Image类，读取和处理图像都要通过这个类
完成
'''
'''剪裁图像'''
# crop(left, upper, right, lower)
# crop()就是对图像进行剪裁，接受一个四个参数的元组
# 分别表示左边边界，上边边界，右边边界，下边边界
img = Image.open('image.jpg')
rect = 80, 20, 310, 360
img.crop(rect).show()

'''生成缩略图'''
# thumbnail函数接受一个元组作为参数，分别对应着缩略图的宽高，在缩略时，
# 函数会保持图片的宽高比例。如果输入的参数宽高和原图像宽高比不同，则会
# 依据最小对应边进行原比例缩放。
img = Image.open('image.jpg')
size = 128, 128
img.thumbnail(size)
img.show()

'''缩放和粘贴'''
# 通过paste()方法粘贴到另一个图像上
# 参数为：被粘贴的图像，box变量(确定被粘贴图像的位置)，可以是定义了左上角的二元组，或者是定
# 义了左、上、右、下坐标的4元组或者为空(0, 0)
image1 = Image.open('imag_1.jpg')
image2 = Image.open('imag_2.jpg.jpg')
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

'''旋转和翻转'''
image = Image.open('imag_1.jpg')
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()




























