
def b():
    yield 3
    yield 4
    return 5, 20

def a(b):
    yield 1
    yield 2
    yield from b


def func():
    print('dddddsss')
    e, f = yield from b()
    print('ddddd')
    print(e,f,'hhhhh')


m = func()
k = next(m)
print(k)
l = m.send(6)
print(l)
m.send(None)
print('ddddffddd')





