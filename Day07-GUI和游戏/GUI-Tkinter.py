import tkinter
import tkinter.messagebox
"""
需要说明的是，GUI应用通常是时间驱动式的，之所以要进入主事件循环就是
要监听鼠标、键盘等各种事件的发生并执行对应代码对事件进行处理，因为事件
会持续的发生，所以需要这样的一个循环一直运行着等待下一个事件的发生，另一
方面，Tk为控件摆放提供了三种布局管理器，通过布局管理器可以对控件进行定位，
这三种管理器分别是：placer(开发者提供控件的大小和摆放位置)、packer(自动将
控件填充到合适的位置)和grid()基于网格坐标来摆放控件。
"""
def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal  flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗？'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('SONGWEI\'S GAME')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象，指定添加到哪个容器中，通过command参数绑定时间回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text, height=2, background='red',width=3)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()

























































