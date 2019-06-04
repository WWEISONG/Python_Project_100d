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



