一、HTTP/0.9

HTTP是基于TCP/IP协议的应用层协议，它不涉及数据包(packet)传输，主要规定了客户端和服务器之间的通信格式，默认使用80端口。

最早版本是1991年发布的0.9版，该版本极其简单，只有一个命令GET

GET / index.html

上面的命令表示，TCP连接(connection)建立后，客户端向服务器请求(request)网页index.html

协议规定，服务器只能回应HTML格式的字符串，不能回应别的格式。

<html>

<body>Hello world</d>

</html>

多看几遍阮老师写的。

内容参考：[http://www.ruanyifeng.com/blog/2016/08/http.html]