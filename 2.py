def odd():
    a = yield 1
    print(a)
    b = yield(3)
    print(b)
    c = yield(5)
    print(c)


o = odd()
c = o.send(None)
print(c,'jjj')
a = o.send(5)
print(a)
b = o.send(6)
print(b)

