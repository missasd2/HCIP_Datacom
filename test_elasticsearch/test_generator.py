

def fib(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a+b

for n in fib(15):
    print(n)



"""
生成器的特点
（1）函数含有yield关键字，会被认为是生成器
（2）函数执行到 yield p，返回p值以及整个生成器处于暂停状态，并跳出当前函数，执行到调用返回值p的语句
（3）当再次执行到这个含有yield的生成器函数时，会自动立即执行到上次暂停的位置继续执行，也就是从yield p这个语句继续执行
"""
def genera_infi(n):
    while True:
        yield n
        n += 1

for x in genera_infi(1):
    print(x)

