##### UNIQUE 约束 和PRIMART KEY 约束

UNIQUE 和 PRIMARY KEY 约束均为列或列集合提供了唯一性的保证。PRIMARY KEY 约束拥有自动定义的UNIQUE约束。区别是，每个表可以有多个UNIQUE约束，但是每个表只能有一个PRIMARY KEY 约束。

##### 创建用户

命令：

CREATE USER 'username'@'host' IDENTIFIED BY 'password';

说明：username 是你将创建的用户名 host 指定该用户在哪个主机上可以登录 如果是本地用户可用localhost 如果想让该用户可以从任意远程主机登录 可以使用通配符 % password 该用户的登录密码 密码可以为空 如果为空则该用户可以不需要密码登录服务器:

```mysql
CREATE USER 'SONGWEI'@'localhost' IDENTIFIED BY '123456';
CREATE USER 'ZHONGHAO'@'%' IDENTIFIED BY '123456';
CREATE USER 'MARK'@'%' IDENTIFIED BY '123456';
```

授权：

```mysql
GRANT ALL PRIVILEGES ON databasename.tablename TO 'username'@'%';
```

说明：privileges 用户的操作权限 如SELECT, INSERT, UPDATE等，如果要授予所有的权限 则使用ALL, databasename 数据库名  tablename 表名 如果要授予该用户对所有数据库和表的相应操作权限则可用*表示：

```mysql
GRANT SELECT, INSERT ON databasename.tablename TO 'uername'@'%';
GRANT ALL ON databasename.* TO 'username'@'%';
GRANT ALL ON *.* TO 'username'@'%';
```

注意：用以上命令授权的用户不能给其他用户授权，如果想让该用户可以授权 用一下命令：

```mysql
GRANT privileges ON databasename.tablename TO 'username'@'%' WITH GRANT OPTIONS;
```

设置和更改用户密码：

```mysql
SET PASSWORD FOR 'username'@'%' = PASSWORD('newpassword');
-- 如果是当前登录用户用：
SET PASSWORD = PASSWORD('newpassword');
```

撤销用户权限：

```mysql
REVOKE ALL privileges ON databasename.tablename FROM 'username'@'%';
-- 注意 撤销是数据库和表部分应当和授权是保持一致
```

删除用户：

```mysql
DROP USER 'username'@'%';
```

##### 索引

使用索引可以快速访问数据库表中的特定信息。索引是对数据库表中一行或多列的值进行排序的一种结构。

##### 常用的几个命令

```mysql
# 选择要操作的Mysql数据库
USE databasename;
# 列出MySQL数据库管理系统的数据库列表
SHOW DATABASES;
# 显示指定数据库的所有表，使用前需要使用USE命令来选择数据库
USE databasename;
SHOW TABLES;
# 显示数据表的属性、属性类型、主键信息、是否为NULL、默认值等其他信息
SHOW COLUMNS FROM tablename;
DESCRIBE tablename;
# 显示数据表的详细索引信息，包括PRIMARY KEY（主键）
SHOW INDEX FROM tablename;
```

##### char 和 varchar

char(n) 若存入字符数小于n，则以空格补于其后，其查询之时再将空格去掉。所以char类型存储的字符串末尾不能有空格。否则数据将出错。

char(n)是固定长度，不管存入几个字符，都将占用4个字节，varchar是存入的实际字符数+1个字节数。但是char类型的字符串检索速度要比varchar类型要快。可以这么理解：char保存的相当于是定长记录，那么我只需要一个记录一个记录的去查询就行，而varchar是变长记录，我们不确定每个记录的长度，在查询的时候我们并不能确定一个记录后边是空值还是有要查询的内容，所以就会把整个查询内容从前往后过一遍。

##### ENUM 和 ENGINE参数

```mysql
CREATE TABLE tablename
(
    attr1    VARCHAR(20) NOT NULL,
    attr2    INT UNSIGNED NOT NULL,
    atrr3    ENUM('F', 'M'),
    PRIMARY KEY (attr1);
) ENGINE = InnoDB;
```

说明：ENUM表示的是枚举的类型。属性的值只能是枚举中的那些值。ENGINE参数表示的使用MYSQL的存储引擎，存储引擎有很多，各有各的特性，常用的有InnoDB, MYISAM等....

##### 载入数据的方法

```mysql
mysql> LOAD DATA LOCAL INFILE 'filename.txt' INTO TABLE tablename;
# 或使用客户端
mysqlimport --local databasename filename.txt；
```

##### NULL值的处理

在MySQL中处理NULL使用IS NULL 和 IS NOT NULL运算符。注意，NULL值与其他任何值的比较（即使是NULL）永远返回false。与NULL值的比较，不是=或者!=。

##### MySQL事务

MySQL事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，即需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等。这些数据库操作语句就构成一个事务。

在MySQL中只有使用了Innodb数据库引擎的数据库或表才支持事务。事务处理可以用来维护数据库的完整性，保证成批的SQL语句要么全部执行。要么全部不执行。事务用来管理insert,update,delete语句。

事务的ACID四个性质。

在MySQL命令行的默认设置下，事务都是自动提交的，即执行SQL语句后就会马上执行COMMIT操作。因此要显示的开启一个事务必须使用命令BEGIN或START TRANSACTION或者执行命令SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。

##### ALTER命令

```mysql
ALTER TABLE tablename DROP attr;
# 指定位置添加列属性
ALTER TABLE tablename ADD attr1 INT FIRST;
ALTER TABLE tablename ADD attr1 INT AFTER attr2;
# 修改字段类型以及名称
ALTER TABLE tablename MODIFY attr CHAR(10);
ALTER TABLE tablename CHANGE attr_old attr_new INT;
ALTER TABLE tablename MODIFY attr NOT NULL DEFAULT 100;
# 使用ALTER来修改字段的默认值
ALTER TABLE tablename ALTER attr SET DEFAULT 1000;
# 删除字段的默认值
ALTER TABLE tablename ALTER attr DROP DEFAULT;
# 修改表名
ALTER TABLE tablename_old RENAME TO tablename_new;
# 修改存储引擎：
ALTER TABLE tablename ENGINE=MYISAM;
# 删除外键约束：
ALTER TABLE tablename DROP FOREIGN KEY keyname;
# 修改字段相对位置
ALTER TABLE tablename MODIFY attr1 INT FIRST | AFTER attr2;
```

##### 临时表

MySQL临时表在我们需要保存一些临时数据时是非常有用的。临时表只在当前连接可见，当关闭连接时，MySQL会自动删除并释放所有空间。

```mysql
mysql> CREATE TEMPORARY TABLE SalesSummary (
    -> product_name VARCHAR(50) NOT NULL
    -> , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
    -> , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
    -> , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
);
```

说明：使用temporary关键字来创建临时表。当使用SHOW TABLES 命令时，不显示临时表。

##### 复制表

第一：用SHOW CREATE TABLENAME 命令将创建表的SQL语句调出来，

第二：把上边的SQL语句复制过来。。。换个名字创建新表(复制表)

第三：用INSERT INTO....SELECT语句将原表的数据导进来。

##### 位运算

位运算是在二进制数上进行计算的运算符。位运算首先会将操作数变成二进制数，进行位运算，然后再将计算结果从二进制变回十进制输出。