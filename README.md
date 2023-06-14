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
> docker安装数据库见
### 运行环境
> 本项目基于***python3.10***开发  
> 运行***requirements.txt***安装依赖库  
> ``` pip install -r requirements.txt ```
> 
## 启动
> nohup python3 server.py &

## TodoList
1.注册验证码
2
