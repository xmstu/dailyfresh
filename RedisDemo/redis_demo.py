from redis.client import StrictRedis

if __name__ == '__main__':

    # 创建一个StrictRedis对象
    # strict_redis = StrictRedis(host='127.0.0.1', port=6379, db=0)
    # decode_responses: 转换成字符串输出
    strict_redis = StrictRedis(decode_responses=True)

    # 通过StrictRedis对象操作Redis
    # 增
    strict_redis.set('aa', '111')
    strict_redis.set('bb', '222')
    result = strict_redis.set('cc', '333')
    print(result)       # 保存成功返回True

    # 删
    # 改
    # 查
    aa = strict_redis.get('aa')
    bb = strict_redis.get('bb')
    cc = strict_redis.get('cc')
    print(aa, bb, cc)

    # 查看所有的键
    mykeys = strict_redis.keys()
    print(mykeys, type(mykeys))




