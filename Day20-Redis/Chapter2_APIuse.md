第二章  API的理解和使用

=== 全局命令 ===

```
# 1. 查看所有的键
keys *
# 2. 键总数  // 直接获取Redis内置的键总数变量 时间O(1)
dbsize
# 3. 检查键是否存在  // 1 or 0
exists key
# 4. 删除键        // 1 or 0
del key [key ...]
# 5. 键过期  // Redis支持对键添加过期时间，当添加过期时间后，会自动删除键
expire key seconds
# 6. ttl 
大于等于0的整数：键剩余的过期时间
-1： 键没设置过期时间
-2： 键不存在
# 7. 键的数据结构类型
type key
如果是字符串则返回string 如果是list则返回list...否则，返回none
```

=== 五种数据结构 === 

key: 字符串 / 哈希 / 列表 / 集合 / 有序集合。我的理解是，每一个key都相当于是一个数据库，key对应着的值是数据结构的具体实现，并且redis对每一种数据结构都有至少两种实现方式，根据具体的场景选择使用合适的数据结构---内部编码。这样设计有两个好处：第一，可以改进内部编码，而对外的数据结构和命令没有影响，这样一旦开发出更优秀的内部编码，无需改动外部数据结构和命令。

1.字符串--命令部分

```
字符串类型的值实际可以是简单字符串、复杂字符串JSON/XML、数字、甚至二进制，但是值最大不能超过512MB

# 常用命令

1. 设置值
set key value [ex seconds] [px milliseconds] [nx | xx]
ex: 为键设置秒级过期时间
px: 为键设置毫秒级过期时间
nx: 键必须不存在，才能设置成功，用于添加
xx: 键必须存在，才能设置成功，用于更新
说明：setnx和setxx与上述是一样的，在实际的应用场景中，setnx的特性保证只有
一个客户端能设置成功，setnx可以作为分布式锁的一种实现方案。
2. 获取值
get key
3. 批量设置值
mset key value [key value ...]
4. 批量获取值
mget key [key ...]
5. 计数
incr key          // 值的自增操作
值不是整数，返回错误
值是整数，返回自增后的结果
键不存在，按照值为0自增，返回结果为1
decr key          // 值的自减
incrby key        // 自增指定数字
decrby key        // 自减指定数字
6. strlen
返回当前值的字符长度，注意每个中文字符是占用三个字节
7. 设置并返回原值
getset key newvalue
getset 和set一样会设置值，但是不同的是，它同时会返回键原来的值
8. 设置指定位置的字符
setrange key offeset value
9. 获取部分字符串
getrange key start end
说明：start和end分别是开始和结束的偏移量，偏移量从0开始计算。
```

1.字符串--内部编码

```
字符串类型的内部编码有3种：
int：8个字节的长整型
embstr: 小于等于39个字节的字符串
raw: 大于39个字节的字符串
```

2.哈希

哈希类型是指键值本身又是一个键值对结构，形如value={{field1, value1}, ...}

```
# 基础命令

1. 设置值
hset key field value
2. 获取值
hget key field value
3. 删除field
hdel key field [field...]
hdel 会删除一个或多个field, 返回结果为成功删除field的个数
4. 计算field个数
hlen key
5. 批量设置或获取field-value
hmget key field [field...]
hmset key field value [field value ...]
6. 判断field是否存在
hexists key field
7. 获取所有的field
hkeys key
8. 获取所有value
hvals key
9. 获取所有的field-value
hgetall key
10. hincrby hincrbyfloat
11. 计算value的字符串长度
hstrlen key field
```

2.哈希---内部编码

```
ziplist 压缩列表：当哈希类型元素个数小于hash-max-ziplist-entries配置，默认是512个、同时所有值都小于hash-max-ziplist-value配置，默认64字节。Redis会使用ziplist作为哈希的内部实现，ziplist使用更加紧凑的结构实现多个元素的连续存储，所以在节省内存方面比hashtable更加优秀。

hashtable 哈希表： 当哈希类型无法满足ziplist的条件时，Redis会使用hashtable作为哈希的内部实现，因为此时ziplist的读写效率会下降。而hashtable的读写时间复杂度O（1）
```

3.列表

列表类型用来存储多个有序的字符串， 列表中的每个字符串称为元素。可以对列表两端插入和弹出，还可以获取指定范围的元素列表、获取指定索引下标的元素等。

注意：列表类型有两个特点：第一、列表中的元素是有序的，这就意味着可以通过索引下标获取某个元素或者某个范围内的元素列表。第二、列表中的元素可以是重复的。

```
1. 从右边插入元素
rpush key value [value ...]
2. 从左向右获取列表的所有元素
lrange key 0 -1
3. 从左边插入元素
lpush key value [value]
4. 向某个元素前或者后插入元素
linsert key before | after pivot value
说明：linsert命令会从列表中找到等于pivot的元素，在其前before或者后after插入一个新的元素value。
5. 获取指定范围内的元素列表
lrange key start end
说明：索引下标从左向右分别是0到N-1，但是从右到左分别是-1到-N
注意：lrange中的end选项包含了自身。
6. 获取列表指定索引下标的元素
lindex key index
7. 获取列表长度
llen key
8. 从左边删除
lpop key
9. 从右边删除
rpop key
10. 删除指定元素
lrem key count value
说明：count > 0从左到右，删掉最多count个元素
count < 0从右到左，删掉最多count绝对值个元素
count = 0 删除所有
```

使用场景：

```
1.消息队列 lpush+brpop：生产者客户端使用lpush从列表左侧插入元素，多个消费者客户端使用brpop阻塞式的抢列表尾部的元素。多个客户端保证了消费的负载均衡和高可用性。

2.文章列表
```

4.集合

使用场景

```
集合类型比较典型的使用场景是标签tag。例如一个用户可能对娱乐、体育比较感兴趣，另一个用户可以对历史、新闻比较感兴趣，这些兴趣点就是标签。
```

集合类型也是用来保存多个的字符串元素，但和列表类型不一样的是，集合中不允许有重复的元素，并且集合中的元素是无序的，不能通过索引下标获取元素。

=== 单线程架构 ===

Redis客户端与服务端模型：

```
1. 客户端发送命令 
2. 服务端执行命令
3. 返回结果
```

因为Redis是单线程来处理命令的，所以一条命令从客户端达到服务端不会立刻被执行，所有命令都会进入一个队列中，然后逐个被执行。所以如果有3个客户端发送命令的话，那么实际上这3个客户端的命令执行顺序是不确定的。但是可以确定的是不会有两条命令被同时执行。

问题：为什么单线程还这么快？

第一，纯内存访问，Redis将所有数据放在内存中，内存的响应时长大约为100ns，这是Redis达到每秒万级别访问的重要基础

第二，非阻塞I/O，Redis使用epoll作为I/O多路复用技术的实现，再加上Redis自身的事件处理模型将epoll中的连接、读写、关闭都转换成事件，不在网络I/O上浪费过多时间。

第三，单线程避免了线程切换和竞态产生的消耗。