## SQLITE3使用说明
#### shell下运行sqlite3 xxx.db进入xxx数据库
### .table查看数据库中的所有表
### .schema table_name查看表table_name的结构
### 创建表可以在sqlite3的命令行下直接运行sql语句，也可以用.read命令执行预先写好的sql脚本
## SQLITE3样列
#### create table names (id integer primary key, fname text, lname text);
#### 建表的时候前面是列名，后面是列的属性，比如类型，是否为主键和相关的一些约束
