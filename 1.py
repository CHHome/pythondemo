def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('消费产品 s%',n)
        r = '200 ok'


def product(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("生产产品 s%", n)
        r = c.send(n)
        print("消费状态 s%", r)
    c.close()


c = consumer()
product(c)