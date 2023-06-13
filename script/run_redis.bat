#windows
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

#redis.conf
#bind 127.0.0.1
#port 6379
#protected-mode no
#daemonize no
#
#databases 16
#dir  ./
#appendonly yes
#appendfilename appendonly.aof
#requirepass xxx