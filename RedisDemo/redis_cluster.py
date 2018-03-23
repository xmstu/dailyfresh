from rediscluster.client import StrictRedisCluster

if __name__ == '__main__':

    nodes = [
        {'host':'192.168.210.174', 'port': 7001},
        {'host':'192.168.210.174', 'port': 7002},
        {'host':'192.168.210.173', 'port': 7004},
    ]

    # 创建连接到集群的对象
    strict_redis_cluster = StrictRedisCluster(
        startup_nodes=nodes, decode_responses=True)
    # 通过strict_redis_cluster对象实现对Redis数据的操作

    strict_redis_cluster.set('username', 'redis')

    username = strict_redis_cluster.get('username')
    print(username)



