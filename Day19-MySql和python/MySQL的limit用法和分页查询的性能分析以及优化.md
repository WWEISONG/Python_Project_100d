##### MySQL的limit用法和分页查询的性能分析以及优化

limit用法：

在我们使用查询语句的时候，经常返回前几条或者中间某几行数据，这个时候怎么办呢？不用担心，mysql已经为我们提供了这样一个功能。

```mysql
SELECT * FROM tablename LIMIT [offset,] rows | rows OFFSET offset
```

说明：LIMIT字句可以被用于强制SELECT语句返回指定的记录数。LIMIT接受一个或两个参数。参数必须是一个整数常量。如果给定两个参数，第一个参数指定第一个返回记录行的偏移量，第二个参数指定返回记录行的最大数目。初始记录行的偏移量是0(而不是1)：

```mysql
SELECT * FROM tablename LIMIT 5, 10; // 检索记录行 6-15
SELECT * FROM tablename LIMIT 95, -1; // 检索记录行 96-last
# 如果只给定一个参数 它表示从第一行返回的最大记录行数--初始偏移量为0
SELECT * FROM tablename LIMIT 5; // 检索前5行
# 相当于是
SELECT * FROM tablename LIMIT 0, n;
```

分页查询语句的性能分析：

如果是中小数据量的应用场景，这样的分页查询方式是足够了的，唯一需要注意的问题确保使用了索引。但是越往后分页，LIMIT语句的偏移量就会越大，速度也会明显变慢。此时我们可以使用子查询的方式来提高分页效率：

```mysql
SELECT * FROM tablename WHERE id >=
(SELECT id FROM tablename WHERE another_id = 123 ORDER BY id LIMIT 10000, 1) LIMIT 10;
```

为什么通过子查询能提高查询效率呢？因为子查询是在索引上完成的(上边代码中的id)，而普通的查询是在数据文件上完成的，通常来说，索引文件要比数据文件小的多，所以操作起来也会更有效率。实际上可以利用类似策略模式的方式去处理分页，比如说如果是一百页以内，就是用最基本的分页方式，大于一百页，则使用子查询的分页方式。

```mysql
代码1：SELECT * FROM tablename ORDER BY id LIMIT 1000000, 30;
代码2：SELECT * FROM tablename WHERE id >=
(SELECT id FROM tablename ORDER BY id LIMIT 1000000, 1) LIMIT 30;
```

说明：因为要取出所有字段内容，第一种需要跨越大量数据块并取出，而第二种基本通过直接根据索引字段定位后，才取出相应的内容，效率自然很大提升。对limit优化，不是直接使用limit，而是先获取到offset的id,然后直接使用limit size 来获取数据。可以看出，越往后分页，那么limit语句的偏移量就越大，那么两者速度差距就越大。

优化思想就是：避免数据量大时扫描过多的记录。

![img](https://segmentfault.com/img/bVLlt0?w=671&h=118)

![img](https://segmentfault.com/img/bVLluR?w=881&h=307)

为了保证index索引列连续，可以为每个表加一个自增字段，并且加上索引。