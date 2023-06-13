# window 续行符为 ^
docker run ^
-d ^
-p 3306:3306 ^
--privileged=true ^
-v E:/software/docker/mysql/log:/var/log/mysql ^
-v E:/software/docker/mysql/data:/var/lib/mysql ^
-v E:/software/docker/mysql/conf:/etc/mysql/conf.d ^
-e MYSQL_ROOT_PASSWORD=123456 ^
--name mysql ^
mysql

#my.cnf
#[client]
#default_character_set=utf8
#[mysqld]
#collation_server=utf8_general_ci
#character_set_server=utf8

#docker exec -it mysql bash
#登录mysql
#mysql -u root -p
#本地用户
#ALTER USER 'root'@'localhost' IDENTIFIED BY 'Lzslov123!';

#添加远程登录用户
#CREATE USER 'dd'@'%' IDENTIFIED WITH mysql_native_password BY '123456!';
#GRANT ALL PRIVILEGES ON *.* TO 'dd'@'%';

#Q&A
#Public Key Retrieval is not allowed
#MySQL在版本8.0之后默认的认证方式都更改为了caching_sha2_password，而我们服务并没有配置sha2相关的插件，所以服务启动时报错
#use mysql
#select host, user, plugin from user;
#可以看到root的plugin是caching_sha2_password，我们希望改成mysql_native_password
#本地：ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY '123456';
#远程：ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';