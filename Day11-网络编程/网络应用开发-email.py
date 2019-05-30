from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

'''
就像我们可以用HTTP(超文本传输协议)来访问一个网站一样，发送邮件要使用SMTP
(简单邮件传输协议), SMTP也是一个建立在TCP(传输控制协议)提供的可靠数据传输
服务的基础上的应用级别协议，它规定了邮件的发送者如何跟发送邮件的服务器进行通信
的细节，而Python中的smtplib模块将这些操作简化成了几个简单的函数
'''

def main():
    sender = '2833061817@qq.com'
    receivers = ['1994425904@qq.com',]
    # 创建一个邮件消息对象
    message = MIMEMultipart()
    content = MIMEText('用Python发送邮件实例代码', 'plain', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(content)
    message['From'] = Header('SONGWEI', 'utf-8')
    message['To'] = Header('XIAOKEAI', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件..', 'utf-8')
    smtp_server = SMTP('smtp.qq.com')
    smtp_server.login(sender, 'fcvrcudyobjzdgfb')
    smtp_server.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

'''
如果需要发送带有附件的邮件，那么可以按照下面的方式进行操作
'''

def main_attac():
    # 创建一个带有附件的消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    # 将文本内容对象添加到邮件消息对象中
    message.attach(text_content)
    message['From'] = Header('SONGWEI', 'utf-8')
    message['To'] = Header('OTHERS', 'utf-8')
    message['Subject'] = Header('Test', 'utf-8')

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('test.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=test.txt'
        message.attach(txt)
    # 创建SMTP对象
    smtp_server = SMTP('smtp.qq.com')
    # 开启安全连接
    smtp_server.starttls()
    sender = '2833061817@qq.com'
    receivers = ['1994425904@qq.com', ]
    smtp_server.login(sender, 'fcvrcudyobjzdgfb')
    smtp_server.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtp_server.quit()
if __name__ == '__main__':
    main_attac()






































