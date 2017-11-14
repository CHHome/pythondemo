# yield的高级使用

myList = []


def b():
    total = 0
    while 1:
        n = yield
        if n is None:
            return total
        total += n


def a(myList):
    #while防止报StopIteration
    while 1:
        total = yield from b()
        # 子return终止的时候赋值，继续往下执行
        myList.append(total)


cur = a(myList)

# send传给子
cur.send(None)
cur.send(1)
cur.send(2)
cur.send(None)
print(myList)

#第二次循环
cur.send(3)
cur.send(4)
cur.send(None)
print(myList)

#结束
cur.close();