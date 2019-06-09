### mysql的核心知识之服务管理
1. 查看mysql服务进程：ps -ef | grep mysql
2. service服务管理：cp -a mysql.server /etc/rc.d/init.d/mysql
3. 启动命令：service mysql start  
  关闭命令：service mysql stop  
  重新启动命令：service mysql restart  
  查看状态命令：service mysql status
4. 登录管理： ln -s /usr/local/mysql/bin/*  /bin  
  登录命令：mysql -uroot -p
5. 默认端口号：3306  
  配置文件：/etc/my.cnf
6. 命令行模式：  
  	登录命令：mysql -u用户 -p密码  
   	退出命令：exit;	quit;

### MySQL操作语句分为四类
1. DDL 数据定义语言 (Data Definition Language)  例如：建库，建表
2. DML 数据操纵语言(Data Manipulation Language) 例如：对表中的数据进行增删改操作
3. DQL 数据查询语言(Data Query Language)	例如：对数据进行查询
4. DCL 数据控制语言(Data Control Language)	例如：对用户的权限进行设置

### MySQL语句
1. create database db1; 
2. select database();/show database;
3. use database;
4. create database if not exists db2; 
5. create database db3 default character set gbk;    
6. show create database XD; # 查看某个库字符集类型
7. show variables like 'character%'; # 查看当前MySQL使用的字符集

### 常用数据类型
	<1>整数型
		类型      大小      范围（有符号）               范围（无符号unsigned）    用途
		TINYINT   1 字节    (-128，127)                (0，255)                 小整数值
		SMALLINT  2 字节    (-32768，32767)            (0，65535)               大整数值
		MEDIUMINT 3 字节    (-8388608，8388607)        (0，16777215)            大整数值
		INT       4 字节    (-2147483648，2147483647)  (0，4294967295)          大整数值
		BIGINT    8 字节     （）            		     (0，2的64次方减1)        极大整数值
   
   <2>浮点型
	FLOAT(m,d）  4 字节    单精度浮点型  备注：m代表总个数，d代表小数位个数
	DOUBLE(m,d） 8 字节    双精度浮点型  备注：m代表总个数，d代表小数位个数
	
	<3>定点型
	DECIMAL(m,d）    依赖于M和D的值    备注：m代表总个数，d代表小数位个数
	
	<4>字符串类型 
	类型          大小              用途
	CHAR          0-255字节         定长字符串
	VARCHAR       0-65535字节       变长字符串
	TINYTEXT      0-255字节         短文本字符串
	TEXT          0-65535字节       长文本数据
	MEDIUMTEXT    0-16777215字节    中等长度文本数据
	LONGTEXT      0-4294967295字节  极大文本数据
	
	char的优缺点：存取速度比varchar更快，但是比varchar更占用空间
	varchar的优缺点：比char省空间。但是存取速度没有char快
	
	<5>时间型
	数据类型    字节数            格式                    备注
	date        3                yyyy-MM-dd              存储日期值
	time        3                HH:mm:ss                存储时分秒
	year        1                yyyy                    存储年
	datetime    8                yyyy-MM-dd HH:mm:ss     存储日期+时间
	timestamp   4                yyyy-MM-dd HH:mm:ss     存储日期+时间，可作时间戳

### 创建表
```mysql
  CREATE TABLE 表名 (
                    字段名1 字段类型1 约束条件1 说明1,
                    字段名2 字段类型2 约束条件2 说明2,
                    字段名3 字段类型3 约束条件3 说明3
                    );
```
```mysql
create table 新表名 as select * from 旧表名 where 1=2;
#(注意：建议这种创建表的方式用于日常测试，因为可能索引什么的会复制不过来)
```
```mysql
create table 新表名 like 旧表名;
```
1. 约束条件
```
comment         ----说明解释
not null        ----不为空
default         ----默认值
unsigned        ----无符号（即正数）
auto_increment  ----自增
zerofill        ----自动填充
unique key      ----唯一值
```
2. 创建示范
```
CREATE TABLE student (
	id tinyint(5) zerofill auto_increment  not null comment '学生学号',
	name varchar(20) default null comment '学生姓名',
	age  tinyint  default null comment '学生年龄',
	class varchar(20) default null comment '学生班级',
	sex char(5) not null comment '学生性别',
	unique key (id)
	)engine=innodb charset=utf8;;
```

### 查看表
1. show tables;
2. desc 表名;
3. 查看创建表的sql语句：show create table 表名;
4. \G :有结束sql语句的作用，还有把显示的数据纵向旋转90度
5. \g :有结束sql语句的作用

### 表结构维护与删除
1. 修改表名：rename table 旧表名 to 新表名;
2. 给表添加一列：alter table 表名 add 列名 类型 (first(第一列)/after 字段名(某一列后面));
3. 修改列类型：alter table 表名 modify 列名 新类型;
4. 修改列名：alter table 表名 change 旧列名 新列名 类型;
5. 删除列：alter table 表名 drop 列名;
6. 修改字符集：alter table 表名 character set 字符集;
7. 删除表：drop table 表名；
8. 看表是否存在，若存在则删除表：drop table if exists 表名;

### DML数据操纵语言
1. 插入表数据：insert into 表名（字段名） values（字段对应值）; # 字段名与字段值一一对应
2. 蠕虫复制（将一张表的数据复制到另一张表中）：
	```
	insert into 表名1 select * from 表名2;

	insert into 表名1（字段名1，字段名2） select 字段名1，字段名2 from 表名2;

	insert into emp (empno,ename) select empno,ename from employee;
	```
3. 建表复制
	```
	create table 表名1 as select 字段名1，字段名2 from 表名2;

	create table emp as select empno ,ename from employee;
	```
4. 一次插入多个值
	```
	 insert into 表名  (字段名) values (对应值1),(对应值2),(对应值3);   
	```

### 表数据的修改与删除
1. 修改：
	```
	update 表名 set 字段名1=值1 where 字段名=值;

	update 表名 set 字段名1=值1,字段名2=值2 where 字段名=值;
	```
2. 删除：
	```
	delete from 表名 where 字段名=值;

	truncate table 表名;
	delete from 表名;
	drop table 表名;
	```
	- 面试题：删除表之前应该怎么做？  
	对数据进行备份操作，以防万一，可以进行数据回退
	- 面试题：delete与truncate与drop 这三种删除数据的共同点都是删除数据，他们的不同点是什么?   
		- delele 会把删除的操作记录给记录起来，以便数据回退，不会释放空间，而且不会删除定义。
		- truncate不会记录删除操作，会把表占用的空间恢复到最初，不会删除定义
		- drop会删除整张表，释放表占用的空间。
		- 删除速度：drop > truncate > delete

### MySQL中文乱码问题
```
mysql> show variables like 'character%';
+--------------------------+----------------------------------+
| Variable_name            | Value                            |
+--------------------------+----------------------------------+
| character_set_client     | utf8                             |
| character_set_connection | utf8                             |
| character_set_database   | utf8                             |
| character_set_filesystem | binary                           |
| character_set_results    | utf8                             |
| character_set_server     | utf8                             |
| character_set_system     | utf8                             |
| character_sets_dir       | /usr/local/mysql/share/charsets/ |
+--------------------------+----------------------------------+
```

- character_set_client：客户端请求数据的字符集
- character_set_connection：客户端与服务器连接的字符集
- character_set_database：数据库服务器中某个库使用的字符集设定，如果建库时没有指明，将默认使用配置上的字符集
- character_set_results：返回给客户端的字符集(从数据库读取到的数据是什么编码的)
- character_set_server：为服务器安装时指定的默认字符集设定。
- character_set_system：系统字符集(修改不了的，就是utf8)
- character_sets_dir：mysql字符集文件的保存路径

- 临时：set names gbk;


- 永久：修改配置文件my.cnf里边的

  ```
  [client]
  default-character-set=gbk
  作用于外部的显示
  
  [mysqld]
  character_set_server=gbk
  作用于内部，会作用于创建库表时默认字符集
  ```

- 修改库的字符集编码

  ```
  alter database xiaoxiao default character set gbk;
  ```

- 修改表的字符集编码

  ```
  alter table employee default character set utf8;
  ```

### DQL数据查询语言
1. 简单查询：
	```
	select * from employee;
	select empno,ename,job as ename_job from employee;
	```
2. 精确条件查询：(= > < != <>)
	```
	select * from employee where ename='后裔';
	select * from employee where sal != 50000;
	select * from employee where sal <> 50000; # 同上
	select * from employee where sal > 10000;
	```
3. 模糊条件查询：(% _)
	```
	show variables like '%aracter%'; 
	select * from employee  where ename like '林_';
	```
4. 范围查询：(between and)
	```
	select * from employee where sal between 10000 and 30000;
	select * from employee where hiredate between '2011-01-01' and '2017-12-1';
	```
5. 离散查询：
	```
	select * from employee where ename in ('猴子','林俊杰','小红','小胡');  
	```
6. 清除重复值：
	```
	select distinct(job) from employee;
	```
7. 统计查询（聚合查询）：
	```
	count(code)或者count(*)
	select count(*) from employee;
	select count(ename) from employee;

	sum()  计算总和 
	select sum(sal) from employee;

	max()	计算最大值
	select * from employee where sal= (select  max(sal) from employee);

	avg()   计算平均值
	select avg(sal) from employee;

	min()   计算最低值
	select * from employee where sal= (select  min(sal) from employee);

	concat函数： 起到连接作用
	select concat(ename,' 是 ',job) as aaaa from employee;
	```
8. 分组查询：group by
	- 作用：把行按字段分组
	- 语法：group by 列1，列2...列N
	- 适用场合：统计场合，一般和聚合函数连用
		```
		select deptnu,count(*) from employee group by deptnu;
		select deptnu,job,count(*) from employee group by deptnu,job;
		select job,count(*) from employee group by job;
		```
9. order by排序
	- 作用：对查询结果排序
	- 语法：order by 字段1，字段2...字段N
	- 适用场合：用于查询结果排序
	```
	select * from employee order by sal;
	select * from employee order by hiredate;
	select  deptnu,job,count(\*) as 总数 from employee group by deptnu,job having 总数>=2 
	order by deptnu desc;
	select  deptnu,job,count(\*) as 总数 from employee group by deptnu,job having 总数>=2 
	order by deptnu asc;
	select  deptnu,job,count(\*) as 总数 from employee group by deptnu,job having 总数>=2 
	order by deptnu;

	-- 顺序：where ---- group by ----- having ------ order by 
	```
10. limit限制查询
	- 作用：对查询结果条数限制
	- 语法：limit n, m   n代表起始值，默认0，m代表取出的条数
	- 适用场合：数量过多时限制数量，确定只有一条或几条时可以达到优化作用
		```
		select * from XD.employee limit 4,5;
		```
11. exists子查询（exists和not exists）
	```
	select * from 表名 a where exists (select 1 from 表名2 where 条件);

	-- eg:查询出公司有员工的部门的详细信息
	select * from dept a where exists (select 1 from employee b where a.deptnu=b.deptnu);
	select * from dept a where not exists (select 1 from employee b where a.deptnu=b.deptnu);
	```
12. 连接查询
	- 左连接关键字：left join 表名 on 条件 / left outer 表名 join on 条件
	- 右连接关键字：right join 表名 on 条件/ right outer 表名 join on 条件
	- 内连接：INNER JOIN 表名 ON 条件;
	- 联合查询：1.去除重复...union...      2.不去重复...union all...
		- union注意事项：
			```
			-- 两个select语句的查询结果的“字段数”必须一致；
			-- 通常，也应该让两个查询语句的字段类型具有一致性；
			-- 也可以联合更多的查询结果；
			-- 用到order by排序时，需要加上limit（加上最大条数就行），需要对子句用括号括起来
			
			-- 对销售员的工资从低到高排序，而文员的工资从高到低排序
			(select * from employee a where a.job = '销售员'  order by a.sal limit 999999 ) union  
			(select * from employee b where b.job = '文员' order by b.sal desc limit 999999);
			```

### DCL数据控制语言（GRANT、DENY、REVOKE）
1. 查看root用户可以在哪台机器登录
	```
	select user,host from mysql.user where user='root';
	```
2. 修改MySQL里的user表
	```
	 update mysql.user set host='localhost' where user='root';
	```
3. 修改密码
	```
	update mysql.user set authentication_string=password('密码') where user='用户' and host='ip';
	```
4. 忘记密码解决方案
	- 修改配置文件my.cnf (默认在/etc/my.cnf)，在[mysqld]下面加上 skip-grant-tables （跳过权限的意思）
	- 重启MySQL服务
	- mysql -uroot -p 无需密码登录进入
	- 修改密码
5. 创建新用户并限制ip网段登录
	```
	create user 'username'@'host' identified by 'password';
	# 示例
	-- 创建一个pig用户，并指定登录密码：123456，可以在任何一台远程主机都可以登录
	create user 'pig'@'%' identified by '123456';
	
​    -- 创建一个pig用户，并指定登录密码：为空，指定在120网段的机器登录
	create user 'pig'@'120.%.%.%' identified by '';
	```
6. 查看权限
	```
	select * from mysql.user where user='pig'\G
	mysql> show grants for 'pig'@'%';
	+---------------------------------+
	| Grants for pig@%                |
	+---------------------------------+
	| GRANT USAGE ON *.* TO 'pig'@'%' |
	+---------------------------------+
	USAGE：无权限的意思
	mysql> show grants for 'root'@'localhost';
	+---------------------------------------------------------------------+
	| Grants for root@localhost                                           |
	+---------------------------------------------------------------------+
	| GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
	+---------------------------------------------------------------------+
	WITH GRANT OPTION:表示这个用户拥有grant权限，即可以对其他用户授权
	```
7. 删除用户
	```
	drop user 'pig'@'%';
	delete from mysql.user where user='pig';
	```

### 数据库表权限的授权与收回（grant）
1. 授权语法：grant 权限1,权限2..... on 数据库对象 to '用户'
	- 权限：all privileges(所有权限) *.*(所有库所有表)
	```
	--对现有用户进行授权：对现有用户pig授予所有库所有表所有权限。
	grant all privileges on *.*  to 'pig';
	```
	
	```
	--对没有的用户进行授权：创建一个新用户dog授予XD库的所有权限，登录密码123456，任何一台主机登录
	grant all privileges on XD.* to 'dog'@'%' identified by '123456';
	```

	```
	--对没有的用户进行授权：创建一个新用户cat授予XD库的employee表 查与修改权限，登录密码123456，任何一台主机登录
	grant select,update on XD.employee to 'cat'@'%' identified by '123456'
	```

	```
	--对没有的用户进行授权：对用户cat授予XD库的employee表insert 权限，登录密码123456，任何一台主机登录
	grant insert on XD.employee to 'cat'@'%' identified by '123456';
	```
2. 回收语法：revoke 权限1,权限2...on 数据库对象 from '用户'@'host'
	```
	--回收pig用户的所有权限（注意：并没有回收它的登录权限）
	revoke all privileges on *.*  from 'pig' @ '%';
	flush privileges;
	```

	```
	--回收pig用户的所有权限（并回收它的登录权限）
	delete from mysql.user where user='pig';
	flush privileges;
	```

	```
	--回收cat用户对XD库的employee的查与修改权限
	revoke select,update on XD.employee from 'cat'@'%';
	flush privileges;
	```

### 事务
1. 定义：数据库事务通常指对数据库进行读或写的一个操作过程。有两个目的，第一个是为数据库操作提供了
一个从失败中恢复到正常状态的方法，同时提供了数据库即使在异常状态下仍能保持一致性的方法；
第二个是当多个应用程序在并发访问数据库时，可以在这些应用程序之间提供一个隔离方法，
以防止彼此的操作互相干扰。
2. 事务特性（ACID）：
	- 原子性(Atomicity)：事务必须是原子工作单元，一个事务中的所有语句，应该做到：要么全做，
	要么一个都不做；
	- 一致性(Consistency):让数据保持逻辑上的“合理性”，比如：小明给小红打10000块钱，既要让小明的账户
	减少10000，又要让小红的账户上增加10000块钱；
	- 隔离性(Isolation)：如果多个事务同时并发执行，但每个事务就像各自独立执行一样。
	- 持久性(Durability)：一个事务执行成功，则对数据来说应该是一个明确的硬盘数据更改
	（而不仅仅是内存中的变化）。
3. 事务的开启、提交、回滚（begin，start transaction，commit，rollback）
4. 开启autocommit（临时生效）：
	```
	OFF（0）：表示关闭
	ON （1）：表示开启

	mysql> set autocommit=0;
	Query OK, 0 rows affected (0.00 sec)

	mysql> show variables like 'autocommit';
	+---------------+-------+
	| Variable_name | Value |
	+---------------+-------+
	| autocommit    | OFF   |
	+---------------+-------+
	mysql> set autocommit=1;
	Query OK, 0 rows affected (0.00 sec)
	mysql> 
	mysql> show variables like 'autocommit';
	+---------------+-------+
	| Variable_name | Value |
	+---------------+-------+
	| autocommit    | ON    |
	```
5. 开启autocommit（永久生效）：修改配置文件：vi /etc/my.cnf,在[mysqld]下面加上：
autocommit=1,记得重启服务才会生效

### 视图
1. 定义：视图是一种虚拟存在的表，是一个逻辑表，它本身是不包含数据的。
作为一个select语句保存在数据字典中的。通过视图，可以展现基表（用来创建视图的表叫做
基表base table）的部分数据，说白了视图的数据就是来自于基表
2. 视图优点：
	- 简单：使用视图的用户完全不需要关心后面对应的表的结构、关联关系和筛选条件，对
	用户来说已经是过滤好的符合条件的结果集
	- 安全：使用视图的用户只能吐过他们被允许查询的结果集，对表的权限管理并不能限制到
	某个行某个列，但是通过视图就可以简单地实现
	- 数据独立：一旦视图的结构确定了，可以屏蔽表结构变化对用户的影响，源表增加列对
	视图没有影响；源表修改列名，则可以通过修改视图来解决，不会造成对访问者的影响
	- 不占用空间：视图是逻辑上的表，不占用内存空间
	- 总之，使用视图大部分情况是为了保障数据安全性，提高查询效率的
3. 缺点：
	- 性能差：sql server必须把视图查询转化成对基本表的查询，如果这个视图是由
	一个复杂的多表查询所定义，那么，即使是视图的一个简单查询，sql server也要
	把它变成一个复杂的结合体，需要花费一定的时间。
	- 修改限制：当用户试图修改试图的某些信息时，数据库必须把它转化为对基本表的
	某些信息的修改，对于简单的试图来说，这是很方便的，但是，对于比较复杂的试图，
	可能是不可修改的。
4. 创建、修改、删除
	```
	--创建的基本语法是：
		create view <视图名称> as select 语句;
		create view <视图名称> (字段) as select 语句;
		create or replace view <视图名称>;
	```

	```
	--修改的语法是：
	alter view <视图名称> as select 语句;
	```

	```
	--视图删除语法：
	drop view <视图名称> ;
	```
### 触发器
1. 定义：触发器就是监视某种情况，并触发某种操作
2. 创建、删除语法：
	```
	create trigger 触发器名称  after/before   
	insert/update/delete on 表名  
	for each row
	begin
		sql语句;
	end
	
	--after/before:可以设置为事件发生前或后
	--insert/update/delete:它们可以在执行insert、update或delete的过程中触发
	--for each row:每隔一行执行一次动作
	```
	
	```
	drop trigger 触发器名称;
	```
3. 演示
	```
	--创建一个员工迟到表：
	 create table work_time_delay(
		empno int not null comment '雇员编号',
		ename varchar(50) comment '雇员姓名',
		status int comment '状态'
		);
	```

	```
	delimiter // 自定义语句的结束符号

		mysql> delimiter //
		mysql> 
		mysql> create trigger trig_work after insert on work_time_delay
			-> for each row
			-> begin
			-> update employee set sal=sal-100 where empno=new.empno;
			-> end
			-> //
		Query OK, 0 rows affected (0.01 sec)

	new：指的是事件发生before或者after保存的新数据
	```

### 存储过程
1. 优缺点：
	- 复杂操作，调用简单
	- 速度快
	
	- 封装复杂
	- 没有灵活性
2. 创建语法：
	```
	/*参数：in|out|inout 参数名称 类型（长度）
        in：表示调用者向过程传入值（传入值可以是字面量或变量）
        out：表示过程向调用者传出值(可以返回多个值)（传出值只能是变量）
        inout：既表示调用者向过程传入值，又表示过程向调用者传出值（值只能是变量）*/
	/*声明变量：declare 变量名 类型(长度) default 默认值;
		给变量赋值：set @变量名=值;
		调用存储命令：call 名称(@变量名);
		删除存储过程命令：drop procedure 名称;
		查看创建的存储过程命令：show create procedure 名称\G;*/
	
	create procedure 名称 (参数....)
		begin
		 过程体;
		 过程体;
		end
	```
3. 示例
	```
	创建一个简单的存储过程：
		mysql> delimiter //
		mysql> create procedure  name(in n int)
			->             begin
			->             select * from employee limit n;
			->             end
			-> //
		Query OK, 0 rows affected (0.00 sec)

		mysql> set @n=5;
			-> //
		Query OK, 0 rows affected (0.00 sec)

		mysql> 
		mysql> call name(@n);
	```

	```
	  mysql>         create procedure  name()
			->             begin
			->             declare  n int default 6;
			->             select * from employee limit n;
			->             end
			-> //
		Query OK, 0 rows affected (0.00 sec)

		mysql> call name();


	```

### 数据库存储引擎
1. 定义：数据库引擎是数据库底层软件组件，不同的存储引擎提供不同的存储机制、
索引技巧、锁定水平等功能，使用不同的数据库引擎，可以获得特定的功能
2. 查看索引
	```
	-- 如何查看数据库支持的引擎
	show engines;

	-- 查看当前数据的引擎：
	show create table 表名\G

	-- 查看当前库所有表的引擎：
	show table status\G
	
	-- 建表时指定引擎
	create table yingqin (id int,name varchar(20)) engine='InnoDB';
	```
3. 修改表的引擎
	```
	alter table 表名 engine='MyiSAm';

	/*修改默认引擎
	​    vi /etc/my.cnf
	​    [mysqld]下面
	​    default-storage-engine=MyIsAM
	​    记得保存后重启服务*/
	```
4. MyISAM与InnoDB的区别
	- MyISAM：支持全文索引（full text）;不支持事务;表级锁;保存表的具体行数;
	奔溃恢复不好
	- Innodb：支持事务;以前的版本是不支持全文索引，但在5.6之后的版本就开始
	支持这个功能了;行级锁（并非绝对，当执行sql语句时不能确定范围时，也会进行
	锁全表例如： update table set id=3 where name like 'a%';）;不保存表的具体
	行数;奔溃恢复好

### 索引
1. 定义：索引是单独的、存储在磁盘上的数据库结构，它们包含着对数据表里的所有记录的
引用指针。使用索引可以快速地找出在某列或多列中有特定值的行。
2. 优缺点：
	- 通过创建唯一索引，来保证数据库表中的每一行数据的唯一性。
​	- 可以加快数据的检索速度。
​	- 可以保证表数据的完整性与准确性

	- 索引需要占用物理空间。
​	- 对表中的数据进行改动时，索引也需要跟着动态维护，降低了数据的维护速度。
3. 常见的索引类型
	- index：普通索引
	- unique：唯一索引
	- primary key：主键索引
	- foreign key：外键索引
	- fulltext: 全文索引
	- 组合索引
4. 索引创建示例：
	 ```
	create table test (
		id int(7) zerofill auto_increment not null,
		username varchar(20),
		servnumber varchar(30),
		password varchar(20),
		createtime datetime,
		unique (id) # 唯一索引
	  )DEFAULT CHARSET=utf8;
	  
	 alter table 表名 add index 索引名称 (字段名称);
	 
	 alter table test add unique unique_username (username);
	-- 注意：假如没有指定索引名称时，会以默认的字段名为索引名称
	
	create index 索引 on 表名 (字段名);
    create index index_createtime on test (createtime);
	
	drop index 索引名称 on 表名;
	drop index unique_username on test;

    alter table 表名 drop index 索引名;
    alter table test drop index createtime;
	```

### MySQL优化思路
1. 查看是否开启了慢查询日志
	```
	mysql> show variables like 'slow%';
	+---------------------+----------+
	| Variable_name       | Value    |
	+---------------------+----------+
	| slow_launch_time    | 2        |
	| slow_query_log      | OFF      |
	| slow_query_log_file | slow.log |
	+---------------------+----------+
	3 rows in set, 1 warning (0.00 sec)

	mysql> set global slow_query_log = on;
	Query OK, 0 rows affected (0.01 sec)

	mysql> show variables like 'slow%';
	+---------------------+----------+
	| Variable_name       | Value    |
	+---------------------+----------+
	| slow_launch_time    | 2        |
	| slow_query_log      | ON       |
	| slow_query_log_file | slow.log |
	+---------------------+----------+
	3 rows in set, 1 warning (0.00 sec)
	
	如果需要修改日志路径：set global slow_query_log_file = '路径';
	```
2. 查看慢查询的时间临界值
	```
	mysql> show variables like '%long%';
	+----------------------------------------------------------+-----------+
	| Variable_name                                            | Value     |
	+----------------------------------------------------------+-----------+
	| long_query_time                                          | 10.000000 |
	| performance_schema_events_stages_history_long_size       | 10000     |
	| performance_schema_events_statements_history_long_size   | 10000     |
	| performance_schema_events_transactions_history_long_size | 10000     |
	| performance_schema_events_waits_history_long_size        | 10000     |
	+----------------------------------------------------------+-----------+
	5 rows in set, 1 warning (0.00 sec)
	```
4. 设置慢查询时间标准
	```
	mysql> set long_query_time = 0.4;
	Query OK, 0 rows affected (0.00 sec)
	
	/*永久生效的设置方法：修改配置文件 vi /etc/my.cnf
	[mysqld]
	slow_query_log = 1
	long_query_time = 0.1
	slow_query_log_file =/usr/local/mysql/mysql_slow.log

	最后必须重启服务才能生效！*/
	```
5. MySQL的sql语句执行过程解析
	- 查看性能详情是否开启
		```
		mysql> show variables like '%profiling%';
		+------------------------+-------+
		| Variable_name          | Value |
		+------------------------+-------+
		| have_profiling         | YES   |
		| profiling              | OFF   |
		| profiling_history_size | 15    |
		+------------------------+-------+
		3 rows in set, 1 warning (0.00 sec)

		mysql> set profiling = on;
		Query OK, 0 rows affected, 1 warning (0.01 sec)
		```
	- 查看性能的记录
		```
		mysql> show profiles;
		+----------+------------+-----------------------------------+
		| Query_ID | Duration   | Query                             |
		+----------+------------+-----------------------------------+
		|        1 | 0.00240450 | show variables like '%profiling%' |
		+----------+------------+-----------------------------------+
		1 row in set, 1 warning (0.00 sec)
		```
	- 查看语句的执行性能详情
		```
		mysql> show profile for query 4;
		+----------------------+----------+
		| Status               | Duration |
		+----------------------+----------+
		| starting             | 0.000068 |
		| checking permissions | 0.000021 |
		| Opening tables       | 0.000025 |
		| init                 | 0.000057 |
		| System lock          | 0.000006 |
		| optimizing           | 0.000003 |
		| optimizing           | 0.000002 |
		| statistics           | 0.000010 |
		| preparing            | 0.000019 |
		| statistics           | 0.000009 |
		| preparing            | 0.000005 |
		| executing            | 0.000009 |
		| Sending data         | 0.000006 |
		| executing            | 0.000002 |
		| Sending data         | 0.002169 |
		| end                  | 0.000014 |
		| query end            | 0.000009 |
		| removing tmp table   | 0.000014 |
		| query end            | 0.000004 |
		| closing tables       | 0.000009 |
		| freeing items        | 0.000117 |
		| cleaning up          | 0.000024 |
		+----------------------+----------+
		22 rows in set, 1 warning (0.00 sec)
		```
	
### SQL语句优化建议
1. 尽量避免使用select *from ，尽量精确到想要的结果字段
2. 尽量避免条件使用or
3. 记得加上limit 限制行数，避免数据量过大消耗性能
4. 使用模糊查询时，%放在前面是会使索引失效
	```
	mysql> explain select * from book where title like '你%'\G;
	*************************** 1. row ***************************
			   id: 1
	  select_type: SIMPLE
			table: book
	   partitions: NULL
			 type: range
	possible_keys: index_title
			  key: index_title
		  key_len: 767
			  ref: NULL
			 rows: 1
		 filtered: 100.00
			Extra: Using index condition
	1 row in set, 1 warning (0.06 sec)

	ERROR:
	No query specified

	mysql> explain select * from book where title like '%你'\G;
	*************************** 1. row ***************************
			   id: 1
	  select_type: SIMPLE
			table: book
	   partitions: NULL
			 type: ALL
	possible_keys: NULL
			  key: NULL
		  key_len: NULL
			  ref: NULL
			 rows: 3
		 filtered: 33.33
			Extra: Using where
	1 row in set, 1 warning (0.00 sec)

	ERROR:
	No query specified/*不好意思,\G后面不能再加;号啦*/

	mysql> explain select * from book where title like '%你%'\G;
	*************************** 1. row ***************************
			   id: 1
	  select_type: SIMPLE
			table: book
	   partitions: NULL
			 type: ALL
	possible_keys: NULL
			  key: NULL
		  key_len: NULL
			  ref: NULL
			 rows: 3
		 filtered: 33.33
			Extra: Using where
	1 row in set, 1 warning (0.00 sec)
	```
5. 要小心条件字段类型的转换
	
### 备份
1. 意义
	- 保护数据的安全
	- 在出现意外的时候（硬盘的损坏，断电，黑客的攻击），以便数据的恢复
	- 导出生产的数据以便研发人员或者测试人员测试学习
	- 高权限的人员操作失误导致数据丢失，以便恢复
2. 备份类型
	- 完全备份：对整个数据库的数据进行备份
	- 部分备份：对部分数据进行备份（可以是一张表也可以是多张表）
	- 增量备份：是以上一次备份为基础来备份变更数据的，节约空间
	- 差异备份：是以第一次完全备份的基础来备份变更备份的，浪费空间
3. 数据库备份方式
	- 逻辑备份：直接生成sql语句保存起来，
	在恢复数据的时候执行备份的sql语句来实现数据的恢复
	- 物理备份：直接拷贝相关的物理数据
	- 区别：逻辑备份效率低，恢复数据效率低，但是逻辑备份节约空间；
	物理备份浪费空间，但是相对逻辑备份而言效率比较高
4. 数据库备份的场景
	- 热备份：备份时，数据库的读写操作不会受到影响
	- 温备份：备份时，数据库的读操作可以进行，但是写操作不能执行
	- 冷备份：备份时，不能进行任何操作
5. 备份语句（mysqldump）
	```
	mysqldump -u 用户 -h host -p 密码 dbname table > 路径
	
	/*远程备份单库*/
	mysqldump -uroot -proot -h120.25.93.69 zabbix | gzip  > 
	/mysql_data_back/zabbix_users.sql.gz
	
	/*远程备份单库并保留创建库语句*/
	mysqldump -uroot -proot -h120.25.93.69 --databases zabbix | gzip  > 
	/mysql_data_back/zabbix_bak.sql.gz
	
	/*远程备份单库单表*/
	mysqldump -uroot -pabc123456 -h120.25.93.69 zabbix  users | gzip  > 
	/mysql_data_back/zabbix_users.sql.gz
	
	/*远程备份多库*/
	mysqldump -uroot -pabc123456 -h120.25.93.69 --databases zabbix XD | gzip  > 
	/mysql_data_back/zabbix_XD.sql.gz
	
	/*远程备份全库*/
	mysqldump -uroot -pabc123456 -h120.25.93.69 --all-databases  | gzip  > 
	/mysql_data_back/all.sql.gz
	
	/*远程恢复数据（备份的数据文件里没有创建库的语句）*/
	mysql -uroot -pabc123456 -h120.25.93.69  zabbix < zabbix_bak.sql
	
	/*远程恢复数据（备份的数据文件里有创建库的语句）*/
	mysql -uroot -pabc123456 -h120.25.93.69  < zabbix_bak.sql
	```
6. 查看数据库源文件路径
	```
	mysql> show variables like 'datadir%';
	+---------------+----------------+
	| Variable_name | Value          |
	+---------------+----------------+
	| datadir       | E:\mysql\data\ |
	+---------------+----------------+
	1 row in set, 1 warning (0.00 sec)
	```

### 锁
1. 两种基本锁类型：排它锁（Exclusive Locks，即X锁）和共享锁（Share Locks，即S锁）
2. 冲突问题：
	- 脏读：某个事务读取的数据是另一个事务正在处理的数据。而另一个事务可能会回滚，造成第一个事务读取的数据是错误的。
	- 不可重复读：在一个事务里两次读入数据，但另一个事务已经更改了第一个事务涉及到的数据，造成第一个事务读入旧数据。
	- 幻读：指当事务不是独立执行时发生的一种现象。例如第一个事务对一个表中的数据进行了修改，这种修改涉及到表中的全部数据行。同时，第二个事务也修改这个表中的数据，这种修改是向表中插入一行新数据。那么，以后就会发生操作第一个事务的用户发现表中还有没有修改的数据行，就好象发生了幻觉一样。
	- 更新丢失：多个事务同时读取某一数据，一个事务成功处理好了数据，被另一个事务写回原值，造成第一个事务更新丢失。
	- SERIALIZABLE-序列化：可以防止除更新丢失外所有的一致性问题

### 事务隔离级别
1. READ UNCOMMITTED-读未提交(会产生脏读)
2. READ COMMITTED-读提交(只防止脏读，但可能造成不可重复读)
3. REPEATABLE READ-重复读(不会产生脏读，也避免了不可重复读，但可能出现幻读)

	
#### MySQL日志  
*	set global general_log='on'  
*	set global log_output='table'  
*	select * from mysql.general_log\G  
*	set global general_log='off'  
*	\W  
*	explain extended select * from t1,t2\G  
*	show warnings  

#### MySQL优化查询
*	select count(\*) from items where id in (select iid from items_links);--> select count(distinct items.id) from items join items_link on (items.id=items_links.iid)  
*	在与where、join和group by语句相关的列上添加索引可以加速查询，order by上添加也有效果，因为他将使服务器更高效的排序  
*	由于上面items中id字段和items_links的iid字段连接，因此应该在这两列上添加索引  
*	alter table items add index(id);

#### where字句
*	where A=:A
	and   B>:B
	and   C=:C
	>索引列A是等值谓语，很明显列A是匹配列，将被用于定义索引片  
	索引列B是一个范围，也将用于定义索引片  
	由于列B是一个范围谓词，所以剩下的列C将不能参与匹配过程——它不能定义索引片

#### 为什么要建索引
1. 通过创建唯一性索引，可以保证数据库表中每一行数据的唯一性。 
2. 可以大大加快 数据的检索速度，这也是创建索引的最主要的原因。 
3. 可以加速表和表之间的连接，特别是在实现数据的参考完整性方面特别有意义。 
4. 在使用分组和排序 子句进行数据检索时，同样可以显著减少查询中分组和排序的时间。 
5. 通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能。

#### 那些列创建索引
1. 对于那些在查询中很少使用或者参考的列不应该创建索引。这是因为，既然这些列很少使用到，因此有索引或者无索引，并不能提高查询速度。相反，由于增加了索引，反而降低了系统的维护速度和增大了空间需求。 
2. 对于那些只有很少数据值的列也不应该增加索引。这是因为，由于这些列的取值很少，例如人事表的性别列，在查询的结果中，结果集的数据行占了表中数据行的很大比 例，即需要在表中搜索的数据行的比例很大。增加索引，并不能明显加快检索速度。 
3. 对于那些定义为text, image和bit数据类型的列不应该增加索引。这是因为，这些列的数据量要么相当大，要么取值很少。 
4. 当修改性能远远大于检索性能时，不应该创建索 引。这是因为，修改性能和检索性能是互相矛盾的。当增加索引时，会提高检索性能，但是会降低修改性能。当减少索引时，会提高修改性能，降低检索性能。因 此，当修改性能远远大于检索性能时，不应该创建索引。

	1. 主键自动建立唯一索引；

	2. 频繁作为查询条件的字段应该创建索引；

	3. 查询中与其他表有关联的字段，例如外键关系；

	4. 频繁更新的字段不适合创建索引，因为每次更新不单单是更新记录，还会更新索引，保存索引文件

	5. where条件里用不到的字段，不创建索引；

	6. 高并发的情况下一般选择复合索引；

	7. 查询中排序的字段创建索引将大大提高排序的速度（索引就是排序加快速查找）；

	8. 查询中统计或者分组的字段；

	9. 表记录太少，不需要创建索引；

	10. 经常增删改的表；

	11. 数据重复且分布平均的字段，因此为经常查询的和经常排序的字段建立索引。注意某些数据包含大量重复数据，因此他建立索引就没有太大的效果，例如性别字段，只有男女，不适合建立索引。

#### 数据库建立索引常用的规则如下：

1. 表的主键、外键必须有索引
2. 数据量超过300的表应该有索引
3. 经常与其他表进行连接的表，在连接字段上应该建立索引
4. 经常出现在Where子句中的字段，特别是大表的字段，应该建立索引
5. 索引应该建在选择性高的字段上
6. 索引应该建在小字段上，对于大的文本字段甚至超长字段，不要建索引
7. 复合索引的建立需要进行仔细分析；尽量考虑用单字段索引代替

#### 数据库索引类型
1. **顺序文件上的索引：**针对按指定属性值升序或降序存储的关系，在该属性上建立一个顺序索引文件，索引文件有属性值和对应的元组指针组成
2. **B+树索引：**将索引属性组织成B+树形式，B+树的叶节点为属性值和对应的元组指针。B+树索引具有动态平衡的优点
3. **散列索引：**是建立若干个桶，将索引属性按照其散列函数值映射到对应的桶中，桶中存放索引属性值和相应的元组指针。散列索引具有查找速度快的特点
4. **位图索引：**用位向量记录索引属性中可能出现的值，每个位向量对应一个可能值

### 一条语句实现
SELECT sum(case when id < 10 then 1 else 0 end),
	sum(case when id > 10 then 1 else 0 end)
FROM `t_comment`

SELECT *
FROM `t_comment` where id > 10 
union
SELECT *
FROM `t_comment` where id < 10 

### utf8和utf8mb4区别
1. mb4就是most bytes 4的意思，专门用来兼容四字节的unicode。好在utf8mb4是utf8的超集，除了将编码改为utf8mb4外不需要做其他转换。当然，为了节省空间，一般情况下使用utf8也就够了。
2. 原来mysql支持的 utf8 编码最大字符长度为 3 字节，如果遇到 4 字节的宽字符就会插入异常了。三个字节的 UTF-8 最大能编码的 Unicode 字符是 0xffff，也就是 Unicode 中的基本多文种平面(BMP)。也就是说，任何不在基本多文本平面的 Unicode字符，都无法使用 Mysql 的 utf8 字符集存储。包括 Emoji 表情(Emoji 是一种特殊的 Unicode 编码，常见于 ios 和 android 手机上)，和很多不常用的汉字，以及任何新增的 Unicode 字符等等。
3.  对于 CHAR 类型数据，utf8mb4 会多消耗一些空间，根据 Mysql 官方建议，使用 VARCHAR  替代 CHAR。

### 时间
1. date(年-月-日) 
create table test(hiredate date);
2. datetime（日期时间类型） 
create table test(hiredate datetime)
3. timestamp（邮戳类型，保存年-月-日 时-分-秒）
create table test(hiredate timestamp)
	
	
	
	
	
	
	




