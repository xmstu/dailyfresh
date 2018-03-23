from redis import StrictRedis

if __name__ == '__main__':
    strict_redis = StrictRedis(decode_responses=True)

    # 1.id为1的用户添加了商品到购物车
    # strict_redis.hset('cart1', 'goods1', 2)
    # strict_redis.hset('cart1', 'goods2', 3)
    strict_redis.hmset('cart1', {'goods1':2, 'goods2':3})

    # 2.取出用户购买的id为1的商品的数量，商品购买数量加1后，再保存回去
    goods1 = strict_redis.hget('cart1', 'goods1')
    goods2 = strict_redis.hget('cart1', 'goods2')
    strict_redis.hset('cart1', 'goods1', int(goods1) + 1)
    # strict_redis.hset('cart1', 'goods2', int(goods2) + 1)

    goods1 = strict_redis.hget('cart1', 'goods1')
    goods2 = strict_redis.hget('cart1', 'goods2')

    # 3.统计用户添加添加到购物车商品的总数量(3+4=7件)
    print('goods1:%s个' % goods1)
    print('goods2:%s个' % goods2)

    vals = strict_redis.hvals('cart1')
    print(vals)
    ret = sum([int(val) for val in vals])
    # ret = int(goods1) + int(goods2)
    print('商品共计:%d个' % ret)

    # 4.用户从购物车中删除了id为1的商品
    strict_redis.hdel('cart1','goods1')
    print(strict_redis.hgetall('cart1'))