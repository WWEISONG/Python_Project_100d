===客户端python===

python中主要使用依赖库redis，实例代码如下：

```python
import redis
# 生成客户端连接
client = redis.StrictRedis(host='127.0.0.1', port=6379)
# 定义key
key = 'hello'
# 给key定义value，成功返回true
setResult = client.set(key, 'python-redis')
# 获取value
value = client.get(key)
```

python中对Redis的Pipeline功能的使用

```python
import redis
def mdel(keys):
    client = redis.StrictRedis(host='127.0.0.1', port=6379)
    pipeline = client.pipeline(transaction=False)
    for key in keys:
        pipeline.delete(key)
    # 执行pipeline
    return pipeline.execute();
```

===客户端管理===

Redis提供了客户端相关API对其状态进行监控和管理

```
1. client list
说明：client list命令能列出与Redis服务端相连的所有客户端连接信息。
其中有id,addr,fd,name

2. 输入缓冲区qbuf、qbuf-free
输入缓冲区过大主要是因为Redis的处理速度跟不上输入缓冲区的输入速度， 并且每次进入输入
缓冲区的命令包含了大量bigkey，从而造成输入缓冲区过大的情况。还有一种情况就是Redis发生
了阻塞，短期内不能处理命令，造成客户端输入的命令积压在了输入缓冲区，造成输入缓冲区过大

监控方法：
a. 通过定期执行client list命令，收集qbuf和qbuf-free找到异常的连接记录。
b. 通过info命令的info clients模块，找到最大的输入缓冲区。

3. 输出缓冲区： obl、oll、omem
Redis为每个客户端分配了输出缓冲区，它的作用是保存命令执行的结果返回给客户端，为
Redis和客户端交互返回结果提供缓冲。

与输入缓冲区不同的是，输出缓冲区的容量可以通过参数client-output-buffer-limit来进行
设置，并且输出缓冲区做的更加细致，按照客户端的不用分为三种：普通客户端，发布订阅客户
端、slave客户端。和输入缓冲区相同的是，输出缓冲区也不会受到maxmemory的限制，如果
使用不当同样会造成maxmemory用满产生的数据丢失、键值淘汰、OOM等情况。

实际上输出缓冲区由两部分组成：固定缓冲区（16KB）和动态缓冲区，其中固定缓冲区返回比较
小的执行结果，而动态缓冲区返回比较大的结果。固定缓冲区使用的字节数组，动态缓冲区使用的列表。obl代表固定缓冲区的长度，oll代表动态缓冲区列表的长度，omem代表使用的字节数。
```

