from redis.client import StrictRedis

if __name__ == '__main__':
    strict_redis = StrictRedis(decode_responses=True)

    # 购买了id为1的商品2件
    strict_redis.hset('user_1', 1, 2)
    # 购买了id为2的商品3件
    strict_redis.hset('user_1', 2, 3)
    # strict_redis.hmset('user_1', {'1': '2', '2': '3'})

    # 查看hash所有的属性
    items = strict_redis.hgetall('user_1')
    print('所有的属性:  %s' % items)

    # 取出id为1的商品, 数量+1后再保存回去
    count = strict_redis.hget('user_1', 1)
    count = int(count)+1
    strict_redis.hset('user_1', 1, count)

    # 累加购买数量
    vals = strict_redis.hvals('user_1')
    print('所有的值: %s' % vals)
    count = 0
    for c in vals:
        count += int(c)
    print('购买商品的总数量: %s' % count)