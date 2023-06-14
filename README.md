# basic-api

## 简介
> 本项目为后端接口程序，开箱即用。采用框架为FastApi，ORM框架为SQLAlchemy，数据库为Mysql和Redis
## 目录结构说说明
> * app -- 业务逻辑
>   * api -- 接口
>   * dependencies -- 依赖
>   * router.py -- 路由文件
> * cache -- 缓存文件目录
> * common -- 通用方法
>   * db -- 数据库方法封装
>   * log_helper.py -- 日志帮助类
>   * response.py -- 相应方法封装
>   * settings.py -- 配置信息获取方法
>   * utils.py -- 通用工具方法
> * conf -- 配置文件目录
>   * *.env -- 不同环境
>   * logging.conf -- 日志配置文件
> * logs -- 日志目录
> * models -- 数据库实体模型类
> * schemas -- 请求参数表单
> * script -- 常用脚本
> * test -- 单元测试
> * server.py -- 程序运行主文件
## 环境配置
### 有数据库环境
> 修改***conf***目录下的***dev.env***文件，配置***mysql***和***redis***
### 无数据库环境
* #### 安装Mysql
1. 指定目录创建如下三个文件夹  
> docker/mysql/log  
> docker/mysql/data  
> docker/mysql/conf  
2. 在***conf***目录下创建***my.cnf***的文件为mysql配置文件，填入如下内容  
> [client]  
> default_character_set=utf8  
> [mysqld]  
> collation_server=utf8_general_ci  
> character_set_server=utf8
3. 拉取mysql镜像  
```
docker pull mysql:latest
```  
4. 运行如下命令
```
//windows的续行符为^，若是linux环境则将^替换为/
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
```
5. 启动后进入连接mysql，添加远程用户 
> 进入容器  
> ```docker exec -it mysql bash```  
> 登录mysql  
> ```mysql -u root -p```  
> 修改本地用户密码  
> ```ALTER USER 'root'@'localhost' IDENTIFIED BY 'Lzslov123!';```  
> 添加远程登录用户  
> ```CREATE USER 'test'@'%' IDENTIFIED WITH mysql_native_password BY '123456!';```  
> ```GRANT ALL PRIVILEGES ON *.* TO 'test'@'%';```

* #### 安装Redis
1. 创建如下目录  
> dokcer/redis/data
2. 在***docker/redis***目录下创建配置文件***redis.conf***，填入如下内容  
> redis.conf  
> bind 127.0.0.1  
> port 6379  
> protected-mode no  
> daemonize no  
> databases 16  
> dir  ./  
> appendonly yes  
> appendfilename appendonly.aof  
> requirepass xxx  
3. 运行如下命令
```
//windows的续行符为^，若是linux环境则将^替换为/
docker run ^
--restart=always ^
--log-opt max-size=100m ^
--log-opt max-file=2 ^
-p 6379:6379 ^
--name redis ^
-v E:/software/docker/redis/redis.conf:/etc/redis/redis.conf ^
-v E:/software/docker/redis/data:/data ^
-d ^
redis redis-server /etc/redis/redis.conf ^
--appendonly yes ^
--requirepass 123456
```
### 运行环境
> 本项目基于***python3.10***开发，运行***requirements.txt***安装依赖库  
> ``` pip install -r requirements.txt ```
## 启动
> ``` nohup python3 server.py & ```
## TodoList
1. 注册校验功能
2. 数据库操作方法扩展
## Q&A
1. 数据库安装后连接报错，Public Key Retrieval is not allowed？
> MySQL在版本8.0之后默认的认证方式都更改为了caching_sha2_password，而我们服务并没有配置sha2相关的插件，所以服务启动时报错  
> use mysql;  
> select host, user, plugin from user;  
> 可以看到root的plugin是caching_sha2_password，我们希望改成mysql_native_password  
> 本地：ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY '123456';  
> 远程：ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '123456';  
