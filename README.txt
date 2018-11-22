md5.py

    输入：字典文件./dict/*
    输出：将计算出的MD5值写入到md5.db中（sqlite数据库）

md5.php:

    一个简单的PHP查询页面，根据输入的MD5查找md5.db其原始内容
    http://172.16.81.144:8080/md5/md5.php
	
crack.py

    输入：
        user_info.txt：包含用户口令MD5值的数据记录
        dict: 密码字典文件
    输出：
        result.csv:csv格式的结果文件，包含破解的用户原始口令（或NULL）
        result.txt:txt格式的结果文件，包含破解的用户原始口令（或NULL）

md5.db:
    sqlite3 md5.db

    CREATE TABLE MD5(
       ID INT PRIMARY KEY     NOT NULL,
       PASSWD           TEXT    NOT NULL,
       PASSWD_MD5        CHAR(32)  NOT NULL
    );
